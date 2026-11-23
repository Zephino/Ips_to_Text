#!/usr/bin/env python3
"""
ips_to_text.py - Dump an .ips file to a readable .txt file.

Handles two kinds of .ips:
  1. ROM patch files (start with "PATCH") - lists every record:
     offset, size, and the bytes it writes (hex + ASCII).
  2. Apple crash/diagnostic reports (plain text / JSON) - copied
     straight to .txt, with JSON pretty-printed when possible.

Usage (Windows):
  python ips_to_text.py "C:\\path\\to\\file.ips"
Output: file.ips.txt next to the original.
"""
import json
import sys
from pathlib import Path


def hexdump(data: bytes, base: int, width: int = 16) -> list[str]:
    lines = []
    for i in range(0, len(data), width):
        chunk = data[i:i + width]
        hx = " ".join(f"{b:02X}" for b in chunk)
        asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        lines.append(f"    {base + i:06X}: {hx:<{width * 3}} {asc}")
    return lines


def dump_patch(raw: bytes) -> list[str]:
    out = ["IPS ROM PATCH", "=" * 60]
    pos = 5
    n = 0
    total = 0
    while pos + 3 <= len(raw):
        if raw[pos:pos + 3] == b"EOF":
            pos += 3
            out.append("")
            out.append("EOF marker reached.")
            if pos + 3 <= len(raw):
                trunc = int.from_bytes(raw[pos:pos + 3], "big")
                out.append(f"Truncate ROM to size: 0x{trunc:06X} ({trunc} bytes)")
            break
        if pos + 5 > len(raw):
            out.append("WARNING: file ended in the middle of a record.")
            break
        offset = int.from_bytes(raw[pos:pos + 3], "big")
        size = int.from_bytes(raw[pos + 3:pos + 5], "big")
        pos += 5
        n += 1
        out.append("")
        if size == 0:  # RLE record
            if pos + 3 > len(raw):
                out.append("WARNING: truncated RLE record.")
                break
            count = int.from_bytes(raw[pos:pos + 2], "big")
            value = raw[pos + 2]
            pos += 3
            total += count
            out.append(f"Record {n}: RLE  offset 0x{offset:06X}  "
                       f"fill {count} bytes with 0x{value:02X}")
        else:
            data = raw[pos:pos + size]
            pos += size
            total += len(data)
            out.append(f"Record {n}: DATA offset 0x{offset:06X}  "
                       f"size {size} bytes")
            out.extend(hexdump(data, offset))
    out.insert(2, f"Records: {n}   Bytes changed: {total}")
    return out


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python ips_to_text.py "path\\to\\file.ips"')
        sys.exit(1)
    src = Path(sys.argv[1])
    raw = src.read_bytes()
    dst = src.with_name(src.name + ".txt")

    if raw[:5] == b"PATCH":
        lines = dump_patch(raw)
        text = "\n".join(lines) + "\n"
    else:
        text = raw.decode("utf-8", errors="replace")
        # Apple .ips reports: a JSON header line, then a JSON body.
        parts = text.split("\n", 1)
        pretty = []
        for part in parts:
            try:
                pretty.append(json.dumps(json.loads(part), indent=2))
            except (json.JSONDecodeError, ValueError):
                pretty.append(part)
        text = "\n\n".join(pretty)

    dst.write_text(text, encoding="utf-8")
    print(f"Wrote {dst}")


if __name__ == "__main__":
    main()

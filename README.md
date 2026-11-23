# IPS & ROM to Text Converter

Turn `.ips` patches, game ROMs and Apple crash reports into plain, readable `.txt` files right in your browser.

**▶ Use it here: https://zephino.github.io/Ips_to_Text/**

No install, no sign-up, and your files are never uploaded. Everything happens on your own computer.

---

## What it does

Drop in any of these and get a text file back:

| File type | How it's detected | What you get |
|---|---|---|
| **ROM patch** (NES, SNES, GB, GBA hacks, randomizers, translations) | Starts with `PATCH` | Every record in the patch: the ROM offset, its size, and the bytes written (hex + ASCII). RLE fills and the optional truncate size are shown too. |
| **Apple crash report** (iPhone, iPad, Mac) | JSON text | The report, pretty-printed so it's easy to read. |
| **Game ROM** | By header, or by extension | Platform, header details (title, region, mapper / cartridge type, sizes, version, header checksum check), CRC32 / SHA-1 / SHA-256 hashes, readable text, and an optional full hex dump. |

### Supported ROMs

| System | Extensions | Header details shown |
|---|---|---|
| NES / Famicom | `.nes` | iNES / NES 2.0, mapper, PRG/CHR size, mirroring, battery, trainer. Also hashes without the 16-byte header (No-Intro style). |
| SNES / Super Famicom | `.sfc` `.smc` | Title, LoROM / HiROM / ExHiROM, FastROM, chips, ROM & save size, region, version, checksum pair. Detects and skips 512-byte copier headers. |
| Game Boy / Color | `.gb` `.gbc` | Title, GB / GBC mode, Super GB, cartridge (MBC) type, ROM & save size, region, licensee, header checksum check. |
| Game Boy Advance | `.gba` | Title, game code & region, maker, version, save type (EEPROM / SRAM / Flash), header checksum check. |
| Nintendo 64 | `.z64` `.v64` `.n64` | Title, game code, region, version, byte order, CRC1/CRC2. Handles all three byte orders. |
| Genesis / Mega Drive | `.md` `.gen` `.bin` | System, copyright, titles, serial, devices, region, checksum check. |
| Master System / Game Gear | `.sms` `.gg` | Product code, version, region, checksum. |
| Anything else | any | Size, hashes, readable text, optional hex dump. |

The hashes let you look up the exact dump on databases like No-Intro. Readable text only finds plain ASCII. Most games store their dialogue in their own text encoding, so it usually won't show up. The hex dump is limited to ROMs of 8 MB or less, because it makes very large files.

Only use ROMs you own. Nothing is uploaded, and this tool doesn't host or share any games.

## How to use

1. Open the [converter page](https://zephino.github.io/Ips_to_Text/).
2. Drag one or more `.ips` or ROM files onto the box, or click it (tap it on a phone) to choose files.
   For ROMs, tick **include full hex dump** first if you want every byte.
3. Read the result on the page, click **Copy text**, or click **Download .txt**. Use **Download all .txt** when you have several files.

Each output file keeps the original name with `.txt` added, e.g. `myhack.ips.txt`.

## Example output (ROM patch)

```
IPS ROM PATCH
============================================================
Records: 2   Bytes changed: 12

Record 1: DATA offset 0x001000  size 4 bytes
    001000: 41 42 43 44                                      ABCD

Record 2: RLE  offset 0x002000  fill 8 bytes with 0xFF

EOF marker reached.
```

- **DATA** records write the listed bytes starting at that offset.
- **RLE** records fill a run of bytes with one value.
- The ASCII column on the right can reveal changed in-game text.

## Using the output with an AI

Language models can't read binary `.ips` files, but they can read this text. Paste or attach the `.txt` in ChatGPT, Claude, or a local model (LM Studio and similar) and ask something like:

> "This is a text dump of an IPS ROM patch for *[game name]*. Each record shows a ROM offset and the bytes written there. Summarize which parts of the ROM it changes, and point out anything that looks like text, graphics, or code."

You'll get much better answers if you also give the AI a ROM map for that game. Very large patches may need to be pasted in pieces.

## Offline version (Windows)

The [`offline`](offline) folder has the IPS patch converter as a script (ROM info is web-only for now):

- `ips_to_text.py`: the converter (needs [Python 3](https://www.python.org/downloads/), with **Add Python to PATH** ticked during install).
- `convert_ips.bat`: double-click to convert every `.ips` in its folder.

**To use it:** put both files in the same folder as your `.ips` files and double-click `convert_ips.bat`. The `.txt` files appear in that same folder.

Or run a single file from Command Prompt:

```
python ips_to_text.py "C:\path\to\yourfile.ips"
```

## Privacy & security

- Files are read only in your browser. Nothing is sent to any server.
- The page loads no outside scripts, fonts, or trackers.
- The page shows a usage counter (visits and files converted). It sends only an anonymous +1 to [CountAPI](https://countapi.mileshilliard.com), never your files.
- See [SECURITY.md](SECURITY.md) for details.

## Project files

```
index.html          the web converter (GitHub Pages)
offline/            Windows script + batch file
CHANGELOG.md        version history
SECURITY.md         security notes
```

## Version

Current version: **1.3.0**. See [CHANGELOG.md](CHANGELOG.md) for history.

## Feedback

Found a file that doesn't convert right? [Open an issue](https://github.com/Zephino/Ips_to_Text/issues) and attach the `.ips` if you can.

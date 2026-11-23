# IPS to Text Converter

Turn `.ips` files into plain, readable `.txt` files right in your browser.

**▶ Use it here: https://zephino.github.io/Ips_to_Text/**

No install, no sign-up, and your files are never uploaded. Everything happens on your own computer.

---

## What it does

`.ips` is used for two very different kinds of file. This tool handles both:

| File type | How it's detected | What you get |
|---|---|---|
| **ROM patch** (NES, SNES, GB, GBA hacks, randomizers, translations) | Starts with `PATCH` | Every record in the patch: the ROM offset, its size, and the bytes written (hex + ASCII). RLE fills and the optional truncate size are shown too. |
| **Apple crash report** (iPhone, iPad, Mac) | JSON text | The report, pretty-printed so it's easy to read. |

## How to use

1. Open the [converter page](https://zephino.github.io/Ips_to_Text/).
2. Drag one or more `.ips` files onto the box, or click it to choose files.
3. Read the result on the page, or click **Download .txt**. Use **Download all .txt** when you have several files.

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

The [`offline`](offline) folder has the same converter as a script:

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
- See [SECURITY.md](SECURITY.md) for details.

## Project files

```
index.html          the web converter (GitHub Pages)
offline/            Windows script + batch file
CHANGELOG.md        version history
SECURITY.md         security notes
```

## Version

Current version: **1.0.1**. See [CHANGELOG.md](CHANGELOG.md) for history.

## Feedback

Found a file that doesn't convert right? [Open an issue](https://github.com/Zephino/Ips_to_Text/issues) and attach the `.ips` if you can.

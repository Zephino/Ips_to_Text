# IPS to Text Converter

A one-page web tool that turns `.ips` files into readable `.txt` files.

- **ROM patches** (`PATCH` header): lists every record with its ROM offset, size and bytes (hex + ASCII), plus RLE fills and the optional truncate size.
- **Apple crash reports** (`.ips` JSON): pretty-printed as JSON.

Everything runs in the browser. No files are uploaded, and the page loads no outside scripts.

## Use it
Open the GitHub Pages link, drop in one or more `.ips` files, then click **Download .txt**.

## Offline version
`ips_to_text.py` and `convert_ips.bat` (in the `offline` folder) do the same thing on Windows. Put both next to your `.ips` files and double-click the `.bat`.

## Version
1.0.0. See [CHANGELOG.md](CHANGELOG.md).

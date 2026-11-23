# Changelog

## [1.3.0] - 2026-11-23
### Added
- ROM files: header info for NES, SNES, Game Boy / Color, GBA, N64, Genesis, Master System / Game Gear.
- CRC32, SHA-1 and SHA-256 hashes for every ROM, plus header-less hashes for NES and copier-headered SNES.
- Readable ASCII text from ROMs, and an optional full hex dump (ROMs up to 8 MB).
- Options checkboxes for ROM text and hex dump.
### Changed
- Renamed the page to "IPS & ROM to Text Converter".

## [1.2.0] - 2026-11-23
### Added
- Phone-friendly layout: larger tap targets, stacked buttons, "Tap to choose" wording on touch screens.
- "Copy text" button on each result, for pasting into an AI app.
- New look: gradient title, upload icon, stat icons, info cards, GitHub link in footer.
### Fixed
- Drop box border drew broken (label was inline).
- Only the first file converted when several were picked at once.
- iPhones could grey out .ips files in the file picker.
- Converting no longer waits on the usage counter.

## [1.1.0] - 2026-11-23
### Added
- Usage counter on the page: total visits and total files converted (via CountAPI).
### Security
- Content-Security-Policy now allows connections to the counter service only.

## [1.0.1] - 2026-11-23
### Changed
- Expanded README: live link, example output, AI tips, offline instructions.

## [1.0.0] - 2026-11-23
### Added
- Web page converter for `.ips` ROM patches and Apple crash reports.
- Drag-and-drop with multiple files, preview, per-file and "download all" buttons.
- Offline Windows tools: `ips_to_text.py` and `convert_ips.bat`.

# Security

- Files (patches and ROMs) are read only in the visitor's browser. Nothing is sent to any server. Hashes are calculated locally.
- The page loads no outside scripts, fonts or trackers.
- Usage counter: the page sends an anonymous "+1" to countapi.mileshilliard.com on each visit and each converted file. No file names, file contents or personal data are sent. The Content-Security-Policy allows connections to that one address only.
- Counter values are public and can be changed by anyone who knows the key, so treat them as a rough guide, not exact stats.
- File names and contents are shown with `textContent`, so a crafted file can't inject HTML or scripts into the page.

To report a problem, open an issue on this repository.

# Security

- Files are read only in the visitor's browser. Nothing is sent to any server.
- The page loads no outside scripts, fonts or trackers. A Content-Security-Policy blocks outside connections.
- File names and contents are shown with `textContent`, so a crafted file can't inject HTML or scripts into the page.

To report a problem, open an issue on this repository.

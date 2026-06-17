---
name: vibe-web-viewer
description: Display Mistral Vibe CLI conversations in a web browser with improved readability. Use when user wants to view CLI chat in browser, mentions terminal readability issues, or requests conversation projection.
---

# Vibe Web Viewer

## Quick start

Launch the viewer for your current conversation:

```bash
python scripts/viewer.py
```

Open `http://localhost:5000` in your browser.

## Features

- **Live updates**: Automatically refreshes as new messages appear in terminal
- **Session browser**: Navigate between all your Vibe CLI conversations
- **Markdown rendering**: Beautiful formatting for code, tables, and text
- **Dark/light themes**: Comfortable reading in any lighting
- **Search**: Find text across all sessions
- **Responsive**: Works on desktop and mobile devices

## Workflows

### View current conversation
```bash
python scripts/viewer.py
```

### View specific session
```bash
python scripts/viewer.py --session session_20260608_113911_5b24dbbf
```

### List all sessions
```bash
python scripts/viewer.py --list
```

### Custom port
```bash
python scripts/viewer.py --port 8080
```

## File Structure

```
vibe-web-viewer/
├── SKILL.md              # This file
├── scripts/
│   └── viewer.py         # Web server
└── templates/
    └── index.html        # Web UI
```

# Typeflow PLAY — Typing Lab (redesigned)

A completely redesigned typing-speed practice application using **Python + Flask**, HTML, CSS, and vanilla JavaScript. No database is required.

## Windows setup

1. Open **this folder** (`typeflow_reimagined`) in VS Code.
2. Open PowerShell in the folder (the folder containing `app.py`).
3. Run:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

4. Open **http://127.0.0.1:5001**.

Alternatively, double-click `start_windows.bat`.

## Features

- Fresh cream/mint playful interface rather than an analytics-app sidebar
- Large typing stage, highlighted characters, shuffle, levels, topic selection
- Countdown clock with 30/60/120-second tests
- Live WPM, accuracy, mistakes, progress and reactive QWERTY keyboard
- Live graph, completed-session performance trend, accuracy donut and difficult-key insights
- Browser-only local test history, CSV download, light/dark switch
- Python API for passage retrieval and final scoring

Test records are saved in browser localStorage, not a database. Clearing browser storage removes history. The optional CSV export is generated in the browser.

**Note:** Port 5001 is deliberately different from the Resume Analyzer's 5000, so they can run simultaneously.

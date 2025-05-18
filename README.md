# StayAwake

A simple macOS menu bar application that prevents your computer from sleeping. Built with Python and rumps.

## Features

- Menu bar interface with easy access
- Set sleep prevention for 15, 30, 60, or 120 minutes
- Visual indicators showing active state (⚡️ when idle, ⏰ when active)
- Countdown timer showing remaining time
- Native macOS integration

## Installation

1. Download the latest release
2. Move StayAwake.app to your Applications folder
3. Launch the app

To build from source:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build the app
pyinstaller --onedir --windowed --name "StayAwake" stay_awake.py
```

## Usage

1. Click the menu bar icon (⚡️)
2. Select desired duration (15, 30, 60, or 120 minutes)
3. The icon will change to ⏰ with a countdown
4. To stop early, click the icon and select "Stop"

## Auto-start at Login

1. Open System Settings
2. Go to General > Login Items
3. Click the "+" button
4. Select StayAwake.app from your Applications folder

## Requirements

- macOS 10.13 or later
- Python 3.8 or later (for building from source) 
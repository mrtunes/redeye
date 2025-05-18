# Stay Awake App

A macOS status bar application that prevents your computer from going to sleep for a specified duration.

## Features
- Lives in your menu bar for easy access (⚡️)
- One-click activation: just select a duration to start
- Shows remaining time in the menu bar (⏰)
- Quick stop option (⌘S)
- Automatically stops when time is up

## Requirements
- macOS
- Python 3.6 or higher
- rumps package

## Installation

1. Clone or download this repository
2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure your virtual environment is activated:
```bash
source venv/bin/activate  # if not already activated
```

2. Run the application:
```bash
python stay_awake.py
```

3. The app will appear in your menu bar with a lightning bolt (⚡️)
4. Click the icon and select a duration (15, 30, 60, or 120 minutes) to start
5. The icon will change to a clock (⏰) showing remaining time
6. To stop early:
   - Select "Stop" from the menu, or
   - Use the keyboard shortcut ⌘S

## How it Works

The application uses macOS's built-in `caffeinate` command to prevent the system from sleeping. The `-i` flag prevents the system from idle sleeping.

## Note

The application must be running for sleep prevention to remain active. Closing the application will restore normal sleep behavior. 
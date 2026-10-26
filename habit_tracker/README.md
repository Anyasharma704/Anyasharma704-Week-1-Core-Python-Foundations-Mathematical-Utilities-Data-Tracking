# Habit Tracker

A small desktop habit tracker using Python, Tkinter, and JSON storage.

## Run
```bash
python habit_tracker.py
```
No third-party packages are required.

## Features
- Add a habit.
- Select a habit and mark it complete for today, or undo completion.
- Delete a selected habit.
- See today's completion count.
- Save habits in `habits.json` so they persist after closing the app.

## Data
The app creates `habits.json` in the same folder as the Python script the first time a habit is saved. Completion is tracked by date.

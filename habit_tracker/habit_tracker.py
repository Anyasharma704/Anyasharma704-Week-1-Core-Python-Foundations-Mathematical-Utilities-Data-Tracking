import json
import tkinter as tk
from tkinter import messagebox
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).with_name("habits.json")
today = date.today().isoformat()
habits = []


def load_habits():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        messagebox.showwarning("Data file", "Could not read habits.json. Starting with an empty list.")
        return []


def save_habits():
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(habits, file, indent=2)


def refresh_list():
    listbox.delete(0, tk.END)
    completed = 0
    for index, habit in enumerate(habits):
        done = habit.get("completed_on") == today
        completed += int(done)
        marker = "✓" if done else "○"
        listbox.insert(tk.END, f"{marker}  {habit['name']}")
    progress.config(text=f"Today's progress: {completed}/{len(habits)} completed")


def add_habit():
    name = habit_entry.get().strip()
    if not name:
        messagebox.showerror("Missing habit", "Type a habit name first.")
        return
    if any(h["name"].casefold() == name.casefold() for h in habits):
        messagebox.showinfo("Already exists", "That habit is already in your list.")
        return
    habits.append({"name": name, "completed_on": ""})
    save_habits()
    habit_entry.delete(0, tk.END)
    refresh_list()


def selected_index():
    selection = listbox.curselection()
    if not selection:
        messagebox.showinfo("Select a habit", "Select a habit from the list first.")
        return None
    return selection[0]


def toggle_complete():
    index = selected_index()
    if index is None:
        return
    if habits[index].get("completed_on") == today:
        habits[index]["completed_on"] = ""
    else:
        habits[index]["completed_on"] = today
    save_habits()
    refresh_list()


def delete_habit():
    index = selected_index()
    if index is None:
        return
    del habits[index]
    save_habits()
    refresh_list()


root = tk.Tk()
root.title("Habit Tracker")
root.geometry("460x470")
root.configure(bg="#f4f0ff")
root.resizable(False, False)

tk.Label(root, text="Habit Tracker", font=("Arial", 21, "bold"),
         bg="#f4f0ff", fg="#513a78").pack(pady=(20, 5))
tk.Label(root, text="Build consistency, one day at a time",
         font=("Arial", 10), bg="#f4f0ff", fg="#514b5e").pack(pady=(0, 12))

habit_entry = tk.Entry(root, width=34, font=("Arial", 11))
habit_entry.pack(pady=5)
habit_entry.bind("<Return>", lambda event: add_habit())

tk.Button(root, text="Add habit", command=add_habit, bg="#6d4bc3",
          fg="white", relief="flat", padx=12, pady=5).pack(pady=5)

listbox = tk.Listbox(root, width=39, height=11, font=("Arial", 11),
                     selectmode=tk.SINGLE, activestyle="dotbox")
listbox.pack(pady=10)

button_frame = tk.Frame(root, bg="#f4f0ff")
button_frame.pack()
tk.Button(button_frame, text="Mark complete / undo", command=toggle_complete,
          bg="#d9f2e6", fg="#234c3b", relief="flat", padx=9, pady=6).grid(row=0, column=0, padx=4)
tk.Button(button_frame, text="Delete selected", command=delete_habit,
          bg="#f7dce2", fg="#6d2937", relief="flat", padx=9, pady=6).grid(row=0, column=1, padx=4)

progress = tk.Label(root, text="", bg="#f4f0ff", fg="#513a78",
                    font=("Arial", 10, "bold"))
progress.pack(pady=12)

habits = load_habits()
refresh_list()
root.mainloop()

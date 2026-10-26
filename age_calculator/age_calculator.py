import tkinter as tk
from tkinter import messagebox
from datetime import date
import calendar


def calculate_exact_age(birth_date: date, today: date) -> tuple[int, int, int]:
    """Return age as (years, months, days), accounting for real month lengths."""
    if birth_date > today:
        raise ValueError("Date of birth cannot be in the future.")

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        # Borrow the number of days in the previous month.
        previous_month = today.month - 1
        previous_year = today.year
        if previous_month == 0:
            previous_month = 12
            previous_year -= 1
        days += calendar.monthrange(previous_year, previous_month)[1]
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return years, months, days


def calculate_age():
    raw_dob = dob_entry.get().strip()

    try:
        # Expected format: YYYY-MM-DD, for example 2005-08-17.
        birth_date = date.fromisoformat(raw_dob)
    except ValueError:
        messagebox.showerror(
            "Invalid date",
            "Please enter a valid date in YYYY-MM-DD format (for example, 2005-08-17)."
        )
        return

    today = date.today()

    if birth_date > today:
        messagebox.showerror("Invalid date", "Date of birth cannot be in the future.")
        return

    years, months, days = calculate_exact_age(birth_date, today)
    result_label.config(
        text=f"Your exact age is:\n{years} years, {months} months, and {days} days"
    )


def clear_form():
    dob_entry.delete(0, tk.END)
    result_label.config(text="")
    dob_entry.focus()


root = tk.Tk()
root.title("Age Calculator")
root.geometry("470x330")
root.resizable(False, False)
root.configure(bg="#f4f0ff")

title = tk.Label(
    root, text="Age Calculator", font=("Arial", 22, "bold"),
    bg="#f4f0ff", fg="#513a78"
)
title.pack(pady=(24, 8))

subtitle = tk.Label(
    root, text="Find your exact age using your date of birth",
    font=("Arial", 10), bg="#f4f0ff", fg="#514b5e"
)
subtitle.pack(pady=(0, 18))

dob_label = tk.Label(
    root, text="Date of birth (YYYY-MM-DD)",
    font=("Arial", 11, "bold"), bg="#f4f0ff", fg="#302744"
)
dob_label.pack()

dob_entry = tk.Entry(root, font=("Arial", 12), width=24, justify="center")
dob_entry.pack(pady=8)
dob_entry.insert(0, "2005-08-17")

button_frame = tk.Frame(root, bg="#f4f0ff")
button_frame.pack(pady=10)

calculate_button = tk.Button(
    button_frame, text="Calculate Age", command=calculate_age,
    font=("Arial", 10, "bold"), bg="#6d4bc3", fg="white",
    activebackground="#513a78", activeforeground="white",
    relief="flat", padx=14, pady=7, cursor="hand2"
)
calculate_button.grid(row=0, column=0, padx=6)

clear_button = tk.Button(
    button_frame, text="Clear", command=clear_form,
    font=("Arial", 10), bg="#e4ddf4", fg="#302744",
    relief="flat", padx=18, pady=7, cursor="hand2"
)
clear_button.grid(row=0, column=1, padx=6)

result_label = tk.Label(
    root, text="", font=("Arial", 13, "bold"),
    bg="#f4f0ff", fg="#513a78", justify="center", wraplength=420
)
result_label.pack(pady=12)

footer = tk.Label(
    root, text="Input is validated • Leap years and month lengths are handled",
    font=("Arial", 8), bg="#f4f0ff", fg="#6f687a"
)
footer.pack(side="bottom", pady=12)

root.bind("<Return>", lambda event: calculate_age())
dob_entry.focus()
root.mainloop()

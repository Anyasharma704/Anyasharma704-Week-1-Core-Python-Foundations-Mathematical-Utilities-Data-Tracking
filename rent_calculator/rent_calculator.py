import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        rent = float(rent_entry.get())
        utilities = float(utilities_entry.get() or 0)
        internet = float(internet_entry.get() or 0)
        people = int(people_entry.get())

        if rent < 0 or utilities < 0 or internet < 0:
            raise ValueError("Expenses cannot be negative.")
        if people <= 0:
            raise ValueError("Number of people must be at least 1.")

        total = rent + utilities + internet
        per_person = total / people
        result.config(
            text=f"Total monthly cost: ₹{total:,.2f}\n"
                 f"Each person's share: ₹{per_person:,.2f}"
        )
    except ValueError as error:
        messagebox.showerror(
            "Check your input",
            str(error) if str(error) in (
                "Expenses cannot be negative.",
                "Number of people must be at least 1."
            ) else "Enter valid numbers for all fields."
        )


root = tk.Tk()
root.title("Rent Calculator")
root.geometry("420x390")
root.configure(bg="#f4f0ff")
root.resizable(False, False)

tk.Label(root, text="Rent Calculator", font=("Arial", 21, "bold"),
         bg="#f4f0ff", fg="#513a78").pack(pady=18)


def add_field(label, default=""):
    tk.Label(root, text=label, bg="#f4f0ff", fg="#302744",
             font=("Arial", 10, "bold")).pack()
    entry = tk.Entry(root, justify="center", font=("Arial", 11), width=25)
    entry.pack(pady=(3, 8))
    if default:
        entry.insert(0, default)
    return entry


rent_entry = add_field("Monthly rent (₹)", "12000")
utilities_entry = add_field("Utilities (₹)", "1500")
internet_entry = add_field("Internet (₹)", "600")
people_entry = add_field("Number of people sharing", "3")

tk.Button(root, text="Calculate split", command=calculate,
          bg="#6d4bc3", fg="white", relief="flat",
          font=("Arial", 10, "bold"), padx=14, pady=7).pack(pady=7)
result = tk.Label(root, text="", bg="#f4f0ff", fg="#513a78",
                  font=("Arial", 12, "bold"), justify="center")
result.pack(pady=8)
root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode


def generate_qr():
    content = content_entry.get().strip()
    if not content:
        messagebox.showerror("Missing input", "Enter some text or a URL first.")
        return

    try:
        qr_image = qrcode.make(content)
        path = filedialog.asksaveasfilename(
            title="Save QR code",
            defaultextension=".png",
            filetypes=[("PNG image", "*.png")],
            initialfile="my_qr_code.png"
        )
        if path:
            qr_image.save(path)
            messagebox.showinfo("Saved", f"QR code saved to:\n{path}")
    except Exception as error:
        messagebox.showerror("Error", f"Could not create QR code:\n{error}")


root = tk.Tk()
root.title("QR Code Generator")
root.geometry("460x260")
root.configure(bg="#f4f0ff")
root.resizable(False, False)

tk.Label(root, text="QR Code Generator", font=("Arial", 21, "bold"),
         bg="#f4f0ff", fg="#513a78").pack(pady=(25, 8))
tk.Label(root, text="Enter text or a website URL",
         font=("Arial", 10), bg="#f4f0ff", fg="#514b5e").pack()

content_entry = tk.Entry(root, width=42, font=("Arial", 11))
content_entry.pack(pady=12)
content_entry.focus()

tk.Button(root, text="Generate and Save QR", command=generate_qr,
          bg="#6d4bc3", fg="white", relief="flat",
          font=("Arial", 10, "bold"), padx=14, pady=8).pack(pady=4)

tk.Label(root, text="Requires the qrcode package. Saves a PNG image.",
         font=("Arial", 8), bg="#f4f0ff", fg="#6f687a").pack(pady=12)

root.bind("<Return>", lambda event: generate_qr())
root.mainloop()

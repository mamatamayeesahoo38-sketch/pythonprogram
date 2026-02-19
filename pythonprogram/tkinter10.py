import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Message Box Demo")
root.geometry("300x250")

# Function to show info
def show_info():
    messagebox.showinfo("Info", "This is an info message.")

# Function to show warning
def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

# Function to show error
def show_error():
    messagebox.showerror("Error", "This is an error message.")

# Function to ask yes/no
def ask_yes_no():
    response = messagebox.askyesno("Confirm", "Do you want to continue?")
    if response:
        messagebox.showinfo("Response", "You clicked Yes.")
    else:
        messagebox.showinfo("Response", "You clicked No.")

# Buttons
tk.Button(root, text="Show Info", command=show_info).pack(pady=5)
tk.Button(root, text="Show Warning", command=show_warning).pack(pady=5)
tk.Button(root, text="Show Error", command=show_error).pack(pady=5)
tk.Button(root, text="Ask Yes/No", command=ask_yes_no).pack(pady=5)

# Start the GUI loop
root.mainloop()

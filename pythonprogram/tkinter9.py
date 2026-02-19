import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Message Box Demo")
root.geometry("300x200")

# Function to show the message box
def show_message():
    messagebox.showinfo("Title", "This is an info message")

# Create a button
btn = tk.Button(root, text="Click Me", command=show_message)
btn.pack(pady=10)

# Start the GUI loop
root.mainloop()
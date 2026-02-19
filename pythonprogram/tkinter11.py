import tkinter as tk

root = tk.Tk()
root.geometry("200x150")

tk.Label(root, text="Top Label").pack(pady=10)
tk.Button(root, text="Click Me").pack(pady=20)
tk.Label(root, text="Bottom Label").pack(pady=5)

root.mainloop()
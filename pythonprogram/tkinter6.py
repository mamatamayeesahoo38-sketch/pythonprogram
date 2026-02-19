import tkinter as tk

root = tk.Tk()
btn = tk.Button(root, text="Click Me", command=lambda: print("Hello"))
btn.pack()
root.mainloop()

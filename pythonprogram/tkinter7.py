import tkinter as tk
def show():
	print("hi")
root = tk.Tk()
btn = tk.Button(root, text="Click Me", command=show)
btn.pack()
root.mainloop()


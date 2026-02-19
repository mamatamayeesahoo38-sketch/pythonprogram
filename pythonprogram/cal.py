import tkinter as tk

# function to add numbers
def add_numbers():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        result = n1 + n2
        entry3.delete(0, tk.END)
        entry3.insert(0, str(result))
    except ValueError:
        entry3.delete(0, tk.END)
        entry3.insert(0, "Invalid input")

# main window
root = tk.Tk()
root.title("Add Two Numbers")

# labels
tk.Label(root, text="Enter First Number").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Enter Second Number").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Result").grid(row=2, column=0, padx=10, pady=5)

# entry fields
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

# button
tk.Button(root, text="Add", command=add_numbers).grid(row=3, column=0, columnspan=2, pady=10)

# run window
root.mainloop()

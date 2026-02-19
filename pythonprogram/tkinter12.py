
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Invalid input")

# First number input
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

# Second number input
tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

# Add Button
tk.Button(root, text="Add", command=add_numbers).pack(pady=10)

# Result display
tk.Label(root, text="Result:").pack(pady=5)
entry_result = tk.Entry(root, width=30)
entry_result.pack(pady=5)

# Start GUI
root.mainloop()
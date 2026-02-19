import tkinter as tk

# function to add numbers
def calculate_SI():
    try:
        p= int(entry1.get())
        t= int(entry2.get())
        r=int(entry3.get())
        SI=(p*t*r)/100

        entry4.delete(0,tk.END)
        entry4.insert(0,int(SI))
        
    except ValueError:
        entry4.delete(0, tk.END)
        entry4.insert(0, "Invalid input")

# main window
root = tk.Tk()
root.title("Simple Interest")

# labels
tk.Label(root, text="principal").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="time").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="rate of interest").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Simple Interest").grid(row=3, column=0, padx=10, pady=5)

# entry fields
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)

tk.Button(root, text="Calculate", command=calculate_SI).grid(row=4, column=0, columnspan=2, pady=10)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2,column=1)
entry4.grid(row=3,column=1)
# button
#tk.Button(root, text="calculate_SI", command=calculate_SI).grid(row=4, column=0, columnspan=2, pady=10)

# run window
root.mainloop()

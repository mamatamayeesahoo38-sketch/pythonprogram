import tkinter as tk

def calculate_si():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        si = (principal * rate * time) / 100
        show_result(si)
    except ValueError:
        show_error("Invalid Input")

def show_result(result):
    result_label.config(text=f"Simple Interest: {result}")

def show_error(message):
    result_label.config(text=message)

root = tk.Tk()
root.title("Simple Interest Calculator")

tk.Label(root, text="Principal:").grid(row=0, column=0)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1)

tk.Label(root, text="Rate of Interest (%):").grid(row=1, column=0)
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1)

tk.Label(root, text="Time (years):").grid(row=2, column=0)
entry_time = tk.Entry(root)
entry_time.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate_si).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Simple Interest:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
from fractions import Fraction




def parse_fraction(frac_str):
    """Convert user input (like '1/2') to a Fraction object."""
    try:
        return Fraction(frac_str)
    except Exception:
        messagebox.showerror("Invalid Input", f"Invalid fraction: {frac_str}")
        return None


def calculate(operation):
    f1 = parse_fraction(entry1.get())
    f2 = parse_fraction(entry2.get())

    if f1 is None or f2 is None:
        return

    try:
        if operation == "+":
            result = f1 + f2
        elif operation == "-":
            result = f1 - f2
        elif operation == "*":
            result = f1 * f2
        elif operation == "/":
            result = f1 / f2
        else:
            return
        result_box.config(state="normal")
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, f"{f1} {operation} {f2} = {result}")
        result_box.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def reduce_fraction():
    f = parse_fraction(entry1.get())
    if f is None:
        return

    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, f"Reduced: {f}")
    result_box.config(state="disabled")


root = tk.Tk()
root.title("Fraction Calculator")
root.geometry("450x300")

# Input fields
tk.Label(root, text="Fraction 1").grid(row=0, column=0)
entry1 = tk.Entry(root, width=15)
entry1.grid(row=1, column=0, padx=10)

tk.Label(root, text="Fraction 2").grid(row=2, column=0)
entry2 = tk.Entry(root, width=15)
entry2.grid(row=3, column=0, padx=10)


tk.Button(root, text="+", width=5, command=lambda: calculate("+")).grid(row=4, column=0, pady=5)
tk.Button(root, text="-", width=5, command=lambda: calculate("-")).grid(row=5, column=0)
tk.Button(root, text="*", width=5, command=lambda: calculate("*")).grid(row=6, column=0)
tk.Button(root, text="/", width=5, command=lambda: calculate("/")).grid(row=7, column=0)

tk.Button(root, text="Reduce", width=10, command=reduce_fraction).grid(row=8, column=0, pady=10)


result_box = tk.Text(root, height=15, width=30, state="disabled")
result_box.grid(row=0, column=1, rowspan=10, padx=10)

root.mainloop()
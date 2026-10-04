import tkinter as tk
from tkinter import messagebox
from fractions import Fraction

raw_num = None
raw_den = None
last_expr = ""   # to store expression like "1/2 + 3/4"

def parse_fraction(text):
    try:
        if "/" in text:
            a, b = text.split("/")
            return int(a), int(b)
        return int(text), 1
    except:
        raise ValueError

def calculate(op):
    global raw_num, raw_den, last_expr

    try:
        n1, d1 = parse_fraction(entry1.get())
        n2, d2 = parse_fraction(entry2.get())

        if d1 == 0 or d2 == 0:
            raise ZeroDivisionError

        # store full expression for display later
        frac1 = f"{n1}/{d1}"
        frac2 = f"{n2}/{d2}"
        last_expr = f"{frac1} {op} {frac2}"

        # compute unsimplified
        if op == "+":
            raw_num = n1 * d2 + n2 * d1
            raw_den = d1 * d2
        elif op == "-":
            raw_num = n1 * d2 - n2 * d1
            raw_den = d1 * d2
        elif op == "*":
            raw_num = n1 * n2
            raw_den = d1 * d2
        elif op == "/":
            if n2 == 0:
                raise ZeroDivisionError
            raw_num = n1 * d2
            raw_den = d1 * n2

        result_label.config(text=f"{last_expr} = {raw_num}/{raw_den}")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero!")
    except:
        messagebox.showerror("Error", "Invalid fraction")

def reduce_answer():
    global raw_num, raw_den, last_expr
    if raw_num is None:
        return

    f = Fraction(raw_num, raw_den)
    result_label.config(text=f"{last_expr} = {f.numerator}/{f.denominator}")

# GUI
root = tk.Tk()
root.title("Fraction Calculator")
root.geometry("310x260")

tk.Label(root, text="Fraction 1:").pack()
entry1 = tk.Entry(root, width=20)
entry1.pack()

tk.Label(root, text="Fraction 2:").pack()
entry2 = tk.Entry(root, width=20)
entry2.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0)
tk.Button(frame, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1)
tk.Button(frame, text="*", width=5, command=lambda: calculate("*")).grid(row=0, column=2)
tk.Button(frame, text="/", width=5, command=lambda: calculate("/")).grid(row=0, column=3)

tk.Button(root, text="Reduce", width=10, command=reduce_answer).pack(pady=8)

result_label = tk.Label(root, text="Answer", font=("Arial", 12))
result_label.pack()

root.mainloop()

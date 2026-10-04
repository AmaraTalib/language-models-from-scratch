import tkinter as tk
from tkinter import messagebox
def say_hello():
    print("Hello!!")
    messagebox.showinfo("title","Hello World")
root=tk.Tk()
label=tk.Label(root,text="Welcome to tkinter")
label.pack()
label=tk.Label(root,text="PYTHON is quite good.")
label.pack()
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root,text="Click me",command=say_hello)
button.pack()
root.geometry("300x200")
root.mainloop()
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('tkinter variables')

def button_func():
    print(string_var.get())
    string_var.set('button pressed')


#Tkinter Variables
string_var = tk.StringVar()
string_var_exercise = tk.StringVar(value='test')


label = ttk.Label(master=root, text="Default", textvariable=string_var)
label.pack()

entry = ttk.Entry(root, textvariable=string_var)
entry.pack()

button = ttk.Button(root, text="Click", command=button_func)
button.pack()

entry2 = ttk.Entry(master=root, textvariable=string_var_exercise)
entry2.pack()

entry3 = ttk.Entry(master=root, textvariable=string_var_exercise)
entry3.pack()

label2 = ttk.Label(master=root, textvariable=string_var_exercise)
label2.pack()

root.mainloop()

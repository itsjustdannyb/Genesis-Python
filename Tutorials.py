import tkinter as tk
from tkinter import ttk


#window
root = tk.Tk()
root.title("Buttons")
root.geometry('600x400')

# button
def button_func():
    print("A Basic Button")
    print(radio_var.get())


btn_string = tk.StringVar(value="A button with StringVar")

button = ttk.Button(master=root, text="A Button", command=button_func, textvariable=btn_string)
button.pack()


# CheckButton
checkVar = tk.IntVar(value=10)
check = ttk.Checkbutton(root,
                        text="Check Box 1",
                        command=lambda: print(checkVar.get()),
                        variable=checkVar,
                        onvalue=10,
                        offvalue=5)
check.pack()

# Radio Buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(root,
                         text="Radio Button 1",
                         value="Radio 1",
                         variable=radio_var,
                         command=lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(root, text="Radio Button 2", value=2, variable=radio_var)
radio2.pack()


# exercise

# def exercise():
#     print(btn_var.get())
#     check2.set()


# variables
btn_var = tk.StringVar(value="I have been summoned")
check2 = tk.BooleanVar()


ex_check = ttk.Checkbutton(root,
                           text="Exercise Check Button",
                           variable=btn_var,
                           command=lambda: print(btn_var.get()))
ex_check.pack()


ex_radio1 = ttk.Radiobutton(root,
                            text="Exercise Radio Button 1",
                            value="A",
                            variable=btn_var,
                            command=lambda: print(check2.get()))
ex_radio1.pack()

ex_radio2 = ttk.Radiobutton(root,
                            text="Exercise Radio Button 2",
                            value="B",
                            variable=btn_var,
                            command=lambda: print(check2.get()))

ex_radio2.pack()

#exit
root.mainloop()

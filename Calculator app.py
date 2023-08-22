from tkinter import *

#root window
root = Tk()
root.title("Calculator!")
entry_box = Entry(root, width=50, borderwidth=3)
entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#click function
def button_click(number):
    # entry_box.delete(0, END)
    current = entry_box.get()
    entry_box.delete(0, 'end')
    entry_box.insert(0, str(current) + str(number))
    return

#clear function
def clear_button():
    entry_box.delete(0, 'end')

#additon function


# f_num = int(first_number)  # fixes global variable error in Pycharm
def add_button():
    first_number = entry_box.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry_box.delete(0, 'end')
    return

#subtract function

def subtract_button():
    first_number = entry_box.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry_box.delete(0, 'end')
    return

#division function
def division_button():
    first_number = entry_box.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry_box.delete(0, 'end')
    return

#multiply button
def multiply_button():
    first_number = entry_box.get()
    global f_num
    global math
    math = "multiplaication"
    f_num = int(first_number)
    entry_box.delete(0, 'end')
    return


# equals function
# s_num = int(second_number) #fixes global variable error in pyCharm
def equals_button():
    second_number = entry_box.get()
    global s_num
    s_num = int(second_number)
    entry_box.delete(0, 'end')

    if math == "addition":
        result = f_num + s_num
        entry_box.insert(0, result)
    elif math == "subtraction":
        result = f_num - s_num
        entry_box.insert(0, result)
    elif math == "division":
        result = f_num / s_num
        entry_box.insert(0, result)
    else:
        result = f_num * s_num
        entry_box.insert(0, result)


#Define Buttons


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=add_button)
button_equal = Button(root, text="=", padx=93, pady=20, command=lambda: equals_button())
button_clear = Button(root, text="Clear", padx=84, pady=20, command=clear_button)

button_multiply = Button(root, text="*", padx=39, pady=40, command=multiply_button)
button_divide = Button(root, text="/", padx=39, pady=40, command=division_button)
button_subtract = Button(root, text="-", padx=39, pady=40, command=subtract_button)


#Display Buttons on the Screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
#prevents app from closing prematurely
root.mainloop()

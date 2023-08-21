from tkinter import *

#root window
root = Tk()
root.title("Calculator!")
entry_box = Entry(root, width=50, borderwidth=3)
entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#addition function
def button_add():
    return

#Define Buttons


button_1 = Button(root, text="1", padx=40, pady=20, command=button_add)
button_2 = Button(root, text="2", padx=40, pady=20, command=button_add)
button_3 = Button(root, text="3", padx=40, pady=20, command=button_add)
button_4 = Button(root, text="4", padx=40, pady=20, command=button_add)
button_5 = Button(root, text="5", padx=40, pady=20, command=button_add)
button_6 = Button(root, text="6", padx=40, pady=20, command=button_add)
button_7 = Button(root, text="7", padx=40, pady=20, command=button_add)
button_8 = Button(root, text="8", padx=40, pady=20, command=button_add)
button_9 = Button(root, text="9", padx=40, pady=20, command=button_add)
button_0 = Button(root, text="0", padx=40, pady=20, command=button_add)

#Display Buttons on the Screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=)

button_7.grid(row=, column=)
button_8.grid(row=, column=)
button_9.grid(row=, column=)


#prevents app from closing prematurely
root.mainloop()

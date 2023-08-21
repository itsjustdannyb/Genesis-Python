from tkinter import *

root = Tk()

def click_btn():
    hello = "Hello " + e.get()
    clk_label = Label(root, text=hello)
    clk_label.pack()


e = Entry(root, width=50, bg="gray", fg="white")
e.pack()

#default text in input box
e.insert(0, "Enter your Name: ")

clk_btn = Button(root, text="Save Name", command=click_btn, padx=45, pady=22.5)
clk_btn.pack()


root.mainloop()

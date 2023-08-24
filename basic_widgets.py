import tkinter as tk
from tkinter import ttk

#create window
root = tk.Tk()
root.title("Tutorial")
root.geometry("800x500")


#functions
def say_hello():
    print("Hello")


#create widgets
text = tk.Text(master=root)
text.pack()

#ttk label
label = ttk.Label(root, text="This is a text")
label.pack()

#ttk entry
entry = ttk.Entry(master=root)
entry.pack()

text2 = ttk.Label(master=root, text='my label')
text2.pack()

#ttk button
btn = ttk.Button(master=root, text="Save", command=root.quit)
btn.pack()

# btn2 = ttk.Button(master=root, text="hello", command=say_hello)
btn2 = ttk.Button(master=root, text="Hello", command=lambda: print("Hello"))
btn2.pack()
#Maintain window
root.mainloop()
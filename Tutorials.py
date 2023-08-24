import tkinter as tk
from tkinter import ttk
#create window
root = tk.Tk()
root.title("Tutorial")
root.geometry("800x500")

#create widgets
text = tk.Text(master=root)
text.pack()

#ttk label
label = ttk.Label(root, text="This is a text")c d
label.pack()

#ttk entry
entry = ttk.Entry(master=root)
entry.pack()

#ttk button
btn = ttk.Button(master=root, text="Save", command=root.quit)
btn.pack()


#Maintain window
root.mainloop()

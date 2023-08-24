import tkinter as tk
from tkinter import ttk

# window
root = tk.Tk()
root.title("Getting and setting widgets")

# functions
def button_func():
    entry_text = entry.get()
    # Update the Label
    #label.configure(text="some other text")
    label['text'] = entry_text
    entry.configure(state='disabled')

def button_func_2():
    # label.configure(text="I am Groot")
    label['text'] = 'I am Groot'
    # entry.configure(state='enabled')
    entry['state'] = 'enabled'
    entry.delete(0, 'end')


# widgets
label = ttk.Label(master=root, text="I am Groot")
label.pack()

entry = ttk.Entry(master=root)
entry.pack()

button = ttk.Button(master=root, text="Click Me", command=button_func)
button.pack()

button2 = ttk.Button(master=root, text="Reset", command=button_func_2)
button2.pack()
# run
root.mainloop()

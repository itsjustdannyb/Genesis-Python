from tkinter import *
from PIL import ImageTk, Image
window = Tk()
window.title("The Comment Section")
window.iconbitmap("C:/Users/user/Downloads/Bams/quote.ico")

button_quit =Button(window, text="Exit Program", command=window.quit)
button_quit.pack()

#Images
my_img = ImageTk.PhotoImage(Image.open("baby panda.jpg"))
my_label = Label(image=my_img)
my_label.pack()


window.mainloop()


from tkinter import *
from PIL import ImageTk, Image

#main window
root = Tk()
root.title("Views")

#functions
def forward(image_number):
    global image_label
    global forward_btn
    global backward_btn

    image_label.grid_forget()
    image_label = Label(image=image_list[image_number], width=500, height=500)
    image_label.grid(row=0, column=0, columnspan=3)

    forward_btn = Button(root, text=">>", command=lambda: forward(image_number + 1))
    forward_btn.grid(row=1, column=2)

    backward_btn = Button(root, text="<<", command=lambda: forward(image_number - 1))
    forward_btn.grid(row=1, column=0)

    if image_number == 3:
        forward_btn = Button(root, text=">>", state=DISABLED)


    return

def backward():
    global image_label
    global forward_btn
    global backward_btn

    return


#Images
image_1 = ImageTk.PhotoImage(Image.open("images/baby panda.jpg"))
image_2 = ImageTk.PhotoImage(Image.open("images/Naruto_watercolor.jpg"))
image_3 = ImageTk.PhotoImage(Image.open("images/luffy_onepiece.jpg"))
image_4 = ImageTk.PhotoImage(Image.open("images/Suka_one piece.jpg"))


#scrolling
image_list = [image_1, image_2, image_3, image_4]


image_label = Label(image=image_1, width=500, height=500)
image_label.grid(row=0, column=0, columnspan=3)

#Buttons
backward_btn = Button(root, text="<<", command=backward)
exit_btn = Button(root, text="Leave", command=root.quit)
forward_btn = Button(root, text=">>", command=lambda: forward(1))


backward_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1)
forward_btn.grid(row=1, column=2)


#Leave window open
root.mainloop()

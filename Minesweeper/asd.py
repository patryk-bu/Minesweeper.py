from tkinter import *


def left(event):
    root.title('clicked left')
    btn1.config(fg='blue')


def right(event):
    root.title('clicked right')
    btn1.config(fg='red')


root = Tk()
root.title('click left or right on button')
btn1 = Button(root, text=' Click on me ... ', width=40)
btn1.pack()
btn1.bind('<Button-1>', left)  # bind left mouse click
btn1.bind('<Button-3>', right)  # bind right mouse click
root.mainloop()
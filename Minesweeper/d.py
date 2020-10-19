from tkinter import *
window = Tk ()
window.title(" ")
window.geometry('600x600')

# Creating the square frame
square_frame = Frame(window, width=100, height=100)
square_frame.grid(column=0, row=0)

# Creating a button inside this frame
btn = Button(square_frame, text ="X", bg = "white")
btn.config(height = 15, width = 15)
btn.grid(column = 0, row = 0)

window.mainloop()
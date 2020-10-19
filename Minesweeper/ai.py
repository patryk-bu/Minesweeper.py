import gui as g
import tkinter as tk
import random as r
import pyautogui as auto


class player:
    def __init__(self):
        self.to_click = ()

    def get_origin(self):
        self.to_click = (r.randrange(3840), r.randrange(2160))
        while not game.origin_clicked:
            self.right_click(self.to_click)
            self.to_click = (r.randrange(3840), r.randrange(2160))

    def left_click(self, coords):
        auto.click(x=coords[0], y=coords[1])

    def right_click(self, coords):
        auto.click(x=coords[0], y=coords[1], button="right")


root = tk.Tk()  # Tkinter window is created
root.lift()
root.attributes("-topmost", True)  # window geometry and attributes are set
game = g.App(root)
game.mainloop()
p = player()
p.get_origin()

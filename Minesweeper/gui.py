import tkinter as tk
import logic as log
import pyautogui as auto
from PIL import Image, ImageTk

field = log.mine_field()


class App(tk.Tk):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.buttons = []
        self.ai_mode = True
        self.image = tk.PhotoImage()
        self.origin_clicked = False
        self.window()  # tkinter window/properties are assigned
        self.to_click = ()

    def window(self):
        column_val = 19
        row = 0  # row is set to 0
        column = 0  # column is set to 0
        for i in range(0,len(field.squares)):  # for i ranging from 0 to length of seats_(list of all seats)

            self.buttons.append(tk.Button(self.parent, text=" ", background="gray"))
            self.buttons[i].grid(row=row, column=column)  # button layout is in a grid
            self.buttons[i].config(height=50, width=50, image=self.image, compound="center")
            #if field.squares[i].is_bomb:
                #self.buttons[i].configure(background="red", text=(field.squares[i].value, "b"))
            column += 1  # one is added for creation of next button in grid
            if column == column_val:  # if column = column_val from database(admin inputted config)
                column = 0  # column is set to 0
                row += 1  # 1 is added to row starting the next row of buttons

            self.buttons[i].bind("<Button-1>", self.on_click)
            self.buttons[i].bind("<Button-2>", self.ai)
            self.buttons[i].bind("<Button-3>", self.flag)
            field.squares[i].button = self.buttons[i]

    def flag(self, event):
        pos = self.buttons.index(event.widget)

        clicked = field.get_obj_by_val(pos)
        if clicked not in field.flagged:
            field.flagged.append(clicked)
            btn_index = field.squares.index(clicked)
            self.buttons[btn_index].configure(background="orange")
        else:
            btn_index = field.squares.index(clicked)
            self.buttons[btn_index].configure(background="gray")
            field.flagged.remove(clicked)

    def on_click(self, event):
        self.get_positions()
        pos = self.buttons.index(event.widget)
        is_bomb = field.click_on_obj(field.get_obj_by_val(pos))
        # print(field.uncovered)
        if is_bomb:
            self.end()
            self.parent.grab_set()
        # else:
        for i in field.uncovered:
            btn_index = field.squares.index(i)
            self.buttons[btn_index].configure(background="white", state="disabled", text=" ")
            field.disabled.append(i)
        for i in field.edge:
            btn_index = field.squares.index(i)
            self.buttons[btn_index].configure(text=i.value, background="light gray", state="disabled")
            field.disabled.append(i)

    def end(self):
        self.parent.grab_set()
        # print("LOSE")
        for i in field.squares:
            if i.is_bomb:
                x = field.squares.index(i)
                self.buttons[x].configure(background="red")

        for i in self.buttons:
            i.configure(state="disabled")
        self.parent.grab_set()

    def get_positions(self):
        for i in self.buttons:
            x = i.winfo_rootx() + 30
            y = i.winfo_rooty() + 30
            # print(x, y)
            sqr_index = self.buttons.index(i)
            field.squares[sqr_index].pixel_pos = (x, y)

    def left_click(self, coords):
        auto.click(x=coords[0], y=coords[1])

    def right_click(self, coords):
        auto.click(x=coords[0], y=coords[1], button="right")

    def ai(self, event):
        to_flag = []
        # print("running")
        for i in field.edge:
            i.button.configure(background="blue")
            around = []
            for j in i.around:
                print("centre: ", i.id, "analysing: ", j.id)
                if j not in field.disabled:
                    if j not in field.flagged:
                        print("true")
                        around.append(j)
                        if len(around) == i.value:
                            to_flag.append(j)
                            print("flag ", j.id)

        to_flag = list(dict.fromkeys(to_flag))
        for i in to_flag:
            self.right_click(i.pixel_pos)
        for i in field.squares:
            if i.is_bomb:
                i.button.configure(background="red", text=(i.id, "b"))
            else:
                i.button.configure(text=i.id)


if __name__ == "__main__":
    root = tk.Tk()  # Tkinter window is created
    root.lift()
    root.attributes("-topmost", True)  # window geometry and attributes are set
    app = App(root)
    app.mainloop()

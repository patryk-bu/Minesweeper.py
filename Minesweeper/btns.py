import tkinter as tk
import logic as log
import pyautogui as auto

field = log.mine_field()


class App(tk.Tk):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.buttons = []
        self.frames = ""
        self.ai_mode = False
        self.origin_clicked = False
        self.window()  # tkinter window/properties are assigned
        self.to_click = ()

    def window(self):
        column_val = 19
        row = 0  # row is set to 0
        column = 0  # column is set to 0

        self.frames = (tk.Frame(self.parent, width=100, height=100))
        self.frames.grid_propagate = False
        self.frames.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        for i in range(0, len(field.squares)):  # for i ranging from 0 to length of seats_(list of all seats)
            self.buttons.append(tk.Button(self.frames, text="", background="gray"))
            self.buttons[i].grid(row=0, column=0)  # button layout is in a grid
            self.buttons[i].grid(sticky="nesw")
            """column += 1  # one is added for creation of next button in grid
            if column == column_val:  # if column = column_val from database(admin inputted config)
                column = 0  # column is set to 0
                row += 1  # 1 is added to row starting the next row of buttons
            if not self.ai_mode:
                self.buttons[i].bind("<Button-1>", self.on_click)
                self.buttons[i].bind("<Button-2>", self.flag)
                self.buttons[i].bind("<Button-3>", self.flag)
            else:
                self.buttons[i].bind("<Button-1>", self.check_origin_click)

        # print(self.buttons)"""

    def check_origin_click(self, event):
        self.get_origin()
        pos = self.buttons.index(event.widget)
        if pos == 0:
            self.origin_clicked = True
            self.ai_mode = False
            self.window()

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
        pos = self.buttons.index(event.widget)
        is_bomb = field.click_on_obj(field.get_obj_by_val(pos))
        # print(field.uncovered)
        if is_bomb:
            self.end()
            self.parent.grab_set()
        # else:
        for i in field.uncovered:
            btn_index = field.squares.index(i)
            self.buttons[btn_index].configure(background="white", state="disabled")
        for i in field.edge:
            btn_index = field.squares.index(i)
            self.buttons[btn_index].configure(text=i.value, background="light gray", state="disabled")

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

    def get_origin(self):
        # y add 60,  x add 50
        x = self.parent.winfo_x() + 20
        y = self.parent.winfo_y() + 75
        for i in self.buttons:
            print(i.winfo_x(), i.winfo_y())


    def left_click(self, coords):
        auto.click(x=coords[0], y=coords[1])

    def right_click(self, coords):
        auto.click(x=coords[0], y=coords[1], button="right")


if __name__ == "__main__":
    root = tk.Tk()  # Tkinter window is created
    root.lift()
    root.attributes("-topmost", True)  # window geometry and attributes are set
    app = App(root)
    app.mainloop()

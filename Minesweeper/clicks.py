import tkinter as tk
def do_popup():
    root.menu.post(??,??)
root = tk.Tk()
root.btn1 = tk.Button(root, text="POPUP", command=do_popup)
root.btn1.grid(row=1, column=1)
root.menu = tk.Menu(root, tearoff=0)
root.menu.add_command(label="a")
root.menu.add_command(label="b")
root.menu.add_command(label="c")
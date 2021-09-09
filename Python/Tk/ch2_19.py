# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch2_19")

html_gif = PhotoImage(file="60019.gif")
# html_gif = PhotoImage(file="10050_100.png")
label = Label(root,image=html_gif)
label.pack()
root.mainloop()
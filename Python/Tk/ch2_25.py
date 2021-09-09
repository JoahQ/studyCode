# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch2_25")
label = Label(root,text="I like Tkinter")
label.pack()
print(label.keys())

root.mainloop()
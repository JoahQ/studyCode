# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch8_1")

for fm in ["red","green","blue"]:
    # Frame(root,bg=fm,height=50,width=250).pack()
    Frame(bg=fm,height=50,width=250).pack()

root.mainloop()
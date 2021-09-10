# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch3_35")

Colors = ["red","orange","yellow","green","blue","purple"]

r = 0
for color in Colors:
    Label(root,text=color,relief="groove",width=20).grid(row=r,column=0)
    Label(root,bg=color,relief="ridge",width=100).grid(row=r,column=1)
    r += 1

root.mainloop()
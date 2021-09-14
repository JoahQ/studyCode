# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch8_1")

fms = {"red":"cross","green":"boat","blue":"clock"}
for fm in fms:
    Frame(root,bg=fm,cursor=fms[fm],height=50,width=250).pack(side=LEFT)
    # Frame(bg=fm,height=50,width=250).pack()

root.mainloop()
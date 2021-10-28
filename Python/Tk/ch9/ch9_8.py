# -*- coding: utf-8 -*-
from Tkinter import *

def printInfo():
    print sp.get()

root = Tk()
root.title("ch9_8")

sp = Spinbox(root,values=(10,38,170,101),command=printInfo)

sp.pack(pady=10,padx=10)

root.mainloop()
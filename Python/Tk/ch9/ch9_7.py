# -*- coding: utf-8 -*-
from Tkinter import *

def printInto():
    print sp.get()

root = Tk()
root.title("ch9_7")

sp = Spinbox(root,from_=0,to = 10,command=printInto)

sp.pack(pady=10,padx=10)

root.mainloop()

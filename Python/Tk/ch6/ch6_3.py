# -*- coding: utf-8 -*-
from Tkinter import *

def callback(*args):
    xl.set(xE.get())
    print "data changed : ",xE.get()

root = Tk()
root.title("ch6_3")

xE = StringVar()
entry = Entry(root,textvariable=xE)
entry.pack(padx=10,pady=5)
xE.trace("w",callback)

xl = StringVar()
label = Label(root,textvariable=xl)
xl.set("同步显示")
label.pack(padx=10,pady=5)

root.mainloop()
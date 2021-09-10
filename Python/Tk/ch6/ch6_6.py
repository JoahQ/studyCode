# -*- coding: utf-8 -*-
from Tkinter import *

def callbackW(name,index,mode):
    xL.set(xE.get())
    print "name = %r, index = %r, mode = %r" % (name,index,mode)

root = Tk()
root.title("ch6_6")

xE = StringVar()

entry = Entry(root,textvariable=xE)
entry.pack(pady=15,padx=20)
xE.trace("w",callbackW)

xL = StringVar()
lab = Label(root,textvariable=xL)
xL.set("同步显示")
lab.pack(pady=5,padx=10)

root.mainloop()
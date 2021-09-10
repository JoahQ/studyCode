# -*- coding: utf-8 -*-
from Tkinter import *

def callbackW(*args):
    xl.set(xE.get())

def callbackR(*args):
    print "Warning: 数据被读取！"

def hit():
    print "读取数据：",xE.get()

root = Tk()
root.title("ch6_5")

xE = StringVar()
entry = Entry(root,textvariable=xE)
entry.pack(padx=10,pady=5)
xE.trace("w",callbackW)
xE.trace("r",callbackR)

xl = StringVar()
label = Label(root,textvariable=xl)
xl.set("同步显示")
label.pack(padx=10,pady=5)

btn = Button(root,text="读取",command=hit)
btn.pack(pady=5)

root.mainloop()
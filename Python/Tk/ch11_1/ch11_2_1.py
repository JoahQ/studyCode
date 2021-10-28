#-*-coding: utf-8 -*-
from Tkinter import *

def mouseMotion(event):
    x1 = event.x
    y1 = event.y
    textVar = "Mouse location - x:{},y:{}".format(x1,y1)
    var.set(textVar)

root = Tk()
root.title("ch11_2_1")
root.geometry("300x180")

x,y = 0,0
var = StringVar()
text = "Mouse location - x:{},y:{}".format(x,y)
var.set(text)

lab = Label(root,textvariable=var)
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)

root.bind("<Motion>",mouseMotion)
root.mainloop()
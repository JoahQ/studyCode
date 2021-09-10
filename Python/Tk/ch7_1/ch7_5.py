# -*- coding: utf-8 -*-
from Tkinter import *

def printSelection():
    label.config(text=u"你选择的是"+var.get())

root = Tk()
root.title("ch7_5")

img1 = PhotoImage(file="1.gif")
img2 = PhotoImage(file="2.gif")
img3 = PhotoImage(file="3.gif")

var = StringVar()
var.set("1")

label = Label(root,text="这是默认值，尚未选择",bg="lightyellow",width=30)
label.pack()

rb1 = Radiobutton(root,image=img1,
                  variable=var,value="1",
                  command=printSelection)
rb1.pack()

rb2 = Radiobutton(root,image=img2,
                  variable=var,value="2",
                  command=printSelection)
rb2.pack()

rb3 = Radiobutton(root,image=img3,
                  variable=var,value="3",
                  command=printSelection)
rb3.pack()

root.mainloop()
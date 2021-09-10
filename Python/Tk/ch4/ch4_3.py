# -*- coding: utf-8 -*-
from Tkinter import *

def msgShow():
    label.configure(text="I love Python",bg="lightyellow",fg="blue")

root = Tk()
root.title("ch4_3")
label = Label(root)
btn1 = Button(root,text="打印消息",command=msgShow)
btn2 = Button(root,text="结束",width=15,command=root.destroy)
label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)

root.mainloop()
# -*- coding: utf-8 -*-
from Tkinter import *

def printSelection():
    label.config(text=u"你是"+var.get())

root = Tk()
root.title("ch7_1")

var = StringVar()
var.set("男生")

label = Label(root,text="这是预设，尚未选择",bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生",variable=var,value="男生",command=printSelection)
rbman.pack()

rbman = Radiobutton(root,text="女生",variable=var,value="女生",command=printSelection)
rbman.pack()

root.mainloop()

# -*- coding: utf-8 -*-
from Tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"

root = Tk()
root.title("ch4_1")
label = Label(root)
btn = Button(root,text="打印消息",command=msgShow)
label.pack()
btn.pack()

root.mainloop()
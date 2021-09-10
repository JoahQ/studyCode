# -*- coding: utf-8 -*-
from Tkinter import *

def msgShow():
    label.configure(text="I love Python",bg="lightyellow",fg="blue")

root = Tk()
root.title("ch4_2")
label = Label(root)
# btn = Button(root,text="打印消息",command=msgShow)
flowerGif = PhotoImage(file="flower.gif")
# btn = Button(root,image=flowerGif,command=msgShow)
# btn = Button(root,image=flowerGif,command=msgShow,text="Click Me",compound=TOP)
# btn = Button(root,image=flowerGif,command=msgShow,text="Click Me",compound=CENTER)
# btn = Button(root,image=flowerGif,command=msgShow,text="Click Me",compound=RIGHT)
btn = Button(root,image=flowerGif,command=msgShow,text="Click Me",compound=LEFT,cursor="star")
label.pack()
btn.pack()

root.mainloop()
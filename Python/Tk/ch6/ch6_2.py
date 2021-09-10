# -*- coding: utf-8 -*-
from Tkinter import *

def btn_hit():
    global msg_on
    if x.get() == "":
        x.set("I like Tkinter")
    else:
        x.set("")

root = Tk()
root.title("ch6_1")

msg_on = False
x = StringVar()

label = Label(root,textvariable=x,fg="blue",bg="lightyellow",font="Verdana 16 bold",width=25,height=2)
label.pack()
btn = Button(root,text="Click Me",command=btn_hit)
btn.pack()



root.mainloop()
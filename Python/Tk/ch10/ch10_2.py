#-*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch10_2")

var = StringVar()
msg = Message(root, textvariable=var, relief=RAISED)
var.set("2016年12月，我一个人订了机票和船票，开始我的南极旅行")
msg.config(bg="yellow")

msg.pack(padx=10,pady=10)

root.mainloop()
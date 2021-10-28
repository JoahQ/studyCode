#-*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch10_1")

myText = "2016年12月，我一个人订了机票和船票，开始我的旅行"

msg = Message(root,bg="yellow",text=myText,font = "times 12 italic")
msg.pack(padx=10,pady=10)

root.mainloop()
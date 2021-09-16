#-*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch8_7")

msg = "欢迎进入Silicon Stone Educaition系统"
ssGif = PhotoImage(file="sse.gif")

logo = Label(root,image=ssGif,text=msg,compound=BOTTOM)
logo.pack()

# 以下是LabelFrame标签框架
labFrame = LabelFrame(root,text="数据验证")
accountL = Label(labFrame,text="Account")
accountL.grid(row=0,column=0)

pwdL = Label(labFrame,text="Password")
pwdL.grid(row=1,column=0)

accountE = Entry(labFrame)
accountE.grid(row=0,column=1)

pwdE = Entry(labFrame,show="*")
pwdE.grid(row=1,column=1,pady=10)

labFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)

root.mainloop()
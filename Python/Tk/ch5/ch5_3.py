# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch5_3")

msg = "欢迎进入Sillicon Stone Education系统"

sseGif = PhotoImage(file="sse.gif")
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
accountL = Label(root,text="Account")
accountL.grid(row=1)

pwdL = Label(root,text="Password")
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = Entry(root)
pwdE = Entry(root,show="*")
accountE.grid(row=1,column=1)
pwdE.grid(row=2,column=1,pady=10)

root.mainloop()
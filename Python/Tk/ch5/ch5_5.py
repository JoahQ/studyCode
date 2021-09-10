# -*- coding: utf-8 -*-
from Tkinter import *

def printInfo():
    print "Account: %s\nPassword: %s" % (accountE.get(),pwdE.get())

root = Tk()
root.title("ch5_4")

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
accountE.insert(0,"Kevin")
pwdE.insert(0,"pwd")
accountE.grid(row=1,column=1,sticky=W)
pwdE.grid(row=2,column=1,pady=10,sticky=W)

#以下建立Login和Quit
loginbtn = Button(root,text="Login",command=printInfo)
loginbtn.grid(row=3,column=0,sticky=E,pady=5)
quitbtn = Button(root,text="Qiut",command=root.quit)
quitbtn.grid(row=3,column=1,sticky=W,pady=5)

root.mainloop()
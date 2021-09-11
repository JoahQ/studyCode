# -*- coding: utf-8 -*-
from Tkinter import *

#以下是callback方法
def selAll():
    entry.select_range(0,END)

def delSel():
    entry.select_clear()

def crl():
    entry.delete(0,END)

def readonly():
    if var.get() == True:
        entry.config(state=DISABLED)
    else:
        entry.config(state=NORMAL)


root = Tk()
root.title("ch7_9")

#以下row=0建立Entry
entry = Entry(root)
entry.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=W)

btnSel = Button(root,text="选取",command=selAll)
btnSel.grid(row=1,column=0,padx=5,pady=5,sticky=W)

btnDesel = Button(root,text="取消选取",command=delSel)
btnDesel.grid(row=1,column=1,padx=5,pady=5,sticky=W)

btnCl = Button(root,text="删除",command=crl)
btnCl.grid(row=1,column=2,padx=5,pady=5,sticky=W)

btnQuit = Button(root,text="结束",command=root.destroy)
btnQuit.grid(row=1,column=3,padx=5,pady=5,sticky=W)

var = BooleanVar()
var.set(False)

chkReadonly = Checkbutton(root,text="只读",variable=var,command=readonly)
chkReadonly.grid(row=2,column=0)

root.mainloop()
#-*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox

def leave(event):
    ret = tkMessageBox.askyesno("ch11_4","是否离开？")
    if ret == True:
        root.destroy()
    else:
        return

root = Tk()
root.title("ch11_4")

root.bind("<Escape>",leave)
lab = Label(root,text="测试Escape键",bg="yellow",fg="blue",height=4,width=20,font="Times 12 bold")
lab.pack(padx=30,pady=30)

root.mainloop()

#-*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox

def myMsg1():
    ret = tkMessageBox.askyesnocancel("Test1","安装失败，再试一次？")
    print "安装失败",ret

def myMsg2():
    ret = tkMessageBox.askyesnocancel("Test2","编辑完成，是或否或取消？")
    print "编辑完成",ret

root = Tk()
root.title("ch10_4")

Button(root,text="安装失败",command = myMsg1).pack()
Button(root,text="编辑完成",command = myMsg2).pack()

root.mainloop()
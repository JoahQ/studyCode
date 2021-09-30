#-*- coding: utf-8 -*-
from Tkinter import *

def printInfo():
    print("垂直尺度值 = %d，水平尺度值 = %d" % (sV.get(),sH.get()))

root = Tk()
root.title("ch9_3")

sV = Scale(root,label = "垂直",from_=0,to = 10)
sV.set(5)
sV.pack()

sH = Scale(root,label="水平",from_=0,to=10,length=300,orient=HORIZONTAL)
sH.set(3)
sH.pack()

Button(root,text="Print",command=printInfo).pack()
root.mainloop()
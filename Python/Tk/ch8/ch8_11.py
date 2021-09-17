#-*- coding: utf-8 -*-
from Tkinter import *
import random

root = Tk()
root.title("ch8_11")

msgYes,msgNo,msgExit = 1,2,3
def MessageBox():
    msgType = random.randint(1,3)
    if msgType == msgYes:
        labTxt = 'Yes'
    elif msgType == msgNo:
        labTxt = 'No'
    elif msgType == msgExit:
        labTxt = 'Exit'
    tl = Toplevel()
    tl.geometry("300x180")
    tl.title("Message Box")
    Label(tl,text=labTxt).pack(fill=BOTH,expand=True)

btn = Button(root,text='Click Me',command=MessageBox)
btn.pack()

root.mainloop()


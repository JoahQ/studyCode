#-*- coding:utf-8 -*-
from Tkinter import *

def callback(envent):
    print "Clicked at",envent.x,envent.y


root = Tk()
root.title("ch11_2")
frame = Frame(root, width=300,height=180)
frame.bind("<Button-1>",callback)
frame.pack()

root.mainloop()
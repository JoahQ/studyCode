#-*- coding: utf-8 -*-
from Tkinter import *
def printInfo():
    print sp.get()

root = Tk()
root.title("ch9_9")

cities = ("新加坡","上海","东京")

sp = Spinbox(root,values=cities,command=printInfo)

sp.pack(pady=10,padx=10)

root.mainloop()
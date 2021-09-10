# -*- coding: utf-8 -*-
from Tkinter import *

def printSelection():
    print cities[var.get()]

root = Tk()
root.title("ch7_3")
cities = {0:"京东",1:"纽约",2:"巴黎",3:"伦敦",4:"香港"}

var = IntVar()
var.set(0)

label = Label(root,text="选择最喜欢的城市",fg="blue",bg="lightyellow",width=30).pack()

for val,city in cities.items():
    Radiobutton(root,
                text=city,
                indicatoron=0,#用盒子取代选项按钮
                width=30,
                variable=var,
                value=val,
                command=printSelection).pack()

root.mainloop()
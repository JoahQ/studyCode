# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch2_1")

screenwidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 300
h = 100
x = (screenwidth - w) / 2
y = (screenHeight - h) / 2
root.geometry("%dx%d+%d+%d" % (w,h,x,y))
label = Label(root,text="I like tkinter")
label.pack()    #包装与定位组件
print(type(label))  #传回Label数据类型
print(label)  #传回Label数据类型
root.mainloop()
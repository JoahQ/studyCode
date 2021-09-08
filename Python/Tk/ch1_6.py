# -*- coding: utf-8 -*-
# ch1_1.py
from Tkinter import *

root = Tk()
root.title("窗口标题")
screenwidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 300
h = 100
x = (screenwidth - w) / 2
y = (screenHeight - h) / 2
root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.configure(bg='#00ff00')#窗口背景颜色
root.iconbitmap("001.ico")#更改图标
root.mainloop()
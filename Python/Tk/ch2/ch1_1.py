# -*- coding: utf-8 -*-
# ch1_1.py
from Tkinter import *

root = Tk()
root.title("窗口标题")
# root.geometry("300x160")#窗口大小
# root.geometry("300x160+400+400")#窗口位置 距离屏幕左上角(400,400)
root.geometry("%dx%d+%d+%d" % (700,300,100,100))#窗口位置 距离屏幕左上角(400,400)
# root.configure(bg='yellow')#窗口背景颜色
root.configure(bg='#00ff00')#窗口背景颜色
root.iconbitmap("001.ico")#更改图标
root.mainloop()
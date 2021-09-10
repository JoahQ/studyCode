#-*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch2_17")
root.geometry("%dx%d+%d+%d" % (700,300,100,100))#窗口位置 距离屏幕左上角(400,400)
label = Label(root,text="raised",height=4,width=20,relief="raised")
label.pack()
root.mainloop()
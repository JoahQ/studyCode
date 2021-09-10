#-*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch2_18")
root.geometry("%dx%d+%d+%d" % (700,300,100,100))#窗口位置 距离屏幕左上角(400,400)
label = Label(root,text="raised",relief="raised",
              bg="lightyellow",padx=120,pady=50)
label.pack()
root.mainloop()
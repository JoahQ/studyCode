# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch2_24---Coursor属性设置光标形状")
root.geometry("%dx%d+%d+%d" % (700,300,100,100))#窗口位置 距离屏幕左上角(400,400)
# label = Label(root,text="raised",relief="raised",
#               bg="lightyellow",
#               padx = 100,pady=100,
#               cursor="heart")

label = Label(root,text="raised",relief="raised",
              bg="lightyellow",
              padx = 100,pady=100,
              cursor="bogosity")

label.pack()
root.mainloop()
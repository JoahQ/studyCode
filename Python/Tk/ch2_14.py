# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch2_14")
# lab = Label(root,bitmap="hourglass",
#             compound="left",text=u"我的天空")

# lab = Label(root,bitmap="hourglass",
#             compound="top",text=u"我的天空")

lab = Label(root,bitmap="hourglass",
            compound="center",text=u"我的天空")
lab.pack()

root.mainloop()
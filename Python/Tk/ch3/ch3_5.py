# -*- coding: utf-8 -*-
from Tkinter import *

Reliefs = ["flat","groove","raised","ridge","solid","sunken"]

root = Tk()
root.title("ch3_5")

for Relief in Reliefs:
    Label(root,text=Relief,relief=Relief,
          fg="blue",
          font="Times 20 bold").pack(side=LEFT,padx=5)

bitMaps = ["error","hourglass","info","questhead","question","warning","gray12","gray25","gray50","gray75"]

for bitMap in bitMaps:
    Label(root,bitmap=bitMap).pack(side=LEFT,padx=5)

root.mainloop()
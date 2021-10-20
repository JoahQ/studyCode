#-*- coding: utf-8 -*-
from Tkinter import *

def bgUpdate(source):
    """更改窗口背景颜色"""
    red = rSlider.get()
    green = gSlider.get()
    blue = bSlider.get()
    print("Red=%d, Green=%d, Blue=%d" % (red,green,blue))
    myColor = "#%02x%02x%02x" % (red,green,blue)
    root.config(bg=myColor)

root = Tk()
root.title("ch9_5")
root.geometry("360x240")

fm = Frame(root)
fm.pack()

rSlider = Scale(fm, from_=0, to=255, command=bgUpdate)
gSlider = Scale(fm, from_=0, to=255, command=bgUpdate)
bSlider = Scale(fm, from_=0, to=255, command=bgUpdate)

gSlider.set(125)
rSlider.grid(row=0, column=0)
gSlider.grid(row=0, column=1)
bSlider.grid(row=0, column=3)

root.mainloop()
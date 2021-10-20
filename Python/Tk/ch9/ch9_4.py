#-*- coding: utf-8 -*-
from Tkinter import *

def bgUpdate(source):
    '''更改窗口背景颜色'''
    red = rSlider.get()
    green = gSlider.get()
    blue = bSlider.get()
    print("R=%d, G=%d,B=%d" % (red,green,blue))
    myColor = "#%02x%02x%02x" % (red,green,blue)
    root.config(bg=myColor)

root = Tk()
root.title("ch9_4")
root.geometry("360x240")

rSlider = Scale(root,from_=0,to=255,command=bgUpdate)
gSlider = Scale(root,from_=0,to=255,command=bgUpdate)
bSlider = Scale(root,from_=0,to=255,command=bgUpdate)

gSlider.set(125)
rSlider.grid(row=0,column=0)
gSlider.grid(row=0,column=1)
bSlider.grid(row=0,column=3)

root.mainloop()
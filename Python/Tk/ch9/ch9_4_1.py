#-*- coding: utf-8 -*-
from Tkinter import *
# from ttk import *
from tkColorChooser import *

def bgUpdate():
    '''更改窗口背景颜色'''
    myColor = askcolor()
    print(type(myColor),myColor)
    root.config(bg=myColor[1])

root = Tk()
root.title("ch9_4_1")
root.geometry("360x240")

btn = Button(text="Select Color",command=bgUpdate)
btn.pack(pady=5)

root.mainloop()
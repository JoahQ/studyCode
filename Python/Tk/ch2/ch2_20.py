# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch2_20")
sseText = """SSE全名是Silicon Stone Education，
这家公司在美国，这是国际专业征服公司，产品多元与丰富。
SSE全名是Silicon Stone Education，这家公司在美国，这是国际专业征服公司，产品多元与丰富。"""

ssgif = PhotoImage(file="60019.gif")
# label = Label(root,text=sseText,image=ssgif,bg="lightyellow",compound="left")
# label = Label(root,text=sseText,image=ssgif,bg="lightyellow",justify="left",compound="right")
label = Label(root,text=sseText,image=ssgif,bg="lightyellow",justify="left",compound="center")

label.pack()

root.mainloop()
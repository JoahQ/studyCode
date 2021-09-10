# -*- coding: utf-8 -*-
from Tkinter import *

win = Tk()
win.title("ch3_36")

lab1 = Label(win,text="明志科技大学",bg="lightyellow",width=15)
lab2 = Label(win,text="长庚大学",bg="lightgreen",width=15)
lab3 = Label(win,text="长庚科技大学",bg="lightblue",width=15)

lab1.place(x=0,y=0)
lab2.place(x=30,y=50)
lab3.place(x=60,y=100)

win.mainloop()
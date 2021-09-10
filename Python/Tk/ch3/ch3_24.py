# -*- coding: utf-8 -*-
from Tkinter import *

window = Tk()
window.title("ch3_14")

lab1 = Label(window,text="明志科技大学",bg="lightyellow",width=15)
lab2 = Label(window,text="长庚大学",bg="lightgreen",width=15)
lab3 = Label(window,text="长庚科技大学",bg="lightblue",width=15)

# lab1.grid(row=0,column=0)
# lab2.grid(row=1,column=0)
# lab3.grid(row=1,column=1)

lab1.grid(row=0,column=0)
lab2.grid(row=1,column=2)
lab3.grid(row=2,column=1)

window.mainloop()
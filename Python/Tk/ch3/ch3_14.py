# -*- coding: utf-8 -*-
from Tkinter import *

window = Tk()
window.title("ch3_14")

lab1 = Label(window,text="明志科技大学",bg="lightyellow",width=15)
lab2 = Label(window,text="长庚大学",bg="lightgreen",width=15)
lab3 = Label(window,text="长庚科技大学",bg="lightblue",width=15)

# lab1.pack()
# lab2.pack(fill=BOTH)
# lab3.pack()
# lab1.pack(side=LEFT,fill=Y)
# lab2.pack(fill=X)
# lab3.pack(fill=X)

# lab1.pack(side=LEFT,fill=Y)
# lab2.pack(fill=BOTH)
# lab3.pack(fill=BOTH)
lab1.pack(side=LEFT,fill=Y)
lab2.pack(fill=BOTH,expand=True)
lab3.pack(fill=BOTH,expand=True)

window.mainloop()
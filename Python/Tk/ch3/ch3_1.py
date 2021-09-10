# -*- coding: utf-8 -*-
from Tkinter import *

window = Tk()
window.title("ch3_1")

lab1 = Label(window,text="明志科技大学",bg="lightyellow",width=15)
lab2 = Label(window,text="长庚大学",bg="lightgreen",width=15)
lab3 = Label(window,text="长庚科技大学",bg="lightblue",width=15)

# lab1.pack(side=BOTTOM)
# lab2.pack(side=BOTTOM)
# lab3.pack(side=BOTTOM)

# lab1.pack(side=LEFT)
# lab2.pack(side=LEFT)
# lab3.pack(side=LEFT)

# lab1.pack()
# lab2.pack(side=RIGHT)
# lab3.pack(side=LEFT)

# lab1.pack(fill=X,pady=10)
# lab2.pack(pady=10)
# lab3.pack(fill=X)

# lab1.pack(padx=50)
# lab2.pack(padx=50)
# lab3.pack(fill=X)

lab1.pack()
lab2.pack(ipadx=10)
lab3.pack(ipady=10)

window.mainloop()
# -*- coding: utf-8 -*-
from Tkinter import *

window = Tk()
window.title("ch3_26")

lab1 = Label(window,text="标签1",relief="raised")
lab2 = Label(window,text="标签2",relief="raised")
lab3 = Label(window,text="标签3",relief="raised")
lab4 = Label(window,text="标签4",relief="raised")
lab5 = Label(window,text="标签5",relief="raised")
lab6 = Label(window,text="标签6",relief="raised")
lab7 = Label(window,text="标签7",relief="raised")
lab8 = Label(window,text="标签8",relief="raised")


lab1.grid(row=0,column=0,padx=10,pady=10)
lab2.grid(row=0,column=1,padx=10,pady=10)
lab3.grid(row=0,column=2,padx=10,pady=10)
lab4.grid(row=0,column=3,padx=10,pady=10)
lab5.grid(row=1,column=0,padx=10,pady=10)
lab6.grid(row=1,column=1,padx=10,pady=10)
lab7.grid(row=1,column=2,padx=10,pady=10)
lab8.grid(row=1,column=3,padx=10,pady=10)

window.mainloop()
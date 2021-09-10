# -*- coding: utf-8 -*-
from Tkinter import *

window = Tk()
window.title("ch3_21")
# window.geometry("300x200")

# lab1 = Label(window,text="Mississippi",bg="red",fg="white",
#              font="Times 24 bold").pack(fill=X)
# lab2 = Label(window,text="Kentucky",bg="green",fg="white",
#              font="Arial 24 bold italic").pack(fill=BOTH,expand=True)
# lab3 = Label(window,text="Purdue",bg="blue",fg="white",
#              font="Times 24 bold").pack(fill=X)

lab1 = Label(window,text="Mississippi",bg="red",fg="white",
             font="Times 24 bold").pack(side=LEFT,fill=Y)
lab2 = Label(window,text="Kentucky",bg="green",fg="white",
             font="Arial 24 bold italic").pack(side=LEFT,fill=BOTH,expand=True)
lab3 = Label(window,text="Purdue",bg="blue",fg="white",
             font="Times 24 bold").pack(side=LEFT,fill=Y)

window.mainloop()
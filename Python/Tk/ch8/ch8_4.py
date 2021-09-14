#-*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch8_4")

fm1 = Frame(root,width=800,height=800,bg="red",relief=GROOVE,borderwidth=10)
fm1.pack(side=LEFT,padx=5,pady=5)

fm2 = Frame(fm1,width=400,height=400,bg="blue",relief=RAISED,borderwidth=10)
fm2.pack(side=LEFT,padx=5,pady=5)

fm2 = Frame(fm2,width=300,height=300,bg="green",relief=RIDGE,borderwidth=10)
fm2.pack(side=LEFT,padx=5,pady=5)

root.mainloop()
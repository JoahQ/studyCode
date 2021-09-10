# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch3_12")

root.geometry("300x180")
oklabel = Label(root,text="OK",font="Times 20 bold",fg="white",bg="blue")

oklabel.pack(anchor=S,side=RIGHT,padx=10,pady=10)

nolabel = Label(root,text="NO",font="Times 20 bold",fg="white",bg="red")
nolabel.pack(anchor=S,side=RIGHT,pady=10)

root.mainloop()
# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch3_23")

root.geometry("300x180")
print u"执行前",root.pack_slaves()
oklabel = Label(root,text="OK",font="Times 20 bold",fg="white",bg="blue")

oklabel.pack(anchor=S,side=RIGHT,padx=10,pady=10)

nolabel = Label(root,text="NO",font="Times 20 bold",fg="white",bg="red")
nolabel.pack(anchor=S,side=RIGHT,pady=10)
print u"执行后",root.pack_slaves()
root.mainloop()
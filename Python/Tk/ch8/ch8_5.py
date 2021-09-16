#-*- coding: utf-8 -*-
from Tkinter import *
root = Tk()

root.title("ch8_5")

fm = Frame(width=150,height=80,relief=RAISED,borderwidth=5)
lab = Label(fm,text="请复选常用的程序语言")
lab.pack()

python = Checkbutton(fm,text="Python")
python.pack(anchor=W)

java = Checkbutton(fm,text="Java")
java.pack(anchor=W)

ruby = Checkbutton(fm,text="Ruby")
ruby.pack(anchor=W)

fm.pack(padx=10,pady=10)

root.mainloop()



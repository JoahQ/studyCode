#-*- coding:utf-8 -*-
from Tkinter import *

def pythonClicked():
    if varPython.get():
        lab.config(text="Select Python")
    else:
        lab.config(text="Unselect Python")

def javaClicked():
    if varJava.get():
        lab.config(text="Select Java")
    else:
        lab.config(text="Unselect Java")

def buttonClickded():
    lab.config(text="Button clicked")

root = Tk()
root.title("ch11_1")
root.geometry("300x180")

btn = Button(root,text="Click me",command=buttonClickded)
btn.pack(anchor=W)
varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",variable=varPython,command=pythonClicked)
cbnPython.pack(anchor=W)

varJava = BooleanVar()
cbnJava = Checkbutton(root,text="Java",variable=varJava,command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(root,bg="yellow",fg="blue",height=2,width=12,font="Times 16 bold")
lab.pack()

root.mainloop()
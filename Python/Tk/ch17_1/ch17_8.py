#-*- coding: utf-8 -*-
from Tkinter import *
from tkFont import *

def familyChanged(event):
    global familyVar
    global text
    f = Font(family=familyVar.get())
    text.config(font=f)

def weightChanged(event):
    f = Font(weight=weightVar.get())
    text.config(font=f)

root = Tk()
root.title("ch17_8")
root.geometry("300x180")

#建立工具栏
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

#建立font family OptionMenu
familyVar = StringVar()
familyFamily= ("Arial","Arial","Times","Courier")
familyVar.set(familyFamily[0])
# family = OptionMenu(root,familyVar,*familyFamily,command=familyChange)
family = OptionMenu(root,familyVar,*families(),command=familyChanged)
family.pack(side=LEFT,pady=2)

#建立font weight OptionMenu
weightVar = StringVar()
weightFamily = ("normal","bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(root,weightVar,*weightFamily,command=weightChanged)
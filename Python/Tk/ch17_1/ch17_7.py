#-*- coding: utf-8 -*-
from Tkinter import *
from ttk import *
import tkFont


def familyChange(event):
    global familyVar
    global text
    f = tkFont.Font(family=familyVar.get())
    text.configure(font=f)

root = Tk()
root.title("ch17_7")
root.geometry("300x180")

familyVar = StringVar()
familyFamily= ("Arial","Arial","Times","Courier")
familyVar.set(familyFamily[0])
# family = OptionMenu(root,familyVar,*familyFamily,command=familyChange)
family = OptionMenu(root,familyVar,*tkFont.families(),command=familyChange)
family.pack(pady=2)

# text = Text(root)
text = Text(root,bg="lightyellow")
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.config(font="System")
text.focus_set()

root.mainloop()

#-*- coding: utf-8 -*-
from Tkinter import *


def buttonClixked(event):
    print "I like thinkter"

def toggle(onoff):
    if var.get() == True:
        onoff.bind("<Button-1>", buttonClixked)
    else:
        onoff.unbind("<Button-1>")

root = Tk()
root.title("ch11_7")
root.geometry("300x180")

btn = Button(root, text = "tkinter")
btn.pack(anchor=W, padx=10, pady=10)

var = BooleanVar()
cbtn = Checkbutton(root, text = "bind/unbind", variable = var, command=lambda : toggle(btn))
cbtn.pack(anchor=W, padx=10)

root.mainloop()
# -*- coding: utf-8 -*-
from Tkinter import *

# def yellow():
#     root.config(bg="yellow")
#
# def blue():
#     root.config(bg="blue")

def bColor(bgColor):
    root.config(bg=bgColor)

root = Tk()
root.title("ch4_5")
root.geometry("300x200")

exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",command=lambda:bColor("blue"))
yellowbtn = Button(root,text="Yellow",command=lambda:bColor("yellow"))

exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()
# -*- coding: utf-8 -*-
from Tkinter import *

def printIndex():
    print "INSERT: ",text.index(INSERT)
    print "CURRENT: ",text.index(CURRENT)
    print "END: ",text.index(END)

root = Tk()
root.title("ch17_12")
root.geometry("300x180")

# 建立Button
btn = Button(root,text="print index",command=printIndex)
btn.pack(pady=3)

text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love you like A love song\n")
# text.insert(END,"梦醒时分")
text.insert(1.14,"梦醒时分")

root.mainloop()
#-*- coding: utf-8 -*-
from Tkinter import *

def key(event):
    print "按了’" + repr(event.char) + "‘键"

root = Tk()
root.title("ch11_5")

root.bind("<Key>",key)

root.mainloop()
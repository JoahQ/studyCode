#-*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch8_10")

tl = Toplevel()
tl.title("Toplevel")
tl.geometry("300x300")
Label(tl,text="I am a Topleve").pack()

root.mainloop()
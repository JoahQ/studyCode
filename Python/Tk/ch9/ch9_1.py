#-*- coding: utf-8 -*-
from Tkinter import *

window = Tk()
window.title("ch9-1")

slider1 = Scale(window,from_=0,to=10).pack()
slider2 = Scale(window,from_=0,to=10,length=300,orient=HORIZONTAL).pack()

window.mainloop()
#-*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title("ch9_2")

slider = Scale(root,
               from_=0,
               to=10,
               troughcolor="yellow",
               width="30",
               tickinterval=2,
               label="My Scale",
               length=300,
               orient=HORIZONTAL)

slider.pack()

root.mainloop()
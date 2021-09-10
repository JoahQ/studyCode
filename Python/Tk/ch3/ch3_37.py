# -*- coding: utf-8 -*-
from Tkinter import *
from ttk import *

root = Tk()
root.title("ch3_37")
root.geometry("240x180")

night = PhotoImage(file="night.gif")
lab1 = Label(root,image=night)
# lab1.place(x=20,y=30)
# lab1.place(x=20,y=30,width=200,height=120)
lab1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

# snow = PhotoImage(file="snow.gif")
# lab2 = Label(root,image=snow)
# # lab2.place(x=200,y=200)
# lab2.place(x=200,y=200,width=100,height=140)
# lab2.place(x=200,y=200,width=100,height=140)

root.mainloop()
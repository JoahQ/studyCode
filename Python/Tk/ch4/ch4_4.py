# -*- coding: utf-8 -*-
from Tkinter import *

counter = 0
def run_counter(digit):
    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000,counting)
    counting()

root = Tk()
root.title("ch4_4")
digit1 = Label(root,bg="yellow",fg="blue",height=3,width=10,font="Helvetic 20 bold")

digit1.pack()
run_counter(digit1)
btn2 = Button(root,text="结束",width=15,command=root.destroy).pack(pady=10)

root.mainloop()
# -*- coding: utf-8 -*-
from Tkinter import *

counter = 0

def run_counter(digiti):
    def counting():
        global counter
        counter += 1
        digiti.config(text=str(counter))
        digiti.after(1000,counting)         #隔1秒(1000毫秒)后调用counting
    counting()

root = Tk()
root.title("ch2_23")
digit = Label(root,bg="yellow",fg="blue",height=3,width=10,font="Helvetic 20 bold")
digit.pack()
run_counter(digit)
root.mainloop()
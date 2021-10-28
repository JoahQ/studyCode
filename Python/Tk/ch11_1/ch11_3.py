#-*- coding:utf-8 -*-
from Tkinter import *

def enter(event):
    x.set("鼠标进入Exit功能按钮")

def leave(event):
    x.set("鼠标离开Exit功能按钮")

root = Tk()
root.title("ch11_3")
root.geometry("300x180")

btn = Button(root,text="Exit",command=root.destroy)
btn.pack(pady=30)
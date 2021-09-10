# -*- coding: utf-8 -*-
from Tkinter import *

# expression = raw_input("请输入数学表达式：")
# print expression
# print "结果是 ：",eval(expression)

def cal():
    out.configure(text="结果 : " + str(eval(equ.get())))

root = Tk()
root.title("ch5_9")

label = Label(root,text="请输入数学表达式：")
label.pack()

equ = Entry(root)
equ.pack(pady=5)
out = Label(root)
out.pack(pady=5)

btn = Button(root,text="计算",command=cal)
btn.pack(pady=5)
root.mainloop()
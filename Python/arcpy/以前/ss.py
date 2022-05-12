#coding=utf-8
from Tkinter import *
from tkFileDialog import *

#创建容器

tk=Tk()
tk.title("我的GUI界面学习")
mainfarm=Frame(tk,width=800, height=100,bg="red")
mainfarm.grid_propagate(0)
mainfarm.grid()
fram=Frame(mainfarm,width=400, height=100,bg="yellow")
fram.grid_propagate(0)
fram.grid()




e = Entry(fram)
e.grid(row=0,column=2)

e.delete(0, END)  # 将输入框里面的内容清空
e.insert(0, '选择文件路径')
filepath=StringVar()
def filefound():
    filepath= askopenfilename()
    print filepath
    e.delete(0, END)  # 将输入框里面的内容清空
    e.insert(0, filepath)

button1=Button(fram,text="button1").grid(row=0,column=1)
button2=Button(fram,text="button2",command=filefound).grid(row=0,column=3)
print fram.size()

mainloop()

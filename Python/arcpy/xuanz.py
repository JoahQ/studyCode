#coding=utf-8
from Tkinter import *
from tkFileDialog import *

#创建容器

tk=Tk()
tk.title("我的GUI界面学习")
tk.minsize(width=600, height=600)
screenwidth = tk.winfo_screenwidth()
screenHeight = tk.winfo_screenheight()
w = 600
h = 600
x = (screenwidth - w) / 2
y = 30
tk.geometry("%dx%d+%d+%d" % (w,h,x,y))

mainfarm=Frame(tk,width=600, height=600)

mainfarm.grid_propagate(0)
mainfarm.grid()

Label(mainfarm,text="").grid(row=0)
Label(mainfarm,text=" ").grid(row=1,column=3)
# Label(mainfarm,text="").grid(row=1,column=0)

e = Entry(mainfarm,width=65)
e.grid(row=1,column=2,sticky=W+E)

e.delete(0, END)  # 将输入框里面的内容清空
filepath=StringVar()
def filefound():
    file_opt = options = {}
    options['defaultextension'] = '.shp'
    options['filetypes'] = [('shp文件', '.shp'),('所有文件', '.*')]
    filepath= askopenfilename(**file_opt)
    print filepath
    e.delete(0, END)  # 将输入框里面的内容清空
    e.insert(0, filepath)

Label(mainfarm,text="输入路径：").grid(row=1,column=1)
opengif = PhotoImage(file="open.gif")
button2=Button(mainfarm,image=opengif,command=filefound).grid(row=1,column=4)
print mainfarm.size()

mainloop()

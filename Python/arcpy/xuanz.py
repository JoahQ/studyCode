#coding=utf-8
from Tkinter import *
from ttk import *
from tkFileDialog import *
import arcpy

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

e2 = Entry(mainfarm,width=65)
e2.grid(row=2,column=2,sticky=W+E)

text= Text(mainfarm,width=100,height=200)

text.grid(row=4,column=1,columnspan=4,sticky=W+E)

text.insert(INSERT,'想得却不可得\n')#INSERT索引表示光标当前的位置

text.insert(END,'你奈人生何')

# filepath=StringVar()
def filefound():
    file_opt = options = {}
    options['defaultextension'] = '.shp'
    options['filetypes'] = [('shp文件', '.shp'),('所有文件', '.*')]
    filepath= askopenfilename(**file_opt)
    print filepath
    e.delete(0, END)  # 将输入框里面的内容清空
    e.insert(0, filepath)

def filefound2():
    foderpath= askdirectory()
    print foderpath
    e2.delete(0, END)  # 将输入框里面的内容清空
    e2.insert(0, foderpath)

def printArcpy():
    arcpy.env.workspace = e.get()
    for fc in arcpy.ListFeatureClasses():
        print fc
    arcpy.env.workspace = e2.get()
    for fc in arcpy.ListWorkspaces("*","FileGDB"):
        print fc

Label(mainfarm,text="输入路径：").grid(row=1,column=1)
Label(mainfarm,text="输出路径：").grid(row=2,column=1)
opengif = PhotoImage(file="open.gif")
button2=Button(mainfarm,image=opengif,command=filefound).grid(row=1,column=4)
button1=Button(mainfarm,image=opengif,command=filefound2).grid(row=2,column=4)
button3=Button(mainfarm,text="开始执行",command=printArcpy).grid(row=3,column=2)
print mainfarm.size()

mainloop()

# -*- coding: utf-8 -*-
from site import addsitedir
from sys import executable
from os import path

interpreter = executable
sitepkg = path.dirname(interpreter) + "\\site-packages"
addsitedir(sitepkg)

from Tkinter import *
from tkFileDialog import *
import arcpy

def main():
    # 创建容器

    tk = Tk()
    tk.title("我的GUI界面学习")
    tk.minsize(width=600, height=600)
    screenwidth = tk.winfo_screenwidth()
    w = 600
    h = 600
    x = (screenwidth - w) / 2
    y = 30
    tk.geometry("%dx%d+%d+%d" % (w, h, x, y))

    mainfarm = Frame(tk, width=600, height=600)

    mainfarm.grid_propagate(0)
    mainfarm.grid()

    Label(mainfarm, text="").grid(row=0)
    Label(mainfarm, text=" ").grid(row=1, column=3)
    # Label(mainfarm,text="").grid(row=1,column=0)

    e = Entry(mainfarm, width=65)
    e.grid(row=1, column=2, sticky=W + E)

    e.delete(0, END)  # 将输入框里面的内容清空

    e2 = Entry(mainfarm, width=65)
    e2.grid(row=2, column=2, sticky=W + E)

    # filepath=StringVar()
    def filefound():
        file_opt = options = {}
        options['defaultextension'] = '.shp'
        options['filetypes'] = [('shp文件', '.shp'), ('所有文件', '.*')]
        filepath = askopenfilename(**file_opt)
        e.delete(0, END)  # 将输入框里面的内容清空
        e.insert(0, filepath)

    def filefound2():
        file_opt = options = {}
        options['defaultextension'] = '.shp'
        options['filetypes'] = [('shp文件', '.shp'), ('所有文件', '.*')]
        filepath = askopenfilename(**file_opt)
        e2.delete(0, END)  # 将输入框里面的内容清空
        e2.insert(0, filepath)

    def printArcpy():
        arcpy.env.workspace = e.get()
        aaa = 8
        for fc in arcpy.ListFeatureClasses():
            Label(mainfarm, text=fc, fg="blue", bg="lightyellow",
                  font="Verdana 16 bold", width=25, height=2).grid(row=aaa, column=2)
            aaa += 1


    # label = Label(mainfarm, textvariable=x, fg="blue", bg="lightyellow", font="Verdana 16 bold", width=25, height=2)
    # label.grid(row=8, column=2)
    Label(mainfarm, text="输入路径：").grid(row=1, column=1)
    Label(mainfarm, text="输出路径：").grid(row=2, column=1)
    opengif = PhotoImage(file="open.gif")
    Button(mainfarm, image=opengif, command=filefound).grid(row=1, column=4)
    Button(mainfarm, image=opengif, command=filefound2).grid(row=2, column=4)
    Button(mainfarm, text="开始执行", command=printArcpy).grid(row=3, column=2)


    mainloop()

if __name__ == "__main__":

    main()

#-*- coding: utf-8 -*-
from Tkinter import *

def printInfo():
    selection = ''
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection = selection + sports[i] + '\t'
    print selection

root = Tk()
root.title("ch8_8")
root.geometry("400x220")

#以下建立标签框架与字典
labFrame = LabelFrame(root,text="选择最喜欢的运动")
sports = {0:"美式足球",1:"棒球",2:"篮球",3:"网球"}
checkboxes = {}
for i in range(len(sports)):
    checkboxes[i] = BooleanVar()
    Checkbutton(labFrame,text=sports[i],variable=checkboxes[i]).grid(row=i+1,sticky=W)

labFrame.pack(ipadx=5,ipady=5,pady=10)
btn = Button(root,text="确定",width=10,command=printInfo)
btn.pack()

root.mainloop()
from Tkinter import *

root = Tk()
root.title("ch2_2")
# label = Label(root,text="I like Tkinter",fg="blue",bg="yellow",height=3,width=15,anchor="nw")
# label = Label(root,text="I like Tkinter",fg="blue",bg="yellow",height=3,width=15,anchor="se")
label = Label(root,text="I like Tkinter",fg="blue",bg="yellow",height=3,width=15,anchor=NW,wraplength= 40)
label.pack()
# print(type(label))
root.mainloop()
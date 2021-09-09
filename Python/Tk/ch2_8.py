from Tkinter import *

root = Tk()
root.title("ch2_8")
# label = Label(root,text="I like Tkinter",fg="blue",bg="yellow",height=3,width=15,font="Helvetic 20 bold")
label = Label(root,text="I like Tkinter",fg="blue",bg="yellow",height=3,width=15,font=("Helvetic", 20, "bold"))
label.pack()
root.mainloop()
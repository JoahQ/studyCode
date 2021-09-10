from Tkinter import *

root = Tk()
root.title("ch2_10")
# label = Label(root,text="abcdefghijklmnopqrstwxyz123456",fg="blue",bg="lightyellow",wraplength = 80,justify="left")
label = Label(root,text="abcdefghijklmnopqrstwxyz123456",fg="blue",bg="lightyellow",wraplength = 80,justify="right")
label.pack()
root.mainloop()
# -*- coding: utf-8 -*-
from Tkinter import *
from ttk import *

root = Tk()
root.title("ch17_1")

yscrollbar = Scrollbar(root)
text = Text(root,height=5,width=30)
yscrollbar.pack(side=RIGHT,fill=Y)
text.pack()
yscrollbar.config(command=text.yview)
text.config(yscrollcommand=yscrollbar.set)
# text.insert(END,"python\nJava\n")
# text.insert(INSERT,"sejflkjsdglj")
str1 = """You can write a Python script to execute and make use of a geoprocessing service in multiple ways. 
The primary way to execute a script is to make use of ArcPy. ArcPy has built-in methods to connect to, execute, 
and handle the result from the service. Alternatively, using the Services Directory, you can use built-in Python 
modules to make REST calls using a JSON structure to transfer results. You will have to build a client from scratch 
with Python code to make use of this. The majority of scripts will connect to and use geoprocessing services 
through ArcPy.
"""
text.insert(END,str1)
root.mainloop()
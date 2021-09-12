# -*- coding: utf-8 -*-
from Tkinter import *

class MyApp(object):
    def __init__(self, root):
        self.root = root

def main():
    root = Tk()
    myapp = MyApp(root)
    root.title("Export Tool")
    root.update()
    root.mainloop()
if __name__ == '__main__':
    main()
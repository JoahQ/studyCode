# -*- coding: utf-8 -*-
from site import addsitedir
from sys import executable
from os import path

interpreter = executable
sitepkg = path.dirname(interpreter) + "\\site-packages"
print(sitepkg)
addsitedir(sitepkg)

import arcpy

def main():
    arcpy.env.workspace = r'D:\gisdata\1234.mdb'
    for fc in arcpy.ListFeatureClasses():
        print fc

if __name__ == "__main__":
    print('Start Processing ...')
    main()
    raw_input("Enter enter key to exit...")
# -*-coding: utf-8 -*-
import arcpy

def a():
    with arcpy.da.SearchCursor(fc, "ww") as cursor:
        for row in cursor:
            if "None" == str(row[0]):
                print str(row[0]) + "ii"
            if "020" in str(row[0]):
                print row[0]

if __name__ == "__main__":
    fc =  r'D:\gisdata\a.gdb\复制'
    a()

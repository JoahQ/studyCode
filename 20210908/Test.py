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
    arcpy.MakeFeatureLayer_management(r'D:\gisdata\新建文件地理数据库.gdb\举证图斑交DLTB打散', "result_fc_layer")

    arcpy.SelectLayerByLocation_management("result_fc_layer", "INTERSECT", r'D:\gisdata\新建文件地理数据库.gdb\abc')

    arcpy.FeatureClassToFeatureClass_conversion("result_fc_layer", r'D:\gisdata\新建文件地理数据库.gdb', "erer")

if __name__ == "__main__":
    print('Start Processing ...')
    main()
    raw_input("Enter enter key to exit...")
# -*- coding: utf-8 -*-

import arcpy

arcpy.MakeFeatureLayer_management(r'D:\gisdata\新建文件地理数据库.gdb\举证图斑交DLTB打散', "result_fc_layer")

arcpy.SelectLayerByLocation_management("result_fc_layer","INTERSECT", r'D:\gisdata\新建文件地理数据库.gdb\abc')

arcpy.FeatureClassToFeatureClass_conversion("result_fc_layer", r'D:\gisdata\新建文件地理数据库.gdb',"erer")

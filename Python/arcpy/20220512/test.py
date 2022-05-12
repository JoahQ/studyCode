
# -*-coding: gbk -*-
# Create Time  : 2022/5/12 
# Author       : QinZhou
# File Name    : test.PY
# Description  :
# ********************************************************* #

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import arcpy

feature_class =r'D:\data\Export_Output.shp'

# Create a list of fields using the ListFields function
# fields = arcpy.ListFields(feature_class)

# Iterate through the list of fields
# for field in fields:
#     # Print field properties
#     if field.type not in ['Geometry', 'OID'] and field.editable:
#         print("Field:       {0}".format(field.name))
#         print("Alias:       {0}".format(field.aliasName))
#         print("Type:        {0}".format(field.type))
#         print("Is Editable: {0}".format(field.editable))
#         print("Required:    {0}".format(field.required))
#         print("Scale:       {0}".format(field.scale))
#         print("Precision:   {0}".format(field.precision))

with arcpy.da.UpdateCursor(feature_class, 'OID@') as cursor:
    for row in cursor:
        print row[0]
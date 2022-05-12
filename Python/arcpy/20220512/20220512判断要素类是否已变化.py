# -*-coding: gbk -*-
# Create Time  : 2022/5/12 
# Author       : QinZhou
# File Name    : 20220512判断要素类是否已变化.PY
# Description  :
# ********************************************************* #
import arcpy
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

def get_field_names(infc):
    field_names = []
    fields = arcpy.ListFields(infc)
    for field in fields:
        if field.type not in ['Geometry', 'OID'] and field.editable and 'SHAPE' not in field.name and 'Shape' not in field.name:
            field_names.append(field.name)
    return field_names

def point_analyse(new_fc, new_date_field, old_fc, image_vecto, sx_field):
    intersect_feature_class = os.path.join(r'in_memory', "in_" + os.path.basename(new_fc))
    select_feature_class = os.path.join(r'in_memory', "sel_" + os.path.basename(new_fc))
    field_list = get_field_names(new_fc)

    get_value_field = "get_value"
    # 编唯一id
    uni_id = "new_uni_id"
    arcpy.AddField_management(uni_id, 'LONG')
    with arcpy.da.UpdateCursor(new_fc, (uni_id, 'OID@')) as cursor:
        for row in cursor:
            row[0] = row[1]
            cursor.updateRow(row)
    del row
    del cursor
    arcpy.Intersect_analysis([new_fc, old_fc], intersect_feature_class)
    where_clause = ''
    for field in field_list:
        if new_date_field != field:
            if where_clause == '':
                where_clause = field + " == " + field + "_1"
            else:
                where_clause += " AND " + field + " == " + field + "_1"
    arcpy.Select_analysis(intersect_feature_class, select_feature_class, where_clause)

    arcpy.AddField_management(select_feature_class, get_value_field, "TEXT")
    arcpy.CalculateField_management(select_feature_class, get_value_field, "!" + new_date_field + "_1!", "PYTHON_9.3")
    



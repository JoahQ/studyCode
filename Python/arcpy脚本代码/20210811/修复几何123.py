# -*- coding: gbk -*-
import sys
import arcpy
import os

reload(sys)
sys.setdefaultencoding("utf-8")

in_path = arcpy.GetParameterAsText(0)

arcpy.env.workspace = in_path
fc_ls = arcpy.ListFeatureClasses()

for fc in fc_ls:
    in_fc = os.path.join(in_path,fc)
    arcpy.AddMessage("      " + fc + " 修复几何...")
    try:
        arcpy.RepairGeometry_management (in_fc)
        arcpy.AddMessage("      修复几何完成！")

    except Exception as e:
        arcpy.AddError(e.message)
        arcpy.AddError("    " + in_fc + " 失败！")



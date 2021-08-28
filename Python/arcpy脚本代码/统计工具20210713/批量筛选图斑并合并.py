# -*- coding: gbk -*-
import arcpy
import os
import sys


reload(sys)
sys.setdefaultencoding("utf-8")

def getNewFileNameQ(dirpath1, file_name_out):
    n = [1]
    def get_new_name(file_name_in):
        new_file_name = file_name_in
        if arcpy.Exists(os.path.join(dirpath1, file_name_in)):
            new_file_name = "%s_%s%s" % (
            os.path.splitext(file_name_in)[0], str(n[0]), os.path.splitext(file_name_in)[1])
            n[0] += 1
            if arcpy.Exists(os.path.join(dirpath1, new_file_name)):
                new_file_name = get_new_name(file_name_in)
        return new_file_name

    return get_new_name(file_name_out)

def selectFeatureClassAll(in_path, out_path, sql_clause):
    arcpy.env.workspace = in_path
    ls = arcpy.ListFeatureClasses()

    out_fcls = []
    c = 0
    for fc in ls:
        c += 1
        in_fc = os.path.join(in_path,fc)
        arcpy.AddMessage("(" + str(c) + ")、" + in_fc)
        out_fc = os.path.join(out_path,os.path.basename(fc).rstrip(os.path.splitext(fc)[1])+"No"+str(c))
        arcpy.Select_analysis(in_fc, out_fc, sql_clause)
        out_fcls.append(out_fc)

    mp = os.path.join(out_path,"A筛选后合并")
    arcpy.Merge_management(out_fcls,mp)

if __name__ == "__main__":
    in_gdbG = arcpy.GetParameterAsText(0)
    out_pathG = arcpy.GetParameterAsText(1)
    whereSql = arcpy.GetParameterAsText(2)

    selectFeatureClassAll(in_gdbG,out_pathG,whereSql)



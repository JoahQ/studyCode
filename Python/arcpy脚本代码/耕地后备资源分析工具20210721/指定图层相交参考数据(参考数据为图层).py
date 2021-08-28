# -*- coding: gbk -*-
import sys
import arcpy
import os
import re
import string

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


def BatchIntersect(in_path, layer_name,consult_layer, out_path):

    cout = 0
    fail = 0
    warning = 0
    fail_list = []
    warning_list = []

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")

    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")

        temp_name1 = os.path.basename(workspace)
        result_gdb = os.path.join(out_path, temp_name1)
        try:
            infc_path = os.path.join(workspace, layer_name)
            if arcpy.Exists(infc_path):

                if not arcpy.Exists(result_gdb):
                    arcpy.AddMessage("    新建 " + result_gdb + " ...")
                    arcpy.CreateFileGDB_management(out_path, temp_name1)
                else:
                    arcpy.AddWarning(u"  警告：" + result_gdb + u" 已存在！")
                    warning_list.append(result_gdb)
                    warning += 1
                    continue

                erase1_path = os.path.join(result_gdb,layer_name)
                arcpy.AddMessage("    " + infc_path + " 与 " + consult_layer + " 相交..." )
                arcpy.Intersect_analysis([infc_path, consult_layer], erase1_path)
            else:
                arcpy.AddError("    " + workspace + " 不存在 \"" + layer_name + "\" 图层! 相交失败！")
                fail_list.append(workspace)
                fail += 1

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " 失败！")
            fail_list.append(workspace)
            fail += 1
            if arcpy.Exists(result_gdb):
                try:
                    arcpy.Delete_management(result_gdb)
                except Exception as e:
                    arcpy.AddMessage(e.message)

    arcpy.AddMessage('+'*60)
    arcpy.AddMessage(u"  成功：" + str(cout - fail - warning) + u" 个！")
    if warning > 0:
        arcpy.AddWarning(u"  警告：" + str(warning) + u" 个！ 如下：")
        arcpy.AddWarning("####" + '*' * 20)
        for fff in warning_list:
            arcpy.AddWarning("  " + fff)
        arcpy.AddWarning("####" + '*' * 20)
    if fail > 0:
        arcpy.AddError(u"  失败：" + str(fail) + u" 个！ 如下：")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)

if __name__ == "__main__":
    in_pathG = arcpy.GetParameterAsText(0)
    layer_nameG = arcpy.GetParameterAsText(1)
    consult_layerG = arcpy.GetParameterAsText(2)
    out_pathG = arcpy.GetParameterAsText(3)

    BatchIntersect(in_pathG, layer_nameG,consult_layerG, out_pathG)

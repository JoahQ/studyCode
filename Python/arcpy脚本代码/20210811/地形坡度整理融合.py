# -*- coding: gbk -*-
import sys
import arcpy
import os

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

def dxpd(in_path,out_path,dissolve_feild4):
    cout = 0
    fail = 0
    warning = 0
    fail_list = []
    warning_list = []

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "ALL")

    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        try:
            # 将每个gdb设为工作区
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()
            temp_name1 = os.path.basename(workspace)
            result_gdb = os.path.join(out_path, temp_name1)

            if not arcpy.Exists(result_gdb):
                arcpy.AddMessage("新建 " + result_gdb + " ...")
                arcpy.CreateFileGDB_management(out_path, temp_name1)
            else:
                arcpy.AddWarning(result_gdb + u" 已存在！")
                warning_list.append(result_gdb)
                warning += 1
                continue
            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                out_fc_path = os.path.join(result_gdb, ifc)
                arcpy.AddMessage("       1.别名：" + arcpy.Describe(infc_path).aliasName)

                arcpy.AddMessage(u"    " + infc_path + u" 正在修复几何 ...")
                arcpy.RepairGeometry_management(infc_path)
                arcpy.AddMessage(u"    正在融合 " + infc_path + u"...")
                arcpy.Dissolve_management(infc_path, out_fc_path, dissolve_feild4, "", "SINGLE_PART", "DISSOLVE_LINES")
                arcpy.AlterAliasName(out_fc_path,arcpy.Describe(infc_path).aliasName)
                arcpy.AddMessage("       2.别名：" + arcpy.Describe(out_fc_path).aliasName)
        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " 失败！")
            fail_list.append(os.path.basename(workspace))
            fail += 1

    arcpy.AddMessage('+' * 60)
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
    in_pathg = arcpy.GetParameterAsText(0)
    out_patha = arcpy.GetParameterAsText(1)
    dfeild = arcpy.GetParameterAsText(2)

    dxpd(in_pathg,out_patha,dfeild)
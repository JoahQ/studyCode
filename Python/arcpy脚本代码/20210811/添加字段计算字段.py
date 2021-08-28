# -*- coding: gbk -*-
import sys
import arcpy
import os

reload(sys)
sys.setdefaultencoding("utf-8")
arcpy.env.overwriteOutput = True

def daochushp(in_path,add_field,field_txt):
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

            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                if int(arcpy.GetCount_management(infc_path).getOutput(0)) > 0:
                    if add_field.strip() != '':
                        arcpy.AddMessage("    添加 " + add_field + " 字段 ...")
                        arcpy.AddField_management(infc_path, add_field, "TEXT", "", "", 50)
                        arcpy.AddMessage("     计算 " + field_txt + " 到 " + add_field + " 字段...")
                        arcpy.CalculateField_management(infc_path, add_field, "'" + field_txt + "'", "PYTHON_9.3")

                else:
                    arcpy.AddWarning(infc_path + " 图斑数为0！")
                    warning_list.append(infc_path)
                    warning += 1

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

def dxpd(in_path,add_field,field_txt):
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

            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                if int(arcpy.GetCount_management(infc_path).getOutput(0)) > 0:
                    if add_field.strip() != '':
                        arcpy.AddMessage("    添加 " + add_field + " 字段 ...")
                        arcpy.AddField_management(infc_path, add_field, "TEXT", "", "", 50)
                        arcpy.AddMessage("     计算 " + field_txt + " 到 " + add_field + " 字段...")
                        arcpy.CalculateField_management(infc_path, add_field, "!" + field_txt + "!", "PYTHON_9.3")

                else:
                    arcpy.AddWarning(infc_path + " 图斑数为0！")
                    warning_list.append(infc_path)
                    warning += 1

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
    addfield_gg = arcpy.GetParameterAsText(1)
    txt = arcpy.GetParameterAsText(2)

    dxpd(in_pathg,addfield_gg,txt)

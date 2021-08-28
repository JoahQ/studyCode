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
            # ��ÿ��gdb��Ϊ������
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()

            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                if int(arcpy.GetCount_management(infc_path).getOutput(0)) > 0:
                    if add_field.strip() != '':
                        arcpy.AddMessage("    ��� " + add_field + " �ֶ� ...")
                        arcpy.AddField_management(infc_path, add_field, "TEXT", "", "", 50)
                        arcpy.AddMessage("     ���� " + field_txt + " �� " + add_field + " �ֶ�...")
                        arcpy.CalculateField_management(infc_path, add_field, "'" + field_txt + "'", "PYTHON_9.3")

                else:
                    arcpy.AddWarning(infc_path + " ͼ����Ϊ0��")
                    warning_list.append(infc_path)
                    warning += 1

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " ʧ�ܣ�")
            fail_list.append(os.path.basename(workspace))
            fail += 1


    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage(u"  �ɹ���" + str(cout - fail - warning) + u" ����")

    if warning > 0:
        arcpy.AddWarning(u"  ���棺" + str(warning) + u" ���� ���£�")
        arcpy.AddWarning("####" + '*' * 20)
        for fff in warning_list:
            arcpy.AddWarning("  " + fff)
        arcpy.AddWarning("####" + '*' * 20)
    if fail > 0:
        arcpy.AddError(u"  ʧ�ܣ�" + str(fail) + u" ���� ���£�")
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
            # ��ÿ��gdb��Ϊ������
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()

            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                if int(arcpy.GetCount_management(infc_path).getOutput(0)) > 0:
                    if add_field.strip() != '':
                        arcpy.AddMessage("    ��� " + add_field + " �ֶ� ...")
                        arcpy.AddField_management(infc_path, add_field, "TEXT", "", "", 50)
                        arcpy.AddMessage("     ���� " + field_txt + " �� " + add_field + " �ֶ�...")
                        arcpy.CalculateField_management(infc_path, add_field, "!" + field_txt + "!", "PYTHON_9.3")

                else:
                    arcpy.AddWarning(infc_path + " ͼ����Ϊ0��")
                    warning_list.append(infc_path)
                    warning += 1

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " ʧ�ܣ�")
            fail_list.append(os.path.basename(workspace))
            fail += 1


    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage(u"  �ɹ���" + str(cout - fail - warning) + u" ����")

    if warning > 0:
        arcpy.AddWarning(u"  ���棺" + str(warning) + u" ���� ���£�")
        arcpy.AddWarning("####" + '*' * 20)
        for fff in warning_list:
            arcpy.AddWarning("  " + fff)
        arcpy.AddWarning("####" + '*' * 20)
    if fail > 0:
        arcpy.AddError(u"  ʧ�ܣ�" + str(fail) + u" ���� ���£�")
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

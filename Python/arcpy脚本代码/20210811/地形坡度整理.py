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

def dxpd(in_path,out_path):
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
            temp_name1 = os.path.basename(workspace) + "�����¶�ͼ.gdb"
            result_gdb = os.path.join(out_path, temp_name1)

            if not arcpy.Exists(result_gdb):
                arcpy.AddMessage("�½� " + result_gdb + " ...")
                arcpy.CreateFileGDB_management(out_path, temp_name1)
            else:
                arcpy.AddWarning(result_gdb + u" �Ѵ��ڣ�")
                warning_list.append(result_gdb)
                warning += 1
                continue
            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                out_fc_name = "DXPD"
                arcpy.AddMessage("      " + infc_path + "...")
                arcpy.FeatureClassToFeatureClass_conversion(infc_path,result_gdb,out_fc_name)

                out_fc_path = os.path.join(result_gdb, out_fc_name)
                arcpy.AlterAliasName(out_fc_path,"�����¶�")
                put_field = "DXPDJB"
                fieldAlias = "�����¶ȼ���"
                arcpy.AddField_management(out_fc_path, put_field, 'TEXT', "#", "#", 10, fieldAlias)
                codeblock1 = """def getV(v):
                                if str(v).strip() in ['1','2','3','4']:
                                    return '��25��'
                                else:
                                    return '��25��'
                            """
                expression = "getV(!PDJB!)"

                arcpy.CalculateField_management(out_fc_path, put_field, expression, "PYTHON_9.3", codeblock1)

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

def trzd(in_path,out_path):
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
            temp_name1 = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1]) + "�����ʵ�ͼ.gdb"
            result_gdb = os.path.join(out_path, temp_name1)

            if not arcpy.Exists(result_gdb):
                arcpy.AddMessage("�½� " + result_gdb + " ...")
                arcpy.CreateFileGDB_management(out_path, temp_name1)
            else:
                arcpy.AddWarning(result_gdb + u" �Ѵ��ڣ�")
                warning_list.append(result_gdb)
                warning += 1
                continue
            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                out_fc_name = "TRZD"
                arcpy.AddMessage("      " + infc_path + " ...")
                arcpy.FeatureClassToFeatureClass_conversion(infc_path,result_gdb,out_fc_name)

                out_fc_path = os.path.join(result_gdb, out_fc_name)
                arcpy.AlterAliasName(out_fc_path,u"�����ʵ�")
                put_field = "TRZD"
                fieldAlias = u"�����ʵ�"
                arcpy.AddMessage("      ����ֶΣ�" + put_field + " ������" + fieldAlias)
                arcpy.AddField_management(out_fc_path, put_field, 'TEXT', "#", "#", 50, fieldAlias)

                arcpy.AddMessage("      �����ֶΣ�" + put_field)
                codeblockvb = """
                
                Dim density
                Dim s1
                Dim s2
                Dim s3
                s1 = "ש������������������ƺ�����������������ɫ��ʯ������ˮ������ճ��"
                s2 = "�ֹ���"
                s3 = Trim([����])
                
                IF InStr(s1,s3) > 0 AND s3 <>"" Then
                density = "���ʡ�ճ�ʻ�ɰ��"
                ELSEIF InStr(s2,s3) > 0 AND s3 <>"" Then
                density = "���ʻ�����ʵ�"
                ELSE
                density = s3
                END IF
                
                """
                expression = "density"

                arcpy.CalculateField_management(out_fc_path, put_field, expression, "VB", codeblockvb)

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
    out_patha = arcpy.GetParameterAsText(1)
    dxpdgg = arcpy.GetParameter(2)
    trzdgg = arcpy.GetParameter(3)

    if dxpdgg and not trzdgg:
        dxpd(in_pathg,out_patha)
    elif not dxpdgg and trzdgg:
        trzd(in_pathg,out_patha)
    else:
        arcpy.AddError("���빴ѡ��ֻ�ܹ�ѡһ����")
        a = []
        print a[99]

# def getV(v):
#     ls = 'ש������������������ƺ�����������������ɫ��ʯ������ˮ������ճ��'.decode('utf-8')
#     ls2 = "�ֹ���".decode('utf-8')
#
#     if str(v.decode('utf-8')).strip() in ls:
#         return '���ʡ�ճ�ʻ�ɰ��'.decode('utf-8')
#     elif str(v.decode('utf-8')).strip() in ls2:
#         return '���ʻ�����ʵ�'.decode('utf-8')
#     else:
#         return v

"""
    ls = [u'ש����',u'�����',u'����',u'����',u'�ƺ���',u'������',u'������',u'��ɫ��',u'ʯ������',u'ˮ����',u'��ճ��']

field_alias = [f.aliasName for f in ls]
Dim density
IF InStr("ש������������������ƺ�����������������ɫ��ʯ������ˮ������ճ��",[����]) > 0 Then
density = "���ʡ�ճ�ʻ�ɰ��"
ELSEIF InStr("�ֹ���",[����]) Then
density = "���ʻ�����ʵ�"
ELSE
density = [����]
END IF



Dim density
Dim s1
Dim s2
Dim s3
s1 = "ש������������������ƺ�����������������ɫ��ʯ������ˮ������ճ��"
s2 = "�ֹ���"
s3 = Trim([abc])

IF InStr(s1,s3) > 0 AND s3 <>"" Then
density = "���ʡ�ճ�ʻ�ɰ��"
ELSEIF InStr(s2,s3) > 0 AND s3 <>"" Then
density = "���ʻ�����ʵ�"
ELSE
density = s3
END IF
"""
# -*- coding: gbk -*-
import arcpy
import os
import string
import sys
import time
import re
sys.path.append(os.path.dirname(__file__))
import xlwt

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

def statisticsArea1(in_path, out_path, statistics_fields, case_fields, name):
    cout = 0
    fail = 0
    fail_list = []

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")

    temp_name1 = getNewFileNameQ(out_path, "result.gdb")
    result_gdb = os.path.join(out_path, temp_name1)
    arcpy.AddMessage("�½� " + result_gdb + " ���ڱ��������Ա�͹�������...")
    arcpy.CreateFileGDB_management(out_path, temp_name1)

    table_lists = []
    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        # ��ÿ��gdb��Ϊ������
        arcpy.env.workspace = workspace
        gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])
        gdbName1 = "".join(re.findall(r"[^()\[\]{},.*/|\\:;?\'\"<>%!@#$&]", gdbName))

        try:

            statistics_table_path = os.path.join(result_gdb,"����ͳ��" + gdbName1)
            fc_path = os.path.join(workspace,"DLTB")
            arcpy.Statistics_analysis(fc_path, statistics_table_path, statistics_fields, case_fields)
            table_lists.append(statistics_table_path)
        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("      " + os.path.basename(workspace) + " ʧ�ܣ�")
            fail += 1

    try:
        table_lists_merge = os.path.join(result_gdb,"a����ͳ�Ʊ�ϲ�")

        hb_name1 = getNewFileNameQ(out_path, name + ".gdb")
        hb_gdb = os.path.join(out_path, hb_name1)
        arcpy.AddMessage("�½� " + hb_gdb + " ���ڱ�������ͳ�Ʊ�ϲ����...")
        arcpy.CreateFileGDB_management(out_path, hb_name1)

        arcpy.AddMessage("���ںϲ�����ͳ�Ʊ�...")
        arcpy.Merge_management(table_lists, table_lists_merge)

        arcpy.TableToTable_conversion(table_lists_merge,hb_gdb,name)

    except Exception as e:
        arcpy.AddError(e.message)
        arcpy.AddError("      �ϲ�ͳ�Ʊ�ʱʧ�ܣ�")
        a = []
        print a[999]

    arcpy.AddMessage('+'*60)
    arcpy.AddMessage("  �ɹ���" + str(cout - fail) + " ����")
    if fail > 0:
        arcpy.AddError("  ʧ�ܣ�" + str(fail) + " ���� ���£�")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)

if __name__ == "__main__":
    in_pathG = arcpy.GetParameterAsText(0)
    out_pathG = arcpy.GetParameterAsText(1)
    nameG = arcpy.GetParameterAsText(2)
    case_fieldsG = arcpy.GetParameterAsText(3)



    asa123 = re.findall(r"[^()\[\]{},.*/|\\:;?\'\"<>%!@#$&]", nameG)
    name11 = "".join(asa123)
    table_name = name11.lstrip(string.digits)
    if table_name == '':
        table_name = "Table" + nameG
    arcpy.AddMessage("����·��: " + in_pathG)
    arcpy.AddMessage("���·��: " + out_pathG)
    arcpy.AddMessage("�����ֶ�: " + case_fieldsG)
    arcpy.AddMessage("�ϲ���ı���: " + table_name)
    arcpy.AddMessage("--" *30)


    statisticsArea1(in_pathG, out_pathG, [["Shape_Area", "SUM"]], case_fieldsG,table_name)
    #GDHBZY;XDM;XMC;DLBM;DLMC;PDJB;ZZSXMC;GGSY;GGTJ;PSTJ;TCHD;TRLX;JTZK;PDFF;PJJG;YKDL;TBLX;BZ

    arcpy.AddMessage("--" *30)
    arcpy.AddMessage("����·��: " + in_pathG)
    arcpy.AddMessage("���·��: " + out_pathG)
    arcpy.AddMessage("�����ֶ�: " + case_fieldsG)
    arcpy.AddMessage("�ϲ���ı���: " + table_name)

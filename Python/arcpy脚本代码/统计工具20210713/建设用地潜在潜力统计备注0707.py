# -*- coding: gbk -*-
import sys
import arcpy
import os
import re
import string
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


def xzqab(e):
    if e == "450102":
        return "������"
    elif e == "450103":
        return "������"
    elif e == "450105":
        return "������"
    elif e == "450107":
        return "��������"
    elif e == "450108":
        return "������"
    elif e == "450109":
        return "������"
    elif e == "450110":
        return "������"
    elif e == "450123":
        return "¡����"
    elif e == "450124":
        return "��ɽ��"
    elif e == "450125":
        return "������"
    elif e == "450126":
        return "������"
    elif e == "450127":
        return "����"
    elif e == "4502":
        return "������"
    elif e == "450202":
        return "������"
    elif e == "450203":
        return "�����"
    elif e == "450204":
        return "������"
    elif e == "450205":
        return "������"
    elif e == "450206":
        return "������"
    elif e == "450222":
        return "������"
    elif e == "450223":
        return "¹կ��"
    elif e == "450224":
        return "�ڰ���"
    elif e == "450225":
        return "��ˮ����������"
    elif e == "450226":
        return "��������������"
    elif e == "4503":
        return "������"
    elif e == "450302":
        return "�����"
    elif e == "450303":
        return "������"
    elif e == "450304":
        return "��ɽ��"
    elif e == "450305":
        return "������"
    elif e == "450311":
        return "��ɽ��"
    elif e == "450312":
        return "�ٹ���"
    elif e == "450321":
        return "��˷��"
    elif e == "450323":
        return "�鴨��"
    elif e == "450324":
        return "ȫ����"
    elif e == "450325":
        return "�˰���"
    elif e == "450326":
        return "������"
    elif e == "450327":
        return "������"
    elif e == "450328":
        return "��ʤ����������"
    elif e == "450329":
        return "��Դ��"
    elif e == "450330":
        return "ƽ����"
    elif e == "450332":
        return "��������������"
    elif e == "450381":
        return "������"
    elif e == "4504":
        return "������"
    elif e == "450403":
        return "������"
    elif e == "450405":
        return "������"
    elif e == "450406":
        return "������"
    elif e == "450421":
        return "������"
    elif e == "450422":
        return "����"
    elif e == "450423":
        return "��ɽ��"
    elif e == "450481":
        return "�Ϫ��"
    elif e == "4505":
        return "������"
    elif e == "450502":
        return "������"
    elif e == "450503":
        return "������"
    elif e == "450512":
        return "��ɽ����"
    elif e == "450521":
        return "������"
    elif e == "4506":
        return "���Ǹ���"
    elif e == "450602":
        return "�ۿ���"
    elif e == "450603":
        return "������"
    elif e == "450621":
        return "��˼��"
    elif e == "450681":
        return "������"
    elif e == "4507":
        return "������"
    elif e == "450702":
        return "������"
    elif e == "450703":
        return "�ձ���"
    elif e == "450721":
        return "��ɽ��"
    elif e == "450722":
        return "�ֱ���"
    elif e == "4508":
        return "�����"
    elif e == "450802":
        return "�۱���"
    elif e == "450803":
        return "������"
    elif e == "450804":
        return "������"
    elif e == "450821":
        return "ƽ����"
    elif e == "450881":
        return "��ƽ��"
    elif e == "4509":
        return "������"
    elif e == "450902":
        return "������"
    elif e == "450903":
        return "������"
    elif e == "450921":
        return "����"
    elif e == "450922":
        return "½����"
    elif e == "450923":
        return "������"
    elif e == "450924":
        return "��ҵ��"
    elif e == "450981":
        return "������"
    elif e == "4510":
        return "��ɫ��"
    elif e == "451002":
        return "�ҽ���"
    elif e == "451003":
        return "������"
    elif e == "451022":
        return "�ﶫ��"
    elif e == "451082":
        return "ƽ����"
    elif e == "451024":
        return "�±���"
    elif e == "451026":
        return "������"
    elif e == "451027":
        return "������"
    elif e == "451028":
        return "��ҵ��"
    elif e == "451029":
        return "������"
    elif e == "451030":
        return "������"
    elif e == "451031":
        return "¡�ָ���������"
    elif e == "451081":
        return "������"
    elif e == "4511":
        return "������"
    elif e == "451102":
        return "�˲���"
    elif e == "451103":
        return "ƽ����"
    elif e == "451121":
        return "��ƽ��"
    elif e == "451122":
        return "��ɽ��"
    elif e == "451123":
        return "��������������"
    elif e == "4512":
        return "�ӳ���"
    elif e == "451202":
        return "��ǽ���"
    elif e == "451203":
        return "������"
    elif e == "451221":
        return "�ϵ���"
    elif e == "451222":
        return "�����"
    elif e == "451223":
        return "��ɽ��"
    elif e == "451224":
        return "������"
    elif e == "451225":
        return "�޳�������������"
    elif e == "451226":
        return "����ë����������"
    elif e == "451227":
        return "��������������"
    elif e == "451228":
        return "��������������"
    elif e == "451229":
        return "������������"
    elif e == "4513":
        return "������"
    elif e == "451302":
        return "�˱���"
    elif e == "451321":
        return "�ó���"
    elif e == "451322":
        return "������"
    elif e == "451323":
        return "������"
    elif e == "451324":
        return "��������������"
    elif e == "451381":
        return "��ɽ��"
    elif e == "4514":
        return "������"
    elif e == "451402":
        return "������"
    elif e == "451421":
        return "������"
    elif e == "451422":
        return "������"
    elif e == "451423":
        return "������"
    elif e == "451424":
        return "������"
    elif e == "451425":
        return "�����"
    elif e == "451481":
        return "ƾ����"
    else:
        return e

def statisticsAreaQ3(in_path, out_path, qzql_path, name):
    cout = 0
    fail = 0
    fail_list = []

    arcpy.env.workspace = qzql_path
    qzql_gdb_list = arcpy.ListWorkspaces("*", "FileGDB")

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")

    # ��gdb
    resultg_name = getNewFileNameQ(out_path, name + "_result.gdb")
    result_gdb = os.path.join(out_path, resultg_name)
    arcpy.AddMessage("�½� " + result_gdb + " ���ڱ�����...")
    arcpy.CreateFileGDB_management(out_path, resultg_name)

    resullist = []
    xjh_list = []

    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        # ��ÿ��gdb��Ϊ������
        arcpy.env.workspace = workspace
        fc_list = arcpy.ListFeatureClasses()
        gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])

        xzqcode = re.findall(r"\d+", gdbName)

        if len(xzqcode) > 0 and not xzqab(xzqcode[0]).isdigit():
            row_values = [cout, xzqab(xzqcode[0]), 0, 0, 0, 0, 0, 0,0,0,0,0,0]
        else:
            row_values = [cout, gdbName, 0, 0, 0, 0, 0,0,0,0,0,0,0]

        try:
            qzql_fc_pathp = ""
            for qzql_gdb in qzql_gdb_list:
                if xzqcode[0] in os.path.basename(qzql_gdb):
                    arcpy.env.workspace = qzql_gdb
                    for qzql_fc in arcpy.ListFeatureClasses():
                        qzql_fc_pathp = os.path.join(qzql_gdb, qzql_fc)
                        break
                    break

            if qzql_fc_pathp == "":
                arcpy.AddError("        �Ҳ����� " + os.path.basename(workspace) + " ��Ӧ�Ľ����õ�Ǳ��Ǳ���ο�ͼ�㣡")
                fail += 1
                resullist.append(row_values)
                fail_list.append(workspace)
                continue

            for in_fc in fc_list:
                in_fc_path = os.path.join(workspace,in_fc)
                arcpy.AddMessage("        " + in_fc)

                if "����" in in_fc or u"����" in in_fc:
                    arcpy.AddMessage("         " + in_fc + "�ཻ ...")
                    intersect_path = os.path.join(result_gdb,in_fc + str(cout))
                    arcpy.Intersect_analysis([in_fc_path,qzql_fc_pathp],intersect_path)
                    xjh_list.append(intersect_path)

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
            fail += 1

    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage("  �ཻ�ɹ���" + str(cout - fail) + " ����")
    if fail > 0:
        arcpy.AddError("  �ཻʧ�ܣ�" + str(fail) + " ���� ���£�")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)

    try:
        meger_path = os.path.join(result_gdb,"H�ϲ�")
        meger_table = os.path.join(result_gdb,getNewFileNameQ(result_gdb, name))
        arcpy.AddMessage("    " + str(len(xjh_list)) + "���ϲ� ...")
        arcpy.Merge_management(xjh_list, meger_path)
        arcpy.AddMessage("    ����ͳ�� ...")
        arcpy.Statistics_analysis(meger_path, meger_table, [["Shape_Area", "SUM"]], ['XMC','PJJG','YKDL','DLBM','BZ'])
    except Exception as e:
        arcpy.AddError("    �ϲ�ʧ�ܣ�")
        arcpy.AddError(e.message)
    # arcpy.AddMessage('+' * 60)
    # arcpy.AddMessage("  �ɹ���" + str(cout - fail) + " ����")
    # if fail > 0:
    #     arcpy.AddError("  ʧ�ܣ�" + str(fail) + " ���� ���£�")
    #     arcpy.AddError("####" + '*' * 20)
    #     for ff in fail_list:
    #         arcpy.AddError("  " + ff)
    #     arcpy.AddError("####" + '*' * 20)
    # arcpy.AddMessage('+' * 60)

if __name__ == "__main__":
    in_pathG = arcpy.GetParameterAsText(0)
    qzql_pathG = arcpy.GetParameterAsText(1)
    out_pathG = arcpy.GetParameterAsText(2)
    table_nameG = arcpy.GetParameterAsText(3)

    listtt123 = re.findall(r"[^\\/:*?\"<>|]", table_nameG)
    table_name_global = "".join(listtt123).strip()

    statisticsAreaQ3(in_pathG, out_pathG, qzql_pathG, table_name_global)

    # ls = [[1, u"��˷��", 0,0,0,0,0],[2, u"��˷��", 0,0,0,0,0],[3, u"��˷��", 0,0,0,0,0]]
    # table_path_e3 = u"D:\\pyCharmWorksp\\ABC������.xls"
    # tableToExcelQ(table_path_e3, ls, u"�˿ѵ������ͳ��")


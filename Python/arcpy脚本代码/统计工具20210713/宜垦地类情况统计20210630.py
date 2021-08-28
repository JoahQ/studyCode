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


def checkLayerNameAndGetPathQ(in_gdb):
    arcpy.env.workspace = in_gdb
    in_fc_list = []
    fc_lists = arcpy.ListFeatureClasses()
    right_name = True
    null_layer = True
    for fc in fc_lists:
        a = ("ũ��" in fc or "δ��" in fc or "����" in fc or "���ʸ���" in fc or "������ȡ" in fc)
        b = (u"ũ��" in fc or u"δ��" in fc or u"����" in fc or u"���ʸ���" in fc or "������ȡ" in fc)
        if a or b:
            in_fc_list.append(os.path.join(arcpy.env.workspace, fc))
        else:
            right_name = False
            arcpy.AddError("    \"" + fc + "\" ͼ���������淶������")
    dataset_ls = arcpy.ListDatasets()
    for dataset in dataset_ls:
        arcpy.env.workspace = os.path.join(in_gdb, dataset)
        fc_ls = arcpy.ListFeatureClasses()
        for fc in fc_ls:
            null_layer = False
            a = ("ũ��" in fc or "δ��" in fc or "����" in fc or "���ʸ���" in fc or "������ȡ" in fc)
            b = (u"ũ��" in fc or u"δ��" in fc or u"����" in fc or u"���ʸ���" in fc or "������ȡ" in fc)
            if a or b:
                in_fc_list.append(os.path.join(arcpy.env.workspace, fc))
            else:
                right_name = False
                arcpy.AddError("    \"" + fc + "\" ͼ���������淶������")

    if len(fc_lists) > 0:
        null_layer = False
    if not right_name:
        arcpy.AddError("���ݿ⣺" + in_gdb + " ͼ���������淶������")
        arcpy.AddMessage("-" * 25)
        arcpy.AddMessage("  ��׼��ͼ������Ӧ��Ϊ��")
        arcpy.AddMessage("     �������ʸ���Ǳ������ͼ��")
        arcpy.AddMessage("     �����õظ���Ǳ������ͼ��")
        arcpy.AddMessage("     �˸�ũ�õ�Ǳ������ͼ��")
        arcpy.AddMessage("     �˸�δ���õ�Ǳ������ͼ��")
        arcpy.AddMessage("-" * 25)
    if null_layer:
        arcpy.AddError("���ݿ⣺" + in_gdb + " Ϊ�ջ������𻵣��޷��򿪣�����")
        right_name = False
    return [right_name, in_fc_list]


def createTableQ(path, name):
    """
    �½����arcgis���Ա���ָ���̶��ֶ�
    :param path:
    :param name:
    :return:
    """
    asa123 = re.findall(r"[^()\[\]{},.*/|\\:;?\'\"<>%!@#$&\-+=`~]", name)
    name11 = "".join(asa123)
    table_name = name11.lstrip(string.digits)
    if table_name == '':
        table_name = "Table" + name
    tb_path = os.path.join(path, table_name)
    field_ls = []
    # ���ֵ������ֶ����ԣ����б��������ֶ�
    field_list = [{'name': 'cout', 'type': 'TEXT', 'alias': '���'},  # 0
                  {'name': 'XZQ1', 'type': 'TEXT', 'alias': '������'},  # 0

                  {'name': 'A2', 'type': 'DOUBLE', 'alias': '2'},  # 1
                  {'name': 'B3', 'type': 'DOUBLE', 'alias': '3'},  # 2
                  {'name': 'C4', 'type': 'DOUBLE', 'alias': '4'},  # 3
                  {'name': 'D5', 'type': 'DOUBLE', 'alias': '5'},  # 4

                  {'name': 'E6', 'type': 'DOUBLE', 'alias': '6'},  # 5
                  {'name': 'F7', 'type': 'DOUBLE', 'alias': '7'},  # 6
                  {'name': 'G8', 'type': 'DOUBLE', 'alias': '8'},  # 7
                  {'name': 'H9', 'type': 'DOUBLE', 'alias': '9'},  # 8
                  {'name': 'I10', 'type': 'DOUBLE', 'alias': '10'},  # 9

                  {'name': 'J11', 'type': 'DOUBLE', 'alias': '11'},  # 10
                  {'name': 'K12', 'type': 'DOUBLE', 'alias': '12'},  # 11
                  {'name': 'L13', 'type': 'DOUBLE', 'alias': '13'},  # 12
                  {'name': 'M14', 'type': 'DOUBLE', 'alias': '14'},  # 13

                  {'name': 'N15', 'type': 'DOUBLE', 'alias': '15'},  # 14
                  {'name': 'O16', 'type': 'DOUBLE', 'alias': '16'},  # 15
                  {'name': 'P17', 'type': 'DOUBLE', 'alias': '17'},  # 16
                  {'name': 'Q18', 'type': 'DOUBLE', 'alias': '18'},  # 17
                  {'name': 'R19', 'type': 'DOUBLE', 'alias': '19'},  # 18
                  {'name': 'S20', 'type': 'DOUBLE', 'alias': '20'},  # 19
                  {'name': 'T21', 'type': 'DOUBLE', 'alias': '21'},  # 20

                  {'name': 'U22', 'type': 'DOUBLE', 'alias': '22'},  # 21
                  {'name': 'V23', 'type': 'DOUBLE', 'alias': '23'},  # 22
                  {'name': 'W24', 'type': 'DOUBLE', 'alias': '24'},  # 23
                  {'name': 'X25', 'type': 'DOUBLE', 'alias': '25'},  # 24
                  {'name': 'Y26', 'type': 'DOUBLE', 'alias': '26'},  # 25
                  {'name': 'Z27', 'type': 'DOUBLE', 'alias': '27'},  # 26

                  {'name': 'AA28', 'type': 'DOUBLE', 'alias': '28'},  # 27
                  {'name': 'AB29', 'type': 'DOUBLE', 'alias': '29'},  # 28
                  {'name': 'AC30', 'type': 'DOUBLE', 'alias': '30'},  # 29
                  {'name': 'AD31', 'type': 'DOUBLE', 'alias': '31'},  # 30
                  {'name': 'AE32', 'type': 'DOUBLE', 'alias': '32'},  # 31
                  {'name': 'AF33', 'type': 'DOUBLE', 'alias': '33'},  # 31
                  {'name': 'AG34', 'type': 'DOUBLE', 'alias': '34'},  # 31
                  {'name': 'AH35', 'type': 'DOUBLE', 'alias': '35'},  # 31
                  {'name': 'AI36', 'type': 'DOUBLE', 'alias': '36'},  # 31
                  {'name': 'A37', 'type': 'DOUBLE', 'alias': '37'},  # 31
                  {'name': 'A38', 'type': 'DOUBLE', 'alias': '38'},  # 31
                  {'name': 'A39', 'type': 'DOUBLE', 'alias': '39'},  # 31
                  {'name': 'A40', 'type': 'DOUBLE', 'alias': '40'},  # 31
                  {'name': 'A41', 'type': 'DOUBLE', 'alias': '41'},  # 31
                  {'name': 'AI42', 'type': 'DOUBLE', 'alias': '42'},  # 31
                  {'name': 'AI43', 'type': 'DOUBLE', 'alias': '43'},  # 31
                  {'name': 'AI44', 'type': 'DOUBLE', 'alias': '44'},  # 31
                  {'name': 'AI45', 'type': 'DOUBLE', 'alias': '45'},  # 31
                  {'name': 'AI46', 'type': 'DOUBLE', 'alias': '46'},  # 31
                  {'name': 'AI47', 'type': 'DOUBLE', 'alias': '47'},  # 31
                  {'name': 'AI48', 'type': 'DOUBLE', 'alias': '48'},  # 31
                  {'name': 'AI49', 'type': 'DOUBLE', 'alias': '49'},  # 31
                  {'name': 'AI50', 'type': 'DOUBLE', 'alias': '50'},  # 31
                  {'name': 'AI51', 'type': 'DOUBLE', 'alias': '51'},  # 31
                  {'name': 'AI52', 'type': 'DOUBLE', 'alias': '52'},  # 31
                  {'name': 'AI53', 'type': 'DOUBLE', 'alias': '53'},  # 31
                  {'name': 'AI54', 'type': 'DOUBLE', 'alias': '54'},  # 31
                  {'name': 'AI55', 'type': 'DOUBLE', 'alias': '55'},  # 31
                  {'name': 'AI56', 'type': 'DOUBLE', 'alias': '56'},  # 31
                  {'name': 'AI57', 'type': 'DOUBLE', 'alias': '57'},  # 31
                  {'name': 'AI58', 'type': 'DOUBLE', 'alias': '58'},  # 31
                  {'name': 'AI59', 'type': 'DOUBLE', 'alias': '59'},  # 31
                  {'name': 'AI60', 'type': 'DOUBLE', 'alias': '60'},  # 31
                  {'name': 'AI61', 'type': 'DOUBLE', 'alias': '61'},  # 31
                  {'name': 'AI62', 'type': 'DOUBLE', 'alias': '62'},  # 31
                  {'name': 'AI63', 'type': 'DOUBLE', 'alias': '63'},  # 31
                  {'name': 'AI64', 'type': 'DOUBLE', 'alias': '64'},  # 31
                  {'name': 'AI65', 'type': 'DOUBLE', 'alias': '65'},  # 31
                  {'name': 'AI66', 'type': 'DOUBLE', 'alias': '66'},  # 31

                  ]

    arcpy.AddMessage("�½� " + table_name + " ���...")
    arcpy.CreateTable_management(path, table_name)
    arcpy.AddMessage("  ����ֶ�...")
    arcpy.AddMessage("-" * 50)
    for field in field_list:
        # arcpy.AddMessage("    �ֶ����� " + field['name'] + " �ֶα����� " + field['alias'])
        arcpy.AddField_management(tb_path, field['name'], field['type'], "#", "#", "#", field['alias'])
        field_ls.append(field['name'])
    arcpy.AddMessage("-" * 50)
    return [tb_path, field_ls]

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

def statisticsAreaQ3(in_path, out_path, where_clause, name):
    cout = 0
    fail = 0
    fail_list = []

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")
    if len(workspaces) <= 0:
        right_name_path = checkLayerNameAndGetPathQ(in_path)
        if not right_name_path[0]:
            fail += 1
            fail_list.append(os.path.basename(in_path))
            arcpy.AddError("||||" + "*" * 20)
            arcpy.AddError(" <" + str(fail) + "> " + os.path.basename(in_path) + " ʧ�ܣ�")
            arcpy.AddError("||||" + "*" * 20)
            sys.exit()
        workspaces = [in_path]

    temp_name1 = getNewFileNameQ(out_path, name + "_result.gdb")
    result_gdb = os.path.join(out_path, temp_name1)
    arcpy.AddMessage("�½� " + result_gdb + " ���ڱ��������Ա�...")
    arcpy.CreateFileGDB_management(out_path, temp_name1)
    # ����
    arcpy.AddMessage("-"*20 + "�½����Ա�" + "-"*20)
    tb_paths = createTableQ(result_gdb, getNewFileNameQ(result_gdb, name))
    tb_path = tb_paths[0]
    field_ls = tb_paths[1]
    tb_name = os.path.basename(tb_path)

    in_cursor = arcpy.da.InsertCursor(tb_path, field_ls)
    resullist = []
    for workspace in workspaces:
        success = True
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        # ��ÿ��gdb��Ϊ������
        arcpy.env.workspace = workspace
        gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])

        right_name_path = checkLayerNameAndGetPathQ(workspace)
        if not right_name_path[0]:
            fail += 1
            fail_list.append(workspace)
            arcpy.AddError("||||" + "*" * 20)
            arcpy.AddError(" <" + str(fail) + "> " + os.path.basename(workspace) + " ʧ�ܣ�")
            arcpy.AddError("||||" + "*" * 20)
            continue

        xzqcode = re.findall(r"\d+", gdbName)
        if len(xzqcode) > 0 and not xzqab(xzqcode[0]).isdigit():
            row_values = [cout, xzqab(xzqcode[0]),
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0]
        else:
            row_values = [cout, gdbName,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0]

        try:
            for iin_fc_path in right_name_path[1]:
                fc = os.path.basename(iin_fc_path)
                arcpy.AddMessage("        " + fc)

                pdff_tb = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "pdff_table" + str(cout)))
                arcpy.Statistics_analysis(iin_fc_path, pdff_tb, [["PDFF", "COUNT"]], 'PDFF')  # COUNT_PDFF
                if "ũ��" in fc or u"ũ��" in fc:
                    with arcpy.da.SearchCursor(pdff_tb, ('PDFF', 'COUNT_PDFF')) as cursor1:
                        for row1 in cursor1:
                            if "��ҵ�ж�" in str(row1[0]):
                                row_values[47] = row_values[47] + row1[1]
                            if "ʵ�ص���" in str(row1[0]):
                                row_values[48] = row_values[48] + row1[1]
                            if "���;�֤" in str(row1[0]):
                                row_values[49] = row_values[49] + row1[1]
                            if "������֤��Ƭ�ж�" in str(row1[0]):
                                row_values[50] = row_values[50] + row1[1]

                elif "δ��" in fc or u"δ��" in fc:
                    with arcpy.da.SearchCursor(pdff_tb, ('PDFF', 'COUNT_PDFF')) as cursor1:
                        for row1 in cursor1:
                            if "��ҵ�ж�" in str(row1[0]):
                                row_values[51] = row_values[51] + row1[1]
                            if "ʵ�ص���" in str(row1[0]):
                                row_values[52] = row_values[52] + row1[1]
                            if "���;�֤" in str(row1[0]):
                                row_values[53] = row_values[53] + row1[1]
                            if "������֤��Ƭ�ж�" in str(row1[0]):
                                row_values[54] = row_values[54] + row1[1]

                elif "����" in fc or u"����" in fc:
                    with arcpy.da.SearchCursor(pdff_tb, ('PDFF', 'COUNT_PDFF')) as cursor1:
                        for row1 in cursor1:
                            if "��ҵ�ж�" in str(row1[0]):
                                row_values[55] = row_values[55] + row1[1]
                            if "ʵ�ص���" in str(row1[0]):
                                row_values[56] = row_values[56] + row1[1]
                            if "���;�֤" in str(row1[0]):
                                row_values[57] = row_values[57] + row1[1]
                            if "������֤��Ƭ�ж�" in str(row1[0]):
                                row_values[58] = row_values[58] + row1[1]

                elif "���ʸ���" in fc or u"���ʸ���" in fc:
                    with arcpy.da.SearchCursor(pdff_tb, ('PDFF', 'COUNT_PDFF')) as cursor1:
                        for row1 in cursor1:
                            if "��ҵ�ж�" in str(row1[0]):
                                row_values[59] = row_values[59] + row1[1]
                            if "ʵ�ص���" in str(row1[0]):
                                row_values[60] = row_values[60] + row1[1]
                            if "���;�֤" in str(row1[0]):
                                row_values[61] = row_values[61] + row1[1]
                            if "������֤��Ƭ�ж�" in str(row1[0]):
                                row_values[62] = row_values[62] + row1[1]

                elif "������ȡ" in fc or u"������ȡ" in fc:
                    with arcpy.da.SearchCursor(pdff_tb, ('PDFF', 'COUNT_PDFF')) as cursor1:
                        for row1 in cursor1:
                            if "��ҵ�ж�" in str(row1[0]):
                                row_values[63] = row_values[63] + row1[1]
                            if "ʵ�ص���" in str(row1[0]):
                                row_values[64] = row_values[64] + row1[1]
                            if "���;�֤" in str(row1[0]):
                                row_values[65] = row_values[65] + row1[1]
                            if "������֤��Ƭ�ж�" in str(row1[0]):
                                row_values[66] = row_values[66] + row1[1]

                if arcpy.Exists(pdff_tb):
                    try:
                        arcpy.Delete_management(pdff_tb)
                    except Exception as e:
                        arcpy.AddMessage(e.message)

                if "������ȡ" in fc or u"������ȡ" in fc:
                    out_feature = iin_fc_path
                else:
                    out_feature = os.path.join(result_gdb, getNewFileNameQ(result_gdb, fc + str(cout)))
                    arcpy.Select_analysis(iin_fc_path, out_feature, where_clause + u" like \'%��%\'")

                if long(arcpy.GetCount_management(out_feature).getOutput(0)) > 0:
                    if "ũ��" in fc or u"ũ��" in fc:
                        nyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "nyd_table" + str(cout)))
                        arcpy.Statistics_analysis(out_feature, nyd_tb1, [["Shape_Area", "SUM"]], ['YKDL', 'ZZSXMC'])
                        with arcpy.da.SearchCursor(nyd_tb1, ('YKDL', 'ZZSXMC', 'SUM_Shape_Area')) as cursor1:
                            for row1 in cursor1:
                                if "0101" in str(row1[0]):
                                    if "���ָ̻�" in str(row1[1]) or "���ɻָ�" in str(row1[1]):
                                        row_values[17] = row_values[17] + row1[2]
                                    else:
                                        row_values[18] = row_values[18] + row1[2]
                                elif "0103" in str(row1[0]):
                                    if "���ָ̻�" in str(row1[1]) or "���ɻָ�" in str(row1[1]):
                                        row_values[20] = row_values[20] + row1[2]
                                    else:
                                        row_values[21] = row_values[21] + row1[2]

                        row_values[16] = row_values[17] + row_values[18]
                        row_values[19] = row_values[20] + row_values[21]
                        row_values[15] = row_values[16] + row_values[19]

                        if arcpy.Exists(nyd_tb1):
                            try:
                                arcpy.Delete_management(nyd_tb1)
                            except Exception as e:
                                arcpy.AddMessage(e.message)

                    elif "δ��" in fc or u"δ��" in fc:
                        wlyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "wlyd_table" + str(cout)))
                        arcpy.Statistics_analysis(out_feature, wlyd_tb1, [["Shape_Area", "SUM"]], 'YKDL')
                        with arcpy.da.SearchCursor(wlyd_tb1, ('YKDL', 'SUM_Shape_Area')) as cursor1:
                            for row1 in cursor1:
                                if "0101" in str(row1[0]):
                                    row_values[23] = row_values[23] + row1[1]
                                if "0103" in str(row1[0]):
                                    row_values[24] = row_values[24] + row1[1]
                        row_values[22] = row_values[23] + row_values[24]

                        if arcpy.Exists(wlyd_tb1):
                            try:
                                arcpy.Delete_management(wlyd_tb1)
                            except Exception as e:
                                arcpy.AddMessage(e.message)

                    elif "����" in fc or u"����" in fc:
                        jsyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "jsyd_table" + str(cout)))
                        arcpy.Statistics_analysis(out_feature, jsyd_tb1, [["Shape_Area", "SUM"]], 'YKDL')
                        with arcpy.da.SearchCursor(jsyd_tb1, ('YKDL', 'SUM_Shape_Area')) as cursor1:
                            for row1 in cursor1:
                                if "0101" in str(row1[0]):
                                    row_values[26] = row_values[26] + row1[1]
                                if "0103" in str(row1[0]):
                                    row_values[27] = row_values[27] + row1[1]
                                if "QT" in str(row1[0]):
                                    row_values[28] = row_values[28] + row1[1]
                        row_values[25] = row_values[26] + row_values[27] + row_values[28]

                        if arcpy.Exists(jsyd_tb1):
                            try:
                                arcpy.Delete_management(jsyd_tb1)
                            except Exception as e:
                                arcpy.AddMessage(e.message)

                    elif "���ʸ���" in fc or u"���ʸ���" in fc:
                        tzgz_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "tzgz_table" + str(cout)))
                        arcpy.Statistics_analysis(out_feature, tzgz_tb1, [["Shape_Area", "SUM"]], ['YKDL', 'ZZSXMC'])
                        with arcpy.da.SearchCursor(tzgz_tb1, ('YKDL', 'ZZSXMC', 'SUM_Shape_Area')) as cursor1:
                            for row1 in cursor1:
                                if "0101" in str(row1[0]):
                                    if "���ָ̻�" in str(row1[1]):
                                        row_values[30] = row_values[30] + row1[2]
                                    elif "���ɻָ�" in str(row1[1]):
                                        row_values[31] = row_values[31] + row1[2]
                                    else:
                                        row_values[32] = row_values[32] + row1[2]
                        row_values[29] = row_values[30] + row_values[31] + row_values[32]

                        if arcpy.Exists(tzgz_tb1):
                            try:
                                arcpy.Delete_management(tzgz_tb1)
                            except Exception as e:
                                arcpy.AddMessage(e.message)

                    elif "������ȡ" in fc or u"������ȡ" in fc:
                        zztq_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "zztq_table" + str(cout)))
                        arcpy.Statistics_analysis(out_feature, zztq_tb1, [["Shape_Area", "SUM"]], ['GDHBZY','YKDL'])
                        with arcpy.da.SearchCursor(zztq_tb1, ('GDHBZY','YKDL', 'SUM_Shape_Area')) as cursor1:
                            for row1 in cursor1:
                                if "ũ�õ�" in str(row1[0]):
                                    if "0101" in str(row1[1]):
                                        row_values[35] = row_values[35] + row1[2]
                                    if "0103" in str(row1[1]):
                                        row_values[36] = row_values[36] + row1[2]

                                if "δ���õ�" in str(row1[0]):
                                    if "0101" in str(row1[1]):
                                        row_values[38] = row_values[38] + row1[2]
                                    if "0103" in str(row1[1]):
                                        row_values[39] = row_values[39] + row1[2]

                                if "�����õ�" in str(row1[0]):
                                    if "0101" in str(row1[1]):
                                        row_values[41] = row_values[41] + row1[2]
                                    if "0103" in str(row1[1]):
                                        row_values[42] = row_values[42] + row1[2]
                                    if "QT" in str(row1[1]):
                                        row_values[43] = row_values[43] + row1[2]

                                if "���ʸ���" in str(row1[0]):
                                    if "0101" in str(row1[1]):
                                        row_values[45] = row_values[45] + row1[2]
                                    if "0103" in str(row1[1]):
                                        row_values[46] = row_values[46] + row1[2]

                        row_values[34] = row_values[35] + row_values[36]
                        row_values[37] = row_values[38] + row_values[39]
                        row_values[40] = row_values[41] + row_values[42] + row_values[43]
                        row_values[44] = row_values[45] + row_values[46]
                        row_values[33] = row_values[34] + row_values[37] + row_values[40] + row_values[44]

                        if arcpy.Exists(zztq_tb1):
                            try:
                                arcpy.Delete_management(zztq_tb1)
                            except Exception as e:
                                arcpy.AddMessage(e.message)
                else:
                    arcpy.AddWarning(u"          ���棺" + gdbName + u" �� " + fc + u" ͼ�㰴" + where_clause +
                                     u"Ϊ\'��\'ɸѡ������ͼ����Ϊ0��")

                if not ("������ȡ" in fc or u"������ȡ" in fc):
                    if arcpy.Exists(out_feature):
                        try:
                            arcpy.Delete_management(out_feature)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

            row_values[14] = row_values[28]
            row_values[13] = row_values[21] + row_values[24] + row_values[27]
            row_values[12] = row_values[20]
            row_values[11] = row_values[12] + row_values[13]

            row_values[10] = row_values[18] + row_values[23] + row_values[26] + row_values[32]
            row_values[9] = row_values[31]
            row_values[8] = row_values[17] + row_values[30]
            row_values[7] = row_values[8] + row_values[9] + row_values[10]
            row_values[6] = row_values[7] + row_values[11] + row_values[14]
            row_values[5] = row_values[14] + row_values[43]

            row_values[4] = row_values[11] + row_values[36] + row_values[39] + row_values[42] + row_values[46]
            row_values[3] = row_values[7] + row_values[35] + row_values[38] + row_values[41] + row_values[45]
            row_values[2] = row_values[3] + row_values[4] + row_values[5]


        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
            fail += 1
            success = False

        if success:
            resullist.append(row_values)
            arcpy.AddMessage("    �� " + tb_name + " ������¼...")
            try:
                in_cursor.insertRow(tuple(row_values))
            except Exception as e:
                arcpy.AddError(e.message)
                arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
                fail += 1
            resullist.append(row_values)
        arcpy.AddMessage("  ")

    del in_cursor

    table_path_e3 = os.path.join(out_path, getNewFileNameQ(out_path, name + ".xls"))
    tableToExcelQ(table_path_e3, resullist, "�˿ѵ������ͳ��")
    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage("  �ɹ���" + str(cout - fail) + " ����")
    if fail > 0:
        arcpy.AddError("  ʧ�ܣ�" + str(fail) + " ���� ���£�")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)


def tableToExcelQ(excel_path3, datalist, sheets_name3='sheet'):
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)

    def set_style(font_name, font_size, borders=False, ali_center=False, bolds=False):
        style_i = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = font_name
        font.height = 20 * font_size
        font.bold = bolds
        style_i.font = font

        if borders:
            borderi = xlwt.Borders()
            borderi.left = xlwt.Borders.THIN
            borderi.bottom = xlwt.Borders.THIN
            borderi.right = xlwt.Borders.THIN
            borderi.top = xlwt.Borders.THIN
            style_i.borders = borderi
        if ali_center:
            ali = xlwt.Alignment()
            ali.horz = 0x02
            ali.vert = 0x01
            ali.wrap = 1
            style_i.alignment = ali
        return style_i

    # �����и�
    def set_row_height(work_sheet, row_index, row_height):
        work_sheet.row(row_index).height_mismatch = True
        work_sheet.row(row_index).height = 20 * row_height

    # �����п�
    def set_col_width(work_sheet, col_index, col_width):
        work_sheet.col(col_index).width = 256 * col_width

    def add_new_sheet(sheet_name):
        worksheets = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)

        style1 = set_style(u'����', 11, True, True)
        style2 = set_style(u'����', 11)
        ali1 = xlwt.Alignment()
        ali1.horz = 0x03
        ali1.vert = 0x01
        style2.alignment = ali1
        del ali1

        style3 = set_style(u'����', 16, False, True, True)
        ali4 = xlwt.Alignment()
        ali4.horz = 0x02
        ali4.vert = 0x00
        style3.alignment = ali4
        del ali4
        bt = u"�������غ���Դ��Ǳ������ͳ�Ʊ��˿ѵ��ࣩ"
        worksheets.write_merge(0, 0, 0, 66, bt, style3)
        worksheets.write_merge(1, 1, 0, 46, u'���������', style2)

        worksheets.write_merge(2, 5, 0, 0, u'���', style1)
        worksheets.write_merge(2, 5, 1, 1, u'����������', style1)
        worksheets.write_merge(2, 4, 2, 5, u'�ܸ��غ���ԴǱ��', style1)

        worksheets.write(5, 2, u'�ܼ�', style1)
        worksheets.write(5, 3, u'ˮ��', style1)
        worksheets.write(5, 4, u'����', style1)
        worksheets.write(5, 5, u'����ũ�õأ�QT��', style1)

        worksheets.write_merge(2, 2, 6, 32, u'���غ���Դ���ͣ��������·���', style1)
        worksheets.write_merge(3, 3, 6, 14, u'�ϼ�', style1)

        worksheets.write_merge(4, 5, 6, 6, u'�ϼ�', style1)
        worksheets.write_merge(4, 4, 7, 10, u'ˮ�0101��', style1)
        worksheets.write(5, 7, u'С��', style1)
        worksheets.write(5, 8, u'���ָ̻�', style1)
        worksheets.write(5, 9, u'���ɻָ�', style1)
        worksheets.write(5, 10, u'δ��ע�ָ�����', style1)

        worksheets.write_merge(4, 4, 11, 13, u'���أ�0103��', style1)
        worksheets.write(5, 11, u'С��', style1)
        worksheets.write(5, 12, u'���ָ̻�', style1)
        worksheets.write(5, 13, u'���ɻָ�', style1)

        worksheets.write_merge(4, 5, 14, 14, u'����ũ�õأ�QT��', style1)

        # �˸�ũ�õ�Ǳ������ͼ��
        worksheets.write_merge(3, 3, 15, 21, u'�˸�ũ�õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 15, 15, u'С��', style1)
        worksheets.write_merge(4, 4, 16, 18, u'ˮ�0101��', style1)
        worksheets.write(5, 16, u'С��', style1)
        worksheets.write(5, 17, u'���ָ̻�', style1)
        worksheets.write(5, 18, u'δ��ע�ָ�����', style1)
        worksheets.write_merge(4, 4, 19, 21, u'���أ�0103��', style1)
        worksheets.write(5, 19, u'С��', style1)
        worksheets.write(5, 20, u'���ָ̻�', style1)
        worksheets.write(5, 21, u'δ��ע�ָ�����', style1)

        # �˸�δ���õ�Ǳ������ͼ��
        worksheets.write_merge(3, 3, 22, 24, u'�˸�δ���õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 22, 22, u'С��', style1)
        worksheets.write_merge(4, 5, 23, 23, u'ˮ�0101��', style1)
        worksheets.write_merge(4, 5, 24, 24, u'���أ�0103��', style1)

        # �����õظ���Ǳ������ͼ��
        worksheets.write_merge(3, 3, 25, 28, u'�����õظ���Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 25, 25, u'С��', style1)
        worksheets.write_merge(4, 5, 26, 26, u'ˮ�0101��', style1)
        worksheets.write_merge(4, 5, 27, 27, u'���أ�0103��', style1)
        worksheets.write_merge(4, 5, 28, 28, u'����ũ�õأ�QT��', style1)

        # �������ʸ���Ǳ������ͼ��
        worksheets.write_merge(3, 3, 29, 32, u'�������ʸ���Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 4, 29, 32, u'ˮ�0101��', style1)
        worksheets.write(5, 29, u'С��', style1)
        worksheets.write(5, 30, u'���ָ̻�', style1)
        worksheets.write(5, 31, u'���ɻָ�', style1)
        worksheets.write(5, 32, u'δ��ע�ָ�����', style1)

        # ������ȡ
        worksheets.write_merge(2, 2, 33, 46, u'������ȡǱ��', style1)
        worksheets.write_merge(3, 5, 33, 33, u'�ϼ�', style1)
        worksheets.write_merge(3, 3, 34, 36, u'�˸�ũ�õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 34, 34, u'С��', style1)
        worksheets.write_merge(4, 5, 35, 35, u'ˮ�0101��', style1)
        worksheets.write_merge(4, 5, 36, 36, u'���أ�0103��', style1)


        worksheets.write_merge(3, 3, 37, 39, u'�˸�δ���õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 37, 37, u'С��', style1)
        worksheets.write_merge(4, 5, 38, 38, u'ˮ�0101��', style1)
        worksheets.write_merge(4, 5, 39, 39, u'���أ�0103��', style1)


        worksheets.write_merge(3, 3, 40, 43, u'�����õظ���Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 40, 40, u'С��', style1)
        worksheets.write_merge(4, 5, 41, 41, u'ˮ�0101��', style1)
        worksheets.write_merge(4, 5, 42, 42, u'���أ�0103��', style1)
        worksheets.write_merge(4, 5, 43, 43, u'����ũ�õأ�QT��', style1)

        worksheets.write_merge(3, 3, 44, 46, u'�������ʸ���Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 44, 44, u'С��', style1)
        worksheets.write_merge(4, 5, 45, 45, u'ˮ�0101��', style1)
        worksheets.write_merge(4, 5, 46, 46, u'���أ�0103��', style1)

        # �ж�����ͼ����
        worksheets.write_merge(2, 2, 47, 66, u'���ж�����ͼ����', style1)
        worksheets.write_merge(3, 3, 47, 50, u'�˸�ũ�õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 47, 47, u'��ҵ�ж�', style1)
        worksheets.write_merge(4, 5, 48, 48, u'ʵ�ص���', style1)
        worksheets.write_merge(4, 5, 49, 49, u'���;�֤', style1)
        worksheets.write_merge(4, 5, 50, 50, u'������֤��Ƭ�ж�', style1)


        worksheets.write_merge(3, 3, 51, 54, u'�˸�δ���õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 51, 51, u'��ҵ�ж�', style1)
        worksheets.write_merge(4, 5, 52, 52, u'ʵ�ص���', style1)
        worksheets.write_merge(4, 5, 53, 53, u'���;�֤', style1)
        worksheets.write_merge(4, 5, 54, 54, u'������֤��Ƭ�ж�', style1)


        worksheets.write_merge(3, 3, 55, 58, u'�����õظ���Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 55, 55, u'��ҵ�ж�', style1)
        worksheets.write_merge(4, 5, 56, 56, u'ʵ�ص���', style1)
        worksheets.write_merge(4, 5, 57, 57, u'���;�֤', style1)
        worksheets.write_merge(4, 5, 58, 58, u'������֤��Ƭ�ж�', style1)

        worksheets.write_merge(3, 3, 59, 62, u'�������ʸ���Ǳ������ͼ��', style1)
        worksheets.write_merge(4, 5, 59, 59, u'��ҵ�ж�', style1)
        worksheets.write_merge(4, 5, 60, 60, u'ʵ�ص���', style1)
        worksheets.write_merge(4, 5, 61, 61, u'���;�֤', style1)
        worksheets.write_merge(4, 5, 62, 62, u'������֤��Ƭ�ж�', style1)

        worksheets.write_merge(3, 3, 63, 66, u'������ȡǱ������ͼ��', style1)
        worksheets.write_merge(4, 5, 63, 63, u'��ҵ�ж�', style1)
        worksheets.write_merge(4, 5, 64, 64, u'ʵ�ص���', style1)
        worksheets.write_merge(4, 5, 65, 65, u'���;�֤', style1)
        worksheets.write_merge(4, 5, 66, 66, u'������֤��Ƭ�ж�', style1)

        # �����и�
        set_row_height(worksheets, row_index=0, row_height=28)
        set_row_height(worksheets, row_index=1, row_height=22)
        set_row_height(worksheets, row_index=2, row_height=20)
        set_row_height(worksheets, row_index=3, row_height=20)
        set_row_height(worksheets, row_index=4, row_height=20)
        set_row_height(worksheets, row_index=5, row_height=40)

        return worksheets

    sheet1 = add_new_sheet(sheets_name3)
    styles = set_style(u'����', 11, True, True)
    style_num = set_style(u'����', 11, True, True)
    ali3 = xlwt.Alignment()
    # 0x02 ��˶��룬0x03 �Ҷ˶���
    ali3.horz = 0x03
    ali3.vert = 0x01
    style_num.alignment = ali3
    num_format_str = '0.0000'
    style_num.num_format_str = num_format_str
    stylesN = set_style(u'����', 11, True, True)
    stylesN.alignment = ali3
    del ali3

    for row in datalist:
        sheet1.write(row[0] + 5, 0, row[0], styles)
        sheet1.write(row[0] + 5, 1, row[1], styles)
        for ij in range(2, 47):
            sheet1.write(row[0] + 5, ij, row[ij] / 10000, style_num)
        for jj in range(47,67):
            sheet1.write(row[0] + 5, jj, row[jj], stylesN)

    # �����п�
    set_col_width(sheet1, col_index=0, col_width=4.71)
    for j in range(1, 47):
        set_col_width(sheet1, col_index=j, col_width=14.71)

    workbook.save(excel_path3)

    arcpy.AddMessage("ͳ�ƽ���ѵ����� " + excel_path3 + "          Excel��")


if __name__ == "__main__":
    in_pathG = arcpy.GetParameterAsText(0)
    out_pathG = arcpy.GetParameterAsText(1)
    table_nameG = arcpy.GetParameterAsText(2)
    whereCG = arcpy.GetParameterAsText(3)

    arcpy.AddMessage(whereCG)
    listtt123 = re.findall(r"[^\\/:*?\"<>|]", table_nameG)
    table_name_global = "".join(listtt123).strip()

    statisticsAreaQ3(in_pathG, out_pathG, whereCG, table_name_global)

    arcpy.AddMessage("in_path: " + in_pathG)
    arcpy.AddMessage("out_path: " + out_pathG)
    arcpy.AddMessage("name: " + table_nameG)


    # ls = [[1, u"��˷��", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    #                                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    #                                          0,0,0,0,0,0],[2, u"��˷��", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    #                                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    #                                          0,0,0,0,0,0],[3, u"��˷��", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    #                                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    #                                          0,0,0,0,0,0]]
    # table_path_e3 = u"D:\\pyCharmWorksp\\wewewe1221.xls"
    # tableToExcelQ(table_path_e3, ls, u"�˿ѵ������ͳ��")

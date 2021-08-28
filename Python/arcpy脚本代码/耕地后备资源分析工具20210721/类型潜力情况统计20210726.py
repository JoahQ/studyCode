# -*- coding: gbk -*-
import sys
import arcpy
import os
import string
import re
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
        arcpy.AddMessage("-"*25)
    if null_layer:
        arcpy.AddError("���ݿ⣺" + in_gdb + " Ϊ�ջ������𻵣��޷��򿪣�����")
        right_name = False
    return [right_name, in_fc_list]

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
    field_list = [{'name': 'cout', 'type': 'TEXT', 'alias': '���'},  #0
                  {'name': 'XZQ', 'type': 'TEXT', 'alias': '������'},  #0

                  {'name': 'A2', 'type': 'DOUBLE', 'alias': '�ܼ�'},  #1
                  {'name': 'B3', 'type': 'DOUBLE', 'alias': '�˸�ũ�õ�Ǳ��-С��'},  #2
                  {'name': 'C4', 'type': 'DOUBLE', 'alias': '�˸�ũ�õ�Ǳ��-���ָ̻�'},  #3
                  {'name': 'D5', 'type': 'DOUBLE', 'alias': '�˸�ũ�õ�Ǳ��-���ɻָ�'},  #4

                  {'name': 'E6', 'type': 'DOUBLE', 'alias': 'ũ�õ�δ��ע�ָ�����-С��'},  #5
                  {'name': 'F7', 'type': 'DOUBLE', 'alias': 'ũ�õ�δ��ע�ָ�����-Բ��'},  #6
                  {'name': 'G8', 'type': 'DOUBLE', 'alias': 'ũ�õ�δ��ע�ָ�����-�ֵ�'},  #7
                  {'name': 'H9', 'type': 'DOUBLE', 'alias': 'ũ�õ�δ��ע�ָ�����-�ݵ�'},  #8
                  {'name': 'I10', 'type': 'DOUBLE', 'alias': 'ũ�õ�δ��ע�ָ�����-����ˮ��'},  #9

                  {'name': 'J11', 'type': 'DOUBLE', 'alias': '�����õ�-С��'},  #10
                  {'name': 'K12', 'type': 'DOUBLE', 'alias': '�����õ�-��ҵ�õ�'},  #11
                  {'name': 'L13', 'type': 'DOUBLE', 'alias': '�����õ�-�ɿ��õ�'},  #12
                  {'name': 'M14', 'type': 'DOUBLE', 'alias': '�����õ�-ũ�彨���õ�'},  #13

                  {'name': 'N15', 'type': 'DOUBLE', 'alias': 'δ���õ�-С��'},  #14
                  {'name': 'O16', 'type': 'DOUBLE', 'alias': 'δ���õ�-�ݵ�'},  #15
                  {'name': 'P17', 'type': 'DOUBLE', 'alias': 'δ���õ�-��½̲Ϳ'},  #16
                  {'name': 'Q18', 'type': 'DOUBLE', 'alias': 'δ���õ�-���'},  #17
                  {'name': 'R19', 'type': 'DOUBLE', 'alias': 'δ���õ�-ɳ��'},  #18
                  {'name': 'BR20', 'type': 'DOUBLE', 'alias': 'δ���õ�-�غ�̲Ϳ'},  #19
                  {'name': 'CR21', 'type': 'DOUBLE', 'alias': 'δ���õ�-�μ��'},  #20

                  {'name': 'S22', 'type': 'DOUBLE', 'alias': '���ʸ���-С��'},  #21
                  {'name': 'T23', 'type': 'DOUBLE', 'alias': '���ʸ���-���ָ̻�'},  #22
                  {'name': 'U24', 'type': 'DOUBLE', 'alias': '���ʸ���-���ɻָ�'},  #23
                  {'name': 'V25', 'type': 'DOUBLE', 'alias': '���ʸ���-����-С��'},  #24
                  {'name': 'W26', 'type': 'DOUBLE', 'alias': '���ʸ���-����-ˮ����'},  #25
                  {'name': 'X27', 'type': 'DOUBLE', 'alias': '���ʸ���-����-����'},  #26
                 
                  {'name': 'Y28', 'type': 'DOUBLE', 'alias': '������ȡ-�ϼ�'},  #27
                  {'name': 'Z29', 'type': 'DOUBLE', 'alias': '������ȡ-�˸�ũ�õ�Ǳ������ͼ��'},  #28
                  {'name': 'AA30', 'type': 'DOUBLE', 'alias': '������ȡ-�˸�δ���õ�Ǳ������ͼ��'},  #29
                  {'name': 'AB31', 'type': 'DOUBLE', 'alias': '������ȡ-�����õظ���Ǳ������ͼ��'},  #30
                  {'name': 'AC32', 'type': 'DOUBLE', 'alias': '������ȡ-�������ʸ���Ǳ������ͼ��'},  #31
                  ]

    arcpy.AddMessage("�½� " + table_name + " ���...")
    arcpy.CreateTable_management(path, table_name)
    arcpy.AddMessage("  ����ֶ�...")
    arcpy.AddMessage("-" * 50)
    for field in field_list:
        # arcpy.AddMessage("    �ֶ����� " + field['name'] + " �ֶα����� " + field['alias'])
        arcpy.AddField_management(tb_path, field['name'], field['type'], "#", "#", "#", field['alias'])
        field_ls.append(field['name'])
    arcpy.AddMessage("-"*50)
    return [tb_path, field_ls]

def getNewFileNameQ(dirpath1, file_name_out):
    n = [1]
    def get_new_name(file_name_in):
        new_file_name = file_name_in
        if arcpy.Exists(os.path.join(dirpath1, file_name_in)):
            new_file_name = "%s_%s%s" % (os.path.splitext(file_name_in)[0], str(n[0]), os.path.splitext(file_name_in)[1])
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

    # ��gdb
    resultg_name = getNewFileNameQ(out_path, name + "_result.gdb")
    result_gdb = os.path.join(out_path, resultg_name)
    arcpy.AddMessage("�½� " + result_gdb + " ���ڱ�����...")
    arcpy.CreateFileGDB_management(out_path, resultg_name)

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

            row_values = [cout, xzqab(xzqcode[0]), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0]
        else:
            row_values = [cout,gdbName,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        try:
            for iin_fc_path in right_name_path[1]:
                fc = os.path.basename(iin_fc_path)
                arcpy.AddMessage("        " + fc)
                if "ũ" in fc or u"ũ" in fc:
                    out_featuren = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "N" +xzqcode[0]+xzqab(xzqcode[0])))
                    arcpy.Select_analysis(iin_fc_path, out_featuren, where_clause + u" like \'%��%\'")
                    nyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "nyd_table" + str(cout)))
                    arcpy.Statistics_analysis(out_featuren, nyd_tb1, [["Shape_Area", "SUM"]], ['DLBM','ZZSXMC'])
                    with arcpy.da.SearchCursor(nyd_tb1, ('DLBM','ZZSXMC', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "���ָ̻�" in str(row1[1]):
                                row_values[4] = row_values[4] + row1[2]
                            elif "���ɻָ�" in str(row1[1]):
                                row_values[5] = row_values[5] + row1[2]
                            else:
                                if "020" in str(row1[0]):
                                    row_values[7] = row_values[7] + row1[2]
                                if "030" in str(row1[0]):
                                    row_values[8] = row_values[8] + row1[2]
                                if "040" in str(row1[0]):
                                    row_values[9] = row_values[9] + row1[2]
                                if "1104" in str(row1[0]):
                                    row_values[10] = row_values[10] + row1[2]

                    if arcpy.Exists(out_featuren):
                        try:
                            arcpy.Delete_management(out_featuren)
                        except Exception as e:
                            arcpy.AddMessage(e.message)
                    if arcpy.Exists(nyd_tb1):
                        try:
                            arcpy.Delete_management(nyd_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

                elif "δ��" in fc or u"δ��" in fc:
                    out_featurew = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "W"+xzqcode[0]+xzqab(xzqcode[0])))
                    arcpy.Select_analysis(iin_fc_path, out_featurew, where_clause + u" like \'%��%\'")

                    wlyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "wlyd_table" + str(cout)))
                    arcpy.Statistics_analysis(out_featurew, wlyd_tb1, [["Shape_Area", "SUM"]], 'DLBM')
                    with arcpy.da.SearchCursor(wlyd_tb1, ('DLBM', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "040" in row1[0]:
                                row_values[16] = row_values[16] + row1[1]
                            if "1106" in row1[0]:
                                row_values[17] = row_values[17] + row1[1]
                            if "1206" in row1[0]:
                                row_values[18] = row_values[18] + row1[1]
                            if "1205" in row1[0]:
                                row_values[19] = row_values[19] + row1[1]
                            if "1105" in row1[0]:
                                row_values[20] = row_values[20] + row1[1]
                            if "1204" in row1[0]:
                                row_values[21] = row_values[21] + row1[1]

                    if arcpy.Exists(out_featurew):
                        try:
                            arcpy.Delete_management(out_featurew)
                        except Exception as e:
                            arcpy.AddMessage(e.message)
                    if arcpy.Exists(wlyd_tb1):
                        try:
                            arcpy.Delete_management(wlyd_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

                elif "����" in fc or u"����" in fc:
                    out_featureJ = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "J"+xzqcode[0]+xzqab(xzqcode[0])))
                    arcpy.Select_analysis(iin_fc_path, out_featureJ, where_clause + u" like \'%��%\'")

                    jsyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "jsyd_table" + str(cout)))
                    arcpy.Statistics_analysis(out_featureJ, jsyd_tb1, [["Shape_Area", "SUM"]], 'DLBM')
                    with arcpy.da.SearchCursor(jsyd_tb1, ('DLBM', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "0601" in row1[0]:
                                row_values[12] = row_values[12] + row1[1]
                            if "0602" in row1[0]:
                                row_values[13] = row_values[13] + row1[1]
                            if "0702" in row1[0]:
                                row_values[14] = row_values[14] + row1[1]

                    if arcpy.Exists(out_featureJ):
                        try:
                            arcpy.Delete_management(out_featureJ)
                        except Exception as e:
                            arcpy.AddMessage(e.message)
                    if arcpy.Exists(jsyd_tb1):
                        try:
                            arcpy.Delete_management(jsyd_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

                elif "���ʸ���" in fc or u"���ʸ���" in fc:
                    out_featureT = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "T"+xzqcode[0]+xzqab(xzqcode[0])))
                    arcpy.Select_analysis(iin_fc_path, out_featureT, where_clause + u" like \'%��%\'")

                    tzgz_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "tzgz_table" + str(cout)))
                    arcpy.Statistics_analysis(out_featureT, tzgz_tb1, [["Shape_Area", "SUM"]], ['DLBM','ZZSXMC'])
                    with arcpy.da.SearchCursor(tzgz_tb1, ('DLBM','ZZSXMC', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "���ָ̻�" in str(row1[1]):
                                row_values[23] = row_values[23] + row1[2]
                            if "���ɻָ�" in str(row1[1]):
                                row_values[24] = row_values[24] + row1[2]

                            if "0102" in str(row1[0]):
                                row_values[26] = row_values[26] + row1[2]
                            if "0103" in str(row1[0]):
                                row_values[27] = row_values[27] + row1[2]

                    if arcpy.Exists(out_featureT):
                        try:
                            arcpy.Delete_management(out_featureT)
                        except Exception as e:
                            arcpy.AddMessage(e.message)
                    if arcpy.Exists(tzgz_tb1):
                        try:
                            arcpy.Delete_management(tzgz_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

                elif "������ȡ" in fc or u"������ȡ" in fc:
                    zztq_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "zztq_table" + str(cout)))
                    arcpy.Statistics_analysis(iin_fc_path, zztq_tb1, [["Shape_Area", "SUM"]], 'GDHBZY')
                    with arcpy.da.SearchCursor(zztq_tb1, ('GDHBZY', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "ũ�õ�" in str(row1[0]):
                                row_values[29] = row_values[29] + row1[1]
                            if "δ���õ�" in str(row1[0]):
                                row_values[30] = row_values[30] + row1[1]
                            if "�����õ�" in str(row1[0]):
                                row_values[31] = row_values[31] + row1[1]
                            if "���ʸ���" in str(row1[0]):
                                row_values[32] = row_values[32] + row1[1]

                    if arcpy.Exists(zztq_tb1):
                        try:
                            arcpy.Delete_management(zztq_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

            row_values[6] = row_values[7] + row_values[8] + row_values[9] + row_values[10]
            row_values[3] = row_values[4] + row_values[5] + row_values[6]
            row_values[11] = row_values[12] + row_values[13] + row_values[14]
            row_values[15] = row_values[16] + row_values[17] + row_values[18] + row_values[19] + row_values[20] + row_values[21]
            row_values[22] = row_values[23] + row_values[24]
            row_values[25] = row_values[26] + row_values[27]
            row_values[28] = row_values[29] + row_values[30] + row_values[31] + row_values[32]

            row_values[2] = row_values[3] + row_values[11] + row_values[15] + row_values[22] + row_values[25] + row_values[28]


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
    table_path_e3 = os.path.join(out_path,getNewFileNameQ(out_path, name + ".xls"))
    tableToExcelQ(table_path_e3, resullist, "�������ͳ�Ʊ�")
    arcpy.AddMessage('+'*60)
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
        bt = u"�������غ���Դ��Ǳ������ͳ��"
        worksheets.write_merge(0, 0, 0, 32, bt, style3)
        worksheets.write_merge(1, 1, 0, 32, u'���������', style2)

        worksheets.write_merge(2, 4, 0, 0, u'���', style1)
        worksheets.write_merge(2, 4, 1, 1, u'����������', style1)
        worksheets.write_merge(2, 4, 2, 2, u'�ܼ�', style1)
        worksheets.write_merge(2, 2, 3, 10, u'�˸�ũ�õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(3, 4, 3, 3, u'С��', style1)
        worksheets.write_merge(3, 4, 4, 4, u'���ָ̻�', style1)
        worksheets.write_merge(3, 4, 5, 5, u'���ɻָ�', style1)
        worksheets.write_merge(3, 3, 6, 10, u'δ��ע�ָ�����', style1)

        worksheets.write_merge(2, 3, 11, 14, u'�����õظ���Ǳ������ͼ��', style1)
        worksheets.write_merge(2, 3, 15, 21, u'�˸�δ���õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(2, 2, 22, 27, u'�������ʸ���Ǳ������ͼ��', style1)
        worksheets.write_merge(2, 2, 28, 32, u'������ȡǱ��', style1)

        worksheets.write_merge(3, 4, 22, 22, u'С��', style1)
        worksheets.write_merge(3, 4, 23, 23, u'���ָ̻�', style1)
        worksheets.write_merge(3, 4, 24, 24, u'���ɻָ�', style1)
        worksheets.write_merge(3, 3, 25, 27, u'����', style1)
        worksheets.write(4, 25, u'С��', style1)
        worksheets.write(4, 26, u'ˮ����', style1)
        worksheets.write(4, 27, u'����', style1)

        worksheets.write_merge(3, 4, 28, 28, u'�ϼ�', style1)
        worksheets.write_merge(3, 4, 29, 29, u'�˸�ũ�õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(3, 4, 30, 30, u'�˸�δ���õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(3, 4, 31, 31, u'�����õظ���Ǳ������ͼ��', style1)
        worksheets.write_merge(3, 4, 32, 32, u'�������ʸ���Ǳ������ͼ��', style1)

        tlist = ['С��', '԰��', '�ֵ�', '�ݵ�', '����ˮ��', 'С��', '��ҵ�õ�', '�ɿ��õ�',
                 'ũ�彨���õ�', 'С��', '�ݵ�', '��½̲Ϳ','���','ɳ��','�غ�̲Ϳ','�μ��']
        for ii in range(6,22):
            worksheets.write(4, ii, tlist[ii-6], style1)
        del ii
        # �����и�
        set_row_height(worksheets, row_index=0, row_height=28)
        set_row_height(worksheets, row_index=1, row_height=22)
        set_row_height(worksheets, row_index=2, row_height=20)
        set_row_height(worksheets, row_index=3, row_height=20)
        set_row_height(worksheets, row_index=4, row_height=50)

        return worksheets

    sheet1 = add_new_sheet(sheets_name3)
    styles = set_style(u'����', 11, True, True)
    style_num = set_style(u'����', 11, True, True)
    ali3 = xlwt.Alignment()
    #0x02 ��˶��룬0x03 �Ҷ˶���
    ali3.horz = 0x03
    ali3.vert = 0x01
    style_num.alignment = ali3
    num_format_str = '0.0000'
    style_num.num_format_str = num_format_str
    del ali3

    for row in datalist:
        sheet1.write(row[0] + 4, 0, row[0], styles)
        sheet1.write(row[0] + 4, 1, row[1], styles)
        for ij in range(2,33):
            sheet1.write(row[0] + 4, ij, row[ij] / 10000, style_num)

    
    # �����п�
    set_col_width(sheet1, col_index=0, col_width=4.71)
    for j in range(1,33):
        set_col_width(sheet1, col_index=j, col_width=14.71)

    workbook.save(excel_path3)

    arcpy.AddMessage("ͳ�ƽ���ѵ�����  " + excel_path3 + "      Excel��")

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

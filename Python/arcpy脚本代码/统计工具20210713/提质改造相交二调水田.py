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

def createTableQ(path1, name1):
    """
    �½����arcgis���Ա���ָ���̶��ֶ�
    :param path1:
    :param name1:
    :return:
    """
    table_name = name1.strip(string.digits)
    if table_name == '':
        table_name = "Table" + name1
    tb_path = os.path.join(path1, table_name)
    field_ls = []
    # ���ֵ������ֶ����ԣ����б��������ֶ�
    field_list = [{'name': 'cout', 'type': 'TEXT', 'alias': '���'},  #0
                  {'name': 'XZQ', 'type': 'TEXT', 'alias': '������'},

                  {'name': 'F2', 'type': 'DOUBLE', 'alias': '��-С��'},  #2
                  {'name': 'G3', 'type': 'DOUBLE', 'alias': '���ɻָ�-0201'},  #3
                  {'name': 'H4', 'type': 'DOUBLE', 'alias': '���ɻָ�-0201K'},  #4
                  {'name': 'I5', 'type': 'DOUBLE', 'alias': '���ɻָ�-0202'},  #5
                  {'name': 'J6', 'type': 'DOUBLE', 'alias': '���ɻָ�-0202K'},  #6
                  {'name': 'K7', 'type': 'DOUBLE', 'alias': '���ɻָ�-0203'},  #7
                  {'name': 'L8', 'type': 'DOUBLE', 'alias': '���ɻָ�-0203K'},  #8
                  {'name': 'M9', 'type': 'DOUBLE', 'alias': '���ɻָ�-0204'},  #9
                  {'name': 'N10', 'type': 'DOUBLE', 'alias': '���ɻָ�-0204K'},  #10
                  {'name': 'O11', 'type': 'DOUBLE', 'alias': '���ɻָ�-0301'},  #11
                  {'name': 'A12', 'type': 'DOUBLE', 'alias': '���ɻָ�-0301K'},  #12
                  {'name': 'Q13', 'type': 'DOUBLE', 'alias': '���ɻָ�-0302'},  #13
                  {'name': 'R14', 'type': 'DOUBLE', 'alias': '���ɻָ�-0302K'},  #14
                  {'name': 'S15', 'type': 'DOUBLE', 'alias': '���ɻָ�-0305'},  #15
                  {'name': 'T16', 'type': 'DOUBLE', 'alias': '���ɻָ�-0307'},  #16
                  {'name': 'U17', 'type': 'DOUBLE', 'alias': '���ɻָ�-0307K'},  #17
                  {'name': 'V18', 'type': 'DOUBLE', 'alias': '���ɻָ�-0403K'},  #18
                  {'name': 'W19', 'type': 'DOUBLE', 'alias': '���ɻָ�-0404'},  # 19
                  {'name': 'X20', 'type': 'DOUBLE', 'alias': '���ɻָ�-1104'},  # 20
                  {'name': 'Y21', 'type': 'DOUBLE', 'alias': '���ɻָ�-1104K'},  # 21
                  {'name': 'Z22', 'type': 'DOUBLE', 'alias': '���ɻָ�-1104A'},  # 22

                  {'name': 'F23', 'type': 'DOUBLE', 'alias': '��-С��'},  # 2
                  {'name': 'G24', 'type': 'DOUBLE', 'alias': '���ɻָ�-0201'},  # 3
                  {'name': 'H25', 'type': 'DOUBLE', 'alias': '���ɻָ�-0201K'},  # 4
                  {'name': 'I26', 'type': 'DOUBLE', 'alias': '���ɻָ�-0202'},  # 5
                  {'name': 'J27', 'type': 'DOUBLE', 'alias': '���ɻָ�-0202K'},  # 6
                  {'name': 'K28', 'type': 'DOUBLE', 'alias': '���ɻָ�-0203'},  # 7
                  {'name': 'L29', 'type': 'DOUBLE', 'alias': '���ɻָ�-0203K'},  # 8
                  {'name': 'M30', 'type': 'DOUBLE', 'alias': '���ɻָ�-0204'},  # 9
                  {'name': 'N31', 'type': 'DOUBLE', 'alias': '���ɻָ�-0204K'},  # 10
                  {'name': 'O32', 'type': 'DOUBLE', 'alias': '���ɻָ�-0301'},  # 11
                  {'name': 'P33', 'type': 'DOUBLE', 'alias': '���ɻָ�-0301K'},  # 12
                  {'name': 'Q34', 'type': 'DOUBLE', 'alias': '���ɻָ�-0302'},  # 13
                  {'name': 'R35', 'type': 'DOUBLE', 'alias': '���ɻָ�-0302K'},  # 14
                  {'name': 'S36', 'type': 'DOUBLE', 'alias': '���ɻָ�-0305'},  # 15
                  {'name': 'T37', 'type': 'DOUBLE', 'alias': '���ɻָ�-0307'},  # 16
                  {'name': 'U38', 'type': 'DOUBLE', 'alias': '���ɻָ�-0307K'},  # 17
                  {'name': 'V39', 'type': 'DOUBLE', 'alias': '���ɻָ�-0403K'},  # 18
                  {'name': 'W40', 'type': 'DOUBLE', 'alias': '���ɻָ�-0404'},  # 19
                  {'name': 'X41', 'type': 'DOUBLE', 'alias': '���ɻָ�-1104'},  # 20
                  {'name': 'Y42', 'type': 'DOUBLE', 'alias': '���ɻָ�-1104K'},  # 21
                  {'name': 'Z43', 'type': 'DOUBLE', 'alias': '���ɻָ�-1104A'},  # 22

                  ]

    arcpy.AddMessage("�½� " + table_name + " ���...")
    arcpy.CreateTable_management(path1, table_name)
    arcpy.AddMessage("  ����ֶ�...")

    for field in field_list:
        arcpy.AddField_management(tb_path, field['name'], field['type'], "#", "#", "#", field['alias'])
        field_ls.append(field['name'])

    return [tb_path, field_ls]

def xiaongjiao(in_path,spj_path, out_path, name):
    # ��gdb
    nametj = getNewFileNameQ(out_path, "result.gdb")
    gdbtj = os.path.join(out_path, nametj)
    arcpy.AddMessage("�½� " + gdbtj + " ���ڱ�����...")
    arcpy.CreateFileGDB_management(out_path, nametj)

    # ����
    arcpy.AddMessage("-"*20 + "�½����Ա�" + "-"*20)
    tb_paths = createTableQ(gdbtj, getNewFileNameQ(gdbtj, name))
    tb_path = tb_paths[0]
    field_ls = tb_paths[1]
    tb_name = os.path.basename(tb_path)

    in_cursor = arcpy.da.InsertCursor(tb_path, field_ls)
    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")

    foder_name = getNewFileNameQ(out_path,"�����ˮ���ཻ��")
    arcpy.CreateFolder_management(out_path, foder_name)
    foder_path = os.path.join(out_path,foder_name)

    row_values = []
    cout = 0
    fail = 0
    fail_list = []
    for workspace in workspaces:
        success = True
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        try:
            # ��ÿ��gdb��Ϊ������
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()
            temp_name1 = getNewFileNameQ(foder_path, os.path.basename(workspace))
            result_gdb = os.path.join(foder_path, temp_name1)
            arcpy.AddMessage("�½� " + result_gdb + " ...")
            arcpy.CreateFileGDB_management(foder_path, temp_name1)
            gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])
            xzqcode = re.findall(r"\d+", gdbName)
            if len(xzqcode) > 0 and not xzqab(xzqcode[0]).isdigit():
                row_values = [cout, xzqab(xzqcode[0])]
            else:
                row_values = [cout, gdbName]

            i = 2
            while i < len(field_ls):
                row_values.append(0)
                i += 1
            # arcpy.AddMessage(row_values)
            # arcpy.AddMessage(len(row_values))
            for ifc in fc_list:
                if "���ʸ���" in ifc or u"���ʸ���" in ifc:
                    infc_path = os.path.join(workspace, ifc)
                    erase1_path = os.path.join(result_gdb, ifc)
                    # arcpy.Erase_analysis(infc_path, tdzz_fc_pathp, erase1_path, ".001 Meters")
                    arcpy.AddMessage(infc_path + "��" + spj_path + " �ཻ...")
                    arcpy.Intersect_analysis([infc_path, spj_path], erase1_path)

                    arcpy.AddMessage(infc_path + " ͳ��...")
                    tzgz_tb1 = os.path.join(gdbtj, "table" + gdbName)
                    arcpy.Statistics_analysis(erase1_path, tzgz_tb1, [["Shape_Area", "SUM"]], ['DLBM', 'ZZSXMC','PJJG'])
                    with arcpy.da.SearchCursor(tzgz_tb1, ('DLBM','ZZSXMC','PJJG','SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "��" in str(row1[2]):
                                if "���ɻָ�" in str(row1[1]):
                                    row_values[2] += row1[3]
                                    if "0201" in str(row1[0]):
                                        row_values[3] += row1[3]
                                    if "0201K" in str(row1[0]):
                                        row_values[4] += row1[3]
                                    if "0202" in str(row1[0]):
                                        row_values[5] += row1[3]
                                    if "0202K" in str(row1[0]):
                                        row_values[6] += row1[3]
                                    if "0203" in str(row1[0]):
                                        row_values[7] += row1[3]
                                    if "0203K" in str(row1[0]):
                                        row_values[8] += row1[3]
                                    if "0204" in str(row1[0]):
                                        row_values[9] += row1[3]
                                    if "0204K" in str(row1[0]):
                                        row_values[10] += row1[3]
                                    if "0301" in str(row1[0]):
                                        row_values[11] += row1[3]
                                    if "0301K" in str(row1[0]):
                                        row_values[12] += row1[3]
                                    if "0302" in str(row1[0]):
                                        row_values[13] += row1[3]
                                    if "0302K" in str(row1[0]):
                                        row_values[14] += row1[3]
                                    if "0305" in str(row1[0]):
                                        row_values[15] += row1[3]
                                    if "0307" in str(row1[0]):
                                        row_values[16] += row1[3]
                                    if "0307K" in str(row1[0]):
                                        row_values[17] += row1[3]
                                    if "0403K" in str(row1[0]):
                                        row_values[18] += row1[3]
                                    if "0404" in str(row1[0]):
                                        row_values[19] += row1[3]
                                    if "1104" in str(row1[0]):
                                        row_values[20] += row1[3]
                                    if "1104K" in str(row1[0]):
                                        row_values[21] += row1[3]
                                    if "1104A" in str(row1[0]):
                                        row_values[22] += row1[3]

                            if "��" in str(row1[2]):
                                if "���ɻָ�" in str(row1[1]):
                                    row_values[23] += row1[3]
                                    if "0201" in str(row1[0]):
                                        row_values[24] += row1[3]
                                    if "0201K" in str(row1[0]):
                                        row_values[25] += row1[3]
                                    if "0202" in str(row1[0]):
                                        row_values[26] += row1[3]
                                    if "0202K" in str(row1[0]):
                                        row_values[27] += row1[3]
                                    if "0203" in str(row1[0]):
                                        row_values[28] += row1[3]
                                    if "0203K" in str(row1[0]):
                                        row_values[29] += row1[3]
                                    if "0204" in str(row1[0]):
                                        row_values[30] += row1[3]
                                    if "0204K" in str(row1[0]):
                                        row_values[31] += row1[3]
                                    if "0301" in str(row1[0]):
                                        row_values[32] += row1[3]
                                    if "0301K" in str(row1[0]):
                                        row_values[33] += row1[3]
                                    if "0302" in str(row1[0]):
                                        row_values[34] += row1[3]
                                    if "0302K" in str(row1[0]):
                                        row_values[35] += row1[3]
                                    if "0305" in str(row1[0]):
                                        row_values[36] += row1[3]
                                    if "0307" in str(row1[0]):
                                        row_values[37] += row1[3]
                                    if "0307K" in str(row1[0]):
                                        row_values[38] += row1[3]
                                    if "0403K" in str(row1[0]):
                                        row_values[39] += row1[3]
                                    if "0404" in str(row1[0]):
                                        row_values[40] += row1[3]
                                    if "1104" in str(row1[0]):
                                        row_values[41] += row1[3]
                                    if "1104K" in str(row1[0]):
                                        row_values[42] += row1[3]
                                    if "1104A" in str(row1[0]):
                                        row_values[43] += row1[3]

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("     " + os.path.basename(workspace) + " ʧ�ܣ�")
            fail += 1
            success = False
        if success:
            arcpy.AddMessage("    �� " + tb_name + " �����¼...")
            try:
                in_cursor.insertRow(tuple(row_values))
            except Exception as e:
                arcpy.AddError(e.message)
                arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
                fail += 1

        arcpy.AddMessage("-"*50)

    arcpy.AddMessage('+'*60)

    del in_cursor
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
    tdzz_pathG = arcpy.GetParameterAsText(1)
    out_pathG = arcpy.GetParameterAsText(2)
    out_nameG = arcpy.GetParameterAsText(3)

    xiaongjiao(in_pathG,tdzz_pathG,out_pathG, out_nameG)

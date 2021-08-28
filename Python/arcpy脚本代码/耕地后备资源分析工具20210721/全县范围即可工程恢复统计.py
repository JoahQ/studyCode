# -*- coding: gbk -*-
import sys
import arcpy
import os
import string
import re

reload(sys)
sys.setdefaultencoding("utf-8")

STATISTICS_FIELD = "TBMJ"
SEARCH_FIELD = "SUM_TBMJ"
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

def createTableQ(path1, name1):
    """
    �½����arcgis���Ա���ָ���̶��ֶ�
    :param path1:
    :param name1:
    :return:
    """
    asa123 = re.findall(r"[^()\[\]{},.*/|\\:;?\'\"<>%!@#$&\^]", name1)
    name11 = "".join(asa123)
    table_name = name11.lstrip(string.digits)
    if table_name == '':
        table_name = "Table" + name1
    tb_path = os.path.join(path1, table_name)
    field_ls = []
    # ���ֵ������ֶ����ԣ����б��������ֶ�
    field_list = [{'name': 'name', 'type': 'TEXT', 'alias': 'ʸ����������'},  #0
                  {'name': 'E', 'type': 'DOUBLE', 'alias': '�أ������ϼ�'},  #1
                  {'name': 'F', 'type': 'DOUBLE', 'alias': '���ɻָ�-С��'},  #2
                  {'name': 'G', 'type': 'DOUBLE', 'alias': '���ɻָ�-0201'},  #3
                  {'name': 'H', 'type': 'DOUBLE', 'alias': '���ɻָ�-0201K'},  #4
                  {'name': 'I', 'type': 'DOUBLE', 'alias': '���ɻָ�-0202'},  #5
                  {'name': 'J', 'type': 'DOUBLE', 'alias': '���ɻָ�-0202K'},  #6
                  {'name': 'K', 'type': 'DOUBLE', 'alias': '���ɻָ�-0203'},  #7
                  {'name': 'L', 'type': 'DOUBLE', 'alias': '���ɻָ�-0203K'},  #8
                  {'name': 'M', 'type': 'DOUBLE', 'alias': '���ɻָ�-0204'},  #9
                  {'name': 'N', 'type': 'DOUBLE', 'alias': '���ɻָ�-0204K'},  #10
                  {'name': 'O', 'type': 'DOUBLE', 'alias': '���ɻָ�-0301'},  #11
                  {'name': 'P', 'type': 'DOUBLE', 'alias': '���ɻָ�-0301K'},  #12
                  {'name': 'Q', 'type': 'DOUBLE', 'alias': '���ɻָ�-0302'},  #13
                  {'name': 'R', 'type': 'DOUBLE', 'alias': '���ɻָ�-0302K'},  #14
                  {'name': 'S', 'type': 'DOUBLE', 'alias': '���ɻָ�-0305'},  #15
                  {'name': 'T', 'type': 'DOUBLE', 'alias': '���ɻָ�-0307'},  #16
                  {'name': 'U', 'type': 'DOUBLE', 'alias': '���ɻָ�-0307K'},  #17
                  {'name': 'V', 'type': 'DOUBLE', 'alias': '���ɻָ�-0403K'},  #18
                  {'name': 'W', 'type': 'DOUBLE', 'alias': '���ɻָ�-0404'},  # 19
                  {'name': 'X', 'type': 'DOUBLE', 'alias': '���ɻָ�-1104'},  # 20
                  {'name': 'Y', 'type': 'DOUBLE', 'alias': '���ɻָ�-1104K'},  # 21
                  {'name': 'Z', 'type': 'DOUBLE', 'alias': '���ɻָ�-1104A'},  # 22

                  {'name': 'AA', 'type': 'DOUBLE', 'alias': '���ָ̻�-С��'},  # 23
                  {'name': 'AB', 'type': 'DOUBLE', 'alias': '���ָ̻�-0201'},  # 24
                  {'name': 'AC', 'type': 'DOUBLE', 'alias': '���ָ̻�-0201K'},  # 25
                  {'name': 'AD', 'type': 'DOUBLE', 'alias': '���ָ̻�-0202'},  # 26
                  {'name': 'AE', 'type': 'DOUBLE', 'alias': '���ָ̻�-0202K'},  # 27
                  {'name': 'AF', 'type': 'DOUBLE', 'alias': '���ָ̻�-0203'},  # 28
                  {'name': 'AG', 'type': 'DOUBLE', 'alias': '���ָ̻�-0203K'},  # 29
                  {'name': 'AH', 'type': 'DOUBLE', 'alias': '���ָ̻�-0204'},  # 30
                  {'name': 'AI', 'type': 'DOUBLE', 'alias': '���ָ̻�-0204K'},  # 31
                  {'name': 'AJ', 'type': 'DOUBLE', 'alias': '���ָ̻�-0301'},  # 32
                  {'name': 'AK', 'type': 'DOUBLE', 'alias': '���ָ̻�-0301K'},  # 33
                  {'name': 'AL', 'type': 'DOUBLE', 'alias': '���ָ̻�-0302'},  # 34
                  {'name': 'AM', 'type': 'DOUBLE', 'alias': '���ָ̻�-0302K'},  # 35
                  {'name': 'AN', 'type': 'DOUBLE', 'alias': '���ָ̻�-0305'},  # 36
                  {'name': 'AO', 'type': 'DOUBLE', 'alias': '���ָ̻�-0307'},  # 37
                  {'name': 'AP', 'type': 'DOUBLE', 'alias': '���ָ̻�-0307K'},  # 38
                  {'name': 'AQ', 'type': 'DOUBLE', 'alias': '���ָ̻�-0403K'},  # 39
                  {'name': 'AR', 'type': 'DOUBLE', 'alias': '���ָ̻�-0404'},  # 40
                  {'name': 'AS', 'type': 'DOUBLE', 'alias': '���ָ̻�-1104'},  # 41
                  {'name': 'AT', 'type': 'DOUBLE', 'alias': '���ָ̻�-1104K'}, # 42
                  {'name': 'AU', 'type': 'DOUBLE', 'alias': '���ָ̻�-1104A'}  # 43
                  ]

    arcpy.AddMessage("�½� " + table_name + " ���...")
    arcpy.CreateTable_management(path1, table_name)
    arcpy.AddMessage("  ����ֶ�...")

    for field in field_list:
        arcpy.AddField_management(tb_path, field['name'], field['type'], "#", "#", "#", field['alias'])
        field_ls.append(field['name'])

    return [tb_path, field_ls]

def findDLTBAndStatisticsAreaQ(in_path11, out_path11, name11):
    """
    ����ͬһ·����
    :param in_path11:
    :param out_path11:
    :param name11:
    :return:
    """
    # ��gdb
    g_name = getNewFileNameQ(out_path11, name11 + ".gdb")
    result_gdb = os.path.join(out_path11, g_name)
    arcpy.AddMessage("�½� " + result_gdb + " ���ڱ�����...")
    arcpy.CreateFileGDB_management(out_path11, g_name)

    temp_name = getNewFileNameQ(out_path11, "temp.gdb")
    temp_gdb = os.path.join(out_path11, temp_name)
    arcpy.AddMessage("�½� " + temp_gdb + " ���ڷŹ�������...")
    arcpy.CreateFileGDB_management(out_path11, temp_name)
    # ����
    arcpy.AddMessage("-"*20 + "�½����Ա�" + "-"*20)

    tb_paths = createTableQ(result_gdb, getNewFileNameQ(result_gdb, name11))
    tb_path = tb_paths[0]
    field_ls = tb_paths[1]
    tb_name = os.path.basename(tb_path)
    in_cursor = arcpy.da.InsertCursor(tb_path, field_ls)

    arcpy.env.workspace = in_path11
    workspaces = arcpy.ListWorkspaces("*", "ALL")
    cout = 0
    fail = 0
    susss = True
    fail_list = []
    arcpy.AddMessage("-" * 50)
    for workspace in workspaces:
        try:
            arcpy.env.workspace = workspace
            DLTB_PATH_1 = os.path.join(workspace, "DLTB")
            gdb_name = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])
            asa = re.findall(r"[^()\[\]{},.*/|\\:;?\'\"<>%!@#$&\^]", gdb_name)
            jkgc_out_name = getNewFileNameQ(temp_gdb, "DLTB" + "".join(asa))
            jkgc_out_path = os.path.join(temp_gdb, jkgc_out_name)
            jkgc_table_path = os.path.join(temp_gdb, getNewFileNameQ(temp_gdb, "table" + "".join(asa)))
            row_values = [gdb_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            cout += 1
            find_DLTB = False
            arcpy.AddMessage("(" + str(cout) + ")" + os.path.basename(workspace))
            if arcpy.Exists(DLTB_PATH_1):
                arcpy.AddMessage("    ������ע ���ָ̻� �� ���ɻָ� ��ͼ��...")
                arcpy.FeatureClassToFeatureClass_conversion(DLTB_PATH_1, temp_gdb, jkgc_out_name,
                                                            'ZZSXDM in (\'GCHF\' ,\'JKHF\')')
                find_DLTB = True
            else:
                dataset_ls = arcpy.ListDatasets()
                for dataset in dataset_ls:
                    DLTB_PATH = os.path.join(os.path.join(workspace, dataset), "DLTB")
                    if arcpy.Exists(DLTB_PATH):
                        arcpy.AddMessage("    ������ע ���ָ̻� �� ���ɻָ� ��ͼ��...")
                        arcpy.FeatureClassToFeatureClass_conversion(DLTB_PATH, temp_gdb, jkgc_out_name,
                                                                    'ZZSXDM in (\'GCHF\' ,\'JKHF\')')
                        find_DLTB = True
                        break
            if not find_DLTB:
                arcpy.AddError("    " + os.path.basename(workspace) + " ���޷��ҵ� DLTBͼ�㣡")

            if arcpy.Exists(jkgc_out_path):
                arcpy.AddMessage("    ͳ�� " + jkgc_out_path + " ...")
                arcpy.Statistics_analysis(jkgc_out_path, jkgc_table_path, [["Shape_Area", "SUM"]], ['ZZSXDM', 'DLBM'])
                with arcpy.da.SearchCursor(jkgc_table_path, ('ZZSXDM', 'DLBM', "SUM_Shape_Area")) as cursor:
                    for row in cursor:
                        if row[0] == 'JKHF' and row[1] == '0201':
                            row_values[3] = row[2] + row_values[3]
                        if row[0] == 'JKHF' and row[1] == '0201K':
                            row_values[4] = row[2] + row_values[4]

                        if row[0] == 'JKHF' and row[1] == '0202':
                            row_values[5] = row[2] + row_values[5]
                        if row[0] == 'JKHF' and row[1] == '0202K':
                            row_values[6] = row[2] + row_values[6]

                        if row[0] == 'JKHF' and row[1] == '0203':
                            row_values[7] = row[2] + row_values[7]
                        if row[0] == 'JKHF' and row[1] == '0203K':
                            row_values[8] = row[2] + row_values[8]

                        if row[0] == 'JKHF' and row[1] == '0204':
                            row_values[9] = row[2] + row_values[9]
                        if row[0] == 'JKHF' and row[1] == '0204K':
                            row_values[10] = row[2] + row_values[10]

                        if row[0] == 'JKHF' and row[1] == '0301':
                            row_values[11] = row[2] + row_values[11]
                        if row[0] == 'JKHF' and row[1] == '0301K':
                            row_values[12] = row[2] + row_values[12]

                        if row[0] == 'JKHF' and row[1] == '0302':
                            row_values[13] = row[2] + row_values[13]
                        if row[0] == 'JKHF' and row[1] == '0302K':
                            row_values[14] = row[2] + row_values[14]

                        if row[0] == 'JKHF' and row[1] == '0305':
                            row_values[15] = row[2] + row_values[15]

                        if row[0] == 'JKHF' and row[1] == '0307':
                            row_values[16] = row[2] + row_values[16]
                        if row[0] == 'JKHF' and row[1] == '0307K':
                            row_values[17] = row[2] + row_values[17]

                        if row[0] == 'JKHF' and row[1] == '0403K':
                            row_values[18] = row[2] + row_values[18]

                        if row[0] == 'JKHF' and row[1] == '0404':
                            row_values[19] = row[2] + row_values[19]

                        if row[0] == 'JKHF' and row[1] == '1104':
                            row_values[20] = row[2] + row_values[20]
                        if row[0] == 'JKHF' and row[1] == '1104K':
                            row_values[21] = row[2] + row_values[21]
                        if row[0] == 'JKHF' and row[1] == '1104A':
                            row_values[22] = row[2] + row_values[22]

                        ############
                        if row[0] == 'GCHF' and row[1] == '0201':
                            row_values[24] = row[2] + row_values[24]
                        if row[0] == 'GCHF' and row[1] == '0201K':
                            row_values[25] = row[2] + row_values[25]

                        if row[0] == 'GCHF' and row[1] == '0202':
                            row_values[26] = row[2] + row_values[26]
                        if row[0] == 'GCHF' and (row[1] == '0202K'):
                            row_values[27] = row[2] + row_values[27]

                        if row[0] == 'GCHF' and row[1] == '0203':
                            row_values[28] = row[2] + row_values[28]
                        if row[0] == 'GCHF' and row[1] == '0203K':
                            row_values[29] = row[2] + row_values[29]

                        if row[0] == 'GCHF' and row[1] == '0204':
                            row_values[30] = row[2] + row_values[30]
                        if row[0] == 'GCHF' and row[1] == '0204K':
                            row_values[31] = row[2] + row_values[31]

                        if row[0] == 'GCHF' and row[1] == '0301':
                            row_values[32] = row[2] + row_values[32]
                        if row[0] == 'GCHF' and row[1] == '0301K':
                            row_values[33] = row[2] + row_values[33]

                        if row[0] == 'GCHF' and row[1] == '0302':
                            row_values[34] = row[2] + row_values[34]
                        if row[0] == 'GCHF' and row[1] == '0302K':
                            row_values[35] = row[2] + row_values[35]

                        if row[0] == 'GCHF' and row[1] == '0305':
                            row_values[36] = row[2] + row_values[36]

                        if row[0] == 'GCHF' and row[1] == '0307':
                            row_values[37] = row[2] + row_values[37]
                        if row[0] == 'GCHF' and row[1] == '0307K':
                            row_values[38] = row[2] + row_values[38]

                        if row[0] == 'GCHF' and row[1] == '0403K':
                            row_values[39] = row[2] + row_values[39]

                        if row[0] == 'GCHF' and row[1] == '0404':
                            row_values[40] = row[2] + row_values[40]

                        if row[0] == 'GCHF' and row[1] == '1104':
                            row_values[41] = row[2] + row_values[41]
                        if row[0] == 'GCHF' and row[1] == '1104K':
                            row_values[42] = row[2] + row_values[42]
                        if row[0] == 'GCHF' and row[1] == '1104A':
                            row_values[43] = row[2] + row_values[43]
            else:
                arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
                fail += 1
                fail_list.append(workspace)
                continue

            row_values[2] = row_values[3] + row_values[4] + row_values[5] + row_values[6] + row_values[7] + \
                             row_values[8] + row_values[9] + row_values[10] + row_values[11] + row_values[12] + \
                             row_values[13] + row_values[14] + row_values[15] + row_values[16] + row_values[17] + \
                             row_values[18] + row_values[19] + row_values[20] + row_values[21] + row_values[22]

            row_values[23] = row_values[24] + row_values[25] + row_values[26] + row_values[27] + row_values[28] + \
                             row_values[29] + row_values[30] + row_values[31] + row_values[32] + row_values[33] + \
                             row_values[34] + row_values[35] + row_values[36] + row_values[37] + row_values[38] + \
                             row_values[39] + row_values[40] + row_values[41] + row_values[42] + row_values[43]

            row_values[1] = row_values[2] + row_values[23]
        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
            fail += 1
            susss = False

        if susss:
            arcpy.AddMessage("    �� " + tb_name + " �����¼...")
            try:
                in_cursor.insertRow(tuple(row_values))
            except Exception as e:
                arcpy.AddError(e.message)
                arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
                fail += 1

        arcpy.AddMessage("-"*50)

    del in_cursor
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
    in_path_global = arcpy.GetParameterAsText(0)
    out_path_global = arcpy.GetParameterAsText(1)
    table_name_global = arcpy.GetParameter(2)
    all_global = arcpy.GetParameter(3)

    arcpy.env.workspace = in_path_global
    folder_list = arcpy.ListWorkspaces("*", "Folder")
    if all_global:
        for folder in folder_list:
            arcpy.AddMessage(folder)
            folder_name = os.path.basename(folder)
            arcpy.AddMessage(folder_name)
            findDLTBAndStatisticsAreaQ(folder, out_path_global, folder_name)
    else:
        findDLTBAndStatisticsAreaQ(in_path_global, out_path_global, table_name_global)

# -*- coding: gbk -*-
import sys
import arcpy
import os
import string
import re

reload(sys)
sys.setdefaultencoding("utf-8")

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
    table_name = name1.strip(string.digits)
    if table_name == '':
        table_name = "Table" + name1
    tb_path = os.path.join(path1, table_name)
    field_ls = []
    # ���ֵ������ֶ����ԣ����б��������ֶ�
    field_list = [{'name': 'name', 'type': 'TEXT', 'alias': 'ʸ����������'},  #0
                  {'name': 'E', 'type': 'DOUBLE', 'alias': '���أ�01��-С��'},  #1
                  {'name': 'F', 'type': 'DOUBLE', 'alias': '���أ�01��-LS'},  #2
                  {'name': 'G', 'type': 'DOUBLE', 'alias': '���أ�01��-FLS'},  #3
                  {'name': 'H', 'type': 'DOUBLE', 'alias': '���أ�01��-LYFL'},  #4
                  {'name': 'I', 'type': 'DOUBLE', 'alias': '���أ�01��-XG'},  #5
                  {'name': 'J', 'type': 'DOUBLE', 'alias': '���أ�01��-LLJZ'},  #6
                  {'name': 'K', 'type': 'DOUBLE', 'alias': '���أ�01��-WG'},  #7
                  {'name': 'L', 'type': 'DOUBLE', 'alias': 'ˮ�0101��-С��'},  #8
                  {'name': 'M', 'type': 'DOUBLE', 'alias': 'ˮ�0101��-LS'},  #9
                  {'name': 'N', 'type': 'DOUBLE', 'alias': 'ˮ�0101��-FLS'},  #10
                  {'name': 'O', 'type': 'DOUBLE', 'alias': 'ˮ�0101��-LYFL'},  #11
                  {'name': 'P', 'type': 'DOUBLE', 'alias': 'ˮ�0101��-XG'},  #12
                  {'name': 'Q', 'type': 'DOUBLE', 'alias': 'ˮ�0101��-LLJZ'},  #13
                  {'name': 'R', 'type': 'DOUBLE', 'alias': 'ˮ�0101��-WG'},  #14
                  {'name': 'S', 'type': 'DOUBLE', 'alias': 'ˮ���أ�0102��-С��'},  #15
                  {'name': 'T', 'type': 'DOUBLE', 'alias': 'ˮ���أ�0102��-LS'},  #16
                  {'name': 'U', 'type': 'DOUBLE', 'alias': 'ˮ���أ�0102��-FLS'},  #17
                  {'name': 'V', 'type': 'DOUBLE', 'alias': 'ˮ���أ�0102��-LYFL'},  #18
                  {'name': 'W', 'type': 'DOUBLE', 'alias': 'ˮ���أ�0102��-XG'},  # 19
                  {'name': 'X', 'type': 'DOUBLE', 'alias': 'ˮ���أ�0102��-LLJZ'},  # 20
                  {'name': 'Y', 'type': 'DOUBLE', 'alias': 'ˮ���أ�0102��-WG'},  # 21

                  {'name': 'Z', 'type': 'DOUBLE', 'alias': '���أ�0103��-С��'},  # 22
                  {'name': 'AA', 'type': 'DOUBLE', 'alias': '���أ�0103��-LS'},  # 23
                  {'name': 'AB', 'type': 'DOUBLE', 'alias': '���أ�0103��-FLS'},  # 24
                  {'name': 'AC', 'type': 'DOUBLE', 'alias': '���أ�0103��-LYFL'},  # 25
                  {'name': 'AD', 'type': 'DOUBLE', 'alias': '���أ�0103��-XG'},  # 26
                  {'name': 'AE', 'type': 'DOUBLE', 'alias': '���أ�0103��-LLJZ'},  # 27
                  {'name': 'AF', 'type': 'DOUBLE', 'alias': '���أ�0103��-WG'},  # 28
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
            asa = re.findall(r"[^()\[\]{},.*/|\:?\'\"<>]", gdb_name)
            gd_out_name = getNewFileNameQ(temp_gdb, "DLTB" + "".join(asa))
            gd_out_path = os.path.join(temp_gdb, gd_out_name)
            gd_table_path = os.path.join(temp_gdb, getNewFileNameQ(temp_gdb, "table" + "".join(asa)))
            row_values = [gdb_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0]
            cout += 1
            find_DLTB = False
            arcpy.AddMessage("(" + str(cout) + ")" + os.path.basename(workspace))
            if arcpy.Exists(DLTB_PATH_1):
                arcpy.AddMessage("    ��������Ϊ���ص�ͼ��...")
                arcpy.FeatureClassToFeatureClass_conversion(DLTB_PATH_1, temp_gdb, gd_out_name,
                                                            'DLBM in (\'0101\', \'0102\', \'0103\')')
                find_DLTB = True
            else:
                dataset_ls = arcpy.ListDatasets()
                for dataset in dataset_ls:
                    DLTB_PATH = os.path.join(os.path.join(workspace, dataset), "DLTB")
                    if arcpy.Exists(DLTB_PATH):
                        arcpy.AddMessage("    ��������Ϊ���ص�ͼ��...")
                        arcpy.FeatureClassToFeatureClass_conversion(DLTB_PATH, temp_gdb, gd_out_name,
                                                                    'DLBM in (\'0101\', \'0102\', \'0103\')')
                        find_DLTB = True
                        break
            if not find_DLTB:
                arcpy.AddError("    " + os.path.basename(workspace) + " ���޷��ҵ� DLTBͼ�㣡ʧ�ܣ�")
                fail += 1
                fail_list.append(workspace)
                continue

            if arcpy.Exists(gd_out_path):
                arcpy.AddMessage("    ͳ�� " + gd_out_path + " ...")
                arcpy.Statistics_analysis(gd_out_path, gd_table_path, [["Shape_Area", "SUM"]], ['DLBM', 'ZZSXDM'])
                with arcpy.da.SearchCursor(gd_table_path, ('DLBM', 'ZZSXDM', 'SUM_Shape_Area')) as cursor:
                    for row in cursor:
                        if row[0] == '0101' and row[1] == 'LS':
                            row_values[9] = row[2] + row_values[9]
                        if row[0] == '0101' and row[1] == 'FLS':
                            row_values[10] = row[2] + row_values[10]
                        if row[0] == '0101' and row[1] == 'LYFL':
                            row_values[11] = row[2] + row_values[11]
                        if row[0] == '0101' and row[1] == 'XG':
                            row_values[12] = row[2] + row_values[12]
                        if row[0] == '0101' and row[1] == 'LLJZ':
                            row_values[13] = row[2] + row_values[13]
                        if row[0] == '0101' and row[1] == 'WG':
                            row_values[14] = row[2] + row_values[14]

                        if row[0] == '0102' and row[1] == 'LS':
                            row_values[16] = row[2] + row_values[16]
                        if row[0] == '0102' and row[1] == 'FLS':
                            row_values[17] = row[2] + row_values[17]
                        if row[0] == '0102' and row[1] == 'LYFL':
                            row_values[18] = row[2] + row_values[18]
                        if row[0] == '0102' and row[1] == 'XG':
                            row_values[19] = row[2] + row_values[19]
                        if row[0] == '0102' and row[1] == 'LLJZ':
                            row_values[20] = row[2] + row_values[20]
                        if row[0] == '0102' and row[1] == 'WG':
                            row_values[21] = row[2] + row_values[21]

                        if row[0] == '0103' and row[1] == 'LS':
                            row_values[23] = row[2] + row_values[23]
                        if row[0] == '0103' and row[1] == 'FLS':
                            row_values[24] = row[2] + row_values[24]
                        if row[0] == '0103' and row[1] == 'LYFL':
                            row_values[25] = row[2] + row_values[25]
                        if row[0] == '0103' and row[1] == 'XG':
                            row_values[26] = row[2] + row_values[26]
                        if row[0] == '0103' and row[1] == 'LLJZ':
                            row_values[27] = row[2] + row_values[27]
                        if row[0] == '0103' and row[1] == 'WG':
                            row_values[28] = row[2] + row_values[28]

            else:
                arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
                fail += 1
                fail_list.append(workspace)
                continue

            row_values[8] = row_values[9] + row_values[10] + row_values[11] + row_values[12] + row_values[13] + \
                             row_values[14]
            row_values[15] = row_values[16] + row_values[17] + row_values[18] + row_values[19] + row_values[20] + \
                             row_values[21]
            row_values[22] = row_values[23] + row_values[24] + row_values[25] + row_values[26] + row_values[27] + \
                             row_values[28]

            row_values[2] = row_values[9] + row_values[16] + row_values[23]
            row_values[3] = row_values[10] + row_values[17] + row_values[24]
            row_values[4] = row_values[11] + row_values[18] + row_values[25]
            row_values[5] = row_values[12] + row_values[19] + row_values[26]
            row_values[6] = row_values[13] + row_values[20] + row_values[27]
            row_values[7] = row_values[14] + row_values[21] + row_values[28]

            row_values[1] = row_values[8] + row_values[15] + row_values[22]

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

    findDLTBAndStatisticsAreaQ(in_path_global, out_path_global, table_name_global)

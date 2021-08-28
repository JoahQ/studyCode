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

XZDMMC_NAME = 'xzdmmc' + str(int(time.time()))
XZDMMC_ALIAS = "��������"
FIELD_LIST = ['GDHBZY', 'XMC', 'XZQDM', 'YKDL']
#���ֵ�һ���ܵĺ���
def createTableQ(path, name):
    """
    �½����arcgis���Ա���ָ���̶��ֶ�
    :param path:
    :param name:
    :return:
    """
    arcpy.AddMessage("+")
    asa123 = re.findall(r"[^()\[\]{},.*/|\\:;?\'\"<>%!@#$&]", name)
    name11 = "".join(asa123)
    table_name = name11.lstrip(string.digits)
    if table_name == '':
        table_name = "Table" + name
    tb_path = os.path.join(path, table_name)
    field_ls = []
    # ���ֵ������ֶ����ԣ����б��������ֶ�
    field_list = [{'name': 'xzqmc', 'type': 'TEXT', 'alias': '����������'},#0

                  {'name': 'C', 'type': 'DOUBLE', 'alias': '�������·�ͼ��-�ϼ�'},#1
                  {'name': 'D', 'type': 'DOUBLE', 'alias': '�Ǹ��غ���Դ��Ǳ��ͼ�����'},#2
                  {'name': 'E', 'type': 'DOUBLE', 'alias': '���غ���Դ��Ǳ��ͼ�����'},#3

                  {'name': 'F', 'type': 'DOUBLE', 'alias': '�ط�������ȡǱ��ͼ�����'},#4

                  {'name': 'G', 'type': 'DOUBLE', 'alias': '���غ���Դ��Ǳ��ͼ�����-�ϼ�'},#5

                  {'name': 'H', 'type': 'DOUBLE', 'alias': '�˸�ũ�õ�Ǳ��-С��'},#6
                  {'name': 'I', 'type': 'DOUBLE', 'alias': '�˸�ũ�õ�Ǳ��-ˮ��'},#7
                  {'name': 'J', 'type': 'DOUBLE', 'alias': '�˸�ũ�õ�Ǳ��-����'},#8

                  {'name': 'K', 'type': 'DOUBLE', 'alias': '�˸�δ���õ�Ǳ��-С��'},#9
                  {'name': 'L', 'type': 'DOUBLE', 'alias': '�˸�δ���õ�Ǳ��-ˮ��'},#10
                  {'name': 'M', 'type': 'DOUBLE', 'alias': '�˸�δ���õ�Ǳ��-����'},#11

                  {'name': 'N', 'type': 'DOUBLE', 'alias': '���ʸ���Ǳ��-С��'},#12
                  {'name': 'O', 'type': 'DOUBLE', 'alias': '���ʸ���Ǳ��-ˮ��'},#13

                  {'name': 'P', 'type': 'DOUBLE', 'alias': '�����õظ���Ǳ��-С��'},#14
                  {'name': 'Q', 'type': 'DOUBLE', 'alias': '�����õظ���Ǳ��-ˮ��'},#15
                  {'name': 'R', 'type': 'DOUBLE', 'alias': '�����õظ���Ǳ��-����'},#16
                  {'name': 'S', 'type': 'DOUBLE', 'alias': '�����õظ���Ǳ��-����ũ�õ�'}]#17

    arcpy.CreateTable_management(path, table_name)

    for field in field_list:
        arcpy.AddField_management(tb_path, field['name'], field['type'], "#", "#", "#", field['alias'])
        field_ls.append(field['name'])
    arcpy.AddMessage("+")
    return [tb_path, field_ls]

def getNewFileNameQ(dirpath, file_name_out):
    n = [1]
    def get_new_name(file_name_in):
        new_file_name = file_name_in
        if arcpy.Exists(os.path.join(dirpath, file_name_in)):
            new_file_name = "%s_%s%s" % (os.path.splitext(file_name_in)[0], str(n[0]), os.path.splitext(file_name_in)[1])
            n[0] += 1
            if arcpy.Exists(os.path.join(dirpath, new_file_name)):
                new_file_name = get_new_name(file_name_in)
        return new_file_name
    return get_new_name(file_name_out)

def checkFeatureClassNameAndGetPathQ(in_workspace_cfn):
    arcpy.env.workspace = in_workspace_cfn
    in_fc_list = []
    ronge_name_list = []
    fc_lists = arcpy.ListFeatureClasses()
    right_name = True
    null_layer = True

    for fc in fc_lists:
        a = (u"ũ�õ�" in fc or u"δ���õ�" in fc or u"�����õ�" in fc or u"���ʸ���" in fc or u"������ȡ" in fc)
        b = ("ũ�õ�" in fc or "δ���õ�" in fc or "�����õ�" in fc or "���ʸ���" in fc or "������ȡ" in fc)
        if b or a:
            in_fc_list.append(os.path.join(arcpy.env.workspace, fc))
        else:
            right_name = False
            ronge_name_list.append(fc)
            arcpy.AddError("    \"" + fc + "\" ͼ���������淶������")

    if len(fc_lists) > 0:
        null_layer = False
    if (not right_name) and len(ronge_name_list) > 0 and len(in_fc_list) == 5:
        arcpy.AddMessage("-" * 25)
        arcpy.AddError(" ���ݿ� " + in_workspace_cfn + " ���ж����ͼ��, ���£�")
        for r in ronge_name_list:
            arcpy.AddError("     " + r)
        arcpy.AddMessage("-" * 25)
        right_name = True
    if not right_name:
        arcpy.AddError("���ݿ⣺" + in_workspace_cfn + " ͼ���������淶������")
        arcpy.AddMessage("-" * 25)
        arcpy.AddMessage("  ��׼��ͼ������Ӧ��Ϊ��")
        arcpy.AddMessage("     �������ʸ���Ǳ������ͼ��")
        arcpy.AddMessage("     �����õظ���Ǳ������ͼ��")
        arcpy.AddMessage("     �˸�ũ�õ�Ǳ������ͼ��")
        arcpy.AddMessage("     �˸�δ���õ�Ǳ������ͼ��")
        arcpy.AddMessage("     ������ȡǱ��ͼ��")
        arcpy.AddMessage("-"*25)
    if null_layer:
        arcpy.AddError("���ݿ⣺" + in_workspace_cfn + " Ϊ�ջ������𻵣��޷��򿪣�����")
        right_name = False

    return [right_name, in_fc_list]

def checkFieldsExistQ(fc_pathcf, field_listcf):
    field_list = arcpy.ListFields(fc_pathcf)
    field_name_list = [field.name for field in field_list]
    not_exist_list = []
    for sd_field in field_listcf:
        if sd_field not in field_name_list:
            not_exist_list.append(sd_field)
    return not_exist_list

def exportFeatureClassQ(in_fc_listex, out_gdbex):
    arcpy.FeatureClassToGeodatabase_conversion(in_fc_listex, out_gdbex)
    data_fc_path = []
    for in_fc_p in in_fc_listex:
        data_fc_path.append(os.path.join(out_gdbex, os.path.basename(in_fc_p)))
    arcpy.AddMessage(" . ")
    return data_fc_path

def getXZMCListQ(fcpath):
    xzmc_list = []
    with arcpy.da.SearchCursor(fcpath, ('XZQDM', 'XZQMC')) as cursor:
        for row in cursor:
            if [row[0], row[1]] not in xzmc_list:
                xzmc_list.append([row[0], row[1]])

    return xzmc_list

#ͳ������
def statisticsAreaQ(in_fc_listsa, out_gdbsa, xzq_path, tb_path_field_list):
    arcpy.AddMessage("ͳ�Ƹ�������غ���Դ��Ǳ��ͼ�� ...")
    table_path = tb_path_field_list[0]
    table_field = tb_path_field_list[1]

    #�ϲ�����
    merge_path = os.path.join(out_gdbsa, getNewFileNameQ(out_gdbsa, "merge"))
    merge_statisticstable_path = os.path.join(out_gdbsa, getNewFileNameQ(out_gdbsa, "merge_statisticsTable"))

    temp_table_list = []
    FIELD_LIST.append(XZDMMC_NAME)
    fieldmappings2 = arcpy.FieldMappings()
    vTab = arcpy.ValueTable()
    for in_fc_path123 in in_fc_listsa:
        arcpy.AddField_management(in_fc_path123, XZDMMC_NAME, 'TEXT', "#", "#", 50, XZDMMC_ALIAS)
        arcpy.CalculateField_management(in_fc_path123, XZDMMC_NAME, "!XZQDM![0:9]", "PYTHON_9.3")
        fc = os.path.basename(in_fc_path123)
        temp_table_path = os.path.join(out_gdbsa, getNewFileNameQ(out_gdbsa, "table_" + fc))
        arcpy.Statistics_analysis(in_fc_path123, temp_table_path, [["Shape_Area", "SUM"]], XZDMMC_NAME)
        temp_table_list.append(temp_table_path)


        fieldmappings2.addTable(in_fc_path123)
        vTab.addRow(in_fc_path123)

    for field in fieldmappings2.fields:
        if field.name not in FIELD_LIST:
            fieldmappings2.removeFieldMap(fieldmappings2.findFieldMapIndex(field.name))
    arcpy.Merge_management(vTab, merge_path, fieldmappings2)

    in_cursor = arcpy.da.InsertCursor(table_path, table_field)
    row_values = []
    xzmc_list = getXZMCListQ(xzq_path)
    arcpy.Statistics_analysis(merge_path, merge_statisticstable_path, [["Shape_Area", "SUM"]],
                              ['GDHBZY', XZDMMC_NAME, 'YKDL'])

    for i in range(len(xzmc_list)):
        row_values.append([xzmc_list[i][1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        with arcpy.da.SearchCursor(merge_statisticstable_path, ('GDHBZY', XZDMMC_NAME, 'YKDL', 'SUM_Shape_Area')) as cursor:
            for row in cursor:
                if row[1] == xzmc_list[i][0]:
                    if ("ũ�õ�" in row[0] or u"ũ�õ�" in row[0]) and row[2] == '0101':
                        row_values[i][7] = row_values[i][7] + row[3]
                    if ("ũ�õ�" in row[0] or u"ũ�õ�" in row[0]) and row[2] == '0103':
                        row_values[i][8] = row_values[i][8] + row[3]

                    if ("δ���õ�" in row[0] or u"δ���õ�" in row[0]) and row[2] == '0101':
                        row_values[i][10] = row_values[i][10] + row[3]
                    if ("δ���õ�" in row[0] or u"δ���õ�" in row[0]) and row[2] == '0103':
                        row_values[i][11] = row_values[i][11] + row[3]

                    if ("���ʸ���" in row[0] or u"���ʸ���" in row[0]) and row[2] == '0101':
                        row_values[i][13] = row_values[i][13] + row[3]

                    if ("�����õ�" in row[0] or u"�����õ�" in row[0]) and row[2] == '0101':
                        row_values[i][15] = row_values[i][15] + row[3]
                    if ("�����õ�" in row[0] or u"�����õ�" in row[0]) and row[2] == '0103':
                        row_values[i][16] = row_values[i][16] + row[3]
                    if ("�����õ�" in row[0] or u"�����õ�" in row[0]) and row[2] == 'QT':
                        row_values[i][17] = row_values[i][17] + row[3]

        row_values[i][6] = row_values[i][7] + row_values[i][8]
        row_values[i][9] = row_values[i][10] + row_values[i][11]
        row_values[i][12] = row_values[i][13]
        row_values[i][14] = row_values[i][15] + row_values[i][16] + row_values[i][17]

        row_values[i][5] = row_values[i][6] + row_values[i][9] + row_values[i][12] + row_values[i][14]
        for in_table_path in temp_table_list:
            table = os.path.basename(in_table_path)
            if "������ȡ" in table or u"������ȡ" in table:
                with arcpy.da.SearchCursor(in_table_path, (XZDMMC_NAME, 'SUM_Shape_Area')) as cursor:
                    for row in cursor:
                        if row[0] == xzmc_list[i][0]:
                            row_values[i][4] = row_values[i][4] + row[1]
            else:
                with arcpy.da.SearchCursor(in_table_path, (XZDMMC_NAME, 'SUM_Shape_Area')) as cursor:
                    for row in cursor:
                        if row[0] == xzmc_list[i][0]:
                            row_values[i][1] = row_values[i][1] + row[1]

        row_values[i][3] = row_values[i][5] - row_values[i][4]
        row_values[i][2] = row_values[i][1] - row_values[i][3]

    for rows in row_values:
        in_cursor.insertRow(tuple(rows))
    del in_cursor

#û����������
def statisticsAreaNoNameQ(in_fc_listsa, out_gdbsa, tb_path_field_list):
    arcpy.AddMessage("ͳ�Ƹ�������غ���Դ��Ǳ��ͼ�� ...")
    table_path = tb_path_field_list[0]
    table_field = tb_path_field_list[1]

    #�ϲ�����
    merge_path = os.path.join(out_gdbsa, getNewFileNameQ(out_gdbsa, "merge"))
    merge_statisticstable_path = os.path.join(out_gdbsa, getNewFileNameQ(out_gdbsa, "merge_statisticsTable"))

    temp_table_list = []
    FIELD_LIST.append(XZDMMC_NAME)
    fieldmappings2 = arcpy.FieldMappings()
    vTab = arcpy.ValueTable()
    for in_fc_path123 in in_fc_listsa:
        arcpy.AddField_management(in_fc_path123, XZDMMC_NAME, 'TEXT', "#", "#", 50, XZDMMC_ALIAS)
        arcpy.CalculateField_management(in_fc_path123, XZDMMC_NAME, "!XZQDM![0:9]", "PYTHON_9.3")
        fc = os.path.basename(in_fc_path123)
        temp_table_path = os.path.join(out_gdbsa, getNewFileNameQ(out_gdbsa, "table_" + fc))
        arcpy.Statistics_analysis(in_fc_path123, temp_table_path, [["Shape_Area", "SUM"]], XZDMMC_NAME)
        temp_table_list.append(temp_table_path)

        fieldmappings2.addTable(in_fc_path123)
        vTab.addRow(in_fc_path123)

    for field in fieldmappings2.fields:
        if field.name not in FIELD_LIST:
            fieldmappings2.removeFieldMap(fieldmappings2.findFieldMapIndex(field.name))
    arcpy.Merge_management(vTab, merge_path, fieldmappings2)

    in_cursor = arcpy.da.InsertCursor(table_path, table_field)
    row_values = []
    xzmc_list = []
    arcpy.Statistics_analysis(merge_path, merge_statisticstable_path, [["Shape_Area", "SUM"]],
                              ['GDHBZY', XZDMMC_NAME, 'YKDL'])

    with arcpy.da.SearchCursor(merge_statisticstable_path, XZDMMC_NAME) as cursor:
        for row in cursor:
            if row[0] not in xzmc_list:
                xzmc_list.append(row[0])

    for i in range(len(xzmc_list)):
        row_values.append([xzmc_list[i], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        with arcpy.da.SearchCursor(merge_statisticstable_path, ('GDHBZY', XZDMMC_NAME, 'YKDL', 'SUM_Shape_Area')) as cursor:
            for row in cursor:
                xzmc_list.append(row[1])
                if row[1] == xzmc_list[i]:
                    if ("ũ�õ�" in row[0] or u"ũ�õ�" in row[0]) and row[2] == '0101':
                        row_values[i][7] = row_values[i][7] + row[3]
                    if ("ũ�õ�" in row[0] or u"ũ�õ�" in row[0]) and row[2] == '0103':
                        row_values[i][8] = row_values[i][8] + row[3]

                    if ("δ���õ�" in row[0] or u"δ���õ�" in row[0]) and row[2] == '0101':
                        row_values[i][10] = row_values[i][10] + row[3]
                    if ("δ���õ�" in row[0] or u"δ���õ�" in row[0]) and row[2] == '0103':
                        row_values[i][11] = row_values[i][11] + row[3]

                    if ("���ʸ���" in row[0] or u"���ʸ���" in row[0]) and row[2] == '0101':
                        row_values[i][13] = row_values[i][13] + row[3]

                    if ("�����õ�" in row[0] or u"�����õ�" in row[0]) and row[2] == '0101':
                        row_values[i][15] = row_values[i][15] + row[3]
                    if ("�����õ�" in row[0] or u"�����õ�" in row[0]) and row[2] == '0103':
                        row_values[i][16] = row_values[i][16] + row[3]
                    if ("�����õ�" in row[0] or u"�����õ�" in row[0]) and row[2] == 'QT':
                        row_values[i][17] = row_values[i][17] + row[3]

        row_values[i][6] = row_values[i][7] + row_values[i][8]
        row_values[i][9] = row_values[i][10] + row_values[i][11]
        row_values[i][12] = row_values[i][13]
        row_values[i][14] = row_values[i][15] + row_values[i][16] + row_values[i][17]

        row_values[i][5] = row_values[i][6] + row_values[i][9] + row_values[i][12] + row_values[i][14]
        for in_table_path in temp_table_list:
            table = os.path.basename(in_table_path)
            if "������ȡ" in table or u"������ȡ" in table:
                with arcpy.da.SearchCursor(in_table_path, (XZDMMC_NAME, 'SUM_Shape_Area')) as cursor:
                    for row in cursor:
                        if row[0] == xzmc_list[i]:
                            row_values[i][4] = row_values[i][4] + row[1]
            else:
                with arcpy.da.SearchCursor(in_table_path, (XZDMMC_NAME, 'SUM_Shape_Area')) as cursor:
                    for row in cursor:
                        if row[0] == xzmc_list[i]:
                            row_values[i][1] = row_values[i][1] + row[1]

        row_values[i][3] = row_values[i][5] - row_values[i][4]
        row_values[i][2] = row_values[i][1] - row_values[i][3]

    for rows in row_values:
        in_cursor.insertRow(tuple(rows))
    del in_cursor

def statisticsXJAreaQ(in_fc_listsa1, out_gdbsa1, tb_path_field_list1):
    arcpy.AddMessage("ͳ��ȫ�ظ��غ���Դ��Ǳ��ͼ�� ...")
    table_path = tb_path_field_list1[0]
    table_field = tb_path_field_list1[1]

    #�ϲ�����
    merge_path = os.path.join(out_gdbsa1, getNewFileNameQ(out_gdbsa1, "merge_�ؼ�"))
    merge_table_pathxj = os.path.join(out_gdbsa1, getNewFileNameQ(out_gdbsa1, "merge_Table_�ؼ�"))

    temp_table_list = []
    FIELD_LIST.append(XZDMMC_NAME)
    fieldmappings2 = arcpy.FieldMappings()
    vTab = arcpy.ValueTable()
    for in_fc_path123 in in_fc_listsa1:
        fc = os.path.basename(in_fc_path123)
        temp_table_path = os.path.join(out_gdbsa1, getNewFileNameQ(out_gdbsa1, "xjtable_" + fc))
        arcpy.Statistics_analysis(in_fc_path123, temp_table_path, [["Shape_Area", "SUM"]], 'XMC')
        temp_table_list.append(temp_table_path)
        fieldmappings2.addTable(in_fc_path123)
        vTab.addRow(in_fc_path123)

    for field in fieldmappings2.fields:
        if field.name not in FIELD_LIST:
            fieldmappings2.removeFieldMap(fieldmappings2.findFieldMapIndex(field.name))
    arcpy.Merge_management(vTab, merge_path, fieldmappings2)

    in_cursor = arcpy.da.InsertCursor(table_path, table_field)
    row_values = ["", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    arcpy.Statistics_analysis(merge_path, merge_table_pathxj, [["Shape_Area", "SUM"]],
                              ['GDHBZY', 'XMC', 'YKDL'])

    with arcpy.da.SearchCursor(merge_table_pathxj, ('GDHBZY', 'XMC', 'YKDL', 'SUM_Shape_Area')) as cursor:
        for row in cursor:
            row_values[0] = row[1]
            if ("ũ�õ�" in row[0] or u"ũ�õ�" in row[0]) and row[2] == '0101':
                row_values[7] = row_values[7] + row[3]
            if ("ũ�õ�" in row[0] or u"ũ�õ�" in row[0]) and row[2] == '0103':
                row_values[8] = row_values[8] + row[3]

            if ("δ���õ�" in row[0] or u"δ���õ�" in row[0]) and row[2] == '0101':
                row_values[10] = row_values[10] + row[3]
            if ("δ���õ�" in row[0] or u"δ���õ�" in row[0]) and row[2] == '0103':
                row_values[11] = row_values[11] + row[3]

            if ("���ʸ���" in row[0] or u"���ʸ���" in row[0]) and row[2] == '0101':
                row_values[13] = row_values[13] + row[3]

            if ("�����õ�" in row[0] or u"�����õ�" in row[0]) and row[2] == '0101':
                row_values[15] = row_values[15] + row[3]
            if ("�����õ�" in row[0] or u"�����õ�" in row[0]) and row[2] == '0103':
                row_values[16] = row_values[16] + row[3]
            if ("�����õ�" in row[0] or u"�����õ�" in row[0]) and row[2] == 'QT':
                row_values[17] = row_values[17] + row[3]

    row_values[6] = row_values[7] + row_values[8]
    row_values[9] = row_values[10] + row_values[11]
    row_values[12] = row_values[13]
    row_values[14] = row_values[15] + row_values[16] + row_values[17]

    row_values[5] = row_values[6] + row_values[9] + row_values[12] + row_values[14]
    for in_table_path in temp_table_list:
        table = os.path.basename(in_table_path)
        if "������ȡ" in table or u"������ȡ" in table:
            with arcpy.da.SearchCursor(in_table_path, ('XMC', 'SUM_Shape_Area')) as cursor:
                for row in cursor:
                    row_values[4] = row_values[4] + row[1]
        else:
            with arcpy.da.SearchCursor(in_table_path, ('XMC', 'SUM_Shape_Area')) as cursor:
                for row in cursor:
                    row_values[1] = row_values[1] + row[1]

    row_values[3] = row_values[5] - row_values[4]
    row_values[2] = row_values[1] - row_values[3]

    in_cursor.insertRow(tuple(row_values))
    del in_cursor

def tableToExcelQ(table_path_e3, fields3, excel_path3, tablename3, sheets_name3='sheet'):

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
        ali1.horz = 0x01
        ali1.vert = 0x01
        style2.alignment = ali1
        del ali1

        style3 = set_style(u'����', 16, False, True, True)
        ali4 = xlwt.Alignment()
        ali4.horz = 0x02
        ali4.vert = 0x00
        style3.alignment = ali4
        del ali4
        bt = u"��5  " + tablename3.strip(string.digits)
        worksheets.write_merge(0, 0, 0, 18, bt, style3)

        worksheets.write(1, 1, '��λ������)��', style2)
        worksheets.write(1, 9, '�ɹ����ͣ��������ɹ�/�����ճɹ�', style2)
        worksheets.write(1, 17, '����', style2)

        worksheets.write_merge(2, 4, 0, 0, '���', style1)
        worksheets.write_merge(2, 4, 1, 1, '����������', style1)
        worksheets.write_merge(2, 2, 2, 4, '�������·�ͼ��', style1)
        worksheets.write_merge(3, 4, 2, 2, '�ϼ�', style1)
        worksheets.write_merge(3, 4, 3, 3, '�Ǹ��غ���Դ��Ǳ��ͼ�����', style1)
        worksheets.write_merge(3, 4, 4, 4, '���غ���Դ��Ǳ��ͼ�����', style1)
        worksheets.write_merge(2, 4, 5, 5, '�ط�������ȡǱ��ͼ�����', style1)
        worksheets.write_merge(2, 2, 6, 18, '���غ���Դ��Ǳ��ͼ�����', style1)
        worksheets.write_merge(3, 4, 6, 6, '�ϼ�', style1)
        worksheets.write_merge(3, 3, 7, 9, '�˸�ũ�õ�Ǳ��', style1)
        worksheets.write_merge(3, 3, 10, 12, '�˸�δ���õ�Ǳ��', style1)
        worksheets.write_merge(3, 3, 13, 14, '���ʸ���Ǳ��', style1)
        worksheets.write_merge(3, 3, 15, 18, '�����õظ���Ǳ��', style1)

        tlist = ['С��', 'ˮ��(0101)', '����(0103)', 'С��', 'ˮ��(0101)', '����(0103)', 'С��', 'ˮ��(0101)',
                 'С��', 'ˮ��(0101)', '����(0103)', '����ũ�õ�']
        for ii in range(7,19):
            worksheets.write(4, ii, tlist[ii-7], style1)
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
    index1 = 0
    if arcpy.Exists(table_path_e3) and int(arcpy.GetCount_management(table_path_e3).getOutput(0)) > 0:
        with arcpy.da.SearchCursor(table_path_e3, fields3) as cursor:
            for row in cursor:
                index1 += 1
                sheet1.write(row[0] + 4, 0, row[0], styles)
                sheet1.write(row[0] + 4, 1, row[1], styles)
                for i in range(2, 19):
                    sheet1.write(row[0] + 4, i, row[i]/10000, style_num)
                set_row_height(sheet1, row[0] + 4, 25)
        del i
        del cursor
    arcpy.AddMessage("index=" + str(index1))
    stylelast = set_style(u'����', 11)
    ali2 = xlwt.Alignment()
    ali2.horz = 0x01
    ali2.vert = 0x01
    stylelast.alignment = ali2
    del ali2
    sheet1.write(index1 + 5, 2, "����ˣ�", stylelast)
    sheet1.write(index1 + 5, 8, "����ˣ�", stylelast)
    sheet1.write(index1 + 5, 14, "�ϱ�ʱ�䣺", stylelast)
    set_row_height(sheet1, index1 + 5, 25)

    # �����п�
    set_col_width(sheet1, col_index=0, col_width=4.71)
    for j in range(1,19):
        set_col_width(sheet1, col_index=j, col_width=16.71)

    workbook.save(excel_path3)

if __name__ == "__main__":
    in_gdbG = arcpy.GetParameterAsText(0)
    xzq_pathG = arcpy.GetParameterAsText(1)
    out_pathG = arcpy.GetParameterAsText(2)
    nameGG = arcpy.GetParameterAsText(3)

    listtt123 = re.findall(r"[^\\/:*?\"<>|]", nameGG)
    nameG = "".join(listtt123).strip()

    in_fc_list0 = checkFeatureClassNameAndGetPathQ(in_gdbG)

    if not in_fc_list0[0]:
        arcpy.AddError("*ʧ�ܣ�����ʸ������ͼ���������淶����ȷ�ϣ�")
        list00 = []
        print list00[99999999]
        sys.exit()

    FIELD_LIST_GLOBAL = ['GDHBZY', 'XMC', 'XZQDM', 'YKDL']
    exile_field = False
    for fcpath in in_fc_list0[1]:
        exile_fieldlist = checkFieldsExistQ(fcpath,FIELD_LIST_GLOBAL)
        if len(exile_fieldlist) > 0:
            exile_field = True
            arcpy.AddError(" ")
            arcpy.AddError("      ʸ�����ݣ�" + os.path.basename(fcpath) + " ͼ��ȱ�� [" + "; ".join(exile_fieldlist) + "] �ֶ�")
    if exile_field:
        list0 = []
        print list0[99999999]
        sys.exit()
    temp_gdb_name = getNewFileNameQ(out_pathG, nameG + ".gdb")
    temp_gdb_path = os.path.join(out_pathG, temp_gdb_name)

    arcpy.CreateFileGDB_management(out_pathG, os.path.basename(temp_gdb_path))

    tb_ptg = createTableQ(temp_gdb_path, getNewFileNameQ(temp_gdb_path, nameG))
    field_lists = ['OBJECTID']
    for ffield in tb_ptg[1]:
        field_lists.append(ffield)

    global_data_list = exportFeatureClassQ(in_fc_list0[1], temp_gdb_path)
    statisticsXJAreaQ(global_data_list, temp_gdb_path, tb_ptg)
    if arcpy.Exists(xzq_pathG):
        FIELD_XZ_GLOBAL = ['XZQDM', 'XZQMC']
        exileXZ_field = False
        exileXZ_fieldlist = checkFieldsExistQ(xzq_pathG, FIELD_XZ_GLOBAL)
        if len(exileXZ_fieldlist) > 0:
            exile_field = True
            arcpy.AddError(" ")
            arcpy.AddError("      " + xzq_pathG + " ȱ�� [" + "; ".join(exile_fieldlist) + "] �ֶ�")
        if exileXZ_field:
            list0 = []
            print list0[99999999]
            sys.exit()
        statisticsAreaQ(global_data_list, temp_gdb_path, xzq_pathG, tb_ptg)
    else:
        statisticsAreaNoNameQ(global_data_list, temp_gdb_path, tb_ptg)

    excel_name = getNewFileNameQ(out_pathG, nameG + ".xls")
    excel_pathG = os.path.join(out_pathG, excel_name)
    tableToExcelQ(tb_ptg[0], field_lists, excel_pathG, nameG, sheets_name3='sheet')

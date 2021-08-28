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
    field_list = [{'name': 'cout', 'type': 'TEXT', 'alias': '���'},
                  {'name': 'XZQ', 'type': 'TEXT', 'alias': '������'},

                  {'name': 'A2', 'type': 'DOUBLE', 'alias': '��-�����'},
                  {'name': 'B3', 'type': 'DOUBLE', 'alias': '��-�����'},
                  {'name': 'D4', 'type': 'DOUBLE', 'alias': '0103-���'},
                  {'name': 'E5', 'type': 'DOUBLE', 'alias': '0101-���'},
                  {'name': 'F6', 'type': 'DOUBLE', 'alias': 'QT-���'},

                  {'name': 'F7', 'type': 'DOUBLE', 'alias': '��-0702-���'},
                  {'name': 'F8', 'type': 'DOUBLE', 'alias': '��-0602-���'},
                  {'name': 'F9', 'type': 'DOUBLE', 'alias': '��-0601-���'},

                  {'name': 'F10', 'type': 'DOUBLE', 'alias': '��-0702-���'},
                  {'name': 'F11', 'type': 'DOUBLE', 'alias': '��-0602-���'},
                  {'name': 'F12', 'type': 'DOUBLE', 'alias': '��-0601-���'},
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

def statisticsAreaQ3(in_path, out_path, qzql_path, pjjg_feild, name):
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

    # ����
    arcpy.AddMessage("-" * 20 + "�½����Ա�" + "-" * 20)
    tb_paths = createTableQ(result_gdb, getNewFileNameQ(result_gdb, name))

    arcpy.AddMessage("-" * 20 + "�½����Ա�" + "-" * 20)
    tb_path_bz = createTableQ(result_gdb, getNewFileNameQ(result_gdb, name+"bz"))

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
                    arcpy.AddMessage("          ͳ�� " + in_fc +" ...")
                    intersect_path = os.path.join(result_gdb,in_fc + str(cout))
                    arcpy.Intersect_analysis([in_fc_path,qzql_fc_pathp],intersect_path)
                    jsyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "jsyd_table" + str(cout)))
                    arcpy.Statistics_analysis(intersect_path, jsyd_tb1, [["Shape_Area", "SUM"]], [pjjg_feild,'YKDL','DLBM'])
                    with arcpy.da.SearchCursor(jsyd_tb1, (pjjg_feild, 'YKDL', 'DLBM', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "��" in str(row1[0]):
                                row_values[2] += row1[3]
                                if "0103" in str(row1[1]):
                                    row_values[4] += row1[3]
                                elif "0101" in str(row1[1]):
                                    row_values[5] += row1[3]
                                elif "QT" in str(row1[1]):
                                    row_values[6] += row1[3]

                                if "0702" in str(row1[2]):
                                    row_values[7] += row1[3]
                                if "0602" in str(row1[2]):
                                    row_values[8] += row1[3]
                                if "0601" in str(row1[2]):
                                    row_values[9] += row1[3]
                            if "��" in str(row1[0]):
                                row_values[3] += row1[3]
                                if "0702" in str(row1[2]):
                                    row_values[10] += row1[3]
                                if "0602" in str(row1[2]):
                                    row_values[11] += row1[3]
                                if "0601" in str(row1[2]):
                                    row_values[12] += row1[3]


                    if arcpy.Exists(intersect_path):
                        try:
                            arcpy.Delete_management(intersect_path)
                        except Exception as e:
                            arcpy.AddMessage(e.message)
                    if arcpy.Exists(jsyd_tb1):
                        try:
                            arcpy.Delete_management(jsyd_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

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
    tableToExcelQ(table_path_e3, resullist, "sheet1")
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
        bt = u"�����õ�Ǳ��Ǳ����ͳ�Ʊ�"
        worksheets.write_merge(0, 0, 0, 6, bt, style3)
        worksheets.write_merge(1, 1, 0, 6, u'���������', style2)

        worksheets.write(2, 0, u'���', style1)
        worksheets.write(2, 1, u'����������', style1)
        worksheets.write(2, 2, u'��-�����', style1)
        worksheets.write(2, 3, u'��-�����', style1)
        worksheets.write(2, 4, u'0103-���', style1)
        worksheets.write(2, 5, u'0101-���', style1)
        worksheets.write(2, 6, u'QT-���', style1)

        worksheets.write(2, 7, u'��-0702', style1)
        worksheets.write(2, 8, u'��-0602', style1)
        worksheets.write(2, 9, u'��-0601', style1)

        worksheets.write(2, 10, u'��-0702', style1)
        worksheets.write(2, 11, u'��-0602', style1)
        worksheets.write(2, 12, u'��-0601', style1)

        # �����и�
        set_row_height(worksheets, row_index=0, row_height=28)
        set_row_height(worksheets, row_index=1, row_height=22)
        set_row_height(worksheets, row_index=2, row_height=20)


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
    del ali3

    for row in datalist:
        sheet1.write(row[0] + 2, 0, row[0], styles)
        sheet1.write(row[0] + 2, 1, row[1], styles)
        for ij in range(2, 13):
            sheet1.write(row[0] + 2, ij, row[ij] / 10000, style_num)

    # �����п�
    set_col_width(sheet1, col_index=0, col_width=5.71)
    for j in range(1, 13):
        set_col_width(sheet1, col_index=j, col_width=14.71)

    workbook.save(excel_path3)

    arcpy.AddMessage(u"ͳ�ƽ���ѵ�����  " + excel_path3 + u"      Excel��")

if __name__ == "__main__":
    in_pathG = arcpy.GetParameterAsText(0)
    qzql_pathG = arcpy.GetParameterAsText(1)
    out_pathG = arcpy.GetParameterAsText(2)
    table_nameG = arcpy.GetParameterAsText(3)
    feild_CG = arcpy.GetParameterAsText(4)

    arcpy.AddMessage(feild_CG)
    listtt123 = re.findall(r"[^\\/:*?\"<>|]", table_nameG)
    table_name_global = "".join(listtt123).strip()

    statisticsAreaQ3(in_pathG, out_pathG, qzql_pathG, feild_CG, table_name_global)

    # ls = [[1, u"��˷��", 0,0,0,0,0],[2, u"��˷��", 0,0,0,0,0],[3, u"��˷��", 0,0,0,0,0]]
    # table_path_e3 = u"D:\\pyCharmWorksp\\ABC������.xls"
    # tableToExcelQ(table_path_e3, ls, u"�˿ѵ������ͳ��")


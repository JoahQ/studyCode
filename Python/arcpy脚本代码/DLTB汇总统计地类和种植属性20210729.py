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
    # field_ls = []
    # ���ֵ������ֶ����ԣ����б��������ֶ�
    field_list = [{'name': 'cout', 'type': 'TEXT', 'alias': u'���'},  # 0
                  {'name': 'XZQ', 'type': 'TEXT', 'alias': u'������'},  # 0
                  ]

    arcpy.AddMessage("�½� " + table_name + " ���...")

    arcpy.CreateTable_management(path, table_name)
    AddFieldQ(tb_path,field_list)
    return tb_path

def AddFieldQ(path, field_list):
    arcpy.AddMessage("  ����ֶ�...")
    for field in field_list:
        arcpy.AddMessage("    �ֶ����� " + field['name'] + " �ֶα����� " + field['alias'])
        arcpy.AddField_management(path, field['name'], field['type'], "#", "#", "#", field['alias'])


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


def statisticsAreaQ3(in_path, out_path, name):
    cout = 0
    fail = 0
    fail_list = []

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")

    # ��gdb
    resultg_name = getNewFileNameQ(out_path, name + "_result.gdb")
    result_gdb = os.path.join(out_path, resultg_name)
    arcpy.AddMessage("�½� " + result_gdb + " ���ڱ�����...")
    arcpy.CreateFileGDB_management(out_path, resultg_name)

    # ����
    arcpy.AddMessage("-" * 20 + "�½����Ա�" + "-" * 20)
    tb_path = createTableQ(result_gdb, getNewFileNameQ(result_gdb, "A" + name))

    tb_name = os.path.basename(tb_path)

    resullist = []
    all_fields = []
    resultdic = dict()
    for workspace in workspaces:
        success = True
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        # ��ÿ��gdb��Ϊ������
        arcpy.env.workspace = workspace
        gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])
        gdbName_new = "".join(re.findall(r"[^()\[\]{},.*/|\\:;?\'\"<>%!@#$&\-+=`~]", gdbName))
        resultdic.clear()

        try:
            xzqcode = re.findall(r"\d+", gdbName)
            resultdic.setdefault(u"���", cout)
            if len(xzqcode) > 0 and not xzqab(xzqcode[0]).isdigit():
                resultdic.setdefault(u"������", xzqab(xzqcode[0]))
            else:
                resultdic.setdefault(u"������", gdbName)

            for fc in arcpy.ListFeatureClasses():
                in_fc_path = os.path.join(workspace, fc)
                st_table_path = os.path.join(result_gdb, "T" + fc + gdbName_new)

                arcpy.AddMessage("      ����ͳ��...")
                arcpy.Statistics_analysis(in_fc_path, st_table_path, [["Shape_Area", "SUM"]], ['DLBM', 'ZZSXDM'])

                with arcpy.da.SearchCursor(st_table_path, ('DLBM','ZZSXDM','SUM_Shape_Area')) as cursor1:
                    for row1 in cursor1:
                        if row1[1] is None and str(row1[1]) == " " and row1[0] is None and str(row1[0]) == " ":
                            continue

                        afield = str(row1[1]).strip() + str(row1[0]).strip()
                        if row1[1] is None and str(row1[1]) == " ":
                            afield = str(row1[0]).strip()

                        if not afield in resultdic:
                            all_fields.append(afield)
                        if not afield in resultdic:
                            resultdic.setdefault(afield,row1[2])
                        elif afield in resultdic:
                            resultdic[afield] += row1[2]

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
            fail += 1
            fail_list.append(os.path.basename(workspace))
            success = False

        if success:
            try:
                resullist.append(resultdic)
                old_fields = arcpy.ListFields(tb_path)
                field_alias = [f.aliasName for f in old_fields]
                field_list = []
                n = len(old_fields) - 1
                dicaa = sorted(resultdic.items(),key=lambda x:x[0])

                for key in dicaa:
                    if key[0] not in field_alias:
                        field_list.append({'name': 'A'+str(n), 'type': 'DOUBLE', 'alias': key[0]})
                        n += 1
                AddFieldQ(tb_path, field_list)

                arcpy.AddMessage("-"*12)
                new_fields = arcpy.ListFields(tb_path)

                field_names = []
                row_values = []


                for tfield in new_fields:
                    if tfield.name != "OBJECTID":
                        field_names.append(tfield.name)
                        row_values.append(resultdic.get(str(tfield.aliasName).decode("utf-8"),0))


                in_cursor = arcpy.da.InsertCursor(tb_path, field_names)
                arcpy.AddMessage("    �� " + tb_name + " ������¼...")

                in_cursor.insertRow(tuple(row_values))
                del in_cursor
            except Exception as e:
                arcpy.AddError(e.message)
                arcpy.AddError("    ͳ��" + os.path.basename(workspace) + " ʧ�ܣ�")
                fail += 1
                fail_list.append(os.path.basename(workspace))

        arcpy.AddMessage("  ")

    #�����ֶν�None��Ϊ0
    # expression =
    code_block = """def calc(a):
                        if a == None:
                            return 0
                        else:
                            return a
    """
    for fieldd in arcpy.ListFields(tb_path):
        if fieldd.name != "OBJECTID" and fieldd.name != "cout" and fieldd.name != "XZQ":
            arcpy.CalculateField_management(tb_path, fieldd.name, "calc(!" +fieldd.name+"!)" , "PYTHON_9.3", code_block)

    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage("  �ɹ���" + str(cout - fail) + " ����")
    if fail > 0:
        arcpy.AddError("  ʧ�ܣ�" + str(fail) + " ���� ���£�")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)


def tableToExcelQ(excel_path3, datalist, field_list, sheets_name3='sheet'):
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

        worksheets.write_merge(0, 0, 0, len(len(field_list) - 1), u'�����ƽ����', style2)

        worksheets.write_merge(1, 3, 0, 0, u'���', style1)
        worksheets.write_merge(1, 3, 1, 1, u'����������', style1)

        worksheets.write_merge(1, 1, 2, 5, u'�˸�ũ�õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(2, 2, 2, 3, u'��ʵʩ��������', style1)
        worksheets.write(3, 2, u'���', style1)
        worksheets.write(3, 3, u'ͼ����', style1)
        worksheets.write_merge(2, 2, 4, 5, u'���ָ̻�', style1)
        worksheets.write(3, 4, u'���', style1)
        worksheets.write(3, 5, u'ͼ����', style1)

        worksheets.write_merge(1, 1, 6, 11, u'�����õظ���Ǳ������ͼ��', style1)
        worksheets.write_merge(2, 2, 6, 7, u'��ʵʩ��������', style1)
        worksheets.write(3, 6, u'���', style1)
        worksheets.write(3, 7, u'ͼ����', style1)
        worksheets.write_merge(2, 2, 8, 9, u'�˸���Ϊ����ũ�õ�', style1)
        worksheets.write(3, 8, u'���', style1)
        worksheets.write(3, 9, u'ͼ����', style1)
        worksheets.write_merge(2, 2, 10, 11, u'��ʵʩ�����ҹ�', style1)
        worksheets.write(3, 10, u'���', style1)
        worksheets.write(3, 11, u'ͼ����', style1)

        worksheets.write_merge(1, 1, 12, 15, u'�˸�δ���õ�Ǳ������ͼ��', style1)
        worksheets.write_merge(2, 2, 12, 13, u'��ʵʩ��������', style1)
        worksheets.write(3, 12, u'���', style1)
        worksheets.write(3, 13, u'ͼ����', style1)
        worksheets.write_merge(2, 2, 14, 15, u'����ũ�ﷶΧ�ڵ�δ���õ�', style1)
        worksheets.write(3, 14, u'���', style1)
        worksheets.write(3, 15, u'ͼ����', style1)

        worksheets.write_merge(1, 1, 16, 19, u'���ʸ���Ǳ������ͼ��', style1)
        worksheets.write_merge(2, 2, 16, 17, u'��ʵʩ��������', style1)
        worksheets.write(3, 16, u'���', style1)
        worksheets.write(3, 17, u'ͼ����', style1)
        worksheets.write_merge(2, 2, 18, 19, u'����ũ�ﷶΧ�ڵ�δ���õ�', style1)
        worksheets.write(3, 18, u'���', style1)
        worksheets.write(3, 19, u'ͼ����', style1)

        # �����и�
        set_row_height(worksheets, row_index=0, row_height=28)
        set_row_height(worksheets, row_index=1, row_height=22)
        set_row_height(worksheets, row_index=2, row_height=20)
        set_row_height(worksheets, row_index=3, row_height=20)
        set_row_height(worksheets, row_index=4, row_height=20)

        return worksheets

    sheet1 = add_new_sheet(sheets_name3)
    styles = set_style(u'����', 11, True, True)
    style_num = set_style(u'����', 11, True, True)
    ali3 = xlwt.Alignment()
    # 0x02 ��˶��룬0x03 �Ҷ˶���
    ali3.horz = 0x03
    ali3.vert = 0x01
    style_num.alignment = ali3

    del ali3

    for row in datalist:
        sheet1.write(row[0] + 3, 0, row[0], styles)
        sheet1.write(row[0] + 3, 1, row[1], styles)
        for ij in range(2, 20):
            sheet1.write(row[0] + 3, ij, row[ij], style_num)

    # �����п�
    set_col_width(sheet1, col_index=0, col_width=4.71)
    for j in range(1, 20):
        set_col_width(sheet1, col_index=j, col_width=16.71)

    workbook.save(excel_path3)

    arcpy.AddMessage("ͳ�ƽ���ѵ�����  " + excel_path3 + "      Excel��")


if __name__ == "__main__":
    in_pathG = arcpy.GetParameterAsText(0)
    out_pathG = arcpy.GetParameterAsText(1)
    table_nameG = arcpy.GetParameterAsText(2)

    listtt123 = re.findall(r"[^\\/:*?\"<>|]", table_nameG)
    table_name_global = "".join(listtt123).strip()

    statisticsAreaQ3(in_pathG, out_pathG, table_name_global)

    arcpy.AddMessage("in_path: " + in_pathG)
    arcpy.AddMessage("out_path: " + out_pathG)
    arcpy.AddMessage("name: " + table_nameG)

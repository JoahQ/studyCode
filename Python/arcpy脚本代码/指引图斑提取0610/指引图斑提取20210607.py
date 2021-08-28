# -*- coding: gbk -*-
import sys
import arcpy
import os

reload(sys)
sys.setdefaultencoding("utf-8")
arcpy.env.overwriteOutput = True
arcpy.env.XYResolution = "0.00001 Meters"
arcpy.env.XYTolerance = "0.0001 Meters"

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

def createGDBAndFeatureclass(out_pathc, gdb_name, templet, spatial_reference):
    arcpy.CreateFileGDB_management(out_pathc, gdb_name)
    outgdb_path = os.path.join(out_path, gdb_name)
    fc_name_list = [u"�˸�ũ�õ�Ǳ������ͼ��", u"�˸�δ���õ�Ǳ������ͼ��", u"�����õظ���Ǳ������ͼ��", u"�������ʸ���Ǳ������ͼ��"]
    for fcname in fc_name_list:
        arcpy.CreateFeatureclass_management(outgdb_path, fcname, "POLYGON", templet, "#", "#", spatial_reference)
    return outgdb_path

def selectFeatureClass(in_dltb, in_xztj, podu_path1, standard_gdb, out_gdb1):
    # """������������"""
    arcpy.AddMessage(u"     ������������")
    erasexz_result = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"���������������"))
    dltb_sel = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"DLTBɸѡ1"))
    where_clause1 = """DLBM LIKE '02%' OR DLBM LIKE '03%' OR DLBM in ('0401','0403','0404') OR 
    DLBM IN ('0102','0103','0601','0602','0702','1105','1106','1204','1206') OR ZZSXDM in ('JKHF','GCHF')"""
    arcpy.Select_analysis(in_dltb, dltb_sel, where_clause1)
    arcpy.Erase_analysis (dltb_sel, in_xztj, erasexz_result)

    # """�������ƾ����ɸѡ����"""
    #��δ���õ�
    wlyd_sel = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"WLYDɸѡ1"))
    arcpy.AddMessage(u"     ��ȡ�˸�δ���õ�Ǳ������ͼ��")
    where_clausewlyd = """DLBM IN ('0404', '1105', '1106', '1204', '1206') AND ZZSXDM NOT IN ('JKHF', 'GCHF')"""
    mul_to_sgl_wlyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"δ���õ�"))
    arcpy.Select_analysis(erasexz_result, wlyd_sel, where_clausewlyd)
    arcpy.MultipartToSinglepart_management(wlyd_sel, mul_to_sgl_wlyd)
    select_wlyd = aggregateAanalysisQ(mul_to_sgl_wlyd,"SUM_Shape_Area >= 3333.35",out_gdb1)

    #�˸�ũ�õ�
    arcpy.AddMessage(u"     ��ȡ�˸�ũ�õ�Ǳ������ͼ��")
    nyd_sel = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"NYDɸѡ1"))
    where_clausenyd = """(DLBM IN ('0201','0202','0203','0204','0301','0302','0303','0304','0305','0306','0307',
    '0401','0403') AND ZZSXDM NOT IN ('JKHF')) OR (DLBM NOT LIKE '%K%' AND ZZSXDM = 'GCHF')"""
    mul_to_sgl_nyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"ũ�õ�"))
    arcpy.Select_analysis(erasexz_result, nyd_sel, where_clausenyd)
    arcpy.MultipartToSinglepart_management(nyd_sel, mul_to_sgl_nyd)
    select_nyd = aggregateAanalysisQ(mul_to_sgl_nyd,"SUM_Shape_Area >= 3333.35",out_gdb1)

    #���ʸ���
    arcpy.AddMessage(u"     ��ȡ�������ʸ���Ǳ������ͼ��")
    tzgz_sel = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"TZGZɸѡ1"))
    where_clausetzgz = """(DLBM IN ('0102','0103','0201K','0202K','0203K','0204K','0301K','0302K','0307K','1104K')) 
    OR ZZSXDM = 'JKHF' """
    erase_result_tzgz = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"���ʸ������6_25���¶�"))
    mul_to_sgl_tzgz = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"���ʸ���"))
    podu_dy2j = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"PDJB����2�¶�ͼ"))
    arcpy.Select_analysis(podu_path1, podu_dy2j, "PDJB not in (\'1\',\'2\')")#F:\����Դ\�����¶�ͼ\450702������\450702������.shp
    arcpy.Select_analysis(erasexz_result, tzgz_sel, where_clausetzgz)
    arcpy.Erase_analysis(tzgz_sel, podu_dy2j, erase_result_tzgz, ".0001 Meters")
    arcpy.MultipartToSinglepart_management(erase_result_tzgz, mul_to_sgl_tzgz)
    select_tzgz = aggregateAanalysisQ(mul_to_sgl_tzgz,"SUM_Shape_Area >=33333.35",out_gdb1)

    #�����õظ���Ǳ������ͼ��
    arcpy.AddMessage(u"     ��ȡ�����õظ���Ǳ������ͼ��")
    jsyd_sel = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"JSYDɸѡ1"))
    where_clausejsyd = """DLBM  IN ('0601','0602','0702')"""
    erase_result_jsyd = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"���������ڽ����õ�"))
    all_jsyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"ȫ�������õ�"))
    merge_jsyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"�����õغϲ�"))
    mul_to_sgl_jsyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"�����õض�ת������"))
    select_jsyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"�����õ�"))
    arcpy.Select_analysis(erasexz_result, jsyd_sel, where_clausejsyd)
    arcpy.Select_analysis(in_dltb, all_jsyd, where_clausejsyd)
    arcpy.Erase_analysis(all_jsyd, jsyd_sel, erase_result_jsyd, ".0001 Meters")
    arcpy.AddField_management(erase_result_jsyd, "TBLX", "TEXT", "", "", "255", "ͼ������", "NULLABLE", "NON_REQUIRED", "")
    arcpy.CalculateField_management(erase_result_jsyd, "TBLX", "\"�˸���Ϊ����ũ�õ�\"", "VB", "")
    arcpy.Merge_management([erase_result_jsyd,jsyd_sel],merge_jsyd)
    arcpy.MultipartToSinglepart_management(merge_jsyd, mul_to_sgl_jsyd)
    arcpy.Select_analysis(mul_to_sgl_jsyd, select_jsyd, "Shape_Area >= 1")

    arcpy.env.workspace = standard_gdb
    fclist = arcpy.ListFeatureClasses()
    arcpy.AddMessage(u"   ")
    for fci in fclist:
        fci_path = os.path.join(standard_gdb,fci)
        if u"δ���õ�" in fci:
            arcpy.AddMessage(u"     ����ȡ���˸�δ���õ�Ǳ������ͼ��׷�ӵ���׼��")
            arcpy.RepairGeometry_management(select_wlyd)
            fieldmappings = arcpy.FieldMappings()
            fieldmappings.addTable(fci_path)
            fieldmappings.addTable(select_wlyd)

            fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("SDBSM"))
            fieldmap.addInputField(select_wlyd, "BSM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("SDBSM"), fieldmap)

            fieldmap1 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQDM"))
            fieldmap1.addInputField(select_wlyd, "ZLDWDM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQDM"), fieldmap1)

            fieldmap2 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQMC"))
            fieldmap2.addInputField(select_wlyd, "ZLDWMC")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQMC"), fieldmap2)

            arcpy.Append_management(select_wlyd, fci_path, "NO_TEST", fieldmappings)
            arcpy.CalculateField_management(fci_path, "GDHBZY", "\"�˸�δ���õ�Ǳ������ͼ��\"", "VB", "")

            del fieldmap
            del fieldmap1
            del fieldmap2
            del fieldmappings
        if u"ũ�õ�" in fci:
            arcpy.AddMessage(u"     ����ȡ���˸�ũ�õ�Ǳ������ͼ��׷�ӵ���׼��")
            arcpy.RepairGeometry_management(select_nyd)
            fieldmappings = arcpy.FieldMappings()
            fieldmappings.addTable(fci_path)
            fieldmappings.addTable(select_nyd)

            fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("SDBSM"))
            fieldmap.addInputField(select_nyd, "BSM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("SDBSM"), fieldmap)

            fieldmap1 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQDM"))
            fieldmap1.addInputField(select_nyd, "ZLDWDM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQDM"), fieldmap1)

            fieldmap2 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQMC"))
            fieldmap2.addInputField(select_nyd, "ZLDWMC")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQMC"), fieldmap2)

            arcpy.Append_management(select_nyd, fci_path, "NO_TEST", fieldmappings)
            arcpy.CalculateField_management(fci_path, "GDHBZY", "\"�˸�ũ�õ�Ǳ������ͼ��\"", "VB", "")

            del fieldmap
            del fieldmap1
            del fieldmap2
            del fieldmappings
        if u"���ʸ���" in fci:
            arcpy.AddMessage(u"     ����ȡ�ĸ������ʸ���Ǳ������ͼ��׷�ӵ���׼��")
            arcpy.RepairGeometry_management(select_tzgz)
            fieldmappings = arcpy.FieldMappings()
            fieldmappings.addTable(fci_path)
            fieldmappings.addTable(select_tzgz)

            fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("SDBSM"))
            fieldmap.addInputField(select_tzgz, "BSM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("SDBSM"), fieldmap)

            fieldmap1 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQDM"))
            fieldmap1.addInputField(select_tzgz, "ZLDWDM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQDM"), fieldmap1)

            fieldmap2 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQMC"))
            fieldmap2.addInputField(select_tzgz, "ZLDWMC")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQMC"), fieldmap2)

            arcpy.Append_management(select_tzgz, fci_path, "NO_TEST", fieldmappings)
            arcpy.CalculateField_management(fci_path, "GDHBZY", "\"�������ʸ���Ǳ������ͼ��\"", "VB", "")

            del fieldmap
            del fieldmap1
            del fieldmap2
            del fieldmappings
        if u"�����õ�" in fci:
            arcpy.AddMessage(u"     ����ȡ�Ľ����õظ���Ǳ������ͼ��׷�ӵ���׼��")
            arcpy.RepairGeometry_management(select_jsyd)
            fieldmappings = arcpy.FieldMappings()
            fieldmappings.addTable(fci_path)
            fieldmappings.addTable(select_jsyd)

            fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("SDBSM"))
            fieldmap.addInputField(select_jsyd, "BSM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("SDBSM"), fieldmap)

            fieldmap1 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQDM"))
            fieldmap1.addInputField(select_jsyd, "ZLDWDM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQDM"), fieldmap1)

            fieldmap2 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQMC"))
            fieldmap2.addInputField(select_jsyd, "ZLDWMC")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQMC"), fieldmap2)

            arcpy.Append_management(select_jsyd, fci_path, "NO_TEST", fieldmappings)
            arcpy.CalculateField_management(fci_path, "GDHBZY", "\"�����õظ���Ǳ������ͼ��\"", "VB", "")

            del fieldmap
            del fieldmap1
            del fieldmap2
            del fieldmappings

        arcpy.AddMessage("XDM��XMC��TBMJ��ֵ��TBLX��ע�ָ�����...")
        calculateValue(fci_path)

def calculateValue(fci_path):
    code_tblx = """ 
        dim AAA
        if [ZZSXMC] = "���ɻָ�" then
        AAA = "���ɻָ�/" & [TBLX]
        elseif [ZZSXMC] = "���ָ̻�" then
        AAA = "���ָ̻�/" & [TBLX]
        else
        AAA = [TBLX]
        end if """
    arcpy.CalculateField_management(fci_path, "TBLX", "AAA", "VB", code_tblx)
    arcpy.CalculateField_management(fci_path, "TBMJ", "round([Shape_Area],2)", "VB", "")
    arcpy.CalculateField_management(fci_path, "XDM", "Left([XZQDM],6)", "VB", "")
    expre_xmc = "ab(!XDM!)"
    code_xmc = """def ab(e):
        if (e == "450102"):
            return "������"
        elif (e == "450103"):
            return "������"
        elif (e == "450105"):
            return "������"
        elif (e == "450107"):
            return "��������"
        elif (e == "450108"):
            return "������"
        elif (e == "450109"):
            return "������"
        elif (e == "450110"):
            return "������"
        elif (e == "450123"):
            return "¡����"
        elif (e == "450124"):
            return "��ɽ��"
        elif (e == "450125"):
            return "������"
        elif (e == "450126"):
            return "������"
        elif (e == "450127"):
            return "����"
        elif (e == "4502"):
            return "������"
        elif (e == "450202"):
            return "������"
        elif (e == "450203"):
            return "�����"
        elif (e == "450204"):
            return "������"
        elif (e == "450205"):
            return "������"
        elif (e == "450206"):
            return "������"
        elif (e == "450222"):
            return "������"
        elif (e == "450223"):
            return "¹կ��"
        elif (e == "450224"):
            return "�ڰ���"
        elif (e == "450225"):
            return "��ˮ����������"
        elif (e == "450226"):
            return "��������������"
        elif (e == "4503"):
            return "������"
        elif (e == "450302"):
            return "�����"
        elif (e == "450303"):
            return "������"
        elif (e == "450304"):
            return "��ɽ��"
        elif (e == "450305"):
            return "������"
        elif (e == "450311"):
            return "��ɽ��"
        elif (e == "450312"):
            return "�ٹ���"
        elif (e == "450321"):
            return "��˷��"
        elif (e == "450323"):
            return "�鴨��"
        elif (e == "450324"):
            return "ȫ����"
        elif (e == "450325"):
            return "�˰���"
        elif (e == "450326"):
            return "������"
        elif (e == "450327"):
            return "������"
        elif (e == "450328"):
            return "��ʤ����������"
        elif (e == "450329"):
            return "��Դ��"
        elif (e == "450330"):
            return "ƽ����"
        elif (e == "450332"):
            return "��������������"
        elif (e == "450381"):
            return "������"
        elif (e == "4504"):
            return "������"
        elif (e == "450403"):
            return "������"
        elif (e == "450405"):
            return "������"
        elif (e == "450406"):
            return "������"
        elif (e == "450421"):
            return "������"
        elif (e == "450422"):
            return "����"
        elif (e == "450423"):
            return "��ɽ��"
        elif (e == "450481"):
            return "�Ϫ��"
        elif (e == "4505"):
            return "������"
        elif (e == "450502"):
            return "������"
        elif (e == "450503"):
            return "������"
        elif (e == "450512"):
            return "��ɽ����"
        elif (e == "450521"):
            return "������"
        elif (e == "4506"):
            return "���Ǹ���"
        elif (e == "450602"):
            return "�ۿ���"
        elif (e == "450603"):
            return "������"
        elif (e == "450621"):
            return "��˼��"
        elif (e == "450681"):
            return "������"
        elif (e == "4507"):
            return "������"
        elif (e == "450702"):
            return "������"
        elif (e == "450703"):
            return "�ձ���"
        elif (e == "450721"):
            return "��ɽ��"
        elif (e == "450722"):
            return "�ֱ���"
        elif (e == "4508"):
            return "�����"
        elif (e == "450802"):
            return "�۱���"
        elif (e == "450803"):
            return "������"
        elif (e == "450804"):
            return "������"
        elif (e == "450821"):
            return "ƽ����"
        elif (e == "450881"):
            return "��ƽ��"
        elif (e == "4509"):
            return "������"
        elif (e == "450902"):
            return "������"
        elif (e == "450903"):
            return "������"
        elif (e == "450921"):
            return "����"
        elif (e == "450922"):
            return "½����"
        elif (e == "450923"):
            return "������"
        elif (e == "450924"):
            return "��ҵ��"
        elif (e == "450981"):
            return "������"
        elif (e == "4510"):
            return "��ɫ��"
        elif (e == "451002"):
            return "�ҽ���"
        elif (e == "451003"):
            return "������"
        elif (e == "451022"):
            return "�ﶫ��"
        elif (e == "451082"):
            return "ƽ����"
        elif (e == "451024"):
            return "�±���"
        elif (e == "451026"):
            return "������"
        elif (e == "451027"):
            return "������"
        elif (e == "451028"):
            return "��ҵ��"
        elif (e == "451029"):
            return "������"
        elif (e == "451030"):
            return "������"
        elif (e == "451031"):
            return "¡�ָ���������"
        elif (e == "451081"):
            return "������"
        elif (e == "4511"):
            return "������"
        elif (e == "451102"):
            return "�˲���"
        elif (e == "451103"):
            return "ƽ����"
        elif (e == "451121"):
            return "��ƽ��"
        elif (e == "451122"):
            return "��ɽ��"
        elif (e == "451123"):
            return "��������������"
        elif (e == "4512"):
            return "�ӳ���"
        elif (e == "451202"):
            return "��ǽ���"
        elif (e == "451203"):
            return "������"
        elif (e == "451221"):
            return "�ϵ���"
        elif (e == "451222"):
            return "�����"
        elif (e == "451223"):
            return "��ɽ��"
        elif (e == "451224"):
            return "������"
        elif (e == "451225"):
            return "�޳�������������"
        elif (e == "451226"):
            return "����ë����������"
        elif (e == "451227"):
            return "��������������"
        elif (e == "451228"):
            return "��������������"
        elif (e == "451229"):
            return "������������"
        elif (e == "4513"):
            return "������"
        elif (e == "451302"):
            return "�˱���"
        elif (e == "451321"):
            return "�ó���"
        elif (e == "451322"):
            return "������"
        elif (e == "451323"):
            return "������"
        elif (e == "451324"):
            return "��������������"
        elif (e == "451381"):
            return "��ɽ��"
        elif (e == "4514"):
            return "������"
        elif (e == "451402"):
            return "������"
        elif (e == "451421"):
            return "������"
        elif (e == "451422"):
            return "������"
        elif (e == "451423"):
            return "������"
        elif (e == "451424"):
            return "������"
        elif (e == "451425"):
            return "�����"
        elif (e == "451481"):
            return "ƾ����" """
    arcpy.CalculateField_management(fci_path, "XMC", expre_xmc, "PYTHON_9.3", code_xmc)

def aggregateAanalysisQ(in_path2,where_clause2,out_gdb2):
    """�ۺϷ���"""

    fc = os.path.basename(in_path2)
    select_1 = os.path.join(out_gdb2,getNewFileNameQ(out_gdb2,  fc + u"ɸѡ����400"))
    buffer_result = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"������"))
    dissolve_result = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"�ںϽ��"))
    spatialJoin = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"�ռ�����"))
    spatialJoin_Statisti = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"����ͳ�Ʊ�"))
    tableSelect = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"ɸѡ��"))
    last_result = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"�ۺϽ��"))

    arcpy.Select_analysis(in_path2, select_1, "Shape_Area > 400")
    arcpy.Buffer_analysis(select_1, buffer_result, "50 Meters", "FULL", "ROUND", "NONE", "")
    arcpy.Dissolve_management(buffer_result, dissolve_result, "", "", "SINGLE_PART", "DISSOLVE_LINES")
    arcpy.AddField_management(dissolve_result, "BH", "LONG")
    arcpy.CalculateField_management(dissolve_result, "BH", "!OBJECTID!", "PYTHON_9.3")
    arcpy.SpatialJoin_analysis(select_1, dissolve_result, spatialJoin, "JOIN_ONE_TO_ONE", "KEEP_ALL", "#", "INTERSECT")
    arcpy.Statistics_analysis(spatialJoin, spatialJoin_Statisti, [["Shape_Area","SUM"]], "BH")
    arcpy.TableSelect_analysis(spatialJoin_Statisti, tableSelect, where_clause2)
    arcpy.JoinField_management(spatialJoin, "BH", tableSelect, "BH", "BH")
    arcpy.Select_analysis(spatialJoin, last_result, "BH = BH_1")

    return last_result

def main():
    temp_name = getNewFileNameQ(out_path, "temp.gdb")
    temp_gdb = os.path.join(out_path, temp_name)
    try:
        if out_gdbnameg[-4:] == ".gdb":
            namegdb = getNewFileNameQ(out_path, out_gdbnameg)
        else:
            namegdb = getNewFileNameQ(out_path, out_gdbnameg + ".gdb")

        arcpy.AddMessage(u"�½� " + temp_gdb + u" ���ڷŹ�������")
        arcpy.CreateFileGDB_management(out_path, temp_name)
        arcpy.AddMessage(u"�½���׼�⣺" + os.path.join(out_path, namegdb) + u" ��Ϊ������ȡ���")
        gdb_result = createGDBAndFeatureclass(out_path, namegdb, templetg, in_dltbg)
        arcpy.AddMessage(u"  ")
        arcpy.AddMessage(u"  ��ʼ��ȡͼ��...")
        selectFeatureClass(in_dltbg, in_XZTJg, in_pdg, gdb_result, temp_gdb)
        arcpy.AddMessage(u"  �����ȡ��")
        arcpy.AddMessage(u"  ")
    except Exception as e:
        arcpy.AddError(e.message)

    if arcpy.Exists(temp_gdb):
        try:
            arcpy.Delete_management(temp_gdb)
        except Exception as e:
            print e.message

if __name__ == "__main__":
    in_dltbg = arcpy.GetParameterAsText(0)#��������ͼ��
    in_XZTJg = arcpy.GetParameterAsText(1)#��������
    in_pdg = arcpy.GetParameterAsText(2)#�¶�
    templetg = arcpy.GetParameterAsText(3)#��׼��ģ��
    out_path = arcpy.GetParameterAsText(4)#���λ��
    out_gdbnameg = arcpy.GetParameterAsText(5)#gdb����

    main()


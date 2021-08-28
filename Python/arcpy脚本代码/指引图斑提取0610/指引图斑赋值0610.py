# -*- coding: gbk -*-
import sys
import arcpy
import os
import time

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

def getNewFieldName(fcp,field_name):
    field_name_list = [field.name for field in arcpy.ListFields(fcp)]
    n = [1]
    def get_new_name(field_name_in):
        new_name = field_name_in
        if new_name in field_name_list:
            new_name = field_name_in + str(n[0])
            n[0] += 1
            if new_name in field_name_list:
                new_name = get_new_name(field_name_in)
        return new_name
    return get_new_name(field_name)

def checkFieldExistOrNot(fcp,field_name):
    field_name_list = [field.name for field in arcpy.ListFields(fcp)]
    if field_name in field_name_list:
        return True
    else:
        return False

def  spaceCalculateMaxValue(inputs_layer,put_field,consult_layer,get_field,temp_gdb):
    """"""
    sec_stamp = str(int(time.time()))
    intersect = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"In" + sec_stamp))
    select1 = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"Se" + sec_stamp))
    dissolve_features = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"MDi" + sec_stamp))
    statistics_table1 = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"MT1_" + sec_stamp))
    st2name = getNewFileNameQ(temp_gdb,"MT2_" + sec_stamp)
    statistics_table2 = os.path.join(temp_gdb,st2name)
    statistics_table3 = os.path.join(temp_gdb, getNewFileNameQ(temp_gdb,"MT3_" + sec_stamp))
    in_objectid = getNewFieldName(inputs_layer,"MID")

    arcpy.Select_analysis(consult_layer, select1)

    get_vle_field = getNewFieldName(select1, "MVLE")
    try:
        # Process: inputs_layer add "groupID" field
        arcpy.AddField_management(inputs_layer, in_objectid, "LONG")
        arcpy.CalculateField_management(inputs_layer, in_objectid, '!OBJECTID!', "PYTHON_9.3")

        # Process: consult_layer add "getVALUE" field
        arcpy.AddField_management(select1, get_vle_field, "TEXT", "#", "#", 250)
        arcpy.CalculateField_management(select1, get_vle_field, "!" + get_field + "!", "PYTHON_9.3")
        # Process: intersect
        arcpy.AddMessage("  �ཻ...")
        arcpy.Intersect_analysis([inputs_layer, select1], intersect, "ALL", ".0001 Meters", "INPUT")

        # Process: Statistics_analysis
        arcpy.AddMessage("  �ں�...")
        arcpy.Dissolve_management(intersect, dissolve_features, [in_objectid, get_vle_field], "", "SINGLE_PART", "DISSOLVE_LINES")
        arcpy.Statistics_analysis(dissolve_features, statistics_table1, [["Shape_Area", "SUM"]], [in_objectid, get_vle_field])
        arcpy.Statistics_analysis(statistics_table1, statistics_table2, [["SUM_Shape_Area", "MAX"]], in_objectid)
        # Process: join field 1
        arcpy.AddMessage("  �����ֶ�...")
        arcpy.JoinField_management(statistics_table1, in_objectid, statistics_table2, in_objectid, [in_objectid,"MAX_SUM_Shape_Area"])
        wc = "\"" + in_objectid + "\" = \"" + in_objectid + "_1\" AND \"SUM_Shape_Area\" = \"MAX_SUM_Shape_Area\""
        arcpy.TableSelect_analysis(statistics_table1,statistics_table3,wc)
        arcpy.JoinField_management(inputs_layer, 'OBJECTID', statistics_table3, in_objectid, get_vle_field)
        arcpy.AddMessage("  " + put_field + " ��ֵ...")
        arcpy.CalculateField_management(inputs_layer, put_field, "!" + get_vle_field + "!", "PYTHON_9.3", "")

    except Exception as e:
        arcpy.AddError(e.message)
    finally:
        if checkFieldExistOrNot(inputs_layer,in_objectid):
            try:
                arcpy.DeleteField_management(inputs_layer, in_objectid)
            except Exception as e:
                arcpy.AddError(e.message)
        if checkFieldExistOrNot(inputs_layer,get_vle_field):
            try:
                arcpy.DeleteField_management(inputs_layer, get_vle_field)
            except Exception as e:
                arcpy.AddError(e.message)

def  spaceCalculateGGSYValue(input_fc,put_feild,consult_fc,temp_gdb):
    """"""
    sec_stamp = str(int(time.time()))
    intersect = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"Gin" + sec_stamp))
    stname = getNewFileNameQ(temp_gdb,"Gt" + sec_stamp)
    statistics_table1 = os.path.join(temp_gdb,stname)

    objectid = getNewFieldName(input_fc,"GID")
    try:
        arcpy.AddField_management(input_fc, objectid, "LONG")
        arcpy.CalculateField_management(input_fc, objectid, '!OBJECTID!', "PYTHON_9.3")

        arcpy.AddMessage("  �ཻ...")
        arcpy.Intersect_analysis([input_fc, consult_fc], intersect, "ALL", ".0001 Meters", "INPUT")

        arcpy.AddMessage("  �����ֶ�...")
        arcpy.Statistics_analysis(intersect, statistics_table1, [["Shape_Area", "SUM"]], objectid)
        arcpy.JoinField_management(input_fc, 'OBJECTID', statistics_table1, objectid, "SUM_Shape_Area")
        expression = "CaGGSY(!SUM_Shape_Area!)"
        codeblock = """def CaGGSY(a):
            if a>0:
                return "��"
            else:
                return "��" """
        arcpy.AddMessage("  ��ֵ...")
        arcpy.CalculateField_management(input_fc, put_feild, expression, "PYTHON_9.3", codeblock)

    except Exception as e:
        arcpy.AddError(e.message)
    finally:
        if checkFieldExistOrNot(input_fc,objectid):
            try:
                arcpy.DeleteField_management(input_fc, objectid)
            except Exception as e:
                arcpy.AddError(e.message)
        if checkFieldExistOrNot(input_fc,"SUM_Shape_Area"):
            try:
                arcpy.DeleteField_management(input_fc, "SUM_Shape_Area")
            except Exception as e:
                arcpy.AddError(e.message)

def  spaceCalculateTBLXValue(input_fc,put_feild,consult_fc,txt_value,temp_gdb):
    """"""
    sec_stamp = str(int(time.time()))
    erase1 = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"Er" + sec_stamp))
    stname = getNewFileNameQ(temp_gdb,"Tt" + sec_stamp)
    statistics_table1 = os.path.join(temp_gdb,stname)

    objectid = getNewFieldName(input_fc,"TID")
    mjzb_field = getNewFieldName(input_fc,"Tmjzb")
    try:
        arcpy.AddField_management(input_fc, objectid, "LONG")
        arcpy.AddField_management(input_fc, mjzb_field, "DOUBLE")
        arcpy.CalculateField_management(input_fc, objectid, '!OBJECTID!', "PYTHON_9.3")

        arcpy.AddMessage("  ����...")
        arcpy.Erase_analysis(input_fc, consult_fc, erase1, ".0001 Meters")
        arcpy.AddMessage("  ����ͳ��...")
        arcpy.Statistics_analysis(erase1, statistics_table1, [["Shape_Area", "SUM"]], objectid)
        arcpy.AddMessage("  �����ֶ�...")
        arcpy.JoinField_management(input_fc, 'OBJECTID', statistics_table1, objectid, "SUM_Shape_Area")

        arcpy.AddMessage("  ��ֵ...")
        exprcode = "ZBmj(!SUM_Shape_Area!,!shape.area@meters!)"
        codezb = """def ZBmj(a, b):
            if a == None:
                return 100
            else:
                return 100 - round(a / b, 4) * 100 """
        arcpy.CalculateField_management(input_fc, mjzb_field, exprcode, "PYTHON_9.3",codezb)

        expression = "CaTBLX(!" + mjzb_field + "!,!" + put_feild + "!,\"" + txt_value + "\")"
        codeblock = """def CaTBLX(a,b,c):
            if (a>0.0001) and (a<100):
                if b == None:
                    return str(a) + "%" + c
                else:
                    return str(a) + "%" + c + "/" + b
            elif (a>=100):
                if b == None:
                    return "100%" + c
                else:
                    return "100%" + c + "/" + b
            else:
                return b """
        arcpy.CalculateField_management(input_fc, put_feild, expression, "PYTHON_9.3", codeblock)

    except Exception as e:
        arcpy.AddError(e.message)
    finally:
        if checkFieldExistOrNot(input_fc,objectid):
            try:
                arcpy.DeleteField_management(input_fc, objectid)
            except Exception as e:
                arcpy.AddError(e.message)
        if checkFieldExistOrNot(input_fc,mjzb_field):
            try:
                arcpy.DeleteField_management(input_fc, mjzb_field)
            except Exception as e:
                arcpy.AddError(e.message)
        if checkFieldExistOrNot(input_fc,"SUM_Shape_Area"):
            try:
                arcpy.DeleteField_management(input_fc, "SUM_Shape_Area")
            except Exception as e:
                arcpy.AddError(e.message)

def calculateValue(fci_path):
    # code_dcbh = """
    #     Dim calculatedcbh
    #     IF Len([OBJECTID]) = 1 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "000000" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 2 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "00000" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 3 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "0000" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 4 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "000" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 5 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "00" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 6 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "0" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 7 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & [OBJECTID]
    #     END IF"""
    # arcpy.CalculateField_management(fci_path, "DCBH", "calculatedcbh", "VB", code_dcbh)
    arcpy.CalculateField_management(fci_path, "DCBH", "!XZQDM![0:12] + \'{:0>7d}\'.format(!OBJECTID!)", "PYTHON_9.3")

    # code_tblx = """
    #     dim AAA
    #     if [ZZSXMC] = "���ɻָ�" then
    #     AAA = "���ɻָ�/" & [TBLX]
    #     elseif [ZZSXMC] = "���ָ̻�" then
    #     AAA = "���ָ̻�/" & [TBLX]
    #     else
    #     AAA = [TBLX]
    #     end if """
    # arcpy.CalculateField_management(fci_path, "TBLX", "AAA", "VB", code_tblx)
    # arcpy.CalculateField_management(fci_path, "TBMJ", "round( [Shape_Area] ,2)", "VB", "")
    # arcpy.CalculateField_management(fci_path, "XDM", "Left( [XZQDM],6 )", "VB", "")
    # expre_xmc = "ab(!XDM!)"
    # code_xmc = """def ab(e):
    #     if (e == "450102"):
    #         return "������"
    #     elif (e == "450103"):
    #         return "������"
    #     elif (e == "450105"):
    #         return "������"
    #     elif (e == "450107"):
    #         return "��������"
    #     elif (e == "450108"):
    #         return "������"
    #     elif (e == "450109"):
    #         return "������"
    #     elif (e == "450110"):
    #         return "������"
    #     elif (e == "450123"):
    #         return "¡����"
    #     elif (e == "450124"):
    #         return "��ɽ��"
    #     elif (e == "450125"):
    #         return "������"
    #     elif (e == "450126"):
    #         return "������"
    #     elif (e == "450127"):
    #         return "����"
    #     elif (e == "4502"):
    #         return "������"
    #     elif (e == "450202"):
    #         return "������"
    #     elif (e == "450203"):
    #         return "�����"
    #     elif (e == "450204"):
    #         return "������"
    #     elif (e == "450205"):
    #         return "������"
    #     elif (e == "450206"):
    #         return "������"
    #     elif (e == "450222"):
    #         return "������"
    #     elif (e == "450223"):
    #         return "¹կ��"
    #     elif (e == "450224"):
    #         return "�ڰ���"
    #     elif (e == "450225"):
    #         return "��ˮ����������"
    #     elif (e == "450226"):
    #         return "��������������"
    #     elif (e == "4503"):
    #         return "������"
    #     elif (e == "450302"):
    #         return "�����"
    #     elif (e == "450303"):
    #         return "������"
    #     elif (e == "450304"):
    #         return "��ɽ��"
    #     elif (e == "450305"):
    #         return "������"
    #     elif (e == "450311"):
    #         return "��ɽ��"
    #     elif (e == "450312"):
    #         return "�ٹ���"
    #     elif (e == "450321"):
    #         return "��˷��"
    #     elif (e == "450323"):
    #         return "�鴨��"
    #     elif (e == "450324"):
    #         return "ȫ����"
    #     elif (e == "450325"):
    #         return "�˰���"
    #     elif (e == "450326"):
    #         return "������"
    #     elif (e == "450327"):
    #         return "������"
    #     elif (e == "450328"):
    #         return "��ʤ����������"
    #     elif (e == "450329"):
    #         return "��Դ��"
    #     elif (e == "450330"):
    #         return "ƽ����"
    #     elif (e == "450332"):
    #         return "��������������"
    #     elif (e == "450381"):
    #         return "������"
    #     elif (e == "4504"):
    #         return "������"
    #     elif (e == "450403"):
    #         return "������"
    #     elif (e == "450405"):
    #         return "������"
    #     elif (e == "450406"):
    #         return "������"
    #     elif (e == "450421"):
    #         return "������"
    #     elif (e == "450422"):
    #         return "����"
    #     elif (e == "450423"):
    #         return "��ɽ��"
    #     elif (e == "450481"):
    #         return "�Ϫ��"
    #     elif (e == "4505"):
    #         return "������"
    #     elif (e == "450502"):
    #         return "������"
    #     elif (e == "450503"):
    #         return "������"
    #     elif (e == "450512"):
    #         return "��ɽ����"
    #     elif (e == "450521"):
    #         return "������"
    #     elif (e == "4506"):
    #         return "���Ǹ���"
    #     elif (e == "450602"):
    #         return "�ۿ���"
    #     elif (e == "450603"):
    #         return "������"
    #     elif (e == "450621"):
    #         return "��˼��"
    #     elif (e == "450681"):
    #         return "������"
    #     elif (e == "4507"):
    #         return "������"
    #     elif (e == "450702"):
    #         return "������"
    #     elif (e == "450703"):
    #         return "�ձ���"
    #     elif (e == "450721"):
    #         return "��ɽ��"
    #     elif (e == "450722"):
    #         return "�ֱ���"
    #     elif (e == "4508"):
    #         return "�����"
    #     elif (e == "450802"):
    #         return "�۱���"
    #     elif (e == "450803"):
    #         return "������"
    #     elif (e == "450804"):
    #         return "������"
    #     elif (e == "450821"):
    #         return "ƽ����"
    #     elif (e == "450881"):
    #         return "��ƽ��"
    #     elif (e == "4509"):
    #         return "������"
    #     elif (e == "450902"):
    #         return "������"
    #     elif (e == "450903"):
    #         return "������"
    #     elif (e == "450921"):
    #         return "����"
    #     elif (e == "450922"):
    #         return "½����"
    #     elif (e == "450923"):
    #         return "������"
    #     elif (e == "450924"):
    #         return "��ҵ��"
    #     elif (e == "450981"):
    #         return "������"
    #     elif (e == "4510"):
    #         return "��ɫ��"
    #     elif (e == "451002"):
    #         return "�ҽ���"
    #     elif (e == "451003"):
    #         return "������"
    #     elif (e == "451022"):
    #         return "�ﶫ��"
    #     elif (e == "451082"):
    #         return "ƽ����"
    #     elif (e == "451024"):
    #         return "�±���"
    #     elif (e == "451026"):
    #         return "������"
    #     elif (e == "451027"):
    #         return "������"
    #     elif (e == "451028"):
    #         return "��ҵ��"
    #     elif (e == "451029"):
    #         return "������"
    #     elif (e == "451030"):
    #         return "������"
    #     elif (e == "451031"):
    #         return "¡�ָ���������"
    #     elif (e == "451081"):
    #         return "������"
    #     elif (e == "4511"):
    #         return "������"
    #     elif (e == "451102"):
    #         return "�˲���"
    #     elif (e == "451103"):
    #         return "ƽ����"
    #     elif (e == "451121"):
    #         return "��ƽ��"
    #     elif (e == "451122"):
    #         return "��ɽ��"
    #     elif (e == "451123"):
    #         return "��������������"
    #     elif (e == "4512"):
    #         return "�ӳ���"
    #     elif (e == "451202"):
    #         return "��ǽ���"
    #     elif (e == "451203"):
    #         return "������"
    #     elif (e == "451221"):
    #         return "�ϵ���"
    #     elif (e == "451222"):
    #         return "�����"
    #     elif (e == "451223"):
    #         return "��ɽ��"
    #     elif (e == "451224"):
    #         return "������"
    #     elif (e == "451225"):
    #         return "�޳�������������"
    #     elif (e == "451226"):
    #         return "����ë����������"
    #     elif (e == "451227"):
    #         return "��������������"
    #     elif (e == "451228"):
    #         return "��������������"
    #     elif (e == "451229"):
    #         return "������������"
    #     elif (e == "4513"):
    #         return "������"
    #     elif (e == "451302"):
    #         return "�˱���"
    #     elif (e == "451321"):
    #         return "�ó���"
    #     elif (e == "451322"):
    #         return "������"
    #     elif (e == "451323"):
    #         return "������"
    #     elif (e == "451324"):
    #         return "��������������"
    #     elif (e == "451381"):
    #         return "��ɽ��"
    #     elif (e == "4514"):
    #         return "������"
    #     elif (e == "451402"):
    #         return "������"
    #     elif (e == "451421"):
    #         return "������"
    #     elif (e == "451422"):
    #         return "������"
    #     elif (e == "451423"):
    #         return "������"
    #     elif (e == "451424"):
    #         return "������"
    #     elif (e == "451425"):
    #         return "�����"
    #     elif (e == "451481"):
    #         return "ƾ����" """
    # arcpy.CalculateField_management(fci_path, "XMC", expre_xmc, "PYTHON_9.3", code_xmc)

def main():
    """"""
    temp_name = getNewFileNameQ(out_path, "temp.gdb")
    temp_gdb1 = os.path.join(out_path, temp_name)
    arcpy.AddMessage(u"�½� " + temp_gdb1 + u" ���ڷŹ�������")
    arcpy.CreateFileGDB_management(out_path, temp_name)
    merge_path = os.path.join(temp_gdb1, getNewFileNameQ(temp_gdb1, u"�ϲ�"))

    arcpy.env.workspace = in_gdb
    fclist = arcpy.ListFeatureClasses()
    arcpy.AddMessage("�ϲ�...")
    arcpy.Merge_management(fclist, merge_path)

    # arcpy.AddMessage("XDM��XMC��TBMJ��ֵ��TBLX��ע�ָ�����...")
    # arcpy.AddMessage("DCBH��ֵ...")
    # calculateValue(merge_path)
    arcpy.AddMessage("���¶ȼ���PDJB��...")
    spaceCalculateMaxValue(merge_path,"PDJB",podutu,"PDJB",temp_gdb1)
    arcpy.AddMessage("���������ͣ�TRLX��...")
    spaceCalculateMaxValue(merge_path,"TRLX",turangtu,"����",temp_gdb1)
    arcpy.AddMessage("�����ˮԴ��GGSY��...")
    spaceCalculateGGSYValue(merge_path, "GGSY", shuiyuantiaojian,temp_gdb1)
    arcpy.AddMessage("TBLX��ע\"��ʵʩ��������\"...")
    spaceCalculateTBLXValue(merge_path, "TBLX", tudizhengzhi, "��ʵʩ��������",temp_gdb1)

    res_name = getNewFileNameQ(out_path, os.path.basename(in_gdb))
    arcpy.AddMessage(u"�½� " + res_name + u" ��Ϊ���ո�ֵ���")
    rs_gdb1 = os.path.join(out_path, res_name)
    arcpy.CreateFileGDB_management(out_path, res_name)

    arcpy.AddMessage("ɸѡ �˸�ũ�õ�Ǳ������ͼ��")
    nyd_path = os.path.join(rs_gdb1, "�˸�ũ�õ�Ǳ������ͼ��")
    arcpy.Select_analysis(merge_path, nyd_path, "GDHBZY LIKE \'%�˸�ũ�õ�Ǳ������ͼ��%\'")

    arcpy.AddMessage("ɸѡ �������ʸ���Ǳ������ͼ��")
    tzgz_path = os.path.join(rs_gdb1, "�������ʸ���Ǳ������ͼ��")
    arcpy.Select_analysis(merge_path, tzgz_path, "GDHBZY LIKE \'%�������ʸ���Ǳ������ͼ��%\'")

    arcpy.AddMessage("ɸѡ �����õظ���Ǳ������ͼ��")
    jsyd_path = os.path.join(rs_gdb1, "�����õظ���Ǳ������ͼ��")
    arcpy.Select_analysis(merge_path, jsyd_path, "GDHBZY LIKE \'%�����õظ���Ǳ������ͼ��%\'")

    arcpy.AddMessage("ɸѡ �˸�δ���õ�Ǳ������ͼ��")
    wlyd_path = os.path.join(rs_gdb1, "�˸�δ���õ�Ǳ������ͼ��")
    arcpy.Select_analysis(merge_path, wlyd_path, "GDHBZY LIKE \'%�˸�δ���õ�Ǳ������ͼ��%\'")

    if arcpy.Exists(jsyd_path) and int(arcpy.GetCount_management(jsyd_path).getOutput(0)) > 0:
        arcpy.AddMessage("�����õظ���Ǳ������ͼ�ߣ�TBLX��ע\"��ʵʩ�����ҹ�\"...")
        spaceCalculateTBLXValue(jsyd_path, "TBLX", zengjiangua, "��ʵʩ�����ҹ�", temp_gdb1)
    if arcpy.Exists(wlyd_path) and int(arcpy.GetCount_management(wlyd_path).getOutput(0)) > 0:
        arcpy.AddMessage("�˸�δ���õ�Ǳ������ͼ�ߣ�TBLX��ע\"����ũ�ﷶΧ�ڵ�δ���õ�\"...")
        spaceCalculateTBLXValue(wlyd_path, "TBLX", jibennongtian, "����ũ�ﷶΧ�ڵ�δ���õ�", temp_gdb1)

    if arcpy.Exists(temp_gdb1):
        try:
            arcpy.Delete_management(temp_gdb1)
        except Exception as e:
            arcpy.AddMessage(e.message)
            arcpy.AddMessage("...")

if __name__ == "__main__":
    in_gdb = arcpy.GetParameterAsText(0)#ָ��ͼ��gdb
    podutu = arcpy.GetParameterAsText(1)#�¶�ͼ
    turangtu = arcpy.GetParameterAsText(2)#����ͼ
    shuiyuantiaojian = arcpy.GetParameterAsText(3)#ˮԴ����
    tudizhengzhi = arcpy.GetParameterAsText(4)#��ʵʩ����������Ŀ

    zengjiangua = arcpy.GetParameterAsText(5)#�����ҹ�����
    jibennongtian = arcpy.GetParameterAsText(6)#����ũ�ﱣ����

    out_path = arcpy.GetParameterAsText(7)

    main()

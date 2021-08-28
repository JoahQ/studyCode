# -*- coding: gbk -*-
import os
import arcpy
import sys
import time
sys.path.append(os.path.dirname(__file__))
import xlwt
arcpy.AddMessage(sys.getdefaultencoding())
reload(sys)
sys.setdefaultencoding('utf-8')
arcpy.AddMessage(sys.getdefaultencoding())
arcpy.env.overwriteOutput = True
arcpy.env.XYResolution = "0.0001 Meters"
arcpy.env.XYTolerance = "0.001 Meters"

HCJG_FEILD_NAME = 'RJHCJG'
HCJG_FEILD_ALIAS = u"����˲���"

CWMS_FEILD_NAME = 'RJHCSM'
CWMS_FEILD_ALIAS = u"����˲�˵��"

MBTC_FEILD_NAME = 'RJMBTC'
MBTC_FEILD_ALIAS = u"Ŀ��ͼ��"

# SX_WHERE_CLAUSE = """XZQDM <> XZQDM_1 OR XZQMC <> XZQMC_1 OR QSXZ <> QSXZ_1 OR DLBM <> DLBM_1 OR DLMC <> DLMC_1 OR
# ZZSXMC <> ZZSXMC_1 OR TBXHMC <> TBXHMC_1 OR SDBSM <> SDBSM_1"""

SX_WHERE_CLAUSE = """(QSXZ IS NULL AND QSXZ_1 IS NOT NULL AND QSXZ_1 <> ' ') OR
(ZZSXMC IS NULL AND ZZSXMC_1 IS NOT NULL AND ZZSXMC_1 <> ' ') OR
(DLBM IS NULL AND DLBM_1 IS NOT NULL AND DLBM_1 <> ' ') OR
(DLMC IS NULL AND DLMC_1 IS NOT NULL AND DLMC_1 <> ' ') OR
(TBXHMC IS NULL AND TBXHMC_1 IS NOT NULL AND TBXHMC_1 <> ' ') OR
(GDLX IS NULL AND GDLX_1 IS NOT NULL AND GDLX_1 <> ' ') OR
(XZQDM IS NULL AND XZQDM_1 IS NOT NULL AND XZQDM_1 <> ' ') OR
(XZQMC IS NULL AND XZQMC_1 IS NOT NULL AND XZQMC_1 <> ' ') OR
QSXZ <> QSXZ_1 OR DLBM <> DLBM_1 OR DLMC <> DLMC_1 OR ZZSXMC <> ZZSXMC_1 OR TBXHMC <> TBXHMC_1 OR GDLX <> GDLX_1 OR
XZQDM <> XZQDM_1 OR XZQMC <> XZQMC_1"""
SX_FIELD_LIST = [['QSXZ', '(QSXZ IS NULL AND QSXZ_1 IS NOT NULL AND QSXZ_1 <> \' \') OR QSXZ <> QSXZ_1'],
                 ['DLBM', '(DLBM IS NULL AND DLBM_1 IS NOT NULL AND DLBM_1 <> \' \') OR DLBM <> DLBM_1'],
                 ['DLMC', '(DLMC IS NULL AND DLMC_1 IS NOT NULL AND DLMC_1 <> \' \') OR DLMC <> DLMC_1'],
                 ['GDLX', '(GDLX IS NULL AND GDLX_1 IS NOT NULL AND GDLX_1 <> \' \') OR GDLX <> GDLX_1'],
                 ['ZZSXMC', '(ZZSXMC IS NULL AND ZZSXMC_1 IS NOT NULL AND ZZSXMC_1 <> \' \') OR ZZSXMC <> ZZSXMC_1'],
                 ['XZQDM', '(XZQDM IS NULL AND XZQDM_1 IS NOT NULL AND XZQDM_1 <> \' \') OR XZQDM <> XZQDM_1'],
                 ['XZQMC', '(XZQMC IS NULL AND XZQMC_1 IS NOT NULL AND XZQMC_1 <> \' \') OR XZQMC <> XZQMC_1'],
                 ['TBXHMC', '(TBXHMC IS NULL AND TBXHMC_1 IS NOT NULL AND TBXHMC_1 <> \' \') OR TBXHMC <> TBXHMC_1']]
# CHECK_FIELD_LIST = ['QSXZ', 'DLBM', 'DLMC','GDLX', 'ZZSXMC', 'TBXHMC', 'TBLX']
CHECK_FIELD_LIST = ['XZQDM', 'XZQMC', 'QSXZ', 'DLBM', 'DLMC','GDLX', 'ZZSXMC', 'TBXHMC', 'TBLX']
def checkSDFieldsExistQ(fc_pathsd):
    field_list = arcpy.ListFields(fc_pathsd)
    field_name_list = [field.name for field in field_list]
    not_exist_list = []
    for sd_field in CHECK_FIELD_LIST:
        if sd_field not in field_name_list:
            not_exist_list.append(sd_field)
    return not_exist_list

def addThreeFieldsQ(fc_path1):
    check_field_lst = []
    try:
        fc_fields_list = arcpy.ListFields(fc_path1)
        for field in fc_fields_list:
            check_field_lst.append(field.name)
        if MBTC_FEILD_NAME not in check_field_lst:
            arcpy.AddField_management(fc_path1, MBTC_FEILD_NAME, 'TEXT', "#", "#", 255, MBTC_FEILD_ALIAS)
        if HCJG_FEILD_NAME not in check_field_lst:
            arcpy.AddField_management(fc_path1, HCJG_FEILD_NAME, 'TEXT', "#", "#", 255, HCJG_FEILD_ALIAS)
        if CWMS_FEILD_NAME not in check_field_lst:
            arcpy.AddField_management(fc_path1, CWMS_FEILD_NAME, 'TEXT', "#", "#", 255, CWMS_FEILD_ALIAS)
    except Exception as e11:
        arcpy.AddError(e11.message)

def chackMultipartNewQ(in_list1, out_gdb1):
    arcpy.AddMessage("����ִ�и���ͼ�μ��...")
    layer_count = 0
    mpart_count_field = "MpartCount" + str(int(time.time()))
    for in_fc_path in in_list1:
        layer_count += 1
        fc = os.path.basename(in_fc_path)
        result_fc_name = getNewFileNameQ(out_gdb1, fc + "_����ͼ�μ����")
        try:
            arcpy.AddMessage("  ")
            arcpy.AddMessage("  (" + str(layer_count) + ")" + fc + " ����ͼ�μ��...")
            arcpy.AddField_management(in_fc_path, mpart_count_field, 'LONG')
            arcpy.CalculateField_management(in_fc_path, mpart_count_field, "!shape.PartCount!", "PYTHON_9.3")
            arcpy.FeatureClassToFeatureClass_conversion(in_fc_path, out_gdb1, result_fc_name, mpart_count_field + " > 1")

            result_fc_path = os.path.join(out_gdb1, result_fc_name)
            addThreeFieldsQ(result_fc_path)
            if int(arcpy.GetCount_management(result_fc_path).getOutput(0)) > 0:

                arcpy.CalculateField_management(result_fc_path, MBTC_FEILD_NAME, "'" + fc + "'", "PYTHON_9.3", "")
                arcpy.CalculateField_management(result_fc_path, HCJG_FEILD_NAME, "'����ͼ��'", "PYTHON_9.3", "")
                arcpy.CalculateField_management(result_fc_path, CWMS_FEILD_NAME, "'����ͼ��'", "PYTHON_9.3", "")
                arcpy.DeleteField_management(result_fc_path, mpart_count_field)
            else:
                arcpy.AddMessage("     " + fc + "ͼ��û�и���ͼ�Σ���")
                arcpy.Delete_management(result_fc_path)
        except Exception as ein:
            arcpy.AddMessage("                      ")
            arcpy.AddError("    " + fc + " ����ͼ�μ��ʧ�ܣ�")
            arcpy.AddError("*" * 20)
            arcpy.AddError(ein.message)
            arcpy.AddError("*" * 20)

        finally:
            try:
                arcpy.DeleteField_management(in_fc_path, mpart_count_field)
            except Exception as ed:
                arcpy.AddError(ed.message)
    arcpy.AddMessage("  ")
    arcpy.AddMessage("����ͼ�μ��ִ�н���!")
    arcpy.AddMessage("  ")

def checkFeatureAreaNewQ(in_fc_list2, temp_dataset2, original_list2, out_gdb2):
    arcpy.AddMessage("ʸ��������ָ��ͼ�߶Աȼ��...")
    for fc_pathtx in in_fc_list2:
        no_exist_list1 = checkSDFieldsExistQ(fc_pathtx)
        if len(no_exist_list1) > 0:
            arcpy.AddError("*ʸ��������ָ��ͼ�߶Աȼ��ʧ�ܣ�����")
            arcpy.AddError("*" * 20)
            arcpy.AddError("      ʸ�����ݣ�" + fc_pathtx + " ͼ��ȱ�� [" + "; ".join(no_exist_list1) + "] �ֶ�")
            arcpy.AddError("*" * 20)
            return 0
    for fc_lsorpath in original_list2:
        no_exist_list2 = checkSDFieldsExistQ(fc_lsorpath)
        if len(no_exist_list2) > 0:
            arcpy.AddError("*ʸ��������ָ��ͼ�߶Աȼ��ʧ�ܣ�����")
            arcpy.AddError("*" * 20)
            arcpy.AddError("      ָ��ͼ�����ݣ�" + fc_lsorpath + " ͼ��ȱ�� [" + "; ".join(no_exist_list2) + "] �ֶ�")
            arcpy.AddError("*" * 20)
            return 0

    layer_count = 0
    for fc_inpathtx in in_fc_list2:
        fc = os.path.basename(fc_inpathtx)
        layer_count += 1
        arcpy.AddMessage("             ")
        arcpy.AddMessage("  (" + str(layer_count) + ")" + fc)
        yzytbxj_path = os.path.join(temp_dataset2, getNewFileNameQ(temp_dataset2, fc + "_yzytbxj"))
        last_result_path = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"_�Աȼ����"))
        try:
            if "������ȡ" in fc or u"������ȡ" in fc:
                arcpy.AddMessage(u"      ��� " + fc + u" ͼ���Ƿ����������·�ָ��ͼ���ص�...")
                zhiyinMeger_path = os.path.join(temp_dataset2, getNewFileNameQ(temp_dataset2, "ָ��ͼ��_meger"))
                arcpy.Merge_management(original_list2, zhiyinMeger_path)

                arcpy.Intersect_analysis([fc_inpathtx, zhiyinMeger_path], last_result_path, "NO_FID", "0.001 Meters", "INPUT")
                addThreeFieldsQ(last_result_path)
                ex_str = "'���·���ָ��ͼ��֮һ�ص�'"
                arcpy.CalculateField_management(last_result_path, CWMS_FEILD_NAME, ex_str, "PYTHON_9.3")
                arcpy.CalculateField_management(last_result_path, MBTC_FEILD_NAME, "'" + fc + "'", "PYTHON_9.3")
                arcpy.CalculateField_management(last_result_path, HCJG_FEILD_NAME, "'����ͼ��'", "PYTHON_9.3")
            else:
                guide_fc_path = ""
                for i in range(len(original_list2)):
                    if fc == os.path.basename(original_list2[i]):
                        guide_fc_path = original_list2[i]
                if arcpy.Exists(guide_fc_path):
                    arcpy.AddMessage(u"      1.��� " + fc + u" ͼ��ɹ��������·�ָ��ͼ�ߵ������Ƿ�һ��...")
                    sx_result_name = getNewFileNameQ(temp_dataset2, fc + "sx_result")
                    sx_result_path = os.path.join(temp_dataset2, sx_result_name)
                    arcpy.Intersect_analysis([fc_inpathtx, guide_fc_path], yzytbxj_path, "NO_FID", "0.001 Meters", "INPUT")
                    arcpy.FeatureClassToFeatureClass_conversion(yzytbxj_path, temp_dataset2, sx_result_name, SX_WHERE_CLAUSE)
                    if int(arcpy.GetCount_management(sx_result_path).getOutput(0)) > 0:
                        addThreeFieldsQ(sx_result_path)
                        sx_layer_name = fc + "sx" + str(int(time.time()))
                        arcpy.MakeFeatureLayer_management(sx_result_path, sx_layer_name)
                        for sx in SX_FIELD_LIST:
                            arcpy.SelectLayerByAttribute_management(sx_layer_name, 'NEW_SELECTION', sx[1])
                            expre_sx1 = "PJ(\"" + sx[0] + "\",!" + CWMS_FEILD_NAME + "!)"
                            code_sx1 = """def PJ(a,b):
                                if b == None:
                                    return  a + ";"
                                else:
                                    return b + a + ";"  """
                            arcpy.CalculateField_management(sx_layer_name, CWMS_FEILD_NAME, expre_sx1, "PYTHON_9.3", code_sx1)

                        expre_sx = "getSX(!" + CWMS_FEILD_NAME + "!)"
                        code_sx = """def getSX(a):
                                return u"�ɹ�����[" + a[0:-1] + "]�ֶ�������ָ��ͼ�߲�һ��" """
                        arcpy.CalculateField_management(sx_result_path, CWMS_FEILD_NAME, expre_sx, "PYTHON_9.3", code_sx)
                        arcpy.Delete_management(sx_layer_name)

                    arcpy.AddMessage(u"      2.��� " + fc + u" ͼ��TBLX�ֶα�ע�����Ƿ�ȱʧ...")
                    tblx_temp_name = getNewFileNameQ(temp_dataset2, fc + "tblx_temp")
                    tblx_temp_path = os.path.join(temp_dataset2, tblx_temp_name)
                    arcpy.FeatureClassToFeatureClass_conversion(yzytbxj_path, temp_dataset2, tblx_temp_name,
                                                                '(TBLX IS NULL AND TBLX_1 IS NOT NULL AND TBLX_1 <> \' \')'
                                                                ' OR TBLX_1 <> TBLX')
                    addThreeFieldsQ(tblx_temp_path)
                    expr_tblx = "tblx(!TBLX_1!.strip(), !TBLX!.strip())"
                    code_tblx = """def tblx(a, b):
                        if a not in b and a != ' ' and a != None:
                            return u"TBLX�ֶα�ע����ȱʧ��ָ��ͼ�߱�ע�С�" + a + u"�����ݣ����ɹ�����û�б�ע"
                        else:
                            return 1 """
                    try:
                        arcpy.CalculateField_management(tblx_temp_path, CWMS_FEILD_NAME, expr_tblx, "PYTHON_9.3", code_tblx)
                    except Exception as cee:
                        print cee.message
                        arcpy.AddMessage(u"      2.��� " + fc + u" ͼ��TBLX�ֶα�ע�����Ƿ�ȱʧ2...")
                        try:
                            expr_tblx_vb = "density"
                            code_tblx_vb = """
                                Dim density
                                If InStr(1,[TBLX], [TBLX_1],1)=0 AND  [TBLX_1] <>" " AND [TBLX_1] <> None Then
                                density = "TBLX�ֶα�ע����ȱʧ��ָ��ͼ�߱�ע�С�" & [TBLX_1] & "�����ݣ����ɹ�����û�б�ע"
                                else
                                density = "1"
                                end if
                                """
                            arcpy.CalculateField_management(tblx_temp_path, CWMS_FEILD_NAME, expr_tblx_vb, "VB",
                                                            code_tblx_vb)
                        except Exception as aa:
                            arcpy.AddError(aa.message)

                    tblx_erase_name = getNewFileNameQ(temp_dataset2, fc + "tblx_erase")
                    tblx_erase_path = os.path.join(temp_dataset2, tblx_erase_name)
                    tblx_result_path = os.path.join(temp_dataset2, getNewFileNameQ(temp_dataset2, fc + "tblx_result"))
                    where_clause_tblx = CWMS_FEILD_NAME + "<> \'1\'"
                    arcpy.FeatureClassToFeatureClass_conversion(tblx_temp_path, temp_dataset2, tblx_erase_name, where_clause_tblx)
                    arcpy.Erase_analysis(tblx_erase_path, sx_result_path, tblx_result_path, "0.001 Meters")

                    # yzytbxj_path�ཻ��CWMS_FEILD_ALIAS
                    arcpy.AddMessage(u"      3.��� " + fc + u" ͼ��ԭDCBH�Ƿ��޸�...")
                    addThreeFieldsQ(yzytbxj_path)
                    expr_dcbh = "a(!DCBH!, !DCBH_1!)"
                    code_dcbh = """def a(x, y):
                        if x.find('-') == -1 and x == y:
                            return "1"
                        elif x.find('-') <> -1 and x[0:x.find('-')] == y and len(x[x.find('-') + 1:]) > 0:
                            return "1"
                        else:
                            return u"DCBH��ָ��ͼ�߲�һ�£�ԭDCBHΪ[" + y + u"], �ɹ����ݵ�DCBHΪ[" + x + u"]"
                    """
                    try:
                        arcpy.CalculateField_management(yzytbxj_path, CWMS_FEILD_NAME, expr_dcbh, "PYTHON_9.3", code_dcbh)
                    except Exception as dee:
                        print dee.message
                        arcpy.AddMessage(u"      3.��� " + fc + u" ͼ��ԭDCBH�Ƿ��޸�2...")
                        try:
                            expr_dcbh_vb = "density"
                            code_dcbh_vb = """
                                Dim density
                                IF InStr(1,[DCBH], "-",1)=0 Then
                                IF StrComp([DCBH],[DCBH_1]) = 0 Then
                                density = "1"
                                ELSE
                                density = "DCBH��ָ��ͼ�߲�һ�£�ԭDCBHΪ[" & [DCBH_1] & "], �ɹ����ݵ�DCBHΪ[" & [DCBH] & "]"
                                END IF
                                ELSE
                                IF Left([DCBH],InStr( [DCBH],"-") - 1) = [DCBH] and Len([DCBH])-InStrRev([DCBH],"-") > 0 Then
                                density = "1"
                                ELSE
                                density = "DCBH��ָ��ͼ�߲�һ�£�ԭDCBHΪ[" & [DCBH_1] & "], �ɹ����ݵ�DCBHΪ[" & [DCBH] & "]"
                                END IF
                                END IF
                                """
                            arcpy.CalculateField_management(yzytbxj_path, CWMS_FEILD_NAME, expr_dcbh_vb, "VB",
                                                            code_dcbh_vb)
                        except Exception as aa:
                            arcpy.AddError(aa.message)

                    dcbh_result_name = getNewFileNameQ(temp_dataset2, fc + "dcbh_result")
                    dcbh_result_path = os.path.join(temp_dataset2, dcbh_result_name)
                    whdcbh = CWMS_FEILD_NAME + "<> \'1\'"
                    arcpy.FeatureClassToFeatureClass_conversion(yzytbxj_path, temp_dataset2, dcbh_result_name, whdcbh)

                    arcpy.AddMessage(u"      4.��� " + fc + u" ͼ��ͼ����ָ��ͼ�߷�Χ�Ƿ�һ��...")
                    fwyz_result_path = os.path.join(temp_dataset2, getNewFileNameQ(temp_dataset2, fc + "fwyz_result"))
                    arcpy.SymDiff_analysis(fc_inpathtx, guide_fc_path, fwyz_result_path, "NO_FID", 0.001)
                    addThreeFieldsQ(fwyz_result_path)
                    result_fc_layer = fc + "result" + str(int(time.time()))
                    arcpy.MakeFeatureLayer_management(fwyz_result_path, result_fc_layer)
                    where_clause1 = """(DCBH = '' OR DCBH IS NULL) AND (DCBH_1 <> '' OR DCBH_1 IS NULL)"""
                    arcpy.SelectLayerByAttribute_management(result_fc_layer, 'NEW_SELECTION', where_clause1)
                    expression = "getDCBH(!DCBH_1!)"
                    codeblock = """def getDCBH(dcbh):
                                    ss = u"ָ��ͼ��DCBHΪ[" + str(dcbh) + u"]��ͼ�߱�ɾ�����߲��ֱ��г�"
                                    return ss"""

                    arcpy.CalculateField_management(result_fc_layer, CWMS_FEILD_NAME, expression, "PYTHON_9.3", codeblock)
                    arcpy.SelectLayerByAttribute_management(result_fc_layer, 'SWITCH_SELECTION')
                    ex_string = "'���·���ָ��ͼ�߷�Χ��һ��'"
                    arcpy.CalculateField_management(result_fc_layer, CWMS_FEILD_NAME, ex_string, "PYTHON_9.3")
                    arcpy.Delete_management(result_fc_layer)

                    arcpy.Merge_management([fwyz_result_path, sx_result_path, tblx_result_path, dcbh_result_path],
                                           last_result_path)
                    arcpy.CalculateField_management(last_result_path, MBTC_FEILD_NAME, "'" + fc + "'", "PYTHON_9.3")
                    arcpy.CalculateField_management(last_result_path, HCJG_FEILD_NAME, "'����ͼ��'", "PYTHON_9.3")

                    try:
                        check_field_lst = [MBTC_FEILD_NAME, HCJG_FEILD_NAME, CWMS_FEILD_NAME]
                        dor_field_list = []
                        fc_fields_list = arcpy.ListFields(fc_inpathtx)
                        for field in fc_fields_list:
                            check_field_lst.append(field.name)
                        for dor_f in arcpy.ListFields(last_result_path):
                            if dor_f.editable and dor_f.type != "Geometry" and dor_f.name not in check_field_lst:
                                dor_field_list.append(dor_f.name)
                        arcpy.DeleteField_management(last_result_path, dor_field_list)
                    except Exception as ein:
                        arcpy.AddError(ein.message)

                    arcpy.AddMessage("      " + fc + " �����ɣ�")
        except Exception as eout:
            arcpy.AddMessage("                      ")
            arcpy.AddError("    " + fc + " ʸ��������ָ��ͼ�߶Աȼ��ʧ�ܣ�")
            arcpy.AddError("*" * 20)
            arcpy.AddError(eout.message)
            arcpy.AddError("*" * 20)

    arcpy.AddMessage("  ")
    arcpy.AddMessage("ʸ��������ָ��ͼ�߶Աȼ��!")
    arcpy.AddMessage("  ")

# def checkGeometryNewQ(in_fc_list3, out_gdb3):
#     arcpy.AddMessage("����ִ�м��μ��...")
#     layer_count = 0
#     for in_feature_class in in_fc_list3:
#         fc = os.path.basename(in_feature_class)
#         layer_count += 1
#         arcpy.AddMessage("             ")
#         arcpy.AddMessage("  (" + str(layer_count) + ")" + fc + " ͼ�㼸�μ��...")
#         cg_table_name = getNewFileNameQ(out_gdb3, fc + "_CheckGeometry")
#         check_geometry_table = os.path.join(out_gdb3, cg_table_name)
#         result_name = getNewFileNameQ(out_gdb3, fc + "_���μ����")
#         result_path = os.path.join(out_gdb3, result_name)
#         in_layer_name = fc + str(int(time.time()))
#         hcsm_feild = "FEILD" + str(int(time.time()))
#         try:
#             arcpy.CheckGeometry_management(in_feature_class, check_geometry_table)
#             if int(arcpy.GetCount_management(check_geometry_table).getOutput(0)) > 0:
#                 try:
#                     arcpy.AddField_management(in_feature_class, hcsm_feild, 'TEXT', "#", "#", 255)
#                     join_id = ""
#                     for field in arcpy.ListFields(in_feature_class):
#                         if field.type == "OID" and not field.editable:
#                             join_id = field.name
#                     if join_id == "":
#                         arcpy.AddError("      " + fc + " ͼ�������ֶ�ʧ�ܣ��Ҳ���OBJECTID�ֶΣ�")
#
#                     arcpy.MakeFeatureLayer_management(in_feature_class, in_layer_name)
#                     arcpy.AddJoin_management(in_layer_name, join_id, check_geometry_table, "FEATURE_ID", "KEEP_COMMON")
#                     arcpy.CalculateField_management(in_layer_name, hcsm_feild, "!" + cg_table_name + ".PROBLEM!", "PYTHON_9.3")
#                     arcpy.RemoveJoin_management(in_layer_name)
#                     arcpy.Delete_management(in_layer_name)
#                     expres = hcsm_feild + " IS NOT NULL AND " + hcsm_feild + " <> \'\'"
#                     arcpy.FeatureClassToFeatureClass_conversion(in_feature_class, out_gdb3, result_name, expres)
#                     addThreeFieldsQ(result_path)
#                     arcpy.CalculateField_management(result_path, MBTC_FEILD_NAME, "'" + fc + "'", "PYTHON_9.3")
#                     arcpy.CalculateField_management(result_path, HCJG_FEILD_NAME, "'����ͼ��'", "PYTHON_9.3")
#                     arcpy.CalculateField_management(result_path, CWMS_FEILD_NAME, "!" + hcsm_feild + "!", "PYTHON_9.3")
#                     arcpy.DeleteField_management(result_path, hcsm_feild)
#                 except Exception as e1:
#                     arcpy.AddMessage("                      ")
#                     arcpy.AddError("    " + fc + " ͼ�㼸�μ��ʧ�ܣ�")
#                     arcpy.AddError("*" * 20)
#                     arcpy.AddError(e1.message)
#                     arcpy.AddError("*" * 20)
#
#                 finally:
#                     try:
#                         arcpy.DeleteField_management(in_feature_class, hcsm_feild)
#                     except Exception as e1:
#                         arcpy.AddError(e1.message)
#             else:
#                 arcpy.AddMessage("     " + fc + " ͼ��û�м��δ���")
#         except Exception as e2:
#             arcpy.AddMessage("                      ")
#             arcpy.AddError("    " + fc + " ͼ�㼸�μ��ʧ�ܣ�")
#             arcpy.AddError("*" * 20)
#             arcpy.AddError(e2.message)
#             arcpy.AddError("*" * 20)
#         finally:
#             if arcpy.Exists(check_geometry_table):
#                 try:
#                     arcpy.Delete_management(check_geometry_table)
#                 except Exception as e1:
#                     arcpy.AddError(e1.message)
#
#     arcpy.AddMessage("  ")
#     arcpy.AddMessage("���μ��ִ�н���!")
#     arcpy.AddMessage("  ")

def checkUnCutupOnlyFZZTQTBQ(in_fc_list4, temp_dataset, out_gdb4, dissolve_feild4):
    arcpy.AddMessage("����ִ�в�����ָ�����...")
    layer_count = 0
    for in_feature_cls in in_fc_list4:
        fc = os.path.basename(in_feature_cls)
        layer_count += 1
        in_feature_point = os.path.join(temp_dataset, getNewFileNameQ(temp_dataset, fc + "_point"))
        dissolve_features = os.path.join(temp_dataset, getNewFileNameQ(temp_dataset, fc + "_dissolve"))
        dissolve_feature_point = os.path.join(temp_dataset, getNewFileNameQ(temp_dataset, fc + "_dis_point"))
        erase_point = os.path.join(temp_dataset, getNewFileNameQ(temp_dataset, fc + "_erase"))
        result_name = getNewFileNameQ(out_gdb4, fc + "_������ָ�������")
        result_path = os.path.join(out_gdb4, result_name)
        in_layer_name = fc + str(int(time.time()))

        if "������ȡ" in fc or u"������ȡ" in fc:
            continue
        else:
            arcpy.AddMessage("             ")
            arcpy.AddMessage("  (" + str(layer_count) + ")" + fc + " ͼ�㲻����ָ�����...")
            try:
                arcpy.Dissolve_management(in_feature_cls, dissolve_features, dissolve_feild4, "", "SINGLE_PART", "DISSOLVE_LINES")
            except Exception as ee1:
                arcpy.AddError("  " + fc + " ͼ���ں�ʧ��!��鿴�����Ƿ��� ")
                arcpy.AddError(dissolve_feild4 + "�ֶ�")
                arcpy.AddError(ee1.message)
                break
            try:
                arcpy.FeatureToPoint_management(in_feature_cls, in_feature_point, "INSIDE")
                arcpy.FeatureToPoint_management(dissolve_features, dissolve_feature_point, "INSIDE")
                arcpy.Erase_analysis(in_feature_point, dissolve_feature_point, erase_point, "0.0001 Meters")

                arcpy.MakeFeatureLayer_management(in_feature_cls, in_layer_name)
                arcpy.SelectLayerByLocation_management(in_layer_name, "INTERSECT", erase_point, "", "NEW_SELECTION")
                arcpy.FeatureClassToFeatureClass_conversion(in_layer_name, out_gdb4, result_name)
                arcpy.Delete_management(in_layer_name)

                if int(arcpy.GetCount_management(result_path).getOutput(0)) > 0:
                    addThreeFieldsQ(result_path)
                    arcpy.CalculateField_management(result_path, HCJG_FEILD_NAME, "'����ͼ��'", "PYTHON_9.3")
                    arcpy.CalculateField_management(result_path, CWMS_FEILD_NAME, "'������ָ���'", "PYTHON_9.3")
                    arcpy.CalculateField_management(result_path, MBTC_FEILD_NAME, "'" + fc + "'", "PYTHON_9.3")
                else:
                    arcpy.AddMessage("      " + fc + " ͼ��û�в�����ָ��棡")
                arcpy.AddMessage("     " + fc + " ͼ�㲻����ָ�������ɣ�")
            except Exception as ee:
                arcpy.AddMessage("                      ")
                arcpy.AddError("    " + fc + " ͼ�㲻����ָ�����ʧ�ܣ�")
                arcpy.AddError("*" * 20)
                arcpy.AddError(ee.message)
                arcpy.AddError("*" * 20)

    arcpy.AddMessage("  ")
    arcpy.AddMessage("������ָ���ִ�н���!")
    arcpy.AddMessage("  ")

def checkTopologyNewQ(in_data_list5, dataset_path5, out_gdb5):
    arcpy.AddMessage("����ִ�����ص����...")

    topology_name = "topology"
    topology_path = os.path.join(dataset_path5, topology_name)
    topology_errors = "topoError"

    try:
        arcpy.AddMessage("    ")
        arcpy.AddMessage("    ��������...")
        arcpy.CreateTopology_management(dataset_path5, topology_name, ".001")
        arcpy.AddMessage("    �����������Ҫ����...")
        list_fcs = []
        for in_fc_path in in_data_list5:
            list_fcs.append(os.path.basename(in_fc_path))
            arcpy.AddFeatureClassToTopology_management(topology_path, in_fc_path, "1", "1")

        arcpy.AddMessage("    ������˹���...")
        for i in range(len(in_data_list5)):
            fc_path = in_data_list5[i]
            arcpy.AddRuleToTopology_management(topology_path, "Must Not Overlap (Area)", fc_path, "", "", "")
            for j in range(i + 1, len(in_data_list5)):
                fc_path2 = in_data_list5[j]
                arcpy.AddRuleToTopology_management(topology_path, "Must Not Overlap With (Area-Area)", fc_path, "", fc_path2, "")

        arcpy.AddMessage("    ������֤...")
        arcpy.ValidateTopology_management(topology_path, "Full_Extent")

        arcpy.AddMessage("    �������˴���...")
        arcpy.ExportTopologyErrors_management(topology_path, dataset_path5, topology_errors)
        errors_poly_path = os.path.join(dataset_path5, topology_errors + "_poly")
        cpoly = int(arcpy.GetCount_management(errors_poly_path).getOutput(0))

        arcpy.AddMessage("    �����������˽��...")
        if cpoly > 0:
            addThreeFieldsQ(errors_poly_path)
            arcpy.AddField_management(errors_poly_path, 'DCBH', 'TEXT', "#", "#", 50, '������')
            arcpy.AddField_management(errors_poly_path, 'DeDCBH', 'TEXT', "#", "#", 50, '��֮�ص�ͼ�ߵĵ�����')

            arcpy.CalculateField_management(errors_poly_path, HCJG_FEILD_NAME, "'����ͼ��'", "PYTHON_9.3", "")
            arcpy.CalculateField_management(errors_poly_path, MBTC_FEILD_NAME, "!OriginObjectClassName!", "PYTHON_9.3", "")

            first_meger_list = []
            for fcs in list_fcs:
                fc_name_first = fcs + "topoErrFirst"
                expr_sec = "DestinationObjectClassName like \'%" + fcs + "%\'"
                in_fc_path = os.path.join(dataset_path5, fcs)

                arcpy.FeatureClassToFeatureClass_conversion(errors_poly_path, dataset_path5, fc_name_first, expr_sec)
                err_first_path = os.path.join(dataset_path5, fc_name_first)
                first_meger_list.append(err_first_path)

                layer_name_first = fc_name_first + "layer" + str(int(time.time()))

                join_id = ""
                for field in arcpy.ListFields(in_fc_path):
                    if field.type == "OID" and not field.editable:
                        join_id = field.name
                if join_id == "":
                    arcpy.AddError("      " + fcs + " ͼ�������ֶ�ʧ�ܣ��Ҳ���OBJECTID�ֶΣ�")

                arcpy.MakeFeatureLayer_management(err_first_path, layer_name_first)
                arcpy.AddJoin_management(layer_name_first, "DestinationObjectID", in_fc_path, join_id, "KEEP_ALL")
                arcpy.CalculateField_management(layer_name_first, 'DeDCBH', "!" + fcs + ".DCBH!", "PYTHON_9.3", "")
                arcpy.RemoveJoin_management(layer_name_first)
                arcpy.Delete_management(layer_name_first)

            merge_first_path = os.path.join(dataset_path5, "FistMerge")
            arcpy.Merge_management(first_meger_list, merge_first_path)
            for fcl in list_fcs:
                fc_name = fcl + "_���ص������"
                expr = MBTC_FEILD_NAME + " like \'%" + fcl + "%\'"
                fcl_path = os.path.join(dataset_path5, fcl)
                err_fc_path = os.path.join(out_gdb5, fc_name)
                try:
                    arcpy.FeatureClassToFeatureClass_conversion(merge_first_path, out_gdb5, fc_name, expr)
                    if int(arcpy.GetCount_management(err_fc_path).getOutput(0)) > 0:
                        layer_name = fc_name + "layer" + str(int(time.time()))
                        join_id = ""
                        for field in arcpy.ListFields(fcl_path):
                            if field.type == "OID" and not field.editable:
                                join_id = field.name
                        if join_id == "":
                            arcpy.AddError("      " + fcl + " ͼ�������ֶ�ʧ�ܣ��Ҳ���OBJECTID�ֶΣ�")
                        arcpy.MakeFeatureLayer_management(err_fc_path, layer_name)
                        arcpy.AddJoin_management(layer_name, "OriginObjectID", fcl_path, join_id, "KEEP_ALL")
                        arcpy.CalculateField_management(layer_name, 'DCBH', "!" + fcl + ".DCBH!", "PYTHON_9.3", "")
                        arcpy.RemoveJoin_management(layer_name)
                        arcpy.Delete_management(layer_name)

                        expression1 = "getValue(!DestinationObjectClassName!, !DeDCBH!)"
                        codeblock1 = """def getValue(val, val2):
                                        ss = "��" + str(val) + "��DCBHΪ["+ str(val2) +"]��Ҫ���ص�"
                                        return ss"""

                        arcpy.CalculateField_management(err_fc_path, CWMS_FEILD_NAME, expression1, "PYTHON_9.3", codeblock1)

                        fc_fields_list = arcpy.ListFields(err_fc_path)
                        check_lst = ['DCBH', MBTC_FEILD_NAME, HCJG_FEILD_NAME, CWMS_FEILD_NAME]
                        delete_ls = []
                        for field in fc_fields_list:
                            if field.editable and field.name not in check_lst and field.type != "Geometry":
                                delete_ls.append(field.name)
                        arcpy.DeleteField_management(err_fc_path, delete_ls)
                    else:
                        if arcpy.Exists(err_fc_path):
                            try:
                                arcpy.Delete_management(err_fc_path)
                            except Exception as e:
                                arcpy.AddError(e.message)
                except Exception as eq:
                    if arcpy.Exists(err_fc_path):
                        try:
                            arcpy.Delete_management(err_fc_path)
                        except Exception as e:
                            arcpy.AddError(e.message)
                    arcpy.AddError(eq.message)

    except Exception as e1223:
        arcpy.AddMessage("                      ")
        arcpy.AddError("    ���ص����ִ��ʧ�ܣ�")
        arcpy.AddError("*" * 20)
        arcpy.AddError(e1223.message)
        arcpy.AddError("*" * 20)

    arcpy.AddMessage("                      ")
    arcpy.AddMessage("���ص����ִ�н�����")
    arcpy.AddMessage("                      ")

def getNewFilePath(dirpath1, file_name_out):
    n = [1]
    def get_new_name(file_name_in):
        new_file_name = file_name_in
        if arcpy.Exists(os.path.join(dirpath1, file_name_in)):
            new_file_name = "%s_%s%s" % (os.path.splitext(file_name_in)[0], str(n[0]), os.path.splitext(file_name_in)[1])
            n[0] += 1
            if arcpy.Exists(os.path.join(dirpath1, new_file_name)):
                new_file_name = get_new_name(file_name_in)
        return new_file_name
    result = get_new_name(file_name_out)
    return os.path.join(dirpath1, result)

def getNewFileNameQ(dirpath2, file_name2):
    n = [1]
    def get_new_name(file_name_in2):
        new_file_name = file_name_in2
        if arcpy.Exists(os.path.join(dirpath2, file_name_in2)):
            new_file_name = "%s_%s%s" % (os.path.splitext(file_name_in2)[0], str(n[0]), os.path.splitext(file_name_in2)[1])
            n[0] += 1
            if arcpy.Exists(os.path.join(dirpath2, new_file_name)):
                new_file_name = get_new_name(file_name_in2)
        return new_file_name
    return get_new_name(file_name2)

def checkFeatureClassNameAndGetPathQ(in_workspace_cfn):
    arcpy.env.workspace = in_workspace_cfn
    in_fc_list = []
    ronge_name_list = []
    fc_lists = arcpy.ListFeatureClasses()
    right_name = True
    null_layer = True
    ls1 = ["�������ʸ���Ǳ������ͼ��", "�����õظ���Ǳ������ͼ��", "�˸�ũ�õ�Ǳ������ͼ��", "�˸�δ���õ�Ǳ������ͼ��", "������ȡǱ��ͼ��"]
    ls2 = [u"�������ʸ���Ǳ������ͼ��",u"�����õظ���Ǳ������ͼ��",u"�˸�ũ�õ�Ǳ������ͼ��",u"�˸�δ���õ�Ǳ������ͼ��",u"������ȡǱ��ͼ��"]
    for fc in fc_lists:
        if fc in ls1 or fc in ls2:
            in_fc_list.append(os.path.join(arcpy.env.workspace, fc))
        else:
            right_name = False
            ronge_name_list.append(fc)
            arcpy.AddError("    \"" + fc + "\" ͼ���������淶������")

    dataset_ls = arcpy.ListDatasets()
    for dataset in dataset_ls:
        arcpy.env.workspace = os.path.join(in_workspace_cfn, dataset)
        fc_ls = arcpy.ListFeatureClasses()
        for fc in fc_ls:
            null_layer = False
            if fc in ls1 or fc in ls2:
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
        arcpy.AddMessage(null_layer)
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

def checkFieldsTypeQ(ffcc, ffield_ls):
    wrong_type_fds = []
    fields = arcpy.ListFields(ffcc)
    for fd in fields:
        if fd.name in ffield_ls and fd.type != "String":
            wrong_type_fds.append(fd.name)
    return wrong_type_fds

def exportFeatureClassQ(in_fc_listex, out_gdbex):
    dataset_name = getNewFileNameQ(out_gdbex, "Dataset")
    dataset_path = os.path.join(out_gdbex, dataset_name)
    arcpy.CreateFeatureDataset_management(out_gdbex, dataset_name, in_fc_listex[0])
    arcpy.FeatureClassToGeodatabase_conversion(in_fc_listex, dataset_path)
    data_fc_path = []
    for in_fc_p in in_fc_listex:
        data_fc_path.append(os.path.join(dataset_path, os.path.basename(in_fc_p)))
    arcpy.AddMessage(" . ")
    return [dataset_path, data_fc_path]

def mergeFeatureClassQ(in_gdb6):
    arcpy.env.workspace = in_gdb6
    list_fcs = arcpy.ListFeatureClasses()
    in_path_list1 = []
    in_path_list2 = []
    in_path_list3 = []
    in_path_list4 = []
    in_path_list5 = []

    merge_path1 = os.path.join(in_gdb6, getNewFileNameQ(in_gdb6, "�˸�ũ�õ�Ǳ������ͼ�߼����"))
    merge_path2 = os.path.join(in_gdb6, getNewFileNameQ(in_gdb6, "�˸�δ���õ�Ǳ������ͼ�߼����"))
    merge_path3 = os.path.join(in_gdb6, getNewFileNameQ(in_gdb6, "�����õظ���Ǳ������ͼ�߼����"))
    merge_path4 = os.path.join(in_gdb6, getNewFileNameQ(in_gdb6, "�������ʸ���Ǳ������ͼ�߼����"))
    merge_path5 = os.path.join(in_gdb6, getNewFileNameQ(in_gdb6, "������ȡǱ��ͼ�߼����"))

    for fc in list_fcs:
        arcpy.RepairGeometry_management(fc)
        if "ũ�õ�" in fc or u"ũ�õ�" in fc:
            in_path_list1.append(os.path.join(in_gdb6, fc))
        elif "δ���õ�" in fc or u"δ���õ�" in fc:
            in_path_list2.append(os.path.join(in_gdb6, fc))
        elif "�����õظ���" in fc or u"�����õظ���" in fc:
            in_path_list3.append(os.path.join(in_gdb6, fc))
        elif "���ʸ���" in fc or u"���ʸ���" in fc:
            in_path_list4.append(os.path.join(in_gdb6, fc))
        elif "������ȡ" in fc or u"������ȡ" in fc:
            in_path_list5.append(os.path.join(in_gdb6, fc))

    try:
        if len(in_path_list1) > 0:
            arcpy.Merge_management(in_path_list1, merge_path1)
        if len(in_path_list2) > 0:
            arcpy.Merge_management(in_path_list2, merge_path2)
        if len(in_path_list3) > 0:
            arcpy.Merge_management(in_path_list3, merge_path3)
        if len(in_path_list4) > 0:
            arcpy.Merge_management(in_path_list4, merge_path4)
        if len(in_path_list5) > 0:
            arcpy.Merge_management(in_path_list5, merge_path5)

        for fc_path1 in in_path_list1:
            if arcpy.Exists(fc_path1):
                try:
                    arcpy.Delete_management(fc_path1)
                except Exception as e2:
                    arcpy.AddError(e2.message)

        for fc_path2 in in_path_list2:
            if arcpy.Exists(fc_path2):
                try:
                    arcpy.Delete_management(fc_path2)
                except Exception as e2:
                    arcpy.AddError(e2.message)

        for fc_path3 in in_path_list3:
            if arcpy.Exists(fc_path3):
                try:
                    arcpy.Delete_management(fc_path3)
                except Exception as e2:
                    arcpy.AddError(e2.message)

        for fc_path4 in in_path_list4:
            if arcpy.Exists(fc_path4):
                try:
                    arcpy.Delete_management(fc_path4)
                except Exception as e2:
                    arcpy.AddError(e2.message)

        for fc_path5 in in_path_list5:
            if arcpy.Exists(fc_path5):
                try:
                    arcpy.Delete_management(fc_path5)
                except Exception as e2:
                    arcpy.AddError(e2.message)
    except Exception as e1:
        arcpy.AddError(e1.message)

    return [merge_path1,merge_path2,merge_path3,merge_path4,merge_path5]

def featureClassToExcelQ(fc_path_list, fields3, excel_path3, sheets_name3='sheet'):

    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)

    def set_style(font_name, font_size, borders=False, ali_center=False, back=False):
        style_i = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = font_name
        font.height = 20 * font_size
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
            style_i.alignment = ali
        if back:
            patterni = xlwt.Pattern()
            patterni.pattern = xlwt.Pattern.SOLID_PATTERN
            patterni.pattern_fore_colour = xlwt.Style.colour_map['ice_blue']
            patterni.pattern_back_colour = xlwt.Style.colour_map['ice_blue']
            style_i.pattern = patterni
        return style_i

    def add_new_sheet(sheet_name):
        worksheets = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
        # �����п�
        worksheets.col(0).width = 256 * 10
        worksheets.col(1).width = 256 * 25
        worksheets.col(2).width = 256 * 25
        worksheets.col(3).width = 256 * 25
        worksheets.col(4).width = 256 * 110
        worksheets.col(5).width = 256 * 10
        worksheets.col(6).width = 256 * 10

        style1 = set_style(u'����', 11, True, True, True)

        worksheets.write(0, 0, '���', style1)
        worksheets.write(0, 1, '�������', style1)
        worksheets.write(0, 2, 'Ŀ��ͼ��', style1)
        worksheets.write(0, 3, '������', style1)
        worksheets.write(0, 4, '��������', style1)
        worksheets.write(0, 5, '�Ƿ�����', style1)
        worksheets.write(0, 6, '��������', style1)

        return worksheets
    r_list = []
    cuid = 0
    for fc in fc_path_list:
        if arcpy.Exists(fc) and int(arcpy.GetCount_management(fc).getOutput(0)) > 0:
            with arcpy.da.SearchCursor(fc, fields3) as cursor:
                for row in cursor:
                    cuid += 1
                    r_list.append([cuid,row[0],row[1],row[2],row[3]])

    if cuid <= 65535:
        worksheet1 = add_new_sheet(sheets_name3)
        style2 = set_style(u'����', 10)
        for row in r_list:
                worksheet1.write(row[0], 0, row[0], style2)#���
                worksheet1.write(row[0], 1, row[1], style2)#�������
                worksheet1.write(row[0], 2, row[2], style2)#Ŀ��ͼ��
                worksheet1.write(row[0], 3, row[3], style2)#������
                worksheet1.write(row[0], 4, row[4], style2)#��������
    else:
        m = 1
        i = 1
        sheet1 = add_new_sheet(sheets_name3 + "{0}".format(m))
        style2 = set_style(u'����', 10)
        for row in r_list:
            sheet1.write(i, 0, row[0], style2)  # ���
            sheet1.write(i, 1, row[1], style2)  # �������
            sheet1.write(i, 2, row[2], style2)  # Ŀ��ͼ��
            sheet1.write(i, 3, row[3], style2)  # ������
            sheet1.write(i, 4, row[4], style2)  # ��������
            i += 1
            if row[0] % 65535 == 0:
                i = 1
                m += 1
                sheet1 = add_new_sheet(sheets_name3 + "{0}".format(m))

    workbook.save(excel_path3)

def main():
    arcpy.AddMessage("��������: " + global_in_path)
    arcpy.AddMessage("ָ��ͼ��: " + global_guide_path)
    arcpy.AddMessage("��������·��: " + global_out_path)
    arcpy.AddMessage("������ָ��ֶ�:  " + global_dissolve_feild)
    arcpy.AddMessage("����ͼ�μ��: " + str(global_fhtxjc))
    # arcpy.AddMessage("���μ��: " + str(global_jhjc))
    arcpy.AddMessage("ʸ��������ָ��ͼ�߶Աȼ��: " + str(global_txfwjc))
    arcpy.AddMessage("������ָ���: " + str(global_bhlfgjc))
    arcpy.AddMessage("���ص����: " + str(global_tpjc))

    if not global_fhtxjc and not global_txfwjc and not global_bhlfgjc and not global_tpjc:
        arcpy.AddError("û��ѡ������������κδ���")
        list0 = []
        print list0[99999999]
        sys.exit()

    in_fc_list0 = checkFeatureClassNameAndGetPathQ(global_in_path)

    FIELD_LIST_GLOBAL = global_dissolve_feild.split(";")
    exile_field = False
    for iaai in CHECK_FIELD_LIST:
        if iaai not in FIELD_LIST_GLOBAL:
            FIELD_LIST_GLOBAL.append(iaai)
    for fcpath in in_fc_list0[1]:
        exile_fieldlist = checkFieldsExistQ(fcpath,FIELD_LIST_GLOBAL)
        if len(exile_fieldlist) > 0:
            exile_field = True
            arcpy.AddError(" ")
            arcpy.AddError("      ʸ�����ݣ�" + os.path.basename(fcpath) + " ͼ��ȱ�� [" + "; ".join(exile_fieldlist) + "] �ֶ�")

    wr_type_field = False
    for fcpath1 in in_fc_list0[1]:
        wr_type_fields = checkFieldsTypeQ(fcpath1, CHECK_FIELD_LIST)
        if len(wr_type_fields) > 0:
            wr_type_field = True
            arcpy.AddError(" ")
            arcpy.AddError("      ʸ�����ݣ�" + os.path.basename(fcpath1) +
                           " ͼ�� [" + "; ".join(wr_type_fields) + "] �ֶε����ʹ����޷����к�����顣����ձ�׼�⽫�ֶ����͸�Ϊ�ı����ͣ�")

    if exile_field:
        list0 = []
        print list0[99999999]
        sys.exit()

    if wr_type_field:
        list0 = []
        print list0[99999999]
        sys.exit()
    if not in_fc_list0[0]:
        arcpy.AddError("*ʧ�ܣ�����ʸ������ͼ���������淶����ȷ�ϣ�")
        list0 = []
        print list0[99999999]
        sys.exit()

    in_gc_list0 = []
    if global_txfwjc:
        if global_guide_path == "" or global_guide_path == "#":
            arcpy.AddError("ִ�� \"ͼ�η�Χ���\" ��Ҫָ��ͼ�ߣ���������")
            list0 = []
            print list0[99999999]
            sys.exit()
        in_gc_list0 = checkFeatureClassNameAndGetPathQ(global_guide_path)
        if not in_gc_list0[0]:
            arcpy.AddError("*ʧ�ܣ�����ָ��ͼ��ͼ���������淶�� ��ȷ�ϣ�")
            list0 = []
            print list0[99999999]
            sys.exit()

    global_result_gdb_name = os.path.basename(global_in_path).rstrip(os.path.splitext(global_in_path)[1]) + "���˼����.gdb"
    global_result_gdb_path = getNewFilePath(global_out_path, global_result_gdb_name)
    arcpy.CreateFileGDB_management(global_out_path, os.path.basename(global_result_gdb_path))

    global_data_list = exportFeatureClassQ(in_fc_list0[1], global_result_gdb_path)

    arcpy.AddMessage(global_result_gdb_path)
    try:
        # if global_jhjc:
        #     arcpy.AddMessage("-"*27 + "���μ��" + "-"*27)
        #     checkGeometryNewQ(global_data_list[1], global_result_gdb_path)
        # ���μ�������޸�����
        for faffaf in global_data_list[1]:
            arcpy.RepairGeometry_management(faffaf)
        if global_fhtxjc:
            arcpy.AddMessage("-"*25 + "����ͼ�μ��" + "-"*25)
            chackMultipartNewQ(global_data_list[1], global_result_gdb_path)
        if global_txfwjc:
            arcpy.AddMessage("-"*25 + "ʸ��������ָ��ͼ�߶Աȼ��" + "-"*25)
            checkFeatureAreaNewQ(global_data_list[1], global_data_list[0], in_gc_list0[1], global_result_gdb_path)
        if global_bhlfgjc:
            arcpy.AddMessage("-"*25 + "������ָ���" + "-"*24)
            checkUnCutupOnlyFZZTQTBQ(global_data_list[1], global_data_list[0], global_result_gdb_path, global_dissolve_feild)
        if global_tpjc:
            arcpy.AddMessage("-"*25 + "���ص����" + "-"*25)
            checkTopologyNewQ(global_data_list[1], global_data_list[0], global_result_gdb_path)

        arcpy.AddMessage("-"*20 + "����ͼ�ߵ���Excel����" + "-"*20)

        global_fields = (HCJG_FEILD_NAME, MBTC_FEILD_NAME, 'DCBH', CWMS_FEILD_NAME)
        global_name = os.path.basename(global_in_path).rstrip(os.path.splitext(global_in_path)[1]) + "���˼������¼��.xls"
        global_excel_file_path = getNewFilePath(global_out_path, global_name)

        arcpy.AddMessage("  ")
        arcpy.AddMessage("������������ ...")
        global_result1_path = mergeFeatureClassQ(global_result_gdb_path)

        arcpy.AddMessage("���ڵ���Excel�� ...")
        featureClassToExcelQ(global_result1_path, global_fields, global_excel_file_path, "����ͼ��")
        arcpy.AddMessage("������ɣ�")
        arcpy.AddMessage("  ")
        arcpy.AddMessage("�������" + global_result_gdb_path)
        arcpy.AddMessage("��¼��" + global_excel_file_path)
        arcpy.AddMessage("  ")
    except Exception as e:
        arcpy.AddError(e.message)

    if arcpy.Exists(global_data_list[0]):
        try:
            arcpy.AddMessage(".")
            arcpy.Delete_management(global_data_list[0])
        except Exception as e:
            arcpy.AddError(e.message)

if __name__ == "__main__":
    global_in_path = arcpy.GetParameterAsText(0)
    global_guide_path = arcpy.GetParameterAsText(1)
    global_out_path = arcpy.GetParameterAsText(2)
    global_dissolve_feild = arcpy.GetParameterAsText(3)

    global_fhtxjc = arcpy.GetParameter(4)
    # global_jhjc = arcpy.GetParameter(5)
    global_txfwjc = arcpy.GetParameter(5)
    global_bhlfgjc = arcpy.GetParameter(6)
    global_tpjc = arcpy.GetParameter(7)

    main()


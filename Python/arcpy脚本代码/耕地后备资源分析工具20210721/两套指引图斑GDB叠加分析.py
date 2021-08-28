# -*- coding: gbk -*-
import sys
import arcpy
import os
import re
import time

reload(sys)
sys.setdefaultencoding("utf-8")
arcpy.env.XYResolution = "0.00001 Meters"
arcpy.env.XYTolerance = "0.0001 Meters"

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

def checkLayerNameAndGetPathQ(in_gdb):
    arcpy.env.workspace = in_gdb
    in_fc_list = []
    fc_lists = arcpy.ListFeatureClasses()
    right_name = True
    null_layer = True
    for fc in fc_lists:
        a = ("�˸�ũ�õ�Ǳ������ͼ��" in fc or "�˸�δ���õ�Ǳ������ͼ��" in fc or "�����õظ���Ǳ������ͼ��" in fc
             or "�������ʸ���Ǳ������ͼ��" in fc or "������ȡǱ��" in fc)
        b = (u"�˸�ũ�õ�Ǳ������ͼ��" in fc or u"�˸�δ���õ�Ǳ������ͼ��" in fc or u"�����õظ���Ǳ������ͼ��" in fc
             or u"�������ʸ���Ǳ������ͼ��" in fc or "������ȡǱ��" in fc)
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
            a = ("�˸�ũ�õ�Ǳ������ͼ��" in fc or "�˸�δ���õ�Ǳ������ͼ��" in fc or "�����õظ���Ǳ������ͼ��" in fc
                 or "�������ʸ���Ǳ������ͼ��" in fc or "������ȡǱ��" in fc)
            b = (u"�˸�ũ�õ�Ǳ������ͼ��" in fc or u"�˸�δ���õ�Ǳ������ͼ��" in fc or u"�����õظ���Ǳ������ͼ��" in fc
                 or u"�������ʸ���Ǳ������ͼ��" in fc or "������ȡǱ��" in fc)
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

def AddAndCalculateField(fci_path,txt_string):
    field_name1 = getNewFieldName(fci_path,"bhlx")
    arcpy.AddField_management(fci_path, field_name1, "TEXT", "#", "#", 255, "�仯����")
    arcpy.CalculateField_management(fci_path, field_name1, "'" + txt_string + "'", "PYTHON_9.3", "")

def SuperpositionAnalysis(in_path,consult_path, out_path, sql_clause):

    arcpy.env.workspace = consult_path#��ָ��ͼ��·��
    arcpy.AddMessage("..." * 12)
    consult_gdb_list = arcpy.ListWorkspaces("*", "FileGDB")
    arcpy.AddMessage("��� " + consult_path + " ·����gdb��ͼ�������Ƿ���ȷ...")
    cout = 0
    fail = 0
    fail_list = []
    wrong_name = False
    for consult_gdb1 in consult_gdb_list:
        wrong_name = False
        cout += 1
        consult_check_layer = checkLayerNameAndGetPathQ(consult_gdb1)
        if not consult_check_layer[0]:
            wrong_name = True
            fail_list.append(consult_gdb1)
            fail += 1
    if wrong_name:
        arcpy.AddError("  ͼ����������" + str(fail) + " ���� ���£�")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)

    arcpy.env.workspace = in_path#ԭָ��ͼ��·��
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")
    arcpy.AddMessage("..."*12)
    arcpy.AddMessage("��� " + in_path + " ·����gdb��ͼ�������Ƿ���ȷ...")
    cout = 0
    fail = 0
    fail_list = []
    wrong_name2 = False
    for in_gdb1 in workspaces:
        cout += 1
        in_check_layer = checkLayerNameAndGetPathQ(in_gdb1)
        if not in_check_layer[0]:
            wrong_name2 = True
            fail_list.append(in_gdb1)
            fail += 1
    if wrong_name2:
        arcpy.AddError("  ͼ����������" + str(fail) + " ���� ���£�")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)

    if wrong_name or wrong_name2:
        aaaa = []
        print aaaa[99]

    arcpy.AddMessage("..." * 12)
    cout = 0
    fail = 0
    fail_list = []
    change_folder_path1 = os.path.join(out_path, "�б仯�Ĳ���")
    if not arcpy.Exists(change_folder_path1):
        arcpy.CreateFolder_management(out_path, "�б仯�Ĳ���")

    nochangefolder_path2 = os.path.join(out_path, "ԭָ��ͼ��ͼ�κ����Զ�û�仯��ͼ��")
    if not arcpy.Exists(nochangefolder_path2):
        arcpy.CreateFolder_management(out_path, "ԭָ��ͼ��ͼ�κ����Զ�û�仯��ͼ��")

    newchangefolder_path = os.path.join(out_path, "��ָ��ͼ�߱仯�˵�ͼ��")
    if not arcpy.Exists(newchangefolder_path):
        arcpy.CreateFolder_management(out_path, "��ָ��ͼ�߱仯�˵�ͼ��")

    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        try:
            # ��ÿ��gdb��Ϊ������
            arcpy.env.workspace = workspace
            old_fc_list = arcpy.ListFeatureClasses()
            arcpy.AddMessage(" ... ")
            temp_name1 = getNewFileNameQ(out_path, "��������" + os.path.basename(workspace))
            result_gdb = os.path.join(out_path, temp_name1)
            arcpy.AddMessage(" �½� " + result_gdb + " ...")
            arcpy.AddMessage("  " + temp_name1 + " ...")
            arcpy.CreateFileGDB_management(out_path, temp_name1)

            gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])

            change_merge = getNewFileNameQ(change_folder_path1, gdbName + "�仯�Ĳ���.gdb")
            change_merge_gdb = os.path.join(change_folder_path1, change_merge)
            arcpy.AddMessage("  �½� " + change_merge_gdb + " ...")
            arcpy.AddMessage("   " + change_merge + " ...")
            arcpy.CreateFileGDB_management(change_folder_path1, change_merge)

            nochange = getNewFileNameQ(nochangefolder_path2, gdbName + "û�仯��ͼ��.gdb")
            nochange_gdb = os.path.join(nochangefolder_path2, nochange)
            arcpy.AddMessage("  �½� " + nochange_gdb + " ...")
            arcpy.AddMessage("   " + nochange + " ...")
            arcpy.CreateFileGDB_management(nochangefolder_path2, nochange)

            newchange = getNewFileNameQ(newchangefolder_path, gdbName + "�仯�˵�ͼ��.gdb")
            newchange_gdb = os.path.join(newchangefolder_path, newchange)
            arcpy.AddMessage("  �½� " + newchange_gdb + " ...")
            arcpy.AddMessage("   " + newchange + " ...")
            arcpy.CreateFileGDB_management(newchangefolder_path, newchange)
            arcpy.AddMessage(" ... ")
            arcpy.AddMessage("  ")

            xzqcode = re.findall(r"\d+", gdbName)

            consult_gdb_pathp = ""
            for con_gdb in consult_gdb_list:
                if xzqcode[0] in os.path.basename(con_gdb):
                    consult_gdb_pathp = con_gdb

            if consult_gdb_pathp == "":
                arcpy.AddError("  " + os.path.basename(workspace) + " ʧ�ܣ��Ҳ�����Ӧ�Ĳο����ݣ�")
                fail += 1
                fail_list.append(workspace)
                continue
            fc_count = 0
            for old_fc in old_fc_list:
                fc_count += 1
                arcpy.AddMessage("    "+ str(fc_count) + "��" + old_fc)
                old_fc_path = os.path.join(workspace, old_fc)
                new_fc_path = os.path.join(consult_gdb_pathp,old_fc)
                if arcpy.Exists(new_fc_path):
                    old_erase_output = os.path.join(result_gdb, old_fc + "���ٵ�")
                    arcpy.AddMessage("       ԭָ��ͼ�ߵ� " + old_fc + " ͼ�� ���� ��ָ��ͼ�ߵ� " + old_fc + " ͼ��ó����ٵĲ���..." )
                    arcpy.Erase_analysis(old_fc_path, new_fc_path, old_erase_output, "0.001 Meters")
                    AddAndCalculateField(old_erase_output,"���ٵĲ���")

                    new_erase_output = os.path.join(result_gdb, old_fc + "������")
                    arcpy.AddMessage("       ��ָ��ͼ�ߵ� " + old_fc + " ͼ�� ���� ԭָ��ͼ�ߵ� " + old_fc + " ͼ��ó����ٵĲ���..." )
                    arcpy.Erase_analysis(new_fc_path, old_fc_path, new_erase_output, "0.001 Meters")
                    AddAndCalculateField(new_erase_output, "�����Ĳ���")

                    intersect1_path = os.path.join(result_gdb, "�ཻ���" + old_fc)
                    arcpy.AddMessage("       ԭָ��ͼ�ߵ� " + old_fc + " �� ��ָ��ͼ�ߵ� " + old_fc + " �ཻ..." )
                    arcpy.Intersect_analysis([old_fc_path, new_fc_path], intersect1_path,"NO_FID")

                    select_out_fc = os.path.join(result_gdb, old_fc + "���Ա仯��")
                    arcpy.AddMessage("       �ཻ��ɸѡ��" + sql_clause + " ..." )
                    arcpy.Select_analysis(intersect1_path, select_out_fc, sql_clause)
                    AddAndCalculateField(select_out_fc, "���Ա仯�Ĳ���")

                    arcpy.AddMessage("       ���Ա仯�Ĳ��ֺ�ͼ�α仯�Ĳ��ֺϲ� ..." )
                    change_merge_fc = os.path.join(result_gdb, "�ϲ�" + old_fc)
                    mul_to_sgl = os.path.join(change_merge_gdb, old_fc)
                    arcpy.Merge_management([old_erase_output,new_erase_output,select_out_fc],change_merge_fc)
                    arcpy.MultipartToSinglepart_management(change_merge_fc, mul_to_sgl)

                    arcpy.AddMessage("       ԭָ��ͼ��ɸѡ��ͼ�η�Χ�����Զ�û�б仯��ͼ�� ..." )
                    in_feature_point = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "FeatureToPoint" + old_fc))
                    arcpy.AddMessage("          �仯����ת�� ..." )
                    arcpy.FeatureToPoint_management(mul_to_sgl, in_feature_point, "INSIDE")

                    arcpy.AddMessage("          ԭָ��ͼ�߰�λ��ѡ�񲢵��� ..." )
                    in_layer_name = old_fc + str(int(time.time()))
                    arcpy.MakeFeatureLayer_management(old_fc_path, in_layer_name)
                    arcpy.SelectLayerByLocation_management(in_layer_name, "INTERSECT", in_feature_point, "", "NEW_SELECTION")
                    old_change_path = os.path.join(result_gdb, old_fc + "ԭָ��ͼ�߱仯��ͼ��")
                    arcpy.FeatureClassToFeatureClass_conversion(in_layer_name, result_gdb, old_fc + "ԭָ��ͼ�߱仯��ͼ��")
                    arcpy.SelectLayerByLocation_management(in_layer_name, "", "", "", "SWITCH_SELECTION")
                    arcpy.FeatureClassToFeatureClass_conversion(in_layer_name, nochange_gdb, old_fc)
                    arcpy.Delete_management(in_layer_name)

                    arcpy.AddMessage("       ��ָ��ͼ��ɸѡ�������ԭָ��ͼ�߱仯�˵�������ͼ�ߣ��ཻ�Ͳ����õ��Ŀ���ֻ��ͼ�ߵ�һ���֣� ..." )
                    arcpy.AddMessage("          ��ָ��ͼ�߰�λ��ѡ�񲢵��� ..." )
                    in_layer_name1 = old_fc + str(int(time.time()))
                    arcpy.MakeFeatureLayer_management(new_fc_path, in_layer_name1)
                    arcpy.SelectLayerByLocation_management(in_layer_name1, "INTERSECT", in_feature_point, "", "NEW_SELECTION")
                    arcpy.SelectLayerByLocation_management(in_layer_name1, "WITHIN", old_change_path, "", "ADD_TO_SELECTION")
                    arcpy.FeatureClassToFeatureClass_conversion(in_layer_name1, newchange_gdb, old_fc)
                    arcpy.Delete_management(in_layer_name1)
                else:
                    arcpy.AddWarning("***������" + new_fc_path + "���������κβ�������ȷ���������ݵ�ͼ���Ƿ�����һ�£�")

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " ʧ�ܣ�")
            fail_list.append(workspace)
            fail += 1

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
    old_pathG = arcpy.GetParameterAsText(0)#ԭָ��ͼ��
    new_pathG = arcpy.GetParameterAsText(1)#��ָ��ͼ��
    out_pathG = arcpy.GetParameterAsText(2)
    where_cluase = arcpy.GetParameterAsText(3)

    if where_cluase == " " or where_cluase == "#":
        where_c = """DLBM <> DLBM_1 OR XZQMC <> XZQMC_1 OR QSXZ <> QSXZ_1 OR DLMC <> DLMC_1 OR GDLX <> GDLX_1 OR ZZSXMC <> ZZSXMC_1 OR
 TBXHMC <> TBXHMC_1"""
    SuperpositionAnalysis(old_pathG,new_pathG,out_pathG,where_cluase)

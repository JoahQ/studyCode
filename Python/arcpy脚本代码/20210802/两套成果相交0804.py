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

def SuperpositionAnalysis(in_path,consult_path, out_path):

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
    warning = 0
    fail_list = []
    warning_list = []
    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        try:
            # ��ÿ��gdb��Ϊ������
            arcpy.env.workspace = workspace
            old_fc_list = arcpy.ListFeatureClasses()

            gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])

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

            temp_name1 = getNewFileNameQ(out_path, os.path.basename(workspace))
            result_gdb = os.path.join(out_path, temp_name1)
            if not arcpy.Exists(result_gdb):
                arcpy.AddMessage("�½� " + result_gdb + " ...")
                arcpy.CreateFileGDB_management(out_path, temp_name1)
            else:
                arcpy.AddWarning(result_gdb + u" �Ѵ��ڣ�")
                warning_list.append(result_gdb)
                warning += 1
                continue

            fc_count = 0
            for old_fc in old_fc_list:
                fc_count += 1
                arcpy.AddMessage("    "+ str(fc_count) + "��" + old_fc)
                in_fc_path = os.path.join(workspace, old_fc)
                consult_fc_path = os.path.join(consult_gdb_pathp,old_fc)
                if arcpy.Exists(consult_fc_path):
                    erase_output = os.path.join(result_gdb, old_fc)
                    arcpy.AddMessage("  " + in_fc_path + " �ཻ  " + consult_fc_path + " ..." )
                    # arcpy.Erase_analysis(in_fc_path, consult_fc_path, erase_output, "0.001 Meters")
                    arcpy.Intersect_analysis([in_fc_path, consult_fc_path], erase_output)
                else:
                    arcpy.AddWarning("***������" + consult_fc_path + "���������κβ�������ȷ���������ݵ�ͼ���Ƿ�����һ�£�")
                    warning_list.append(consult_fc_path)

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " ʧ�ܣ�")
            fail_list.append(workspace)
            fail += 1

    arcpy.AddMessage('+'*60)
    arcpy.AddMessage(u"  �ɹ���" + str(cout - fail - warning) + u" ����")
    if warning > 0:
        arcpy.AddWarning(u"  ���棺" + str(warning) + u" ���� ���£�")
        arcpy.AddWarning("####" + '*' * 20)
        for fff in warning_list:
            arcpy.AddWarning("  " + fff)
        arcpy.AddWarning("####" + '*' * 20)
    if fail > 0:
        arcpy.AddError(u"  ʧ�ܣ�" + str(fail) + u" ���� ���£�")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)


if __name__ == "__main__":
    old_pathG = arcpy.GetParameterAsText(0)#ԭָ��ͼ��
    new_pathG = arcpy.GetParameterAsText(1)#��ָ��ͼ��
    out_pathG = arcpy.GetParameterAsText(2)

    SuperpositionAnalysis(old_pathG,new_pathG,out_pathG)

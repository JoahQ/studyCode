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
        a = ("宜耕农用地潜力调查图斑" in fc or "宜耕未利用地潜力调查图斑" in fc or "建设用地复垦潜力调查图斑" in fc
             or "耕地提质改造潜力调查图斑" in fc or "自主提取潜力" in fc)
        b = (u"宜耕农用地潜力调查图斑" in fc or u"宜耕未利用地潜力调查图斑" in fc or u"建设用地复垦潜力调查图斑" in fc
             or u"耕地提质改造潜力调查图斑" in fc or "自主提取潜力" in fc)
        if a or b:
            in_fc_list.append(os.path.join(arcpy.env.workspace, fc))
        else:
            right_name = False
            arcpy.AddError("    \"" + fc + "\" 图层命名不规范！！！")
    dataset_ls = arcpy.ListDatasets()
    for dataset in dataset_ls:
        arcpy.env.workspace = os.path.join(in_gdb, dataset)
        fc_ls = arcpy.ListFeatureClasses()
        for fc in fc_ls:
            null_layer = False
            a = ("宜耕农用地潜力调查图斑" in fc or "宜耕未利用地潜力调查图斑" in fc or "建设用地复垦潜力调查图斑" in fc
                 or "耕地提质改造潜力调查图斑" in fc or "自主提取潜力" in fc)
            b = (u"宜耕农用地潜力调查图斑" in fc or u"宜耕未利用地潜力调查图斑" in fc or u"建设用地复垦潜力调查图斑" in fc
                 or u"耕地提质改造潜力调查图斑" in fc or "自主提取潜力" in fc)
            if a or b:
                in_fc_list.append(os.path.join(arcpy.env.workspace, fc))
            else:
                right_name = False
                arcpy.AddError("    \"" + fc + "\" 图层命名不规范！！！")

    if len(fc_lists) > 0:
        null_layer = False
    if not right_name:
        arcpy.AddError("数据库：" + in_gdb + " 图层命名不规范！！！")
        arcpy.AddMessage("-" * 25)
        arcpy.AddMessage("  标准的图层名称应该为：")
        arcpy.AddMessage("     耕地提质改造潜力调查图斑")
        arcpy.AddMessage("     建设用地复垦潜力调查图斑")
        arcpy.AddMessage("     宜耕农用地潜力调查图斑")
        arcpy.AddMessage("     宜耕未利用地潜力调查图斑")
        arcpy.AddMessage("-"*25)
    if null_layer:
        arcpy.AddError("数据库：" + in_gdb + " 为空或者已损坏，无法打开！！！")
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
    arcpy.AddField_management(fci_path, field_name1, "TEXT", "#", "#", 255, "变化类型")
    arcpy.CalculateField_management(fci_path, field_name1, "'" + txt_string + "'", "PYTHON_9.3", "")

def SuperpositionAnalysis(in_path,consult_path, out_path, sql_clause):

    arcpy.env.workspace = consult_path#新指引图斑路径
    arcpy.AddMessage("..." * 12)
    consult_gdb_list = arcpy.ListWorkspaces("*", "FileGDB")
    arcpy.AddMessage("检查 " + consult_path + " 路径下gdb的图层命名是否正确...")
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
        arcpy.AddError("  图层命名错误：" + str(fail) + " 个！ 如下：")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)

    arcpy.env.workspace = in_path#原指引图斑路径
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")
    arcpy.AddMessage("..."*12)
    arcpy.AddMessage("检查 " + in_path + " 路径下gdb的图层命名是否正确...")
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
        arcpy.AddError("  图层命名错误：" + str(fail) + " 个！ 如下：")
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
    change_folder_path1 = os.path.join(out_path, "有变化的部分")
    if not arcpy.Exists(change_folder_path1):
        arcpy.CreateFolder_management(out_path, "有变化的部分")

    nochangefolder_path2 = os.path.join(out_path, "原指引图斑图形和属性都没变化的图斑")
    if not arcpy.Exists(nochangefolder_path2):
        arcpy.CreateFolder_management(out_path, "原指引图斑图形和属性都没变化的图斑")

    newchangefolder_path = os.path.join(out_path, "新指引图斑变化了的图斑")
    if not arcpy.Exists(newchangefolder_path):
        arcpy.CreateFolder_management(out_path, "新指引图斑变化了的图斑")

    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        try:
            # 将每个gdb设为工作区
            arcpy.env.workspace = workspace
            old_fc_list = arcpy.ListFeatureClasses()
            arcpy.AddMessage(" ... ")
            temp_name1 = getNewFileNameQ(out_path, "过程数据" + os.path.basename(workspace))
            result_gdb = os.path.join(out_path, temp_name1)
            arcpy.AddMessage(" 新建 " + result_gdb + " ...")
            arcpy.AddMessage("  " + temp_name1 + " ...")
            arcpy.CreateFileGDB_management(out_path, temp_name1)

            gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])

            change_merge = getNewFileNameQ(change_folder_path1, gdbName + "变化的部分.gdb")
            change_merge_gdb = os.path.join(change_folder_path1, change_merge)
            arcpy.AddMessage("  新建 " + change_merge_gdb + " ...")
            arcpy.AddMessage("   " + change_merge + " ...")
            arcpy.CreateFileGDB_management(change_folder_path1, change_merge)

            nochange = getNewFileNameQ(nochangefolder_path2, gdbName + "没变化的图斑.gdb")
            nochange_gdb = os.path.join(nochangefolder_path2, nochange)
            arcpy.AddMessage("  新建 " + nochange_gdb + " ...")
            arcpy.AddMessage("   " + nochange + " ...")
            arcpy.CreateFileGDB_management(nochangefolder_path2, nochange)

            newchange = getNewFileNameQ(newchangefolder_path, gdbName + "变化了的图斑.gdb")
            newchange_gdb = os.path.join(newchangefolder_path, newchange)
            arcpy.AddMessage("  新建 " + newchange_gdb + " ...")
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
                arcpy.AddError("  " + os.path.basename(workspace) + " 失败！找不到对应的参考数据！")
                fail += 1
                fail_list.append(workspace)
                continue
            fc_count = 0
            for old_fc in old_fc_list:
                fc_count += 1
                arcpy.AddMessage("    "+ str(fc_count) + "、" + old_fc)
                old_fc_path = os.path.join(workspace, old_fc)
                new_fc_path = os.path.join(consult_gdb_pathp,old_fc)
                if arcpy.Exists(new_fc_path):
                    old_erase_output = os.path.join(result_gdb, old_fc + "减少的")
                    arcpy.AddMessage("       原指引图斑的 " + old_fc + " 图层 擦除 新指引图斑的 " + old_fc + " 图层得出减少的部分..." )
                    arcpy.Erase_analysis(old_fc_path, new_fc_path, old_erase_output, "0.001 Meters")
                    AddAndCalculateField(old_erase_output,"减少的部分")

                    new_erase_output = os.path.join(result_gdb, old_fc + "新增的")
                    arcpy.AddMessage("       新指引图斑的 " + old_fc + " 图层 擦除 原指引图斑的 " + old_fc + " 图层得出减少的部分..." )
                    arcpy.Erase_analysis(new_fc_path, old_fc_path, new_erase_output, "0.001 Meters")
                    AddAndCalculateField(new_erase_output, "新增的部分")

                    intersect1_path = os.path.join(result_gdb, "相交结果" + old_fc)
                    arcpy.AddMessage("       原指引图斑的 " + old_fc + " 与 新指引图斑的 " + old_fc + " 相交..." )
                    arcpy.Intersect_analysis([old_fc_path, new_fc_path], intersect1_path,"NO_FID")

                    select_out_fc = os.path.join(result_gdb, old_fc + "属性变化的")
                    arcpy.AddMessage("       相交后筛选出" + sql_clause + " ..." )
                    arcpy.Select_analysis(intersect1_path, select_out_fc, sql_clause)
                    AddAndCalculateField(select_out_fc, "属性变化的部分")

                    arcpy.AddMessage("       属性变化的部分和图形变化的部分合并 ..." )
                    change_merge_fc = os.path.join(result_gdb, "合并" + old_fc)
                    mul_to_sgl = os.path.join(change_merge_gdb, old_fc)
                    arcpy.Merge_management([old_erase_output,new_erase_output,select_out_fc],change_merge_fc)
                    arcpy.MultipartToSinglepart_management(change_merge_fc, mul_to_sgl)

                    arcpy.AddMessage("       原指引图斑筛选出图形范围和属性都没有变化的图斑 ..." )
                    in_feature_point = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "FeatureToPoint" + old_fc))
                    arcpy.AddMessage("          变化部分转点 ..." )
                    arcpy.FeatureToPoint_management(mul_to_sgl, in_feature_point, "INSIDE")

                    arcpy.AddMessage("          原指引图斑按位置选择并导出 ..." )
                    in_layer_name = old_fc + str(int(time.time()))
                    arcpy.MakeFeatureLayer_management(old_fc_path, in_layer_name)
                    arcpy.SelectLayerByLocation_management(in_layer_name, "INTERSECT", in_feature_point, "", "NEW_SELECTION")
                    old_change_path = os.path.join(result_gdb, old_fc + "原指引图斑变化的图斑")
                    arcpy.FeatureClassToFeatureClass_conversion(in_layer_name, result_gdb, old_fc + "原指引图斑变化的图斑")
                    arcpy.SelectLayerByLocation_management(in_layer_name, "", "", "", "SWITCH_SELECTION")
                    arcpy.FeatureClassToFeatureClass_conversion(in_layer_name, nochange_gdb, old_fc)
                    arcpy.Delete_management(in_layer_name)

                    arcpy.AddMessage("       新指引图斑筛选出相对于原指引图斑变化了的完整的图斑（相交和擦除得到的可能只是图斑的一部分） ..." )
                    arcpy.AddMessage("          新指引图斑按位置选择并导出 ..." )
                    in_layer_name1 = old_fc + str(int(time.time()))
                    arcpy.MakeFeatureLayer_management(new_fc_path, in_layer_name1)
                    arcpy.SelectLayerByLocation_management(in_layer_name1, "INTERSECT", in_feature_point, "", "NEW_SELECTION")
                    arcpy.SelectLayerByLocation_management(in_layer_name1, "WITHIN", old_change_path, "", "ADD_TO_SELECTION")
                    arcpy.FeatureClassToFeatureClass_conversion(in_layer_name1, newchange_gdb, old_fc)
                    arcpy.Delete_management(in_layer_name1)
                else:
                    arcpy.AddWarning("***不存在" + new_fc_path + "，不进行任何操作！请确认两套数据的图层是否命名一致！")

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " 失败！")
            fail_list.append(workspace)
            fail += 1

    arcpy.AddMessage('+'*60)
    arcpy.AddMessage("  成功：" + str(cout - fail) + " 个！")
    if fail > 0:
        arcpy.AddError("  失败：" + str(fail) + " 个！ 如下：")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)


if __name__ == "__main__":
    old_pathG = arcpy.GetParameterAsText(0)#原指引图斑
    new_pathG = arcpy.GetParameterAsText(1)#新指引图斑
    out_pathG = arcpy.GetParameterAsText(2)
    where_cluase = arcpy.GetParameterAsText(3)

    if where_cluase == " " or where_cluase == "#":
        where_c = """DLBM <> DLBM_1 OR XZQMC <> XZQMC_1 OR QSXZ <> QSXZ_1 OR DLMC <> DLMC_1 OR GDLX <> GDLX_1 OR ZZSXMC <> ZZSXMC_1 OR
 TBXHMC <> TBXHMC_1"""
    SuperpositionAnalysis(old_pathG,new_pathG,out_pathG,where_cluase)

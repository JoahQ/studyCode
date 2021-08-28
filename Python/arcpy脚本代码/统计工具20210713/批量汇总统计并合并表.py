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

def checkLayerNameAndGetPathQ(in_gdb):
    arcpy.env.workspace = in_gdb
    in_fc_list = []
    fc_lists = arcpy.ListFeatureClasses()
    right_name = True
    null_layer = True
    for fc in fc_lists:
        a = ("农用" in fc or "未利" in fc or "建设" in fc or "提质改造" in fc or "自主提取" in fc)
        b = (u"农用" in fc or u"未利" in fc or u"建设" in fc or u"提质改造" in fc or "自主提取" in fc)
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
            a = ("农用" in fc or "未利" in fc or "建设" in fc or "提质改造" in fc or "自主提取" in fc)
            b = (u"农用" in fc or u"未利" in fc or u"建设" in fc or u"提质改造" in fc or "自主提取" in fc)
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
        arcpy.AddMessage("     自主提取潜力调查图斑")
        arcpy.AddMessage("-" * 25)
    if null_layer:
        arcpy.AddError("数据库：" + in_gdb + " 为空或者已损坏，无法打开！！！")
        right_name = False
    return [right_name, in_fc_list]

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

def statisticsArea1(in_path, out_path, statistics_fields, case_fields, name):
    cout = 0
    fail = 0
    fail_list = []

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")
    if len(workspaces) <= 0:
        right_name_path = checkLayerNameAndGetPathQ(in_path)
        if not right_name_path[0]:
            fail += 1
            fail_list.append(os.path.basename(in_path))
            arcpy.AddError("||||" + "*" * 20)
            arcpy.AddError(" <" + str(fail) + "> " + os.path.basename(in_path) + " 失败！")
            arcpy.AddError("||||" + "*" * 20)
            sys.exit()
        workspaces = [in_path]
    temp_name1 = getNewFileNameQ(out_path, "result.gdb")
    result_gdb = os.path.join(out_path, temp_name1)
    arcpy.AddMessage("新建 " + result_gdb + " 用于保存结果属性表和过程数据...")
    arcpy.CreateFileGDB_management(out_path, temp_name1)

    folder_path = os.path.join(out_path, "合并")
    if not arcpy.Exists(folder_path):
        arcpy.CreateFolder_management(out_path, "合并")

    merge_name = getNewFileNameQ(folder_path, "合并.gdb")
    merge_gdb = os.path.join(folder_path, merge_name)
    arcpy.CreateFileGDB_management(folder_path, merge_name)
    table_lists = []
    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        # 将每个gdb设为工作区
        arcpy.env.workspace = workspace
        gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])

        right_name_path = checkLayerNameAndGetPathQ(workspace)
        if not right_name_path[0]:
            fail += 1
            fail_list.append(workspace)
            arcpy.AddError("||||" + "*" * 20)
            arcpy.AddError(" <" + str(fail) + "> " + os.path.basename(workspace) + " 失败！")
            arcpy.AddError("||||" + "*" * 20)
            continue
        try:
            merge_fc_path = os.path.join(merge_gdb, "合并" + gdbName)
            merge_table_path = os.path.join(result_gdb,"汇总统计" + gdbName)
            arcpy.Merge_management(right_name_path[1],merge_fc_path)
            #[["Shape_Area", "SUM"]]
            arcpy.Statistics_analysis(merge_fc_path, merge_table_path, statistics_fields, case_fields)
            table_lists.append(merge_table_path)
        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("      " + os.path.basename(workspace) + " 失败！")
            fail += 1

    try:
        table_lists_merge = os.path.join(result_gdb,"a所有统计表合并")

        hb_name1 = getNewFileNameQ(out_path, name + ".gdb")
        hb_gdb = os.path.join(out_path, hb_name1)
        arcpy.AddMessage("新建 " + hb_gdb + " 用于保存最终统计表合并结果...")
        arcpy.CreateFileGDB_management(out_path, hb_name1)

        arcpy.AddMessage("正在合并汇总统计表...")
        arcpy.Merge_management(table_lists, table_lists_merge)

        arcpy.TableToTable_conversion(table_lists_merge,hb_gdb,name)

    except Exception as e:
        arcpy.AddError(e.message)
        arcpy.AddError("      合并统计表时失败！")
        a = []
        print a[999]

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
    in_pathG = arcpy.GetParameterAsText(0)
    out_pathG = arcpy.GetParameterAsText(1)
    nameG = arcpy.GetParameterAsText(2)
    case_fieldsG = arcpy.GetParameterAsText(3)



    asa123 = re.findall(r"[^()\[\]{},.*/|\\:;?\'\"<>%!@#$&]", nameG)
    name11 = "".join(asa123)
    table_name = name11.lstrip(string.digits)
    if table_name == '':
        table_name = "Table" + nameG
    arcpy.AddMessage("输入路径: " + in_pathG)
    arcpy.AddMessage("输出路径: " + out_pathG)
    arcpy.AddMessage("分组字段: " + case_fieldsG)
    arcpy.AddMessage("合并后的表名: " + table_name)
    arcpy.AddMessage("--" *30)


    statisticsArea1(in_pathG, out_pathG, [["Shape_Area", "SUM"]], case_fieldsG,table_name)
    #GDHBZY;XDM;XMC;DLBM;DLMC;PDJB;ZZSXMC;GGSY;GGTJ;PSTJ;TCHD;TRLX;JTZK;PDFF;PJJG;YKDL;TBLX;BZ

    arcpy.AddMessage("--" *30)
    arcpy.AddMessage("输入路径: " + in_pathG)
    arcpy.AddMessage("输出路径: " + out_pathG)
    arcpy.AddMessage("分组字段: " + case_fieldsG)
    arcpy.AddMessage("合并后的表名: " + table_name)

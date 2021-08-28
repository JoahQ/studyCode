# -*- coding: gbk -*-
import sys
import arcpy
import os

reload(sys)
sys.setdefaultencoding("utf-8")

def checkFeatureClassName(in_workspace_cfn):
    arcpy.env.workspace = in_workspace_cfn
    fc_lists = arcpy.ListFeatureClasses()
    right_name = True
    ls1 = ["耕地提质改造潜力调查图斑", "建设用地复垦潜力调查图斑", "宜耕农用地潜力调查图斑", "宜耕未利用地潜力调查图斑", "自主提取潜力图斑"]
    ls2 = [u"耕地提质改造潜力调查图斑",u"建设用地复垦潜力调查图斑",u"宜耕农用地潜力调查图斑",u"宜耕未利用地潜力调查图斑",u"自主提取潜力图斑"]
    for fc in fc_lists:
        if not (fc in ls1 or fc in ls2):
            right_name = False
            arcpy.AddError("    \"" + fc + "\" 图层命名不规范！！！")
    if len(fc_lists) <= 0:
        right_name = False
        arcpy.AddError("数据库：" + in_workspace_cfn + " 没有图层！！！")
    if not right_name:
        arcpy.AddError("数据库：" + in_workspace_cfn + " 图层命名不规范！！！")
        arcpy.AddMessage("-" * 25)
        arcpy.AddMessage("  标准的图层名称应该为：")
        arcpy.AddMessage("     耕地提质改造潜力调查图斑")
        arcpy.AddMessage("     建设用地复垦潜力调查图斑")
        arcpy.AddMessage("     宜耕农用地潜力调查图斑")
        arcpy.AddMessage("     宜耕未利用地潜力调查图斑")
        arcpy.AddMessage("     自主提取潜力图斑")
        arcpy.AddMessage("-"*25)

    return right_name

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

def mergeFeatureClass(in_path, out_path, name):

    arcpy.env.workspace = in_path
    # 获取工作区内的gdb列表
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")
    list_fcs1 = []
    list_fcs2 = []
    list_fcs3 = []
    list_fcs4 = []
    list_fcs5 = []
    cout = 0
    fail = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    for workspace in workspaces:
        right = checkFeatureClassName(workspace)
        if right:
            continue
        else:
            fail += 1
            arcpy.AddError(u"     " + os.path.basename(workspace) + u" 失败！")


    if fail > 0:
        list0 = []
        print list0[99999999]
        sys.exit()
    
    namegdb = getNewFileNameQ(out_path, name + ".gdb")
    arcpy.CreateFileGDB_management(out_path, namegdb)
    outgdb_path = os.path.join(out_path, namegdb)
    for workspace in workspaces:
        cout += 1
        arcpy.AddMessage(str(cout) + "、" + os.path.basename(workspace))
        arcpy.env.workspace = workspace
        fc_lista = arcpy.ListFeatureClasses()
        for fac in fc_lista:
            clsPath = os.path.join(workspace, fac)

            if "提质改造" in fac:
                list_fcs1.append(clsPath)

            elif "建设用地" in fac:
                list_fcs2.append(clsPath)

            elif "农用地" in fac:
                list_fcs3.append(clsPath)

            elif "未利用地" in fac:
                list_fcs4.append(clsPath)

            elif "自主提取" in fac:
                list_fcs5.append(clsPath)


    out_path1 = os.path.join(outgdb_path, u"耕地提质改造潜力调查图斑")
    out_path2 = os.path.join(outgdb_path, u"建设用地复垦潜力调查图斑")
    out_path3 = os.path.join(outgdb_path, u"宜耕农用地潜力调查图斑")
    out_path4 = os.path.join(outgdb_path, u"宜耕未利用地潜力调查图斑")
    out_path5 = os.path.join(outgdb_path, u"自主提取潜力图斑")

    arcpy.AddMessage("  ")
    arcpy.AddMessage(u"找到" + str(cout) + u" 个gdb。\n ")
    arcpy.AddMessage(u"开始合并...")
    arcpy.AddMessage("  ")
    arcpy.AddMessage("-" * 20)

    if len(list_fcs1) > 0:
        try:
            arcpy.AddMessage(u"正在合并耕地提质改造潜力调查图斑...")
            arcpy.Merge_management(list_fcs1, out_path1)
        except Exception as e:
            arcpy.AddError(e.message)

    if len(list_fcs2) > 0:
        try:
            arcpy.AddMessage(u"正在合并建设用地复垦潜力调查图斑...")
            arcpy.Merge_management(list_fcs2, out_path2)
        except Exception as e:
            arcpy.AddError(e.message)

    if len(list_fcs3) > 0:
        try:
            arcpy.AddMessage(u"正在合并宜耕农用地潜力调查图斑...")
            arcpy.Merge_management(list_fcs3, out_path3)
        except Exception as e:
            arcpy.AddError(e.message)

    if len(list_fcs4) > 0:
        try:
            arcpy.AddMessage(u"正在合并宜耕未利用地潜力调查图斑...")
            arcpy.Merge_management(list_fcs4, out_path4)
        except Exception as e:
            arcpy.AddError(e.message)

    if len(list_fcs5) > 0:
        try:
            arcpy.AddMessage(u"正在合并自主提取潜力图斑...")
            arcpy.Merge_management(list_fcs5, out_path5)
        except Exception as e:
            arcpy.AddError(e.message)

    arcpy.AddMessage(" ")
    if arcpy.Exists(out_path1):
        arcpy.AddMessage(u"耕地提质改造潜力调查图斑 合并后图斑数：" + str(arcpy.GetCount_management(out_path1).getOutput(0)))
    if arcpy.Exists(out_path2):
        arcpy.AddMessage(u"建设用地复垦潜力调查图斑 合并后图斑数：" + str(arcpy.GetCount_management(out_path2).getOutput(0)))
    if arcpy.Exists(out_path3):
        arcpy.AddMessage(u"宜耕农用地潜力调查图斑 合并后图斑数：" + str(arcpy.GetCount_management(out_path3).getOutput(0)))
    if arcpy.Exists(out_path4):
        arcpy.AddMessage(u"宜耕未利用地潜力调查图斑 合并后图斑数：" + str(arcpy.GetCount_management(out_path4).getOutput(0)))
    if arcpy.Exists(out_path5):
        arcpy.AddMessage(u"自主提取潜力图斑 合并后图斑数：" + str(arcpy.GetCount_management(out_path5).getOutput(0)))


if __name__ == "__main__":

    in_pathgg = arcpy.GetParameterAsText(0)
    out_pathgg = arcpy.GetParameterAsText(1)
    namegg = arcpy.GetParameterAsText(2)
    anshifang = arcpy.GetParameter(3)
    fendai = arcpy.GetParameter(4)

    if anshifang:
        city_list = [u"01南宁市", u"02柳州市", u"03桂林市", u"04梧州市", u"05北海市", u"06防城港市", u"07钦州市", u"08贵港市",
                     u"09玉林市", u"10百色市", u"11贺州市", u"12河池市", u"13来宾市", u"14崇左市"]
        for city in city_list:
            in_pathcc = os.path.join(in_pathgg, city)
            if not arcpy.Exists(in_pathcc):
                arcpy.CreateFolder_management(in_pathgg, city)
            arcpy.AddMessage(" ")
            arcpy.AddMessage(city)
            if arcpy.Exists(in_pathcc):
                arcpy.AddMessage("+" * 60)
                mergeFeatureClass(in_pathcc, out_pathgg, city + u"合并")
                arcpy.AddMessage("+"*60)
            else:
                arcpy.AddMessage(in_pathcc + u" 不存在！")
                arcpy.AddMessage(" ")
    elif fendai:
        fffddd = ["35","36","37"]
        for fdf in fffddd:
            in_pathcc = os.path.join(in_pathgg, fdf)
            arcpy.AddMessage("  " * 20)
            mergeFeatureClass(in_pathcc, out_pathgg, fdf + u"合并")
            arcpy.AddMessage("+"*20)
    else:
        mergeFeatureClass(in_pathgg, out_pathgg, namegg)





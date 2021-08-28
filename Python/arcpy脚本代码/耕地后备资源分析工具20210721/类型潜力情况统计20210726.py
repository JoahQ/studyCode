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
        arcpy.AddMessage("-"*25)
    if null_layer:
        arcpy.AddError("数据库：" + in_gdb + " 为空或者已损坏，无法打开！！！")
        right_name = False
    return [right_name, in_fc_list]

def xzqab(e):
    if e == "450102":
        return "兴宁区"
    elif e == "450103":
        return "青秀区"
    elif e == "450105":
        return "江南区"
    elif e == "450107":
        return "西乡塘区"
    elif e == "450108":
        return "良庆区"
    elif e == "450109":
        return "邕宁区"
    elif e == "450110":
        return "武鸣区"
    elif e == "450123":
        return "隆安县"
    elif e == "450124":
        return "马山县"
    elif e == "450125":
        return "上林县"
    elif e == "450126":
        return "宾阳县"
    elif e == "450127":
        return "横县"
    elif e == "4502":
        return "柳州市"
    elif e == "450202":
        return "城中区"
    elif e == "450203":
        return "鱼峰区"
    elif e == "450204":
        return "柳南区"
    elif e == "450205":
        return "柳北区"
    elif e == "450206":
        return "柳江区"
    elif e == "450222":
        return "柳城县"
    elif e == "450223":
        return "鹿寨县"
    elif e == "450224":
        return "融安县"
    elif e == "450225":
        return "融水苗族自治县"
    elif e == "450226":
        return "三江侗族自治县"
    elif e == "4503":
        return "桂林市"
    elif e == "450302":
        return "秀峰区"
    elif e == "450303":
        return "叠彩区"
    elif e == "450304":
        return "象山区"
    elif e == "450305":
        return "七星区"
    elif e == "450311":
        return "雁山区"
    elif e == "450312":
        return "临桂区"
    elif e == "450321":
        return "阳朔县"
    elif e == "450323":
        return "灵川县"
    elif e == "450324":
        return "全州县"
    elif e == "450325":
        return "兴安县"
    elif e == "450326":
        return "永福县"
    elif e == "450327":
        return "灌阳县"
    elif e == "450328":
        return "龙胜各族自治县"
    elif e == "450329":
        return "资源县"
    elif e == "450330":
        return "平乐县"
    elif e == "450332":
        return "恭城瑶族自治县"
    elif e == "450381":
        return "荔浦市"
    elif e == "4504":
        return "梧州市"
    elif e == "450403":
        return "万秀区"
    elif e == "450405":
        return "长洲区"
    elif e == "450406":
        return "龙圩区"
    elif e == "450421":
        return "苍梧县"
    elif e == "450422":
        return "藤县"
    elif e == "450423":
        return "蒙山县"
    elif e == "450481":
        return "岑溪市"
    elif e == "4505":
        return "北海市"
    elif e == "450502":
        return "海城区"
    elif e == "450503":
        return "银海区"
    elif e == "450512":
        return "铁山港区"
    elif e == "450521":
        return "合浦县"
    elif e == "4506":
        return "防城港市"
    elif e == "450602":
        return "港口区"
    elif e == "450603":
        return "防城区"
    elif e == "450621":
        return "上思县"
    elif e == "450681":
        return "东兴市"
    elif e == "4507":
        return "钦州市"
    elif e == "450702":
        return "钦南区"
    elif e == "450703":
        return "钦北区"
    elif e == "450721":
        return "灵山县"
    elif e == "450722":
        return "浦北县"
    elif e == "4508":
        return "贵港市"
    elif e == "450802":
        return "港北区"
    elif e == "450803":
        return "港南区"
    elif e == "450804":
        return "覃塘区"
    elif e == "450821":
        return "平南县"
    elif e == "450881":
        return "桂平市"
    elif e == "4509":
        return "玉林市"
    elif e == "450902":
        return "玉州区"
    elif e == "450903":
        return "福绵区"
    elif e == "450921":
        return "容县"
    elif e == "450922":
        return "陆川县"
    elif e == "450923":
        return "博白县"
    elif e == "450924":
        return "兴业县"
    elif e == "450981":
        return "北流市"
    elif e == "4510":
        return "百色市"
    elif e == "451002":
        return "右江区"
    elif e == "451003":
        return "田阳市"
    elif e == "451022":
        return "田东县"
    elif e == "451082":
        return "平果县"
    elif e == "451024":
        return "德保县"
    elif e == "451026":
        return "那坡县"
    elif e == "451027":
        return "凌云县"
    elif e == "451028":
        return "乐业县"
    elif e == "451029":
        return "田林县"
    elif e == "451030":
        return "西林县"
    elif e == "451031":
        return "隆林各族自治县"
    elif e == "451081":
        return "靖西市"
    elif e == "4511":
        return "贺州市"
    elif e == "451102":
        return "八步区"
    elif e == "451103":
        return "平桂区"
    elif e == "451121":
        return "昭平县"
    elif e == "451122":
        return "钟山县"
    elif e == "451123":
        return "富川瑶族自治县"
    elif e == "4512":
        return "河池市"
    elif e == "451202":
        return "金城江区"
    elif e == "451203":
        return "宜州区"
    elif e == "451221":
        return "南丹县"
    elif e == "451222":
        return "天峨县"
    elif e == "451223":
        return "凤山县"
    elif e == "451224":
        return "东兰县"
    elif e == "451225":
        return "罗城仫佬族自治县"
    elif e == "451226":
        return "环江毛南族自治县"
    elif e == "451227":
        return "巴马瑶族自治县"
    elif e == "451228":
        return "都安瑶族自治县"
    elif e == "451229":
        return "大化瑶族自治县"
    elif e == "4513":
        return "来宾市"
    elif e == "451302":
        return "兴宾区"
    elif e == "451321":
        return "忻城县"
    elif e == "451322":
        return "象州县"
    elif e == "451323":
        return "武宣县"
    elif e == "451324":
        return "金秀瑶族自治县"
    elif e == "451381":
        return "合山市"
    elif e == "4514":
        return "崇左市"
    elif e == "451402":
        return "江州区"
    elif e == "451421":
        return "扶绥县"
    elif e == "451422":
        return "宁明县"
    elif e == "451423":
        return "龙州县"
    elif e == "451424":
        return "大新县"
    elif e == "451425":
        return "天等县"
    elif e == "451481":
        return "凭祥市"
    else:
        return e
    
def createTableQ(path, name):
    """
    新建表格，arcgis属性表，已指定固定字段
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
    # 用字典设置字段属性，用列表存放所有字段
    field_list = [{'name': 'cout', 'type': 'TEXT', 'alias': '序号'},  #0
                  {'name': 'XZQ', 'type': 'TEXT', 'alias': '行政区'},  #0

                  {'name': 'A2', 'type': 'DOUBLE', 'alias': '总计'},  #1
                  {'name': 'B3', 'type': 'DOUBLE', 'alias': '宜耕农用地潜力-小计'},  #2
                  {'name': 'C4', 'type': 'DOUBLE', 'alias': '宜耕农用地潜力-工程恢复'},  #3
                  {'name': 'D5', 'type': 'DOUBLE', 'alias': '宜耕农用地潜力-即可恢复'},  #4

                  {'name': 'E6', 'type': 'DOUBLE', 'alias': '农用地未标注恢复属性-小计'},  #5
                  {'name': 'F7', 'type': 'DOUBLE', 'alias': '农用地未标注恢复属性-圆地'},  #6
                  {'name': 'G8', 'type': 'DOUBLE', 'alias': '农用地未标注恢复属性-林地'},  #7
                  {'name': 'H9', 'type': 'DOUBLE', 'alias': '农用地未标注恢复属性-草地'},  #8
                  {'name': 'I10', 'type': 'DOUBLE', 'alias': '农用地未标注恢复属性-坑塘水面'},  #9

                  {'name': 'J11', 'type': 'DOUBLE', 'alias': '建设用地-小计'},  #10
                  {'name': 'K12', 'type': 'DOUBLE', 'alias': '建设用地-工业用地'},  #11
                  {'name': 'L13', 'type': 'DOUBLE', 'alias': '建设用地-采矿用地'},  #12
                  {'name': 'M14', 'type': 'DOUBLE', 'alias': '建设用地-农村建设用地'},  #13

                  {'name': 'N15', 'type': 'DOUBLE', 'alias': '未利用地-小计'},  #14
                  {'name': 'O16', 'type': 'DOUBLE', 'alias': '未利用地-草地'},  #15
                  {'name': 'P17', 'type': 'DOUBLE', 'alias': '未利用地-内陆滩涂'},  #16
                  {'name': 'Q18', 'type': 'DOUBLE', 'alias': '未利用地-裸地'},  #17
                  {'name': 'R19', 'type': 'DOUBLE', 'alias': '未利用地-沙地'},  #18
                  {'name': 'BR20', 'type': 'DOUBLE', 'alias': '未利用地-沿海滩涂'},  #19
                  {'name': 'CR21', 'type': 'DOUBLE', 'alias': '未利用地-盐碱地'},  #20

                  {'name': 'S22', 'type': 'DOUBLE', 'alias': '提质改造-小计'},  #21
                  {'name': 'T23', 'type': 'DOUBLE', 'alias': '提质改造-工程恢复'},  #22
                  {'name': 'U24', 'type': 'DOUBLE', 'alias': '提质改造-即可恢复'},  #23
                  {'name': 'V25', 'type': 'DOUBLE', 'alias': '提质改造-耕地-小计'},  #24
                  {'name': 'W26', 'type': 'DOUBLE', 'alias': '提质改造-耕地-水浇地'},  #25
                  {'name': 'X27', 'type': 'DOUBLE', 'alias': '提质改造-耕地-旱地'},  #26
                 
                  {'name': 'Y28', 'type': 'DOUBLE', 'alias': '自主提取-合计'},  #27
                  {'name': 'Z29', 'type': 'DOUBLE', 'alias': '自主提取-宜耕农用地潜力调查图斑'},  #28
                  {'name': 'AA30', 'type': 'DOUBLE', 'alias': '自主提取-宜耕未利用地潜力调查图斑'},  #29
                  {'name': 'AB31', 'type': 'DOUBLE', 'alias': '自主提取-建设用地复垦潜力调查图斑'},  #30
                  {'name': 'AC32', 'type': 'DOUBLE', 'alias': '自主提取-耕地提质改造潜力调查图斑'},  #31
                  ]

    arcpy.AddMessage("新建 " + table_name + " 表格...")
    arcpy.CreateTable_management(path, table_name)
    arcpy.AddMessage("  添加字段...")
    arcpy.AddMessage("-" * 50)
    for field in field_list:
        # arcpy.AddMessage("    字段名： " + field['name'] + " 字段别名： " + field['alias'])
        arcpy.AddField_management(tb_path, field['name'], field['type'], "#", "#", "#", field['alias'])
        field_ls.append(field['name'])
    arcpy.AddMessage("-"*50)
    return [tb_path, field_ls]

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

def statisticsAreaQ3(in_path, out_path, where_clause, name):
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

    # 建gdb
    resultg_name = getNewFileNameQ(out_path, name + "_result.gdb")
    result_gdb = os.path.join(out_path, resultg_name)
    arcpy.AddMessage("新建 " + result_gdb + " 用于保存结果...")
    arcpy.CreateFileGDB_management(out_path, resultg_name)

    # 建表
    arcpy.AddMessage("-"*20 + "新建属性表" + "-"*20)
    tb_paths = createTableQ(result_gdb, getNewFileNameQ(result_gdb, name))

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

        xzqcode = re.findall(r"\d+", gdbName)
        if len(xzqcode) > 0 and not xzqab(xzqcode[0]).isdigit():

            row_values = [cout, xzqab(xzqcode[0]), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0]
        else:
            row_values = [cout,gdbName,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        try:
            for iin_fc_path in right_name_path[1]:
                fc = os.path.basename(iin_fc_path)
                arcpy.AddMessage("        " + fc)
                if "农" in fc or u"农" in fc:
                    out_featuren = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "N" +xzqcode[0]+xzqab(xzqcode[0])))
                    arcpy.Select_analysis(iin_fc_path, out_featuren, where_clause + u" like \'%是%\'")
                    nyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "nyd_table" + str(cout)))
                    arcpy.Statistics_analysis(out_featuren, nyd_tb1, [["Shape_Area", "SUM"]], ['DLBM','ZZSXMC'])
                    with arcpy.da.SearchCursor(nyd_tb1, ('DLBM','ZZSXMC', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "工程恢复" in str(row1[1]):
                                row_values[4] = row_values[4] + row1[2]
                            elif "即可恢复" in str(row1[1]):
                                row_values[5] = row_values[5] + row1[2]
                            else:
                                if "020" in str(row1[0]):
                                    row_values[7] = row_values[7] + row1[2]
                                if "030" in str(row1[0]):
                                    row_values[8] = row_values[8] + row1[2]
                                if "040" in str(row1[0]):
                                    row_values[9] = row_values[9] + row1[2]
                                if "1104" in str(row1[0]):
                                    row_values[10] = row_values[10] + row1[2]

                    if arcpy.Exists(out_featuren):
                        try:
                            arcpy.Delete_management(out_featuren)
                        except Exception as e:
                            arcpy.AddMessage(e.message)
                    if arcpy.Exists(nyd_tb1):
                        try:
                            arcpy.Delete_management(nyd_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

                elif "未利" in fc or u"未利" in fc:
                    out_featurew = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "W"+xzqcode[0]+xzqab(xzqcode[0])))
                    arcpy.Select_analysis(iin_fc_path, out_featurew, where_clause + u" like \'%是%\'")

                    wlyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "wlyd_table" + str(cout)))
                    arcpy.Statistics_analysis(out_featurew, wlyd_tb1, [["Shape_Area", "SUM"]], 'DLBM')
                    with arcpy.da.SearchCursor(wlyd_tb1, ('DLBM', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "040" in row1[0]:
                                row_values[16] = row_values[16] + row1[1]
                            if "1106" in row1[0]:
                                row_values[17] = row_values[17] + row1[1]
                            if "1206" in row1[0]:
                                row_values[18] = row_values[18] + row1[1]
                            if "1205" in row1[0]:
                                row_values[19] = row_values[19] + row1[1]
                            if "1105" in row1[0]:
                                row_values[20] = row_values[20] + row1[1]
                            if "1204" in row1[0]:
                                row_values[21] = row_values[21] + row1[1]

                    if arcpy.Exists(out_featurew):
                        try:
                            arcpy.Delete_management(out_featurew)
                        except Exception as e:
                            arcpy.AddMessage(e.message)
                    if arcpy.Exists(wlyd_tb1):
                        try:
                            arcpy.Delete_management(wlyd_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

                elif "建设" in fc or u"建设" in fc:
                    out_featureJ = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "J"+xzqcode[0]+xzqab(xzqcode[0])))
                    arcpy.Select_analysis(iin_fc_path, out_featureJ, where_clause + u" like \'%是%\'")

                    jsyd_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "jsyd_table" + str(cout)))
                    arcpy.Statistics_analysis(out_featureJ, jsyd_tb1, [["Shape_Area", "SUM"]], 'DLBM')
                    with arcpy.da.SearchCursor(jsyd_tb1, ('DLBM', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "0601" in row1[0]:
                                row_values[12] = row_values[12] + row1[1]
                            if "0602" in row1[0]:
                                row_values[13] = row_values[13] + row1[1]
                            if "0702" in row1[0]:
                                row_values[14] = row_values[14] + row1[1]

                    if arcpy.Exists(out_featureJ):
                        try:
                            arcpy.Delete_management(out_featureJ)
                        except Exception as e:
                            arcpy.AddMessage(e.message)
                    if arcpy.Exists(jsyd_tb1):
                        try:
                            arcpy.Delete_management(jsyd_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

                elif "提质改造" in fc or u"提质改造" in fc:
                    out_featureT = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "T"+xzqcode[0]+xzqab(xzqcode[0])))
                    arcpy.Select_analysis(iin_fc_path, out_featureT, where_clause + u" like \'%是%\'")

                    tzgz_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "tzgz_table" + str(cout)))
                    arcpy.Statistics_analysis(out_featureT, tzgz_tb1, [["Shape_Area", "SUM"]], ['DLBM','ZZSXMC'])
                    with arcpy.da.SearchCursor(tzgz_tb1, ('DLBM','ZZSXMC', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "工程恢复" in str(row1[1]):
                                row_values[23] = row_values[23] + row1[2]
                            if "即可恢复" in str(row1[1]):
                                row_values[24] = row_values[24] + row1[2]

                            if "0102" in str(row1[0]):
                                row_values[26] = row_values[26] + row1[2]
                            if "0103" in str(row1[0]):
                                row_values[27] = row_values[27] + row1[2]

                    if arcpy.Exists(out_featureT):
                        try:
                            arcpy.Delete_management(out_featureT)
                        except Exception as e:
                            arcpy.AddMessage(e.message)
                    if arcpy.Exists(tzgz_tb1):
                        try:
                            arcpy.Delete_management(tzgz_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

                elif "自主提取" in fc or u"自主提取" in fc:
                    zztq_tb1 = os.path.join(result_gdb, getNewFileNameQ(result_gdb, "zztq_table" + str(cout)))
                    arcpy.Statistics_analysis(iin_fc_path, zztq_tb1, [["Shape_Area", "SUM"]], 'GDHBZY')
                    with arcpy.da.SearchCursor(zztq_tb1, ('GDHBZY', 'SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "农用地" in str(row1[0]):
                                row_values[29] = row_values[29] + row1[1]
                            if "未利用地" in str(row1[0]):
                                row_values[30] = row_values[30] + row1[1]
                            if "建设用地" in str(row1[0]):
                                row_values[31] = row_values[31] + row1[1]
                            if "提质改造" in str(row1[0]):
                                row_values[32] = row_values[32] + row1[1]

                    if arcpy.Exists(zztq_tb1):
                        try:
                            arcpy.Delete_management(zztq_tb1)
                        except Exception as e:
                            arcpy.AddMessage(e.message)

            row_values[6] = row_values[7] + row_values[8] + row_values[9] + row_values[10]
            row_values[3] = row_values[4] + row_values[5] + row_values[6]
            row_values[11] = row_values[12] + row_values[13] + row_values[14]
            row_values[15] = row_values[16] + row_values[17] + row_values[18] + row_values[19] + row_values[20] + row_values[21]
            row_values[22] = row_values[23] + row_values[24]
            row_values[25] = row_values[26] + row_values[27]
            row_values[28] = row_values[29] + row_values[30] + row_values[31] + row_values[32]

            row_values[2] = row_values[3] + row_values[11] + row_values[15] + row_values[22] + row_values[25] + row_values[28]


        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    统计" + os.path.basename(workspace) + " 失败！")
            fail += 1
            success = False

        if success:
            resullist.append(row_values)
            arcpy.AddMessage("    向 " + tb_name + " 表插入记录...")
            try:
                in_cursor.insertRow(tuple(row_values))
            except Exception as e:
                arcpy.AddError(e.message)
                arcpy.AddError("    统计" + os.path.basename(workspace) + " 失败！")
                fail += 1
            resullist.append(row_values)
        arcpy.AddMessage("  ")

    del in_cursor
    table_path_e3 = os.path.join(out_path,getNewFileNameQ(out_path, name + ".xls"))
    tableToExcelQ(table_path_e3, resullist, "类型情况统计表")
    arcpy.AddMessage('+'*60)
    arcpy.AddMessage("  成功：" + str(cout - fail) + " 个！")
    if fail > 0:
        arcpy.AddError("  失败：" + str(fail) + " 个！ 如下：")
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

    # 设置行高
    def set_row_height(work_sheet, row_index, row_height):
        work_sheet.row(row_index).height_mismatch = True
        work_sheet.row(row_index).height = 20 * row_height

    # 设置列宽
    def set_col_width(work_sheet, col_index, col_width):
        work_sheet.col(col_index).width = 256 * col_width
    def add_new_sheet(sheet_name):
        worksheets = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)

        style1 = set_style(u'宋体', 11, True, True)
        style2 = set_style(u'宋体', 11)
        ali1 = xlwt.Alignment()
        ali1.horz = 0x03
        ali1.vert = 0x01
        style2.alignment = ali1
        del ali1

        style3 = set_style(u'宋体', 16, False, True, True)
        ali4 = xlwt.Alignment()
        ali4.horz = 0x02
        ali4.vert = 0x00
        style3.alignment = ali4
        del ali4
        bt = u"广西耕地后备资源等潜力调查统计"
        worksheets.write_merge(0, 0, 0, 32, bt, style3)
        worksheets.write_merge(1, 1, 0, 32, u'面积：公顷', style2)

        worksheets.write_merge(2, 4, 0, 0, u'序号', style1)
        worksheets.write_merge(2, 4, 1, 1, u'行政区名称', style1)
        worksheets.write_merge(2, 4, 2, 2, u'总计', style1)
        worksheets.write_merge(2, 2, 3, 10, u'宜耕农用地潜力调查图斑', style1)
        worksheets.write_merge(3, 4, 3, 3, u'小计', style1)
        worksheets.write_merge(3, 4, 4, 4, u'工程恢复', style1)
        worksheets.write_merge(3, 4, 5, 5, u'即可恢复', style1)
        worksheets.write_merge(3, 3, 6, 10, u'未标注恢复属性', style1)

        worksheets.write_merge(2, 3, 11, 14, u'建设用地复垦潜力调查图斑', style1)
        worksheets.write_merge(2, 3, 15, 21, u'宜耕未利用地潜力调查图斑', style1)
        worksheets.write_merge(2, 2, 22, 27, u'耕地提质改造潜力调查图斑', style1)
        worksheets.write_merge(2, 2, 28, 32, u'自主提取潜力', style1)

        worksheets.write_merge(3, 4, 22, 22, u'小计', style1)
        worksheets.write_merge(3, 4, 23, 23, u'工程恢复', style1)
        worksheets.write_merge(3, 4, 24, 24, u'即可恢复', style1)
        worksheets.write_merge(3, 3, 25, 27, u'耕地', style1)
        worksheets.write(4, 25, u'小计', style1)
        worksheets.write(4, 26, u'水浇地', style1)
        worksheets.write(4, 27, u'旱地', style1)

        worksheets.write_merge(3, 4, 28, 28, u'合计', style1)
        worksheets.write_merge(3, 4, 29, 29, u'宜耕农用地潜力调查图斑', style1)
        worksheets.write_merge(3, 4, 30, 30, u'宜耕未利用地潜力调查图斑', style1)
        worksheets.write_merge(3, 4, 31, 31, u'建设用地复垦潜力调查图斑', style1)
        worksheets.write_merge(3, 4, 32, 32, u'耕地提质改造潜力调查图斑', style1)

        tlist = ['小计', '园地', '林地', '草地', '坑塘水面', '小计', '工业用地', '采矿用地',
                 '农村建设用地', '小计', '草地', '内陆滩涂','裸地','沙地','沿海滩涂','盐碱地']
        for ii in range(6,22):
            worksheets.write(4, ii, tlist[ii-6], style1)
        del ii
        # 设置行高
        set_row_height(worksheets, row_index=0, row_height=28)
        set_row_height(worksheets, row_index=1, row_height=22)
        set_row_height(worksheets, row_index=2, row_height=20)
        set_row_height(worksheets, row_index=3, row_height=20)
        set_row_height(worksheets, row_index=4, row_height=50)

        return worksheets

    sheet1 = add_new_sheet(sheets_name3)
    styles = set_style(u'宋体', 11, True, True)
    style_num = set_style(u'宋体', 11, True, True)
    ali3 = xlwt.Alignment()
    #0x02 左端对齐，0x03 右端对齐
    ali3.horz = 0x03
    ali3.vert = 0x01
    style_num.alignment = ali3
    num_format_str = '0.0000'
    style_num.num_format_str = num_format_str
    del ali3

    for row in datalist:
        sheet1.write(row[0] + 4, 0, row[0], styles)
        sheet1.write(row[0] + 4, 1, row[1], styles)
        for ij in range(2,33):
            sheet1.write(row[0] + 4, ij, row[ij] / 10000, style_num)

    
    # 设置列宽
    set_col_width(sheet1, col_index=0, col_width=4.71)
    for j in range(1,33):
        set_col_width(sheet1, col_index=j, col_width=14.71)

    workbook.save(excel_path3)

    arcpy.AddMessage("统计结果已导出到  " + excel_path3 + "      Excel表。")

if __name__ == "__main__":
    in_pathG = arcpy.GetParameterAsText(0)
    out_pathG = arcpy.GetParameterAsText(1)
    table_nameG = arcpy.GetParameterAsText(2)
    whereCG = arcpy.GetParameterAsText(3)

    arcpy.AddMessage(whereCG)
    listtt123 = re.findall(r"[^\\/:*?\"<>|]", table_nameG)
    table_name_global = "".join(listtt123).strip()

    statisticsAreaQ3(in_pathG, out_pathG, whereCG, table_name_global)

    arcpy.AddMessage("in_path: " + in_pathG)
    arcpy.AddMessage("out_path: " + out_pathG)
    arcpy.AddMessage("name: " + table_nameG)

# -*- coding: gbk -*-
import sys
import arcpy
import os
import re
import string

reload(sys)
sys.setdefaultencoding("utf-8")
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

def createTableQ(path1, name1):
    """
    新建表格，arcgis属性表，已指定固定字段
    :param path1:
    :param name1:
    :return:
    """
    table_name = name1.strip(string.digits)
    if table_name == '':
        table_name = "Table" + name1
    tb_path = os.path.join(path1, table_name)
    field_ls = []
    # 用字典设置字段属性，用列表存放所有字段
    field_list = [{'name': 'cout', 'type': 'TEXT', 'alias': '序号'},  #0
                  {'name': 'XZQ', 'type': 'TEXT', 'alias': '行政区'},

                  {'name': 'F2', 'type': 'DOUBLE', 'alias': '是-小计'},  #2
                  {'name': 'G3', 'type': 'DOUBLE', 'alias': '即可恢复-0201'},  #3
                  {'name': 'H4', 'type': 'DOUBLE', 'alias': '即可恢复-0201K'},  #4
                  {'name': 'I5', 'type': 'DOUBLE', 'alias': '即可恢复-0202'},  #5
                  {'name': 'J6', 'type': 'DOUBLE', 'alias': '即可恢复-0202K'},  #6
                  {'name': 'K7', 'type': 'DOUBLE', 'alias': '即可恢复-0203'},  #7
                  {'name': 'L8', 'type': 'DOUBLE', 'alias': '即可恢复-0203K'},  #8
                  {'name': 'M9', 'type': 'DOUBLE', 'alias': '即可恢复-0204'},  #9
                  {'name': 'N10', 'type': 'DOUBLE', 'alias': '即可恢复-0204K'},  #10
                  {'name': 'O11', 'type': 'DOUBLE', 'alias': '即可恢复-0301'},  #11
                  {'name': 'A12', 'type': 'DOUBLE', 'alias': '即可恢复-0301K'},  #12
                  {'name': 'Q13', 'type': 'DOUBLE', 'alias': '即可恢复-0302'},  #13
                  {'name': 'R14', 'type': 'DOUBLE', 'alias': '即可恢复-0302K'},  #14
                  {'name': 'S15', 'type': 'DOUBLE', 'alias': '即可恢复-0305'},  #15
                  {'name': 'T16', 'type': 'DOUBLE', 'alias': '即可恢复-0307'},  #16
                  {'name': 'U17', 'type': 'DOUBLE', 'alias': '即可恢复-0307K'},  #17
                  {'name': 'V18', 'type': 'DOUBLE', 'alias': '即可恢复-0403K'},  #18
                  {'name': 'W19', 'type': 'DOUBLE', 'alias': '即可恢复-0404'},  # 19
                  {'name': 'X20', 'type': 'DOUBLE', 'alias': '即可恢复-1104'},  # 20
                  {'name': 'Y21', 'type': 'DOUBLE', 'alias': '即可恢复-1104K'},  # 21
                  {'name': 'Z22', 'type': 'DOUBLE', 'alias': '即可恢复-1104A'},  # 22

                  {'name': 'F23', 'type': 'DOUBLE', 'alias': '否-小计'},  # 2
                  {'name': 'G24', 'type': 'DOUBLE', 'alias': '即可恢复-0201'},  # 3
                  {'name': 'H25', 'type': 'DOUBLE', 'alias': '即可恢复-0201K'},  # 4
                  {'name': 'I26', 'type': 'DOUBLE', 'alias': '即可恢复-0202'},  # 5
                  {'name': 'J27', 'type': 'DOUBLE', 'alias': '即可恢复-0202K'},  # 6
                  {'name': 'K28', 'type': 'DOUBLE', 'alias': '即可恢复-0203'},  # 7
                  {'name': 'L29', 'type': 'DOUBLE', 'alias': '即可恢复-0203K'},  # 8
                  {'name': 'M30', 'type': 'DOUBLE', 'alias': '即可恢复-0204'},  # 9
                  {'name': 'N31', 'type': 'DOUBLE', 'alias': '即可恢复-0204K'},  # 10
                  {'name': 'O32', 'type': 'DOUBLE', 'alias': '即可恢复-0301'},  # 11
                  {'name': 'P33', 'type': 'DOUBLE', 'alias': '即可恢复-0301K'},  # 12
                  {'name': 'Q34', 'type': 'DOUBLE', 'alias': '即可恢复-0302'},  # 13
                  {'name': 'R35', 'type': 'DOUBLE', 'alias': '即可恢复-0302K'},  # 14
                  {'name': 'S36', 'type': 'DOUBLE', 'alias': '即可恢复-0305'},  # 15
                  {'name': 'T37', 'type': 'DOUBLE', 'alias': '即可恢复-0307'},  # 16
                  {'name': 'U38', 'type': 'DOUBLE', 'alias': '即可恢复-0307K'},  # 17
                  {'name': 'V39', 'type': 'DOUBLE', 'alias': '即可恢复-0403K'},  # 18
                  {'name': 'W40', 'type': 'DOUBLE', 'alias': '即可恢复-0404'},  # 19
                  {'name': 'X41', 'type': 'DOUBLE', 'alias': '即可恢复-1104'},  # 20
                  {'name': 'Y42', 'type': 'DOUBLE', 'alias': '即可恢复-1104K'},  # 21
                  {'name': 'Z43', 'type': 'DOUBLE', 'alias': '即可恢复-1104A'},  # 22

                  ]

    arcpy.AddMessage("新建 " + table_name + " 表格...")
    arcpy.CreateTable_management(path1, table_name)
    arcpy.AddMessage("  添加字段...")

    for field in field_list:
        arcpy.AddField_management(tb_path, field['name'], field['type'], "#", "#", "#", field['alias'])
        field_ls.append(field['name'])

    return [tb_path, field_ls]

def xiaongjiao(in_path,spj_path, out_path, name):
    # 建gdb
    nametj = getNewFileNameQ(out_path, "result.gdb")
    gdbtj = os.path.join(out_path, nametj)
    arcpy.AddMessage("新建 " + gdbtj + " 用于保存结果...")
    arcpy.CreateFileGDB_management(out_path, nametj)

    # 建表
    arcpy.AddMessage("-"*20 + "新建属性表" + "-"*20)
    tb_paths = createTableQ(gdbtj, getNewFileNameQ(gdbtj, name))
    tb_path = tb_paths[0]
    field_ls = tb_paths[1]
    tb_name = os.path.basename(tb_path)

    in_cursor = arcpy.da.InsertCursor(tb_path, field_ls)
    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")

    foder_name = getNewFileNameQ(out_path,"与二调水田相交后")
    arcpy.CreateFolder_management(out_path, foder_name)
    foder_path = os.path.join(out_path,foder_name)

    row_values = []
    cout = 0
    fail = 0
    fail_list = []
    for workspace in workspaces:
        success = True
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        try:
            # 将每个gdb设为工作区
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()
            temp_name1 = getNewFileNameQ(foder_path, os.path.basename(workspace))
            result_gdb = os.path.join(foder_path, temp_name1)
            arcpy.AddMessage("新建 " + result_gdb + " ...")
            arcpy.CreateFileGDB_management(foder_path, temp_name1)
            gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])
            xzqcode = re.findall(r"\d+", gdbName)
            if len(xzqcode) > 0 and not xzqab(xzqcode[0]).isdigit():
                row_values = [cout, xzqab(xzqcode[0])]
            else:
                row_values = [cout, gdbName]

            i = 2
            while i < len(field_ls):
                row_values.append(0)
                i += 1
            # arcpy.AddMessage(row_values)
            # arcpy.AddMessage(len(row_values))
            for ifc in fc_list:
                if "提质改造" in ifc or u"提质改造" in ifc:
                    infc_path = os.path.join(workspace, ifc)
                    erase1_path = os.path.join(result_gdb, ifc)
                    # arcpy.Erase_analysis(infc_path, tdzz_fc_pathp, erase1_path, ".001 Meters")
                    arcpy.AddMessage(infc_path + "与" + spj_path + " 相交...")
                    arcpy.Intersect_analysis([infc_path, spj_path], erase1_path)

                    arcpy.AddMessage(infc_path + " 统计...")
                    tzgz_tb1 = os.path.join(gdbtj, "table" + gdbName)
                    arcpy.Statistics_analysis(erase1_path, tzgz_tb1, [["Shape_Area", "SUM"]], ['DLBM', 'ZZSXMC','PJJG'])
                    with arcpy.da.SearchCursor(tzgz_tb1, ('DLBM','ZZSXMC','PJJG','SUM_Shape_Area')) as cursor1:
                        for row1 in cursor1:
                            if "是" in str(row1[2]):
                                if "即可恢复" in str(row1[1]):
                                    row_values[2] += row1[3]
                                    if "0201" in str(row1[0]):
                                        row_values[3] += row1[3]
                                    if "0201K" in str(row1[0]):
                                        row_values[4] += row1[3]
                                    if "0202" in str(row1[0]):
                                        row_values[5] += row1[3]
                                    if "0202K" in str(row1[0]):
                                        row_values[6] += row1[3]
                                    if "0203" in str(row1[0]):
                                        row_values[7] += row1[3]
                                    if "0203K" in str(row1[0]):
                                        row_values[8] += row1[3]
                                    if "0204" in str(row1[0]):
                                        row_values[9] += row1[3]
                                    if "0204K" in str(row1[0]):
                                        row_values[10] += row1[3]
                                    if "0301" in str(row1[0]):
                                        row_values[11] += row1[3]
                                    if "0301K" in str(row1[0]):
                                        row_values[12] += row1[3]
                                    if "0302" in str(row1[0]):
                                        row_values[13] += row1[3]
                                    if "0302K" in str(row1[0]):
                                        row_values[14] += row1[3]
                                    if "0305" in str(row1[0]):
                                        row_values[15] += row1[3]
                                    if "0307" in str(row1[0]):
                                        row_values[16] += row1[3]
                                    if "0307K" in str(row1[0]):
                                        row_values[17] += row1[3]
                                    if "0403K" in str(row1[0]):
                                        row_values[18] += row1[3]
                                    if "0404" in str(row1[0]):
                                        row_values[19] += row1[3]
                                    if "1104" in str(row1[0]):
                                        row_values[20] += row1[3]
                                    if "1104K" in str(row1[0]):
                                        row_values[21] += row1[3]
                                    if "1104A" in str(row1[0]):
                                        row_values[22] += row1[3]

                            if "否" in str(row1[2]):
                                if "即可恢复" in str(row1[1]):
                                    row_values[23] += row1[3]
                                    if "0201" in str(row1[0]):
                                        row_values[24] += row1[3]
                                    if "0201K" in str(row1[0]):
                                        row_values[25] += row1[3]
                                    if "0202" in str(row1[0]):
                                        row_values[26] += row1[3]
                                    if "0202K" in str(row1[0]):
                                        row_values[27] += row1[3]
                                    if "0203" in str(row1[0]):
                                        row_values[28] += row1[3]
                                    if "0203K" in str(row1[0]):
                                        row_values[29] += row1[3]
                                    if "0204" in str(row1[0]):
                                        row_values[30] += row1[3]
                                    if "0204K" in str(row1[0]):
                                        row_values[31] += row1[3]
                                    if "0301" in str(row1[0]):
                                        row_values[32] += row1[3]
                                    if "0301K" in str(row1[0]):
                                        row_values[33] += row1[3]
                                    if "0302" in str(row1[0]):
                                        row_values[34] += row1[3]
                                    if "0302K" in str(row1[0]):
                                        row_values[35] += row1[3]
                                    if "0305" in str(row1[0]):
                                        row_values[36] += row1[3]
                                    if "0307" in str(row1[0]):
                                        row_values[37] += row1[3]
                                    if "0307K" in str(row1[0]):
                                        row_values[38] += row1[3]
                                    if "0403K" in str(row1[0]):
                                        row_values[39] += row1[3]
                                    if "0404" in str(row1[0]):
                                        row_values[40] += row1[3]
                                    if "1104" in str(row1[0]):
                                        row_values[41] += row1[3]
                                    if "1104K" in str(row1[0]):
                                        row_values[42] += row1[3]
                                    if "1104A" in str(row1[0]):
                                        row_values[43] += row1[3]

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("     " + os.path.basename(workspace) + " 失败！")
            fail += 1
            success = False
        if success:
            arcpy.AddMessage("    向 " + tb_name + " 插入记录...")
            try:
                in_cursor.insertRow(tuple(row_values))
            except Exception as e:
                arcpy.AddError(e.message)
                arcpy.AddError("    统计" + os.path.basename(workspace) + " 失败！")
                fail += 1

        arcpy.AddMessage("-"*50)

    arcpy.AddMessage('+'*60)

    del in_cursor
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
    tdzz_pathG = arcpy.GetParameterAsText(1)
    out_pathG = arcpy.GetParameterAsText(2)
    out_nameG = arcpy.GetParameterAsText(3)

    xiaongjiao(in_pathG,tdzz_pathG,out_pathG, out_nameG)

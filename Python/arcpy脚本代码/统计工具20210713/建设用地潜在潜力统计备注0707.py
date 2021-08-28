# -*- coding: gbk -*-
import sys
import arcpy
import os
import re
import string
sys.path.append(os.path.dirname(__file__))
import xlwt

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

def statisticsAreaQ3(in_path, out_path, qzql_path, name):
    cout = 0
    fail = 0
    fail_list = []

    arcpy.env.workspace = qzql_path
    qzql_gdb_list = arcpy.ListWorkspaces("*", "FileGDB")

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")

    # 建gdb
    resultg_name = getNewFileNameQ(out_path, name + "_result.gdb")
    result_gdb = os.path.join(out_path, resultg_name)
    arcpy.AddMessage("新建 " + result_gdb + " 用于保存结果...")
    arcpy.CreateFileGDB_management(out_path, resultg_name)

    resullist = []
    xjh_list = []

    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        # 将每个gdb设为工作区
        arcpy.env.workspace = workspace
        fc_list = arcpy.ListFeatureClasses()
        gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])

        xzqcode = re.findall(r"\d+", gdbName)

        if len(xzqcode) > 0 and not xzqab(xzqcode[0]).isdigit():
            row_values = [cout, xzqab(xzqcode[0]), 0, 0, 0, 0, 0, 0,0,0,0,0,0]
        else:
            row_values = [cout, gdbName, 0, 0, 0, 0, 0,0,0,0,0,0,0]

        try:
            qzql_fc_pathp = ""
            for qzql_gdb in qzql_gdb_list:
                if xzqcode[0] in os.path.basename(qzql_gdb):
                    arcpy.env.workspace = qzql_gdb
                    for qzql_fc in arcpy.ListFeatureClasses():
                        qzql_fc_pathp = os.path.join(qzql_gdb, qzql_fc)
                        break
                    break

            if qzql_fc_pathp == "":
                arcpy.AddError("        找不到与 " + os.path.basename(workspace) + " 对应的建设用地潜在潜力参考图层！")
                fail += 1
                resullist.append(row_values)
                fail_list.append(workspace)
                continue

            for in_fc in fc_list:
                in_fc_path = os.path.join(workspace,in_fc)
                arcpy.AddMessage("        " + in_fc)

                if "建设" in in_fc or u"建设" in in_fc:
                    arcpy.AddMessage("         " + in_fc + "相交 ...")
                    intersect_path = os.path.join(result_gdb,in_fc + str(cout))
                    arcpy.Intersect_analysis([in_fc_path,qzql_fc_pathp],intersect_path)
                    xjh_list.append(intersect_path)

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    统计" + os.path.basename(workspace) + " 失败！")
            fail += 1

    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage("  相交成功：" + str(cout - fail) + " 个！")
    if fail > 0:
        arcpy.AddError("  相交失败：" + str(fail) + " 个！ 如下：")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)

    try:
        meger_path = os.path.join(result_gdb,"H合并")
        meger_table = os.path.join(result_gdb,getNewFileNameQ(result_gdb, name))
        arcpy.AddMessage("    " + str(len(xjh_list)) + "个合并 ...")
        arcpy.Merge_management(xjh_list, meger_path)
        arcpy.AddMessage("    汇总统计 ...")
        arcpy.Statistics_analysis(meger_path, meger_table, [["Shape_Area", "SUM"]], ['XMC','PJJG','YKDL','DLBM','BZ'])
    except Exception as e:
        arcpy.AddError("    合并失败！")
        arcpy.AddError(e.message)
    # arcpy.AddMessage('+' * 60)
    # arcpy.AddMessage("  成功：" + str(cout - fail) + " 个！")
    # if fail > 0:
    #     arcpy.AddError("  失败：" + str(fail) + " 个！ 如下：")
    #     arcpy.AddError("####" + '*' * 20)
    #     for ff in fail_list:
    #         arcpy.AddError("  " + ff)
    #     arcpy.AddError("####" + '*' * 20)
    # arcpy.AddMessage('+' * 60)

if __name__ == "__main__":
    in_pathG = arcpy.GetParameterAsText(0)
    qzql_pathG = arcpy.GetParameterAsText(1)
    out_pathG = arcpy.GetParameterAsText(2)
    table_nameG = arcpy.GetParameterAsText(3)

    listtt123 = re.findall(r"[^\\/:*?\"<>|]", table_nameG)
    table_name_global = "".join(listtt123).strip()

    statisticsAreaQ3(in_pathG, out_pathG, qzql_pathG, table_name_global)

    # ls = [[1, u"阳朔县", 0,0,0,0,0],[2, u"阳朔县", 0,0,0,0,0],[3, u"阳朔县", 0,0,0,0,0]]
    # table_path_e3 = u"D:\\pyCharmWorksp\\ABC第三方.xls"
    # tableToExcelQ(table_path_e3, ls, u"宜垦地类情况统计")


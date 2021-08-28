# -*- coding: gbk -*-
import sys
import arcpy
import os

reload(sys)
sys.setdefaultencoding("utf-8")
arcpy.SetLogHistory(True)
def xzqabGetName(e):
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
        return "田阳区"
    elif e == "451022":
        return "田东县"
    elif e == "451082":
        return "平果市"
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

def huafenxiancode(in_path,out_path,gdbname,field):
    cout = 0
    fail = 0
    warning = 0
    fail_list = []
    warning_list = []

    # list_code = ["451026", "451028", "451029", "451030", "451031", "451081","450102","450103","450105","450107",
    #              "450108","450109","450110","450123","450124","450125","450126","450127","450202","450203","450204",
    #              "450205","450206","450222","450224","450225","450226","450502","450503","450512","450521","450602",
    #              "450603","450621","450681","450702","450703","450721","450804","451002","451003","451022","451082",
    #              "451024","451027","451202","451203","451221","451222","451223","451224","451225","451226","451227",
    #              "451228","451229","451302","451321","451381","451402","451421","451422","451423","451424","451425",
    #              "451481","450223","450302","450303","450304","450305","450311","450312","450321","450323","450324",
    #              "450325","450326","450327","450328","450329","450330","450332","450381","450403","450405","450406",
    #              "450421","450422","450423","450481","450722","450802","450803","450821","450881","450902","450903",
    #              "450921","450922","450923","450924","450981","451102","451103","451121","451122","451123","451322",
    #              "451323","451324"]
    list_code = []
    with arcpy.da.SearchCursor(in_path, field) as cursor:
        for row in cursor:
            if str(row[0]).strip() not in list_code:
                list_code.append(str(row[0]).strip())
                cout += 1
                arcpy.AddMessage(" (" + str(cout) + ") " + str(row[0]).strip())

    arcpy.AddMessage("=+*" * 80)
    cout = 0
    for code in list_code:
        out_gdb_name = code + xzqabGetName(code) + gdbname + ".gdb"
        out_gdb = os.path.join(out_path, out_gdb_name)
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + out_gdb_name)
        arcpy.AddMessage("  ")


        if not arcpy.Exists(out_gdb):
            arcpy.AddMessage("新建 " + out_gdb + " ...")
            arcpy.CreateFileGDB_management(out_path, out_gdb_name)
        else:
            arcpy.AddWarning(out_gdb_name + u" 已存在！")
            warning_list.append(out_gdb_name)
            warning += 1
            continue
        out_fc_path = os.path.join(out_gdb,gdbname)
        expr_sec = field + " like \'%" + str(code) + "%\'"
        try:
            arcpy.Select_analysis(in_path, out_fc_path, expr_sec)
        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + out_gdb_name + " 失败！")
            fail_list.append(out_gdb_name)
            fail += 1
            if arcpy.Exists(out_gdb):
                try:
                    arcpy.Delete_management(out_gdb)
                except Exception as e:
                    arcpy.AddMessage(e.message)


    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage(u"  成功：" + str(cout - fail - warning) + u" 个！")
    if warning > 0:
        arcpy.AddWarning(u"  警告：" + str(warning) + u" 个！ 如下：")
        arcpy.AddWarning("####" + '*' * 20)
        for fff in warning_list:
            arcpy.AddWarning("  " + fff)
        arcpy.AddWarning("####" + '*' * 20)
    if fail > 0:
        arcpy.AddError(u"  失败：" + str(fail) + u" 个！ 如下：")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)

if __name__ == "__main__":
    in_pathg = arcpy.GetParameterAsText(0)
    out_patha = arcpy.GetParameterAsText(1)
    out_name = arcpy.GetParameterAsText(2)
    ffff = arcpy.GetParameterAsText(3)

    huafenxiancode(in_pathg,out_patha,out_name,ffff)
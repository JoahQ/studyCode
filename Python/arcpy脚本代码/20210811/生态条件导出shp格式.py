# -*- coding: gbk -*-
import sys
import arcpy
import os
import re
import logging
import time

reload(sys)
sys.setdefaultencoding("utf-8")
arcpy.env.overwriteOutput = True

log_folder_path = os.path.join(os.path.dirname(__file__),"log")
if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path)
log_path = os.path.join(log_folder_path,"ST" + str(int(time.time())) + ".log")

logging.basicConfig(filename=log_path,filemode='a',level=logging.INFO,
                    format='%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p')

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

def daochushp(in_path,out_path,add_field,field_txt,addname):
    cout = 0
    fail = 0
    warning = 0
    fail_list = []
    warning_list = []

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "ALL")

    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        logging.info(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])
        xzqcode = re.findall(r"\d+", gdbName)
        shpfile_name = xzqcode[0] + xzqabGetName(xzqcode[0]) + addname + ".shp"
        shp_path = os.path.join(out_path,shpfile_name)
        try:
            # 将每个gdb设为工作区
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()

            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                if int(arcpy.GetCount_management(infc_path).getOutput(0)) > 0:
                    if add_field.strip() != '':
                        arcpy.AddMessage("    添加 " + add_field + " 字段 ...")
                        arcpy.AddField_management(infc_path, add_field, "TEXT", "", "", 50)
                        arcpy.AddMessage("     计算 " + field_txt + " 到 " + add_field + " 字段...")
                        arcpy.CalculateField_management(infc_path, add_field, "'" + field_txt + "'", "PYTHON_9.3")


                    arcpy.AddMessage("    导出 " + shpfile_name + " ...")
                    arcpy.FeatureClassToFeatureClass_conversion(infc_path,out_path,shpfile_name)
                else:
                    arcpy.AddWarning(infc_path + " 图斑数为0！")
                    logging.warning(infc_path + " 图斑数为0！")
                    warning_list.append(infc_path)
                    warning += 1

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " 失败！")
            logging.error("    " + os.path.basename(workspace) + " 失败！")
            logging.error(e.message)
            fail_list.append(os.path.basename(workspace))
            fail += 1
            if arcpy.Exists(shp_path):
                try:
                    arcpy.Delete_management(shp_path)
                except Exception as e:
                    arcpy.AddError(e.message)

    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage(u"  成功：" + str(cout - fail - warning) + u" 个！")
    logging.info(u"  成功：" + str(cout - fail - warning) + u" 个！")

    if warning > 0:
        arcpy.AddWarning(u"  警告：" + str(warning) + u" 个！ 如下：")
        arcpy.AddWarning("####" + '*' * 20)
        for fff in warning_list:
            arcpy.AddWarning("  " + fff)
            logging.warning("  " + fff)
        arcpy.AddWarning("####" + '*' * 20)
    if fail > 0:
        arcpy.AddError(u"  失败：" + str(fail) + u" 个！ 如下：")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
            logging.error("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)

if __name__ == "__main__":
    in_pathg = arcpy.GetParameterAsText(0)
    out_patha = arcpy.GetParameterAsText(1)
    addfield_gg = arcpy.GetParameterAsText(2)
    txt = arcpy.GetParameterAsText(3)
    add_name = arcpy.GetParameterAsText(4)

    logging.info("开始执行...")
    logging.info(in_pathg)
    logging.info(out_patha)
    logging.info(addfield_gg)
    logging.info(txt)
    logging.info(add_name)
    daochushp(in_pathg,out_patha,addfield_gg,txt,add_name)
    logging.info("执行结束！")
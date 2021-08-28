# -*- coding: gbk -*-
import sys
import arcpy
import os
import time

reload(sys)
sys.setdefaultencoding("utf-8")
arcpy.env.overwriteOutput = True
arcpy.env.XYResolution = "0.00001 Meters"
arcpy.env.XYTolerance = "0.0001 Meters"

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

def checkFieldExistOrNot(fcp,field_name):
    field_name_list = [field.name for field in arcpy.ListFields(fcp)]
    if field_name in field_name_list:
        return True
    else:
        return False

def  spaceCalculateMaxValue(inputs_layer,put_field,consult_layer,get_field,temp_gdb):
    """"""
    sec_stamp = str(int(time.time()))
    intersect = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"In" + sec_stamp))
    select1 = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"Se" + sec_stamp))
    dissolve_features = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"MDi" + sec_stamp))
    statistics_table1 = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"MT1_" + sec_stamp))
    st2name = getNewFileNameQ(temp_gdb,"MT2_" + sec_stamp)
    statistics_table2 = os.path.join(temp_gdb,st2name)
    statistics_table3 = os.path.join(temp_gdb, getNewFileNameQ(temp_gdb,"MT3_" + sec_stamp))
    in_objectid = getNewFieldName(inputs_layer,"MID")

    arcpy.Select_analysis(consult_layer, select1)

    get_vle_field = getNewFieldName(select1, "MVLE")
    try:
        # Process: inputs_layer add "groupID" field
        arcpy.AddField_management(inputs_layer, in_objectid, "LONG")
        arcpy.CalculateField_management(inputs_layer, in_objectid, '!OBJECTID!', "PYTHON_9.3")

        # Process: consult_layer add "getVALUE" field
        arcpy.AddField_management(select1, get_vle_field, "TEXT", "#", "#", 250)
        arcpy.CalculateField_management(select1, get_vle_field, "!" + get_field + "!", "PYTHON_9.3")
        # Process: intersect
        arcpy.AddMessage("  相交...")
        arcpy.Intersect_analysis([inputs_layer, select1], intersect, "ALL", ".0001 Meters", "INPUT")

        # Process: Statistics_analysis
        arcpy.AddMessage("  融合...")
        arcpy.Dissolve_management(intersect, dissolve_features, [in_objectid, get_vle_field], "", "SINGLE_PART", "DISSOLVE_LINES")
        arcpy.Statistics_analysis(dissolve_features, statistics_table1, [["Shape_Area", "SUM"]], [in_objectid, get_vle_field])
        arcpy.Statistics_analysis(statistics_table1, statistics_table2, [["SUM_Shape_Area", "MAX"]], in_objectid)
        # Process: join field 1
        arcpy.AddMessage("  连接字段...")
        arcpy.JoinField_management(statistics_table1, in_objectid, statistics_table2, in_objectid, [in_objectid,"MAX_SUM_Shape_Area"])
        wc = "\"" + in_objectid + "\" = \"" + in_objectid + "_1\" AND \"SUM_Shape_Area\" = \"MAX_SUM_Shape_Area\""
        arcpy.TableSelect_analysis(statistics_table1,statistics_table3,wc)
        arcpy.JoinField_management(inputs_layer, 'OBJECTID', statistics_table3, in_objectid, get_vle_field)
        arcpy.AddMessage("  " + put_field + " 赋值...")
        arcpy.CalculateField_management(inputs_layer, put_field, "!" + get_vle_field + "!", "PYTHON_9.3", "")

    except Exception as e:
        arcpy.AddError(e.message)
    finally:
        if checkFieldExistOrNot(inputs_layer,in_objectid):
            try:
                arcpy.DeleteField_management(inputs_layer, in_objectid)
            except Exception as e:
                arcpy.AddError(e.message)
        if checkFieldExistOrNot(inputs_layer,get_vle_field):
            try:
                arcpy.DeleteField_management(inputs_layer, get_vle_field)
            except Exception as e:
                arcpy.AddError(e.message)

def  spaceCalculateGGSYValue(input_fc,put_feild,consult_fc,temp_gdb):
    """"""
    sec_stamp = str(int(time.time()))
    intersect = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"Gin" + sec_stamp))
    stname = getNewFileNameQ(temp_gdb,"Gt" + sec_stamp)
    statistics_table1 = os.path.join(temp_gdb,stname)

    objectid = getNewFieldName(input_fc,"GID")
    try:
        arcpy.AddField_management(input_fc, objectid, "LONG")
        arcpy.CalculateField_management(input_fc, objectid, '!OBJECTID!', "PYTHON_9.3")

        arcpy.AddMessage("  相交...")
        arcpy.Intersect_analysis([input_fc, consult_fc], intersect, "ALL", ".0001 Meters", "INPUT")

        arcpy.AddMessage("  连接字段...")
        arcpy.Statistics_analysis(intersect, statistics_table1, [["Shape_Area", "SUM"]], objectid)
        arcpy.JoinField_management(input_fc, 'OBJECTID', statistics_table1, objectid, "SUM_Shape_Area")
        expression = "CaGGSY(!SUM_Shape_Area!)"
        codeblock = """def CaGGSY(a):
            if a>0:
                return "有"
            else:
                return "无" """
        arcpy.AddMessage("  赋值...")
        arcpy.CalculateField_management(input_fc, put_feild, expression, "PYTHON_9.3", codeblock)

    except Exception as e:
        arcpy.AddError(e.message)
    finally:
        if checkFieldExistOrNot(input_fc,objectid):
            try:
                arcpy.DeleteField_management(input_fc, objectid)
            except Exception as e:
                arcpy.AddError(e.message)
        if checkFieldExistOrNot(input_fc,"SUM_Shape_Area"):
            try:
                arcpy.DeleteField_management(input_fc, "SUM_Shape_Area")
            except Exception as e:
                arcpy.AddError(e.message)

def  spaceCalculateTBLXValue(input_fc,put_feild,consult_fc,txt_value,temp_gdb):
    """"""
    sec_stamp = str(int(time.time()))
    erase1 = os.path.join(temp_gdb,getNewFileNameQ(temp_gdb,"Er" + sec_stamp))
    stname = getNewFileNameQ(temp_gdb,"Tt" + sec_stamp)
    statistics_table1 = os.path.join(temp_gdb,stname)

    objectid = getNewFieldName(input_fc,"TID")
    mjzb_field = getNewFieldName(input_fc,"Tmjzb")
    try:
        arcpy.AddField_management(input_fc, objectid, "LONG")
        arcpy.AddField_management(input_fc, mjzb_field, "DOUBLE")
        arcpy.CalculateField_management(input_fc, objectid, '!OBJECTID!', "PYTHON_9.3")

        arcpy.AddMessage("  擦除...")
        arcpy.Erase_analysis(input_fc, consult_fc, erase1, ".0001 Meters")
        arcpy.AddMessage("  汇总统计...")
        arcpy.Statistics_analysis(erase1, statistics_table1, [["Shape_Area", "SUM"]], objectid)
        arcpy.AddMessage("  连接字段...")
        arcpy.JoinField_management(input_fc, 'OBJECTID', statistics_table1, objectid, "SUM_Shape_Area")

        arcpy.AddMessage("  赋值...")
        exprcode = "ZBmj(!SUM_Shape_Area!,!shape.area@meters!)"
        codezb = """def ZBmj(a, b):
            if a == None:
                return 100
            else:
                return 100 - round(a / b, 4) * 100 """
        arcpy.CalculateField_management(input_fc, mjzb_field, exprcode, "PYTHON_9.3",codezb)

        expression = "CaTBLX(!" + mjzb_field + "!,!" + put_feild + "!,\"" + txt_value + "\")"
        codeblock = """def CaTBLX(a,b,c):
            if (a>0.0001) and (a<100):
                if b == None:
                    return str(a) + "%" + c
                else:
                    return str(a) + "%" + c + "/" + b
            elif (a>=100):
                if b == None:
                    return "100%" + c
                else:
                    return "100%" + c + "/" + b
            else:
                return b """
        arcpy.CalculateField_management(input_fc, put_feild, expression, "PYTHON_9.3", codeblock)

    except Exception as e:
        arcpy.AddError(e.message)
    finally:
        if checkFieldExistOrNot(input_fc,objectid):
            try:
                arcpy.DeleteField_management(input_fc, objectid)
            except Exception as e:
                arcpy.AddError(e.message)
        if checkFieldExistOrNot(input_fc,mjzb_field):
            try:
                arcpy.DeleteField_management(input_fc, mjzb_field)
            except Exception as e:
                arcpy.AddError(e.message)
        if checkFieldExistOrNot(input_fc,"SUM_Shape_Area"):
            try:
                arcpy.DeleteField_management(input_fc, "SUM_Shape_Area")
            except Exception as e:
                arcpy.AddError(e.message)

def calculateValue(fci_path):
    # code_dcbh = """
    #     Dim calculatedcbh
    #     IF Len([OBJECTID]) = 1 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "000000" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 2 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "00000" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 3 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "0000" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 4 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "000" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 5 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "00" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 6 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & "0" & [OBJECTID]
    #     ELSEIF Len([OBJECTID]) = 7 THEN
    #     calculatedcbh = (Left([XZQDM], 12)) & [OBJECTID]
    #     END IF"""
    # arcpy.CalculateField_management(fci_path, "DCBH", "calculatedcbh", "VB", code_dcbh)
    arcpy.CalculateField_management(fci_path, "DCBH", "!XZQDM![0:12] + \'{:0>7d}\'.format(!OBJECTID!)", "PYTHON_9.3")

    # code_tblx = """
    #     dim AAA
    #     if [ZZSXMC] = "即可恢复" then
    #     AAA = "即可恢复/" & [TBLX]
    #     elseif [ZZSXMC] = "工程恢复" then
    #     AAA = "工程恢复/" & [TBLX]
    #     else
    #     AAA = [TBLX]
    #     end if """
    # arcpy.CalculateField_management(fci_path, "TBLX", "AAA", "VB", code_tblx)
    # arcpy.CalculateField_management(fci_path, "TBMJ", "round( [Shape_Area] ,2)", "VB", "")
    # arcpy.CalculateField_management(fci_path, "XDM", "Left( [XZQDM],6 )", "VB", "")
    # expre_xmc = "ab(!XDM!)"
    # code_xmc = """def ab(e):
    #     if (e == "450102"):
    #         return "兴宁区"
    #     elif (e == "450103"):
    #         return "青秀区"
    #     elif (e == "450105"):
    #         return "江南区"
    #     elif (e == "450107"):
    #         return "西乡塘区"
    #     elif (e == "450108"):
    #         return "良庆区"
    #     elif (e == "450109"):
    #         return "邕宁区"
    #     elif (e == "450110"):
    #         return "武鸣区"
    #     elif (e == "450123"):
    #         return "隆安县"
    #     elif (e == "450124"):
    #         return "马山县"
    #     elif (e == "450125"):
    #         return "上林县"
    #     elif (e == "450126"):
    #         return "宾阳县"
    #     elif (e == "450127"):
    #         return "横县"
    #     elif (e == "4502"):
    #         return "柳州市"
    #     elif (e == "450202"):
    #         return "城中区"
    #     elif (e == "450203"):
    #         return "鱼峰区"
    #     elif (e == "450204"):
    #         return "柳南区"
    #     elif (e == "450205"):
    #         return "柳北区"
    #     elif (e == "450206"):
    #         return "柳江区"
    #     elif (e == "450222"):
    #         return "柳城县"
    #     elif (e == "450223"):
    #         return "鹿寨县"
    #     elif (e == "450224"):
    #         return "融安县"
    #     elif (e == "450225"):
    #         return "融水苗族自治县"
    #     elif (e == "450226"):
    #         return "三江侗族自治县"
    #     elif (e == "4503"):
    #         return "桂林市"
    #     elif (e == "450302"):
    #         return "秀峰区"
    #     elif (e == "450303"):
    #         return "叠彩区"
    #     elif (e == "450304"):
    #         return "象山区"
    #     elif (e == "450305"):
    #         return "七星区"
    #     elif (e == "450311"):
    #         return "雁山区"
    #     elif (e == "450312"):
    #         return "临桂区"
    #     elif (e == "450321"):
    #         return "阳朔县"
    #     elif (e == "450323"):
    #         return "灵川县"
    #     elif (e == "450324"):
    #         return "全州县"
    #     elif (e == "450325"):
    #         return "兴安县"
    #     elif (e == "450326"):
    #         return "永福县"
    #     elif (e == "450327"):
    #         return "灌阳县"
    #     elif (e == "450328"):
    #         return "龙胜各族自治县"
    #     elif (e == "450329"):
    #         return "资源县"
    #     elif (e == "450330"):
    #         return "平乐县"
    #     elif (e == "450332"):
    #         return "恭城瑶族自治县"
    #     elif (e == "450381"):
    #         return "荔浦市"
    #     elif (e == "4504"):
    #         return "梧州市"
    #     elif (e == "450403"):
    #         return "万秀区"
    #     elif (e == "450405"):
    #         return "长洲区"
    #     elif (e == "450406"):
    #         return "龙圩区"
    #     elif (e == "450421"):
    #         return "苍梧县"
    #     elif (e == "450422"):
    #         return "藤县"
    #     elif (e == "450423"):
    #         return "蒙山县"
    #     elif (e == "450481"):
    #         return "岑溪市"
    #     elif (e == "4505"):
    #         return "北海市"
    #     elif (e == "450502"):
    #         return "海城区"
    #     elif (e == "450503"):
    #         return "银海区"
    #     elif (e == "450512"):
    #         return "铁山港区"
    #     elif (e == "450521"):
    #         return "合浦县"
    #     elif (e == "4506"):
    #         return "防城港市"
    #     elif (e == "450602"):
    #         return "港口区"
    #     elif (e == "450603"):
    #         return "防城区"
    #     elif (e == "450621"):
    #         return "上思县"
    #     elif (e == "450681"):
    #         return "东兴市"
    #     elif (e == "4507"):
    #         return "钦州市"
    #     elif (e == "450702"):
    #         return "钦南区"
    #     elif (e == "450703"):
    #         return "钦北区"
    #     elif (e == "450721"):
    #         return "灵山县"
    #     elif (e == "450722"):
    #         return "浦北县"
    #     elif (e == "4508"):
    #         return "贵港市"
    #     elif (e == "450802"):
    #         return "港北区"
    #     elif (e == "450803"):
    #         return "港南区"
    #     elif (e == "450804"):
    #         return "覃塘区"
    #     elif (e == "450821"):
    #         return "平南县"
    #     elif (e == "450881"):
    #         return "桂平市"
    #     elif (e == "4509"):
    #         return "玉林市"
    #     elif (e == "450902"):
    #         return "玉州区"
    #     elif (e == "450903"):
    #         return "福绵区"
    #     elif (e == "450921"):
    #         return "容县"
    #     elif (e == "450922"):
    #         return "陆川县"
    #     elif (e == "450923"):
    #         return "博白县"
    #     elif (e == "450924"):
    #         return "兴业县"
    #     elif (e == "450981"):
    #         return "北流市"
    #     elif (e == "4510"):
    #         return "百色市"
    #     elif (e == "451002"):
    #         return "右江区"
    #     elif (e == "451003"):
    #         return "田阳市"
    #     elif (e == "451022"):
    #         return "田东县"
    #     elif (e == "451082"):
    #         return "平果县"
    #     elif (e == "451024"):
    #         return "德保县"
    #     elif (e == "451026"):
    #         return "那坡县"
    #     elif (e == "451027"):
    #         return "凌云县"
    #     elif (e == "451028"):
    #         return "乐业县"
    #     elif (e == "451029"):
    #         return "田林县"
    #     elif (e == "451030"):
    #         return "西林县"
    #     elif (e == "451031"):
    #         return "隆林各族自治县"
    #     elif (e == "451081"):
    #         return "靖西市"
    #     elif (e == "4511"):
    #         return "贺州市"
    #     elif (e == "451102"):
    #         return "八步区"
    #     elif (e == "451103"):
    #         return "平桂区"
    #     elif (e == "451121"):
    #         return "昭平县"
    #     elif (e == "451122"):
    #         return "钟山县"
    #     elif (e == "451123"):
    #         return "富川瑶族自治县"
    #     elif (e == "4512"):
    #         return "河池市"
    #     elif (e == "451202"):
    #         return "金城江区"
    #     elif (e == "451203"):
    #         return "宜州区"
    #     elif (e == "451221"):
    #         return "南丹县"
    #     elif (e == "451222"):
    #         return "天峨县"
    #     elif (e == "451223"):
    #         return "凤山县"
    #     elif (e == "451224"):
    #         return "东兰县"
    #     elif (e == "451225"):
    #         return "罗城仫佬族自治县"
    #     elif (e == "451226"):
    #         return "环江毛南族自治县"
    #     elif (e == "451227"):
    #         return "巴马瑶族自治县"
    #     elif (e == "451228"):
    #         return "都安瑶族自治县"
    #     elif (e == "451229"):
    #         return "大化瑶族自治县"
    #     elif (e == "4513"):
    #         return "来宾市"
    #     elif (e == "451302"):
    #         return "兴宾区"
    #     elif (e == "451321"):
    #         return "忻城县"
    #     elif (e == "451322"):
    #         return "象州县"
    #     elif (e == "451323"):
    #         return "武宣县"
    #     elif (e == "451324"):
    #         return "金秀瑶族自治县"
    #     elif (e == "451381"):
    #         return "合山市"
    #     elif (e == "4514"):
    #         return "崇左市"
    #     elif (e == "451402"):
    #         return "江州区"
    #     elif (e == "451421"):
    #         return "扶绥县"
    #     elif (e == "451422"):
    #         return "宁明县"
    #     elif (e == "451423"):
    #         return "龙州县"
    #     elif (e == "451424"):
    #         return "大新县"
    #     elif (e == "451425"):
    #         return "天等县"
    #     elif (e == "451481"):
    #         return "凭祥市" """
    # arcpy.CalculateField_management(fci_path, "XMC", expre_xmc, "PYTHON_9.3", code_xmc)

def main():
    """"""
    temp_name = getNewFileNameQ(out_path, "temp.gdb")
    temp_gdb1 = os.path.join(out_path, temp_name)
    arcpy.AddMessage(u"新建 " + temp_gdb1 + u" 用于放过程数据")
    arcpy.CreateFileGDB_management(out_path, temp_name)
    merge_path = os.path.join(temp_gdb1, getNewFileNameQ(temp_gdb1, u"合并"))

    arcpy.env.workspace = in_gdb
    fclist = arcpy.ListFeatureClasses()
    arcpy.AddMessage("合并...")
    arcpy.Merge_management(fclist, merge_path)

    # arcpy.AddMessage("XDM、XMC、TBMJ赋值，TBLX标注恢复属性...")
    # arcpy.AddMessage("DCBH赋值...")
    # calculateValue(merge_path)
    arcpy.AddMessage("赋坡度级别（PDJB）...")
    spaceCalculateMaxValue(merge_path,"PDJB",podutu,"PDJB",temp_gdb1)
    arcpy.AddMessage("赋土壤类型（TRLX）...")
    spaceCalculateMaxValue(merge_path,"TRLX",turangtu,"土类",temp_gdb1)
    arcpy.AddMessage("赋灌溉水源（GGSY）...")
    spaceCalculateGGSYValue(merge_path, "GGSY", shuiyuantiaojian,temp_gdb1)
    arcpy.AddMessage("TBLX标注\"已实施土地整治\"...")
    spaceCalculateTBLXValue(merge_path, "TBLX", tudizhengzhi, "已实施土地整治",temp_gdb1)

    res_name = getNewFileNameQ(out_path, os.path.basename(in_gdb))
    arcpy.AddMessage(u"新建 " + res_name + u" 作为最终赋值结果")
    rs_gdb1 = os.path.join(out_path, res_name)
    arcpy.CreateFileGDB_management(out_path, res_name)

    arcpy.AddMessage("筛选 宜耕农用地潜力调查图斑")
    nyd_path = os.path.join(rs_gdb1, "宜耕农用地潜力调查图斑")
    arcpy.Select_analysis(merge_path, nyd_path, "GDHBZY LIKE \'%宜耕农用地潜力调查图斑%\'")

    arcpy.AddMessage("筛选 耕地提质改造潜力调查图斑")
    tzgz_path = os.path.join(rs_gdb1, "耕地提质改造潜力调查图斑")
    arcpy.Select_analysis(merge_path, tzgz_path, "GDHBZY LIKE \'%耕地提质改造潜力调查图斑%\'")

    arcpy.AddMessage("筛选 建设用地复垦潜力调查图斑")
    jsyd_path = os.path.join(rs_gdb1, "建设用地复垦潜力调查图斑")
    arcpy.Select_analysis(merge_path, jsyd_path, "GDHBZY LIKE \'%建设用地复垦潜力调查图斑%\'")

    arcpy.AddMessage("筛选 宜耕未利用地潜力调查图斑")
    wlyd_path = os.path.join(rs_gdb1, "宜耕未利用地潜力调查图斑")
    arcpy.Select_analysis(merge_path, wlyd_path, "GDHBZY LIKE \'%宜耕未利用地潜力调查图斑%\'")

    if arcpy.Exists(jsyd_path) and int(arcpy.GetCount_management(jsyd_path).getOutput(0)) > 0:
        arcpy.AddMessage("建设用地复垦潜力调查图斑，TBLX标注\"已实施增减挂钩\"...")
        spaceCalculateTBLXValue(jsyd_path, "TBLX", zengjiangua, "已实施增减挂钩", temp_gdb1)
    if arcpy.Exists(wlyd_path) and int(arcpy.GetCount_management(wlyd_path).getOutput(0)) > 0:
        arcpy.AddMessage("宜耕未利用地潜力调查图斑，TBLX标注\"基本农田范围内的未利用地\"...")
        spaceCalculateTBLXValue(wlyd_path, "TBLX", jibennongtian, "基本农田范围内的未利用地", temp_gdb1)

    if arcpy.Exists(temp_gdb1):
        try:
            arcpy.Delete_management(temp_gdb1)
        except Exception as e:
            arcpy.AddMessage(e.message)
            arcpy.AddMessage("...")

if __name__ == "__main__":
    in_gdb = arcpy.GetParameterAsText(0)#指引图斑gdb
    podutu = arcpy.GetParameterAsText(1)#坡度图
    turangtu = arcpy.GetParameterAsText(2)#土壤图
    shuiyuantiaojian = arcpy.GetParameterAsText(3)#水源条件
    tudizhengzhi = arcpy.GetParameterAsText(4)#已实施土地整治项目

    zengjiangua = arcpy.GetParameterAsText(5)#增减挂钩清查库
    jibennongtian = arcpy.GetParameterAsText(6)#基本农田保护区

    out_path = arcpy.GetParameterAsText(7)

    main()

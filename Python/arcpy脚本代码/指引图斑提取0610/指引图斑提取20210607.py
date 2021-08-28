# -*- coding: gbk -*-
import sys
import arcpy
import os

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

def createGDBAndFeatureclass(out_pathc, gdb_name, templet, spatial_reference):
    arcpy.CreateFileGDB_management(out_pathc, gdb_name)
    outgdb_path = os.path.join(out_path, gdb_name)
    fc_name_list = [u"宜耕农用地潜力调查图斑", u"宜耕未利用地潜力调查图斑", u"建设用地复垦潜力调查图斑", u"耕地提质改造潜力调查图斑"]
    for fcname in fc_name_list:
        arcpy.CreateFeatureclass_management(outgdb_path, fcname, "POLYGON", templet, "#", "#", spatial_reference)
    return outgdb_path

def selectFeatureClass(in_dltb, in_xztj, podu_path1, standard_gdb, out_gdb1):
    # """擦除限制条件"""
    arcpy.AddMessage(u"     擦除限制条件")
    erasexz_result = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"擦除限制条件结果"))
    dltb_sel = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"DLTB筛选1"))
    where_clause1 = """DLBM LIKE '02%' OR DLBM LIKE '03%' OR DLBM in ('0401','0403','0404') OR 
    DLBM IN ('0102','0103','0601','0602','0702','1105','1106','1204','1206') OR ZZSXDM in ('JKHF','GCHF')"""
    arcpy.Select_analysis(in_dltb, dltb_sel, where_clause1)
    arcpy.Erase_analysis (dltb_sel, in_xztj, erasexz_result)

    # """擦除限制局域后筛选数据"""
    #宜未利用地
    wlyd_sel = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"WLYD筛选1"))
    arcpy.AddMessage(u"     提取宜耕未利用地潜力调查图斑")
    where_clausewlyd = """DLBM IN ('0404', '1105', '1106', '1204', '1206') AND ZZSXDM NOT IN ('JKHF', 'GCHF')"""
    mul_to_sgl_wlyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"未利用地"))
    arcpy.Select_analysis(erasexz_result, wlyd_sel, where_clausewlyd)
    arcpy.MultipartToSinglepart_management(wlyd_sel, mul_to_sgl_wlyd)
    select_wlyd = aggregateAanalysisQ(mul_to_sgl_wlyd,"SUM_Shape_Area >= 3333.35",out_gdb1)

    #宜耕农用地
    arcpy.AddMessage(u"     提取宜耕农用地潜力调查图斑")
    nyd_sel = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"NYD筛选1"))
    where_clausenyd = """(DLBM IN ('0201','0202','0203','0204','0301','0302','0303','0304','0305','0306','0307',
    '0401','0403') AND ZZSXDM NOT IN ('JKHF')) OR (DLBM NOT LIKE '%K%' AND ZZSXDM = 'GCHF')"""
    mul_to_sgl_nyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"农用地"))
    arcpy.Select_analysis(erasexz_result, nyd_sel, where_clausenyd)
    arcpy.MultipartToSinglepart_management(nyd_sel, mul_to_sgl_nyd)
    select_nyd = aggregateAanalysisQ(mul_to_sgl_nyd,"SUM_Shape_Area >= 3333.35",out_gdb1)

    #提质改造
    arcpy.AddMessage(u"     提取耕地提质改造潜力调查图斑")
    tzgz_sel = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"TZGZ筛选1"))
    where_clausetzgz = """(DLBM IN ('0102','0103','0201K','0202K','0203K','0204K','0301K','0302K','0307K','1104K')) 
    OR ZZSXDM = 'JKHF' """
    erase_result_tzgz = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"提质改造擦除6_25度坡度"))
    mul_to_sgl_tzgz = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"提质改造"))
    podu_dy2j = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"PDJB大于2坡度图"))
    arcpy.Select_analysis(podu_path1, podu_dy2j, "PDJB not in (\'1\',\'2\')")#F:\后备资源\完整坡度图\450702钦南区\450702钦南区.shp
    arcpy.Select_analysis(erasexz_result, tzgz_sel, where_clausetzgz)
    arcpy.Erase_analysis(tzgz_sel, podu_dy2j, erase_result_tzgz, ".0001 Meters")
    arcpy.MultipartToSinglepart_management(erase_result_tzgz, mul_to_sgl_tzgz)
    select_tzgz = aggregateAanalysisQ(mul_to_sgl_tzgz,"SUM_Shape_Area >=33333.35",out_gdb1)

    #建设用地复垦潜力调查图斑
    arcpy.AddMessage(u"     提取建设用地复垦潜力调查图斑")
    jsyd_sel = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"JSYD筛选1"))
    where_clausejsyd = """DLBM  IN ('0601','0602','0702')"""
    erase_result_jsyd = os.path.join(out_gdb1, getNewFileNameQ(out_gdb1, u"限制条件内建设用地"))
    all_jsyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"全部建设用地"))
    merge_jsyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"建设用地合并"))
    mul_to_sgl_jsyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"建设用地多转单部件"))
    select_jsyd = os.path.join(out_gdb1,getNewFileNameQ(out_gdb1, u"建设用地"))
    arcpy.Select_analysis(erasexz_result, jsyd_sel, where_clausejsyd)
    arcpy.Select_analysis(in_dltb, all_jsyd, where_clausejsyd)
    arcpy.Erase_analysis(all_jsyd, jsyd_sel, erase_result_jsyd, ".0001 Meters")
    arcpy.AddField_management(erase_result_jsyd, "TBLX", "TEXT", "", "", "255", "图斑类型", "NULLABLE", "NON_REQUIRED", "")
    arcpy.CalculateField_management(erase_result_jsyd, "TBLX", "\"宜复垦为其他农用地\"", "VB", "")
    arcpy.Merge_management([erase_result_jsyd,jsyd_sel],merge_jsyd)
    arcpy.MultipartToSinglepart_management(merge_jsyd, mul_to_sgl_jsyd)
    arcpy.Select_analysis(mul_to_sgl_jsyd, select_jsyd, "Shape_Area >= 1")

    arcpy.env.workspace = standard_gdb
    fclist = arcpy.ListFeatureClasses()
    arcpy.AddMessage(u"   ")
    for fci in fclist:
        fci_path = os.path.join(standard_gdb,fci)
        if u"未利用地" in fci:
            arcpy.AddMessage(u"     将提取的宜耕未利用地潜力调查图斑追加到标准库")
            arcpy.RepairGeometry_management(select_wlyd)
            fieldmappings = arcpy.FieldMappings()
            fieldmappings.addTable(fci_path)
            fieldmappings.addTable(select_wlyd)

            fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("SDBSM"))
            fieldmap.addInputField(select_wlyd, "BSM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("SDBSM"), fieldmap)

            fieldmap1 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQDM"))
            fieldmap1.addInputField(select_wlyd, "ZLDWDM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQDM"), fieldmap1)

            fieldmap2 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQMC"))
            fieldmap2.addInputField(select_wlyd, "ZLDWMC")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQMC"), fieldmap2)

            arcpy.Append_management(select_wlyd, fci_path, "NO_TEST", fieldmappings)
            arcpy.CalculateField_management(fci_path, "GDHBZY", "\"宜耕未利用地潜力调查图斑\"", "VB", "")

            del fieldmap
            del fieldmap1
            del fieldmap2
            del fieldmappings
        if u"农用地" in fci:
            arcpy.AddMessage(u"     将提取的宜耕农用地潜力调查图斑追加到标准库")
            arcpy.RepairGeometry_management(select_nyd)
            fieldmappings = arcpy.FieldMappings()
            fieldmappings.addTable(fci_path)
            fieldmappings.addTable(select_nyd)

            fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("SDBSM"))
            fieldmap.addInputField(select_nyd, "BSM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("SDBSM"), fieldmap)

            fieldmap1 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQDM"))
            fieldmap1.addInputField(select_nyd, "ZLDWDM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQDM"), fieldmap1)

            fieldmap2 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQMC"))
            fieldmap2.addInputField(select_nyd, "ZLDWMC")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQMC"), fieldmap2)

            arcpy.Append_management(select_nyd, fci_path, "NO_TEST", fieldmappings)
            arcpy.CalculateField_management(fci_path, "GDHBZY", "\"宜耕农用地潜力调查图斑\"", "VB", "")

            del fieldmap
            del fieldmap1
            del fieldmap2
            del fieldmappings
        if u"提质改造" in fci:
            arcpy.AddMessage(u"     将提取的耕地提质改造潜力调查图斑追加到标准库")
            arcpy.RepairGeometry_management(select_tzgz)
            fieldmappings = arcpy.FieldMappings()
            fieldmappings.addTable(fci_path)
            fieldmappings.addTable(select_tzgz)

            fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("SDBSM"))
            fieldmap.addInputField(select_tzgz, "BSM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("SDBSM"), fieldmap)

            fieldmap1 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQDM"))
            fieldmap1.addInputField(select_tzgz, "ZLDWDM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQDM"), fieldmap1)

            fieldmap2 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQMC"))
            fieldmap2.addInputField(select_tzgz, "ZLDWMC")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQMC"), fieldmap2)

            arcpy.Append_management(select_tzgz, fci_path, "NO_TEST", fieldmappings)
            arcpy.CalculateField_management(fci_path, "GDHBZY", "\"耕地提质改造潜力调查图斑\"", "VB", "")

            del fieldmap
            del fieldmap1
            del fieldmap2
            del fieldmappings
        if u"建设用地" in fci:
            arcpy.AddMessage(u"     将提取的建设用地复垦潜力调查图斑追加到标准库")
            arcpy.RepairGeometry_management(select_jsyd)
            fieldmappings = arcpy.FieldMappings()
            fieldmappings.addTable(fci_path)
            fieldmappings.addTable(select_jsyd)

            fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("SDBSM"))
            fieldmap.addInputField(select_jsyd, "BSM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("SDBSM"), fieldmap)

            fieldmap1 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQDM"))
            fieldmap1.addInputField(select_jsyd, "ZLDWDM")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQDM"), fieldmap1)

            fieldmap2 = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex("XZQMC"))
            fieldmap2.addInputField(select_jsyd, "ZLDWMC")
            fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex("XZQMC"), fieldmap2)

            arcpy.Append_management(select_jsyd, fci_path, "NO_TEST", fieldmappings)
            arcpy.CalculateField_management(fci_path, "GDHBZY", "\"建设用地复垦潜力调查图斑\"", "VB", "")

            del fieldmap
            del fieldmap1
            del fieldmap2
            del fieldmappings

        arcpy.AddMessage("XDM、XMC、TBMJ赋值，TBLX标注恢复属性...")
        calculateValue(fci_path)

def calculateValue(fci_path):
    code_tblx = """ 
        dim AAA
        if [ZZSXMC] = "即可恢复" then
        AAA = "即可恢复/" & [TBLX]
        elseif [ZZSXMC] = "工程恢复" then
        AAA = "工程恢复/" & [TBLX]
        else
        AAA = [TBLX]
        end if """
    arcpy.CalculateField_management(fci_path, "TBLX", "AAA", "VB", code_tblx)
    arcpy.CalculateField_management(fci_path, "TBMJ", "round([Shape_Area],2)", "VB", "")
    arcpy.CalculateField_management(fci_path, "XDM", "Left([XZQDM],6)", "VB", "")
    expre_xmc = "ab(!XDM!)"
    code_xmc = """def ab(e):
        if (e == "450102"):
            return "兴宁区"
        elif (e == "450103"):
            return "青秀区"
        elif (e == "450105"):
            return "江南区"
        elif (e == "450107"):
            return "西乡塘区"
        elif (e == "450108"):
            return "良庆区"
        elif (e == "450109"):
            return "邕宁区"
        elif (e == "450110"):
            return "武鸣区"
        elif (e == "450123"):
            return "隆安县"
        elif (e == "450124"):
            return "马山县"
        elif (e == "450125"):
            return "上林县"
        elif (e == "450126"):
            return "宾阳县"
        elif (e == "450127"):
            return "横县"
        elif (e == "4502"):
            return "柳州市"
        elif (e == "450202"):
            return "城中区"
        elif (e == "450203"):
            return "鱼峰区"
        elif (e == "450204"):
            return "柳南区"
        elif (e == "450205"):
            return "柳北区"
        elif (e == "450206"):
            return "柳江区"
        elif (e == "450222"):
            return "柳城县"
        elif (e == "450223"):
            return "鹿寨县"
        elif (e == "450224"):
            return "融安县"
        elif (e == "450225"):
            return "融水苗族自治县"
        elif (e == "450226"):
            return "三江侗族自治县"
        elif (e == "4503"):
            return "桂林市"
        elif (e == "450302"):
            return "秀峰区"
        elif (e == "450303"):
            return "叠彩区"
        elif (e == "450304"):
            return "象山区"
        elif (e == "450305"):
            return "七星区"
        elif (e == "450311"):
            return "雁山区"
        elif (e == "450312"):
            return "临桂区"
        elif (e == "450321"):
            return "阳朔县"
        elif (e == "450323"):
            return "灵川县"
        elif (e == "450324"):
            return "全州县"
        elif (e == "450325"):
            return "兴安县"
        elif (e == "450326"):
            return "永福县"
        elif (e == "450327"):
            return "灌阳县"
        elif (e == "450328"):
            return "龙胜各族自治县"
        elif (e == "450329"):
            return "资源县"
        elif (e == "450330"):
            return "平乐县"
        elif (e == "450332"):
            return "恭城瑶族自治县"
        elif (e == "450381"):
            return "荔浦市"
        elif (e == "4504"):
            return "梧州市"
        elif (e == "450403"):
            return "万秀区"
        elif (e == "450405"):
            return "长洲区"
        elif (e == "450406"):
            return "龙圩区"
        elif (e == "450421"):
            return "苍梧县"
        elif (e == "450422"):
            return "藤县"
        elif (e == "450423"):
            return "蒙山县"
        elif (e == "450481"):
            return "岑溪市"
        elif (e == "4505"):
            return "北海市"
        elif (e == "450502"):
            return "海城区"
        elif (e == "450503"):
            return "银海区"
        elif (e == "450512"):
            return "铁山港区"
        elif (e == "450521"):
            return "合浦县"
        elif (e == "4506"):
            return "防城港市"
        elif (e == "450602"):
            return "港口区"
        elif (e == "450603"):
            return "防城区"
        elif (e == "450621"):
            return "上思县"
        elif (e == "450681"):
            return "东兴市"
        elif (e == "4507"):
            return "钦州市"
        elif (e == "450702"):
            return "钦南区"
        elif (e == "450703"):
            return "钦北区"
        elif (e == "450721"):
            return "灵山县"
        elif (e == "450722"):
            return "浦北县"
        elif (e == "4508"):
            return "贵港市"
        elif (e == "450802"):
            return "港北区"
        elif (e == "450803"):
            return "港南区"
        elif (e == "450804"):
            return "覃塘区"
        elif (e == "450821"):
            return "平南县"
        elif (e == "450881"):
            return "桂平市"
        elif (e == "4509"):
            return "玉林市"
        elif (e == "450902"):
            return "玉州区"
        elif (e == "450903"):
            return "福绵区"
        elif (e == "450921"):
            return "容县"
        elif (e == "450922"):
            return "陆川县"
        elif (e == "450923"):
            return "博白县"
        elif (e == "450924"):
            return "兴业县"
        elif (e == "450981"):
            return "北流市"
        elif (e == "4510"):
            return "百色市"
        elif (e == "451002"):
            return "右江区"
        elif (e == "451003"):
            return "田阳市"
        elif (e == "451022"):
            return "田东县"
        elif (e == "451082"):
            return "平果县"
        elif (e == "451024"):
            return "德保县"
        elif (e == "451026"):
            return "那坡县"
        elif (e == "451027"):
            return "凌云县"
        elif (e == "451028"):
            return "乐业县"
        elif (e == "451029"):
            return "田林县"
        elif (e == "451030"):
            return "西林县"
        elif (e == "451031"):
            return "隆林各族自治县"
        elif (e == "451081"):
            return "靖西市"
        elif (e == "4511"):
            return "贺州市"
        elif (e == "451102"):
            return "八步区"
        elif (e == "451103"):
            return "平桂区"
        elif (e == "451121"):
            return "昭平县"
        elif (e == "451122"):
            return "钟山县"
        elif (e == "451123"):
            return "富川瑶族自治县"
        elif (e == "4512"):
            return "河池市"
        elif (e == "451202"):
            return "金城江区"
        elif (e == "451203"):
            return "宜州区"
        elif (e == "451221"):
            return "南丹县"
        elif (e == "451222"):
            return "天峨县"
        elif (e == "451223"):
            return "凤山县"
        elif (e == "451224"):
            return "东兰县"
        elif (e == "451225"):
            return "罗城仫佬族自治县"
        elif (e == "451226"):
            return "环江毛南族自治县"
        elif (e == "451227"):
            return "巴马瑶族自治县"
        elif (e == "451228"):
            return "都安瑶族自治县"
        elif (e == "451229"):
            return "大化瑶族自治县"
        elif (e == "4513"):
            return "来宾市"
        elif (e == "451302"):
            return "兴宾区"
        elif (e == "451321"):
            return "忻城县"
        elif (e == "451322"):
            return "象州县"
        elif (e == "451323"):
            return "武宣县"
        elif (e == "451324"):
            return "金秀瑶族自治县"
        elif (e == "451381"):
            return "合山市"
        elif (e == "4514"):
            return "崇左市"
        elif (e == "451402"):
            return "江州区"
        elif (e == "451421"):
            return "扶绥县"
        elif (e == "451422"):
            return "宁明县"
        elif (e == "451423"):
            return "龙州县"
        elif (e == "451424"):
            return "大新县"
        elif (e == "451425"):
            return "天等县"
        elif (e == "451481"):
            return "凭祥市" """
    arcpy.CalculateField_management(fci_path, "XMC", expre_xmc, "PYTHON_9.3", code_xmc)

def aggregateAanalysisQ(in_path2,where_clause2,out_gdb2):
    """聚合分析"""

    fc = os.path.basename(in_path2)
    select_1 = os.path.join(out_gdb2,getNewFileNameQ(out_gdb2,  fc + u"筛选大于400"))
    buffer_result = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"缓冲结果"))
    dissolve_result = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"融合结果"))
    spatialJoin = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"空间连接"))
    spatialJoin_Statisti = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"汇总统计表"))
    tableSelect = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"筛选表"))
    last_result = os.path.join(out_gdb2, getNewFileNameQ(out_gdb2, fc + u"聚合结果"))

    arcpy.Select_analysis(in_path2, select_1, "Shape_Area > 400")
    arcpy.Buffer_analysis(select_1, buffer_result, "50 Meters", "FULL", "ROUND", "NONE", "")
    arcpy.Dissolve_management(buffer_result, dissolve_result, "", "", "SINGLE_PART", "DISSOLVE_LINES")
    arcpy.AddField_management(dissolve_result, "BH", "LONG")
    arcpy.CalculateField_management(dissolve_result, "BH", "!OBJECTID!", "PYTHON_9.3")
    arcpy.SpatialJoin_analysis(select_1, dissolve_result, spatialJoin, "JOIN_ONE_TO_ONE", "KEEP_ALL", "#", "INTERSECT")
    arcpy.Statistics_analysis(spatialJoin, spatialJoin_Statisti, [["Shape_Area","SUM"]], "BH")
    arcpy.TableSelect_analysis(spatialJoin_Statisti, tableSelect, where_clause2)
    arcpy.JoinField_management(spatialJoin, "BH", tableSelect, "BH", "BH")
    arcpy.Select_analysis(spatialJoin, last_result, "BH = BH_1")

    return last_result

def main():
    temp_name = getNewFileNameQ(out_path, "temp.gdb")
    temp_gdb = os.path.join(out_path, temp_name)
    try:
        if out_gdbnameg[-4:] == ".gdb":
            namegdb = getNewFileNameQ(out_path, out_gdbnameg)
        else:
            namegdb = getNewFileNameQ(out_path, out_gdbnameg + ".gdb")

        arcpy.AddMessage(u"新建 " + temp_gdb + u" 用于放过程数据")
        arcpy.CreateFileGDB_management(out_path, temp_name)
        arcpy.AddMessage(u"新建标准库：" + os.path.join(out_path, namegdb) + u" 作为最终提取结果")
        gdb_result = createGDBAndFeatureclass(out_path, namegdb, templetg, in_dltbg)
        arcpy.AddMessage(u"  ")
        arcpy.AddMessage(u"  开始提取图斑...")
        selectFeatureClass(in_dltbg, in_XZTJg, in_pdg, gdb_result, temp_gdb)
        arcpy.AddMessage(u"  完成提取！")
        arcpy.AddMessage(u"  ")
    except Exception as e:
        arcpy.AddError(e.message)

    if arcpy.Exists(temp_gdb):
        try:
            arcpy.Delete_management(temp_gdb)
        except Exception as e:
            print e.message

if __name__ == "__main__":
    in_dltbg = arcpy.GetParameterAsText(0)#三调地类图斑
    in_XZTJg = arcpy.GetParameterAsText(1)#限制条件
    in_pdg = arcpy.GetParameterAsText(2)#坡度
    templetg = arcpy.GetParameterAsText(3)#标准库模板
    out_path = arcpy.GetParameterAsText(4)#输出位置
    out_gdbnameg = arcpy.GetParameterAsText(5)#gdb名字

    main()


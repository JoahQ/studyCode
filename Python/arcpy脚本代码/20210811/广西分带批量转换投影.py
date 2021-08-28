# -*- coding: gbk -*-
import sys
import arcpy
import os
import re

reload(sys)
sys.setdefaultencoding("utf-8")
arcpy.SetLogHistory(True)
def gxplzhty(in_path,out_path):
    cout = 0
    fail = 0
    warning = 0
    fail_list = []
    warning_list = []

    list35 = ["451026", "451028", "451029", "451030", "451031", "451081"]

    list36 = ["450102","450103","450105","450107","450108","450109","450110","450123","450124","450125","450126",
              "450127","450202","450203","450204","450205","450206","450222","450224","450225","450226","450502",
              "450503","450512","450521","450602","450603","450621","450681","450702","450703","450721","450804",
              "451002","451003","451022","451082","451024","451027","451202","451203","451221","451222","451223",
              "451224","451225","451226","451227","451228","451229","451302","451321","451381","451402","451421",
              "451422","451423","451424","451425","451481"]

    list37 = ["450223","450302","450303","450304","450305","450311","450312","450321","450323","450324","450325",
              "450326","450327","450328","450329","450330","450332","450381","450403","450405","450406","450421",
              "450422","450423","450481","450722","450802","450803","450821","450881","450902","450903","450921",
              "450922","450923","450924","450981","451102","451103","451121","451122","451123","451322","451323",
              "451324"]

    arcpy.env.workspace = in_path
    workspaces = arcpy.ListWorkspaces("*", "ALL")

    for workspace in workspaces:
        arcpy.AddMessage("=" * 60)
        cout += 1
        arcpy.AddMessage(" (" + str(cout) + ") " + os.path.basename(workspace))
        arcpy.AddMessage("  ")
        gdbName = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1])
        temp_name1 = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1]) + ".gdb"
        out_gdb_path = os.path.join(out_path, temp_name1)
        try:
            xzqcode = re.findall(r"\d+", gdbName)

            if xzqcode[0] in list35:
                outprjdir = "PROJCS['CGCS2000_3_Degree_GK_Zone_35',GEOGCS['GCS_China_Geodetic_Coordinate_System_2000'," \
                            "DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0]," \
                            "UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',35500000.0]," \
                            "PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',105.0],PARAMETER['Scale_Factor',1.0]," \
                            "PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
            elif xzqcode[0] in list36:
                outprjdir = "PROJCS['CGCS2000_3_Degree_GK_Zone_36',GEOGCS['GCS_China_Geodetic_Coordinate_System_2000'," \
                            "DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0]," \
                            "UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',36500000.0]," \
                            "PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',108.0],PARAMETER['Scale_Factor',1.0]," \
                            "PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
            elif xzqcode[0] in list37:
                outprjdir = "PROJCS['CGCS2000_3_Degree_GK_Zone_37',GEOGCS['GCS_China_Geodetic_Coordinate_System_2000'," \
                            "DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0]," \
                            "UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',37500000.0]," \
                            "PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',111.0],PARAMETER['Scale_Factor',1.0]," \
                            "PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
            else:
                arcpy.AddError(workspace + u" 县代码不正确！")
                fail_list.append(os.path.basename(workspace))
                fail += 1
                continue

            if not arcpy.Exists(out_gdb_path):
                arcpy.AddMessage(u"新建 " + out_gdb_path + u" ...")
                arcpy.CreateFileGDB_management(out_path, temp_name1)
            else:
                arcpy.AddWarning(workspace + u" 已存在！")
                warning_list.append(workspace)
                warning += 1
                continue

            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()
            fc_count = 0
            for fc in fc_list:
                fc_count += 1
                in_fc_path = os.path.join(workspace,fc)
                out_fc_path = os.path.join(out_gdb_path,fc)
                arcpy.AddMessage("     " + str(fc_count) + "、" + fc)
                arcpy.AddMessage("          转换前投影为：" + arcpy.Describe(in_fc_path).spatialReference.name)
                arcpy.Project_management(in_fc_path, out_fc_path, outprjdir)
                arcpy.AddMessage("          转换后投影为：" + arcpy.Describe(out_fc_path).spatialReference.name)
                arcpy.AddMessage("          ")

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + workspace + " 失败！")
            fail_list.append(workspace)
            fail += 1
            if arcpy.Exists(out_gdb_path):
                try:
                    arcpy.Delete_management(out_gdb_path)
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

    gxplzhty(in_pathg,out_patha)
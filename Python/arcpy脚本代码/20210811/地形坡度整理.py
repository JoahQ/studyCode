# -*- coding: gbk -*-
import sys
import arcpy
import os

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

def dxpd(in_path,out_path):
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
        arcpy.AddMessage("  ")
        try:
            # 将每个gdb设为工作区
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()
            temp_name1 = os.path.basename(workspace) + "地形坡度图.gdb"
            result_gdb = os.path.join(out_path, temp_name1)

            if not arcpy.Exists(result_gdb):
                arcpy.AddMessage("新建 " + result_gdb + " ...")
                arcpy.CreateFileGDB_management(out_path, temp_name1)
            else:
                arcpy.AddWarning(result_gdb + u" 已存在！")
                warning_list.append(result_gdb)
                warning += 1
                continue
            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                out_fc_name = "DXPD"
                arcpy.AddMessage("      " + infc_path + "...")
                arcpy.FeatureClassToFeatureClass_conversion(infc_path,result_gdb,out_fc_name)

                out_fc_path = os.path.join(result_gdb, out_fc_name)
                arcpy.AlterAliasName(out_fc_path,"地形坡度")
                put_field = "DXPDJB"
                fieldAlias = "地形坡度级别"
                arcpy.AddField_management(out_fc_path, put_field, 'TEXT', "#", "#", 10, fieldAlias)
                codeblock1 = """def getV(v):
                                if str(v).strip() in ['1','2','3','4']:
                                    return '≤25°'
                                else:
                                    return '＞25°'
                            """
                expression = "getV(!PDJB!)"

                arcpy.CalculateField_management(out_fc_path, put_field, expression, "PYTHON_9.3", codeblock1)

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " 失败！")
            fail_list.append(os.path.basename(workspace))
            fail += 1

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

def trzd(in_path,out_path):
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
        arcpy.AddMessage("  ")
        try:
            # 将每个gdb设为工作区
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()
            temp_name1 = os.path.basename(workspace).rstrip(os.path.splitext(workspace)[1]) + "土壤质地图.gdb"
            result_gdb = os.path.join(out_path, temp_name1)

            if not arcpy.Exists(result_gdb):
                arcpy.AddMessage("新建 " + result_gdb + " ...")
                arcpy.CreateFileGDB_management(out_path, temp_name1)
            else:
                arcpy.AddWarning(result_gdb + u" 已存在！")
                warning_list.append(result_gdb)
                warning += 1
                continue
            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                out_fc_name = "TRZD"
                arcpy.AddMessage("      " + infc_path + " ...")
                arcpy.FeatureClassToFeatureClass_conversion(infc_path,result_gdb,out_fc_name)

                out_fc_path = os.path.join(result_gdb, out_fc_name)
                arcpy.AlterAliasName(out_fc_path,u"土壤质地")
                put_field = "TRZD"
                fieldAlias = u"土壤质地"
                arcpy.AddMessage("      添加字段：" + put_field + " 别名：" + fieldAlias)
                arcpy.AddField_management(out_fc_path, put_field, 'TEXT', "#", "#", 50, fieldAlias)

                arcpy.AddMessage("      计算字段：" + put_field)
                codeblockvb = """
                
                Dim density
                Dim s1
                Dim s2
                Dim s3
                s1 = "砖红壤赤红壤红壤黄壤黄红壤黄棕壤二合土紫色土石灰岩土水稻土红粘土"
                s2 = "粗骨土"
                s3 = Trim([土类])
                
                IF InStr(s1,s3) > 0 AND s3 <>"" Then
                density = "壤质、粘质或砂质"
                ELSEIF InStr(s2,s3) > 0 AND s3 <>"" Then
                density = "砾质或更粗质地"
                ELSE
                density = s3
                END IF
                
                """
                expression = "density"

                arcpy.CalculateField_management(out_fc_path, put_field, expression, "VB", codeblockvb)

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " 失败！")
            fail_list.append(os.path.basename(workspace))
            fail += 1

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
    dxpdgg = arcpy.GetParameter(2)
    trzdgg = arcpy.GetParameter(3)

    if dxpdgg and not trzdgg:
        dxpd(in_pathg,out_patha)
    elif not dxpdgg and trzdgg:
        trzd(in_pathg,out_patha)
    else:
        arcpy.AddError("必须勾选且只能勾选一个！")
        a = []
        print a[99]

# def getV(v):
#     ls = '砖红壤赤红壤红壤黄壤黄红壤黄棕壤二合土紫色土石灰岩土水稻土红粘土'.decode('utf-8')
#     ls2 = "粗骨土".decode('utf-8')
#
#     if str(v.decode('utf-8')).strip() in ls:
#         return '壤质、粘质或砂质'.decode('utf-8')
#     elif str(v.decode('utf-8')).strip() in ls2:
#         return '砾质或更粗质地'.decode('utf-8')
#     else:
#         return v

"""
    ls = [u'砖红壤',u'赤红壤',u'红壤',u'黄壤',u'黄红壤',u'黄棕壤',u'二合土',u'紫色土',u'石灰岩土',u'水稻土',u'红粘土']

field_alias = [f.aliasName for f in ls]
Dim density
IF InStr("砖红壤赤红壤红壤黄壤黄红壤黄棕壤二合土紫色土石灰岩土水稻土红粘土",[土类]) > 0 Then
density = "壤质、粘质或砂质"
ELSEIF InStr("粗骨土",[土类]) Then
density = "砾质或更粗质地"
ELSE
density = [土类]
END IF



Dim density
Dim s1
Dim s2
Dim s3
s1 = "砖红壤赤红壤红壤黄壤黄红壤黄棕壤二合土紫色土石灰岩土水稻土红粘土"
s2 = "粗骨土"
s3 = Trim([abc])

IF InStr(s1,s3) > 0 AND s3 <>"" Then
density = "壤质、粘质或砂质"
ELSEIF InStr(s2,s3) > 0 AND s3 <>"" Then
density = "砾质或更粗质地"
ELSE
density = s3
END IF
"""
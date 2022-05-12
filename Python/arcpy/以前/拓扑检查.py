# -*- coding: gbk -*-
import os
import arcpy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
arcpy.AddMessage(sys.getdefaultencoding())

arcpy.env.XYResolution = "0.0001 Meters" #设置XY分辨率
arcpy.env.XYTolerance = "0.001 Meters"   #设置XY容差

def checkTopology(in_path, out_path):
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
            fc_list = arcpy.ListFeatureClasses() #列出gdb内的要素类图层
            in_fc_path_list = []
            for fc in fc_list:
                in_fc_path_list.append(os.path.join(workspace,fc))

            # 在输出路径out_path下新建gdb
            gdb_name1 = os.path.basename(workspace)
            result_gdb = os.path.join(out_path, gdb_name1)
            if not arcpy.Exists(result_gdb):
                arcpy.AddMessage("    新建 " + result_gdb + " ...")
                arcpy.CreateFileGDB_management(out_path, gdb_name1)
            else:
                arcpy.AddWarning(result_gdb + " 已存在！")
                warning_list.append(result_gdb)
                warning += 1
                continue

            arcpy.AddMessage("    在 " + result_gdb + " 内新建要素数据集...")
            dataset_name = "dataset"
            dataset_path = os.path.join(result_gdb,dataset_name)
            # 引用包含要应用的空间参考的要素类或要素数据集，
            # 将in_fc_path_list[0]的坐标作为要素数据集的坐标，所以gdb内的所有要素类应该是统一坐标
            arcpy.CreateFeatureDataset_management(result_gdb, dataset_name, in_fc_path_list[0])

            #导入要素类到数据集
            arcpy.AddMessage("    向 " + dataset_path + " 导入要素类图层...")
            arcpy.FeatureClassToGeodatabase_conversion(in_fc_path_list,dataset_path)

            #在dataset数据内创建拓扑
            arcpy.AddMessage("    创建拓扑...")
            topology_name = "topology"
            topology_path = os.path.join(dataset_path, topology_name)
            arcpy.CreateTopology_management(dataset_path, topology_name)

            # 将导入dataset的要素类添加到拓扑中
            arcpy.AddMessage("    向拓扑中添加要素类...")
            dataset_fc_path_lsit = []  #数据集中的要素类绝对路径列表
            for ifc_name in fc_list:
                # 拼接数据集中的要素类绝对路径
                dataset_fc_path = os.path.join(dataset_path,ifc_name)
                dataset_fc_path_lsit.append(dataset_fc_path)
                arcpy.AddFeatureClassToTopology_management(topology_path, dataset_fc_path, "1", "1")

            arcpy.AddMessage("    添加拓扑规则...")
            for i in range(len(dataset_fc_path_lsit)):
                fc_path1 = dataset_fc_path_lsit[i]
                #规则1：不能重叠
                arcpy.AddRuleToTopology_management(topology_path, "Must Not Overlap (Area)", fc_path1, "", "", "")
                for j in range(i + 1, len(dataset_fc_path_lsit)):
                    fc_path2 = dataset_fc_path_lsit[j]
                    # 规则2：不能重叠与其他要素类重叠
                    arcpy.AddRuleToTopology_management(topology_path, "Must Not Overlap With (Area-Area)", fc_path1, "", fc_path2, "")

            arcpy.AddMessage("    拓扑验证...")
            arcpy.ValidateTopology_management(topology_path, "Full_Extent")

            arcpy.AddMessage("    导出拓扑错误...")
            arcpy.ExportTopologyErrors_management(topology_path, dataset_path, "topoError")

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
    in_path_globle = arcpy.GetParameterAsText(0)
    out_path_globe = arcpy.GetParameterAsText(1)

    checkTopology(in_path_globle,out_path_globe)
# -*- coding: gbk -*-
import os
import arcpy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
arcpy.AddMessage(sys.getdefaultencoding())

arcpy.env.XYResolution = "0.0001 Meters" #����XY�ֱ���
arcpy.env.XYTolerance = "0.001 Meters"   #����XY�ݲ�

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
            # ��ÿ��gdb��Ϊ������
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses() #�г�gdb�ڵ�Ҫ����ͼ��
            in_fc_path_list = []
            for fc in fc_list:
                in_fc_path_list.append(os.path.join(workspace,fc))

            # �����·��out_path���½�gdb
            gdb_name1 = os.path.basename(workspace)
            result_gdb = os.path.join(out_path, gdb_name1)
            if not arcpy.Exists(result_gdb):
                arcpy.AddMessage("    �½� " + result_gdb + " ...")
                arcpy.CreateFileGDB_management(out_path, gdb_name1)
            else:
                arcpy.AddWarning(result_gdb + " �Ѵ��ڣ�")
                warning_list.append(result_gdb)
                warning += 1
                continue

            arcpy.AddMessage("    �� " + result_gdb + " ���½�Ҫ�����ݼ�...")
            dataset_name = "dataset"
            dataset_path = os.path.join(result_gdb,dataset_name)
            # ���ð���ҪӦ�õĿռ�ο���Ҫ�����Ҫ�����ݼ���
            # ��in_fc_path_list[0]��������ΪҪ�����ݼ������꣬����gdb�ڵ�����Ҫ����Ӧ����ͳһ����
            arcpy.CreateFeatureDataset_management(result_gdb, dataset_name, in_fc_path_list[0])

            #����Ҫ���ൽ���ݼ�
            arcpy.AddMessage("    �� " + dataset_path + " ����Ҫ����ͼ��...")
            arcpy.FeatureClassToGeodatabase_conversion(in_fc_path_list,dataset_path)

            #��dataset�����ڴ�������
            arcpy.AddMessage("    ��������...")
            topology_name = "topology"
            topology_path = os.path.join(dataset_path, topology_name)
            arcpy.CreateTopology_management(dataset_path, topology_name)

            # ������dataset��Ҫ������ӵ�������
            arcpy.AddMessage("    �����������Ҫ����...")
            dataset_fc_path_lsit = []  #���ݼ��е�Ҫ�������·���б�
            for ifc_name in fc_list:
                # ƴ�����ݼ��е�Ҫ�������·��
                dataset_fc_path = os.path.join(dataset_path,ifc_name)
                dataset_fc_path_lsit.append(dataset_fc_path)
                arcpy.AddFeatureClassToTopology_management(topology_path, dataset_fc_path, "1", "1")

            arcpy.AddMessage("    ������˹���...")
            for i in range(len(dataset_fc_path_lsit)):
                fc_path1 = dataset_fc_path_lsit[i]
                #����1�������ص�
                arcpy.AddRuleToTopology_management(topology_path, "Must Not Overlap (Area)", fc_path1, "", "", "")
                for j in range(i + 1, len(dataset_fc_path_lsit)):
                    fc_path2 = dataset_fc_path_lsit[j]
                    # ����2�������ص�������Ҫ�����ص�
                    arcpy.AddRuleToTopology_management(topology_path, "Must Not Overlap With (Area-Area)", fc_path1, "", fc_path2, "")

            arcpy.AddMessage("    ������֤...")
            arcpy.ValidateTopology_management(topology_path, "Full_Extent")

            arcpy.AddMessage("    �������˴���...")
            arcpy.ExportTopologyErrors_management(topology_path, dataset_path, "topoError")

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " ʧ�ܣ�")
            fail_list.append(os.path.basename(workspace))
            fail += 1

    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage(u"  �ɹ���" + str(cout - fail - warning) + u" ����")
    if warning > 0:
        arcpy.AddWarning(u"  ���棺" + str(warning) + u" ���� ���£�")
        arcpy.AddWarning("####" + '*' * 20)
        for fff in warning_list:
            arcpy.AddWarning("  " + fff)
        arcpy.AddWarning("####" + '*' * 20)
    if fail > 0:
        arcpy.AddError(u"  ʧ�ܣ�" + str(fail) + u" ���� ���£�")
        arcpy.AddError("####" + '*' * 20)
        for ff in fail_list:
            arcpy.AddError("  " + ff)
        arcpy.AddError("####" + '*' * 20)
    arcpy.AddMessage('+' * 60)

if __name__ == "__main__":
    in_path_globle = arcpy.GetParameterAsText(0)
    out_path_globe = arcpy.GetParameterAsText(1)

    checkTopology(in_path_globle,out_path_globe)
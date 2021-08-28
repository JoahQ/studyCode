# -*- coding: gbk -*-
import sys
import arcpy
import os

reload(sys)
sys.setdefaultencoding("utf-8")

def checkFeatureClassName(in_workspace_cfn):
    arcpy.env.workspace = in_workspace_cfn
    fc_lists = arcpy.ListFeatureClasses()
    right_name = True
    ls1 = ["�������ʸ���Ǳ������ͼ��", "�����õظ���Ǳ������ͼ��", "�˸�ũ�õ�Ǳ������ͼ��", "�˸�δ���õ�Ǳ������ͼ��", "������ȡǱ��ͼ��"]
    ls2 = [u"�������ʸ���Ǳ������ͼ��",u"�����õظ���Ǳ������ͼ��",u"�˸�ũ�õ�Ǳ������ͼ��",u"�˸�δ���õ�Ǳ������ͼ��",u"������ȡǱ��ͼ��"]
    for fc in fc_lists:
        if not (fc in ls1 or fc in ls2):
            right_name = False
            arcpy.AddError("    \"" + fc + "\" ͼ���������淶������")
    if len(fc_lists) <= 0:
        right_name = False
        arcpy.AddError("���ݿ⣺" + in_workspace_cfn + " û��ͼ�㣡����")
    if not right_name:
        arcpy.AddError("���ݿ⣺" + in_workspace_cfn + " ͼ���������淶������")
        arcpy.AddMessage("-" * 25)
        arcpy.AddMessage("  ��׼��ͼ������Ӧ��Ϊ��")
        arcpy.AddMessage("     �������ʸ���Ǳ������ͼ��")
        arcpy.AddMessage("     �����õظ���Ǳ������ͼ��")
        arcpy.AddMessage("     �˸�ũ�õ�Ǳ������ͼ��")
        arcpy.AddMessage("     �˸�δ���õ�Ǳ������ͼ��")
        arcpy.AddMessage("     ������ȡǱ��ͼ��")
        arcpy.AddMessage("-"*25)

    return right_name

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

def mergeFeatureClass(in_path, out_path, name):

    arcpy.env.workspace = in_path
    # ��ȡ�������ڵ�gdb�б�
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")
    list_fcs1 = []
    list_fcs2 = []
    list_fcs3 = []
    list_fcs4 = []
    list_fcs5 = []
    cout = 0
    fail = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    for workspace in workspaces:
        right = checkFeatureClassName(workspace)
        if right:
            continue
        else:
            fail += 1
            arcpy.AddError(u"     " + os.path.basename(workspace) + u" ʧ�ܣ�")


    if fail > 0:
        list0 = []
        print list0[99999999]
        sys.exit()
    
    namegdb = getNewFileNameQ(out_path, name + ".gdb")
    arcpy.CreateFileGDB_management(out_path, namegdb)
    outgdb_path = os.path.join(out_path, namegdb)
    for workspace in workspaces:
        cout += 1
        arcpy.AddMessage(str(cout) + "��" + os.path.basename(workspace))
        arcpy.env.workspace = workspace
        fc_lista = arcpy.ListFeatureClasses()
        for fac in fc_lista:
            clsPath = os.path.join(workspace, fac)

            if "���ʸ���" in fac:
                list_fcs1.append(clsPath)

            elif "�����õ�" in fac:
                list_fcs2.append(clsPath)

            elif "ũ�õ�" in fac:
                list_fcs3.append(clsPath)

            elif "δ���õ�" in fac:
                list_fcs4.append(clsPath)

            elif "������ȡ" in fac:
                list_fcs5.append(clsPath)


    out_path1 = os.path.join(outgdb_path, u"�������ʸ���Ǳ������ͼ��")
    out_path2 = os.path.join(outgdb_path, u"�����õظ���Ǳ������ͼ��")
    out_path3 = os.path.join(outgdb_path, u"�˸�ũ�õ�Ǳ������ͼ��")
    out_path4 = os.path.join(outgdb_path, u"�˸�δ���õ�Ǳ������ͼ��")
    out_path5 = os.path.join(outgdb_path, u"������ȡǱ��ͼ��")

    arcpy.AddMessage("  ")
    arcpy.AddMessage(u"�ҵ�" + str(cout) + u" ��gdb��\n ")
    arcpy.AddMessage(u"��ʼ�ϲ�...")
    arcpy.AddMessage("  ")
    arcpy.AddMessage("-" * 20)

    if len(list_fcs1) > 0:
        try:
            arcpy.AddMessage(u"���ںϲ��������ʸ���Ǳ������ͼ��...")
            arcpy.Merge_management(list_fcs1, out_path1)
        except Exception as e:
            arcpy.AddError(e.message)

    if len(list_fcs2) > 0:
        try:
            arcpy.AddMessage(u"���ںϲ������õظ���Ǳ������ͼ��...")
            arcpy.Merge_management(list_fcs2, out_path2)
        except Exception as e:
            arcpy.AddError(e.message)

    if len(list_fcs3) > 0:
        try:
            arcpy.AddMessage(u"���ںϲ��˸�ũ�õ�Ǳ������ͼ��...")
            arcpy.Merge_management(list_fcs3, out_path3)
        except Exception as e:
            arcpy.AddError(e.message)

    if len(list_fcs4) > 0:
        try:
            arcpy.AddMessage(u"���ںϲ��˸�δ���õ�Ǳ������ͼ��...")
            arcpy.Merge_management(list_fcs4, out_path4)
        except Exception as e:
            arcpy.AddError(e.message)

    if len(list_fcs5) > 0:
        try:
            arcpy.AddMessage(u"���ںϲ�������ȡǱ��ͼ��...")
            arcpy.Merge_management(list_fcs5, out_path5)
        except Exception as e:
            arcpy.AddError(e.message)

    arcpy.AddMessage(" ")
    if arcpy.Exists(out_path1):
        arcpy.AddMessage(u"�������ʸ���Ǳ������ͼ�� �ϲ���ͼ������" + str(arcpy.GetCount_management(out_path1).getOutput(0)))
    if arcpy.Exists(out_path2):
        arcpy.AddMessage(u"�����õظ���Ǳ������ͼ�� �ϲ���ͼ������" + str(arcpy.GetCount_management(out_path2).getOutput(0)))
    if arcpy.Exists(out_path3):
        arcpy.AddMessage(u"�˸�ũ�õ�Ǳ������ͼ�� �ϲ���ͼ������" + str(arcpy.GetCount_management(out_path3).getOutput(0)))
    if arcpy.Exists(out_path4):
        arcpy.AddMessage(u"�˸�δ���õ�Ǳ������ͼ�� �ϲ���ͼ������" + str(arcpy.GetCount_management(out_path4).getOutput(0)))
    if arcpy.Exists(out_path5):
        arcpy.AddMessage(u"������ȡǱ��ͼ�� �ϲ���ͼ������" + str(arcpy.GetCount_management(out_path5).getOutput(0)))


if __name__ == "__main__":

    in_pathgg = arcpy.GetParameterAsText(0)
    out_pathgg = arcpy.GetParameterAsText(1)
    namegg = arcpy.GetParameterAsText(2)
    anshifang = arcpy.GetParameter(3)
    fendai = arcpy.GetParameter(4)

    if anshifang:
        city_list = [u"01������", u"02������", u"03������", u"04������", u"05������", u"06���Ǹ���", u"07������", u"08�����",
                     u"09������", u"10��ɫ��", u"11������", u"12�ӳ���", u"13������", u"14������"]
        for city in city_list:
            in_pathcc = os.path.join(in_pathgg, city)
            if not arcpy.Exists(in_pathcc):
                arcpy.CreateFolder_management(in_pathgg, city)
            arcpy.AddMessage(" ")
            arcpy.AddMessage(city)
            if arcpy.Exists(in_pathcc):
                arcpy.AddMessage("+" * 60)
                mergeFeatureClass(in_pathcc, out_pathgg, city + u"�ϲ�")
                arcpy.AddMessage("+"*60)
            else:
                arcpy.AddMessage(in_pathcc + u" �����ڣ�")
                arcpy.AddMessage(" ")
    elif fendai:
        fffddd = ["35","36","37"]
        for fdf in fffddd:
            in_pathcc = os.path.join(in_pathgg, fdf)
            arcpy.AddMessage("  " * 20)
            mergeFeatureClass(in_pathcc, out_pathgg, fdf + u"�ϲ�")
            arcpy.AddMessage("+"*20)
    else:
        mergeFeatureClass(in_pathgg, out_pathgg, namegg)





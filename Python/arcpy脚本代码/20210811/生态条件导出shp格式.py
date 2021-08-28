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
        return "������"
    elif e == "450103":
        return "������"
    elif e == "450105":
        return "������"
    elif e == "450107":
        return "��������"
    elif e == "450108":
        return "������"
    elif e == "450109":
        return "������"
    elif e == "450110":
        return "������"
    elif e == "450123":
        return "¡����"
    elif e == "450124":
        return "��ɽ��"
    elif e == "450125":
        return "������"
    elif e == "450126":
        return "������"
    elif e == "450127":
        return "����"
    elif e == "4502":
        return "������"
    elif e == "450202":
        return "������"
    elif e == "450203":
        return "�����"
    elif e == "450204":
        return "������"
    elif e == "450205":
        return "������"
    elif e == "450206":
        return "������"
    elif e == "450222":
        return "������"
    elif e == "450223":
        return "¹կ��"
    elif e == "450224":
        return "�ڰ���"
    elif e == "450225":
        return "��ˮ����������"
    elif e == "450226":
        return "��������������"
    elif e == "4503":
        return "������"
    elif e == "450302":
        return "�����"
    elif e == "450303":
        return "������"
    elif e == "450304":
        return "��ɽ��"
    elif e == "450305":
        return "������"
    elif e == "450311":
        return "��ɽ��"
    elif e == "450312":
        return "�ٹ���"
    elif e == "450321":
        return "��˷��"
    elif e == "450323":
        return "�鴨��"
    elif e == "450324":
        return "ȫ����"
    elif e == "450325":
        return "�˰���"
    elif e == "450326":
        return "������"
    elif e == "450327":
        return "������"
    elif e == "450328":
        return "��ʤ����������"
    elif e == "450329":
        return "��Դ��"
    elif e == "450330":
        return "ƽ����"
    elif e == "450332":
        return "��������������"
    elif e == "450381":
        return "������"
    elif e == "4504":
        return "������"
    elif e == "450403":
        return "������"
    elif e == "450405":
        return "������"
    elif e == "450406":
        return "������"
    elif e == "450421":
        return "������"
    elif e == "450422":
        return "����"
    elif e == "450423":
        return "��ɽ��"
    elif e == "450481":
        return "�Ϫ��"
    elif e == "4505":
        return "������"
    elif e == "450502":
        return "������"
    elif e == "450503":
        return "������"
    elif e == "450512":
        return "��ɽ����"
    elif e == "450521":
        return "������"
    elif e == "4506":
        return "���Ǹ���"
    elif e == "450602":
        return "�ۿ���"
    elif e == "450603":
        return "������"
    elif e == "450621":
        return "��˼��"
    elif e == "450681":
        return "������"
    elif e == "4507":
        return "������"
    elif e == "450702":
        return "������"
    elif e == "450703":
        return "�ձ���"
    elif e == "450721":
        return "��ɽ��"
    elif e == "450722":
        return "�ֱ���"
    elif e == "4508":
        return "�����"
    elif e == "450802":
        return "�۱���"
    elif e == "450803":
        return "������"
    elif e == "450804":
        return "������"
    elif e == "450821":
        return "ƽ����"
    elif e == "450881":
        return "��ƽ��"
    elif e == "4509":
        return "������"
    elif e == "450902":
        return "������"
    elif e == "450903":
        return "������"
    elif e == "450921":
        return "����"
    elif e == "450922":
        return "½����"
    elif e == "450923":
        return "������"
    elif e == "450924":
        return "��ҵ��"
    elif e == "450981":
        return "������"
    elif e == "4510":
        return "��ɫ��"
    elif e == "451002":
        return "�ҽ���"
    elif e == "451003":
        return "������"
    elif e == "451022":
        return "�ﶫ��"
    elif e == "451082":
        return "ƽ����"
    elif e == "451024":
        return "�±���"
    elif e == "451026":
        return "������"
    elif e == "451027":
        return "������"
    elif e == "451028":
        return "��ҵ��"
    elif e == "451029":
        return "������"
    elif e == "451030":
        return "������"
    elif e == "451031":
        return "¡�ָ���������"
    elif e == "451081":
        return "������"
    elif e == "4511":
        return "������"
    elif e == "451102":
        return "�˲���"
    elif e == "451103":
        return "ƽ����"
    elif e == "451121":
        return "��ƽ��"
    elif e == "451122":
        return "��ɽ��"
    elif e == "451123":
        return "��������������"
    elif e == "4512":
        return "�ӳ���"
    elif e == "451202":
        return "��ǽ���"
    elif e == "451203":
        return "������"
    elif e == "451221":
        return "�ϵ���"
    elif e == "451222":
        return "�����"
    elif e == "451223":
        return "��ɽ��"
    elif e == "451224":
        return "������"
    elif e == "451225":
        return "�޳�������������"
    elif e == "451226":
        return "����ë����������"
    elif e == "451227":
        return "��������������"
    elif e == "451228":
        return "��������������"
    elif e == "451229":
        return "������������"
    elif e == "4513":
        return "������"
    elif e == "451302":
        return "�˱���"
    elif e == "451321":
        return "�ó���"
    elif e == "451322":
        return "������"
    elif e == "451323":
        return "������"
    elif e == "451324":
        return "��������������"
    elif e == "451381":
        return "��ɽ��"
    elif e == "4514":
        return "������"
    elif e == "451402":
        return "������"
    elif e == "451421":
        return "������"
    elif e == "451422":
        return "������"
    elif e == "451423":
        return "������"
    elif e == "451424":
        return "������"
    elif e == "451425":
        return "�����"
    elif e == "451481":
        return "ƾ����"
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
            # ��ÿ��gdb��Ϊ������
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()

            for ifc in fc_list:
                infc_path = os.path.join(workspace, ifc)
                if int(arcpy.GetCount_management(infc_path).getOutput(0)) > 0:
                    if add_field.strip() != '':
                        arcpy.AddMessage("    ��� " + add_field + " �ֶ� ...")
                        arcpy.AddField_management(infc_path, add_field, "TEXT", "", "", 50)
                        arcpy.AddMessage("     ���� " + field_txt + " �� " + add_field + " �ֶ�...")
                        arcpy.CalculateField_management(infc_path, add_field, "'" + field_txt + "'", "PYTHON_9.3")


                    arcpy.AddMessage("    ���� " + shpfile_name + " ...")
                    arcpy.FeatureClassToFeatureClass_conversion(infc_path,out_path,shpfile_name)
                else:
                    arcpy.AddWarning(infc_path + " ͼ����Ϊ0��")
                    logging.warning(infc_path + " ͼ����Ϊ0��")
                    warning_list.append(infc_path)
                    warning += 1

        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + os.path.basename(workspace) + " ʧ�ܣ�")
            logging.error("    " + os.path.basename(workspace) + " ʧ�ܣ�")
            logging.error(e.message)
            fail_list.append(os.path.basename(workspace))
            fail += 1
            if arcpy.Exists(shp_path):
                try:
                    arcpy.Delete_management(shp_path)
                except Exception as e:
                    arcpy.AddError(e.message)

    arcpy.AddMessage('+' * 60)
    arcpy.AddMessage(u"  �ɹ���" + str(cout - fail - warning) + u" ����")
    logging.info(u"  �ɹ���" + str(cout - fail - warning) + u" ����")

    if warning > 0:
        arcpy.AddWarning(u"  ���棺" + str(warning) + u" ���� ���£�")
        arcpy.AddWarning("####" + '*' * 20)
        for fff in warning_list:
            arcpy.AddWarning("  " + fff)
            logging.warning("  " + fff)
        arcpy.AddWarning("####" + '*' * 20)
    if fail > 0:
        arcpy.AddError(u"  ʧ�ܣ�" + str(fail) + u" ���� ���£�")
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

    logging.info("��ʼִ��...")
    logging.info(in_pathg)
    logging.info(out_patha)
    logging.info(addfield_gg)
    logging.info(txt)
    logging.info(add_name)
    daochushp(in_pathg,out_patha,addfield_gg,txt,add_name)
    logging.info("ִ�н�����")
# -*- coding: gbk -*-
import sys
import arcpy
import os

reload(sys)
sys.setdefaultencoding("utf-8")
arcpy.SetLogHistory(True)
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
            arcpy.AddMessage("�½� " + out_gdb + " ...")
            arcpy.CreateFileGDB_management(out_path, out_gdb_name)
        else:
            arcpy.AddWarning(out_gdb_name + u" �Ѵ��ڣ�")
            warning_list.append(out_gdb_name)
            warning += 1
            continue
        out_fc_path = os.path.join(out_gdb,gdbname)
        expr_sec = field + " like \'%" + str(code) + "%\'"
        try:
            arcpy.Select_analysis(in_path, out_fc_path, expr_sec)
        except Exception as e:
            arcpy.AddError(e.message)
            arcpy.AddError("    " + out_gdb_name + " ʧ�ܣ�")
            fail_list.append(out_gdb_name)
            fail += 1
            if arcpy.Exists(out_gdb):
                try:
                    arcpy.Delete_management(out_gdb)
                except Exception as e:
                    arcpy.AddMessage(e.message)


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
    in_pathg = arcpy.GetParameterAsText(0)
    out_patha = arcpy.GetParameterAsText(1)
    out_name = arcpy.GetParameterAsText(2)
    ffff = arcpy.GetParameterAsText(3)

    huafenxiancode(in_pathg,out_patha,out_name,ffff)
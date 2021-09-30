#encoding: utf-8
import arcpy
import math

class Point:
    X=0
    Y=0
def CaculateAngle(pointArray,angle):
    if len(pointArray)<3:
        return False
    for i in range(0, len(pointArray)):
        print i, pointArray[i]
        ptL=Point()
        ptM=Point()
        ptR=Point()
        if i<len(pointArray)-2:
         ptL=pointArray[i]
         ptM=pointArray[i+1]
         ptR=pointArray[i+2]
        elif i==len(pointArray)-2:
            ptL = pointArray[i]
            ptM = pointArray[i + 1]
            ptR = pointArray[0]
        elif i == len(pointArray) - 1:
            ptL = pointArray[i]
            ptM = pointArray[0]
            ptR = pointArray[1]
        AML=Point()
        AML.X=ptL.X-ptM.X
        AML.Y=ptL.Y-ptM.Y

        AMR=Point()
        AMR.X=ptR.X-ptM.X
        AMR.Y = ptR.Y - ptM.Y

        ab=(AML.X*AMR.X+AML.Y*AMR.Y)
        M=(math.sqrt(AML.X*AML.X+AML.Y*AML.Y)*math.sqrt(AMR.X*AMR.X+AMR.Y*AMR.Y));
        cosA=ab/M

        #向量乘积小于0，说明是大于90度，不用判断
        if ab<0:
            continue
        #因为0到π/2是递减,所以小于cos给定角度值，那么角度比给定角度值大,就返回了
        elif cosA<=math.cos(angle/180*math.pi):
            continue
        elif cosA>math.cos(angle/180*math.pi):
            return True
    # 遍历所有的顶点了，说明满足要求
    return False


testData=ur"D:\gisdata\Export_Output.shp"
inpath = 'D:\\gisdata\\test0929.txt'
uipath = unicode(inpath, "utf8")
outFile = open(uipath, "w")
for row in arcpy.da.SearchCursor(testData, ["FID", "SHAPE@"]):
    ID = row[0]
    tempPart = []
    partnum = 0
    for part in row[1]:
        print("Part {0}:".format(partnum))
        tempPart = []
        ptnum=0
        pointArray=[]
        for pnt in part:
         if pnt:
            print("点 {0}:".format(ptnum))
            point = Point()
            point.X = pnt.X
            point.Y = pnt.Y
            pointArray.append(point)
            ptnum+=1
         else:
              print("内环:")
        pointArray.pop(len(pointArray)-1)

        #将不符合要求的写入到txt文件中
        if CaculateAngle(pointArray, 45):
            outFile.write("{0}\n".format(ID))
            print("ID为{0}的属性面含有不满足要求的锐角\n".format(ID))
    partnum += 1
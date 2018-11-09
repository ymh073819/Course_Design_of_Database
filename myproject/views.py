# coding=utf-8
from django.shortcuts import render_to_response,render,redirect,HttpResponseRedirect
from django.http import  HttpResponse,Http404
from myproject.forms import *
from myproject.models import *
from django.contrib.auth import login,logout,authenticate
from django.conf import settings
from django.contrib.auth.hashers import make_password
import time
from django.contrib.admin.views.decorators import staff_member_required  #装饰器
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
import random
import xlrd
import uuid
import random
from xlwt import *
import datetime
from collections import namedtuple
from django.db.models import *
import math
import pymysql

def pdf(x):
    return math.exp(-(x) ** 2 / (2)) / (math.sqrt(2 * math.pi))

def sum_fun_xk(xk, func):
    return sum([func(each) for each in xk])

def integral(a, b, n, func):
    h = (b - a)/float(n)
    xk = [a + i*h for i in range(1, n)]
    return h/2 * (func(a) + 2 * sum_fun_xk(xk, func) + func(b))

def cdfd(a,b,u,o):
    if o ==0:
        return 0
    else:
        return integral((a-u)/o,(b-u)/o,10000,pdf)
#通过正态分布求概率的函数（求积分）


def data2base(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'reason': '请先登录'})
    x = y = z = w = 0

    if request.GET['table'] == '1':
        tbCell_list = []
        #print('table:1')
        f=open(r'C:\Users\Administrator\Desktop\数据库系统原理课程设计-18\三门峡地区TD-LTE网络数据-2017-03\1.tbCell.csv','r',encoding='utf-8')
        next(f)  # 将文件标记移到下一行
        for line in f:
            #print(line)
            parts = line.replace('"', '')  # 将字典中的"替换空
            parts = parts.split(',')  # 按;对字符串进行切片
            #print(parts)
            y = y + 1
            tbCell_list.append(
            tbCell(
            CITY = parts[0],
            SECTOR_ID = parts[1],
            SECTOR_NAME = parts[2],
            ENODEBID = parts[3],
            ENODEB_NAME = parts[4],
            EARFCN = int(parts[5]),
            PCI = int(parts[6]),
            PSS = int(parts[7]),
            SSS = int(parts[8]),
            TAC = int(parts[9]),
            VENDOR = parts[10],
            LONGITUDE = float(parts[11]),
            LATITUDE = float(parts[12]),
            STYLE = parts[13],
            AZIMUTH = int(parts[14]),
            HEIGHT = None if parts[15]=='' else int(parts[15]),
            ELECTTILT = None if parts[16]=='' else int(parts[16]),
            MECHTILT = None if parts[15]=='' else int(parts[17]),
            TOTLETILT = None if parts[15]=='' else int(parts[18]),
                   )
            )
            if y == 50:  # 在for line in f循环中判断 每组50行输入  最后一组可能不足50行  在for循环结束后
                tbCell.objects.bulk_create(tbCell_list)
                z = z + 1
                y = 0
                print('第' + str(z) + '组数据导入成功')
                tbCell_list.clear()

        tbCell.objects.bulk_create(tbCell_list)
        f.close()

    elif request.GET['table'] == '2':
        print('table:2')
        KPI_list = []
        f = open(r'C:\Users\Administrator\Desktop\数据库系统原理课程设计-18\三门峡地区TD-LTE网络数据-2017-03\表12优化区17日-19日KPI指标统计表-0717至0719.csv', 'r',
                 encoding='utf-8')
        next(f)  # 将文件标记移到下一行
        for line in f:
            #print(line)
            parts1 = line
            parts1 = parts1.split('"')  # 第一次分割   将小区详细信息  分解出来为part1[0] part1[1] part1[2]
            parts = parts1[0].split(',')
            parts2 = parts1[2].split(',')
            for x in parts2:
                if x == '':
                    parts2.remove(x)

            y = y + 1
            KPI_list.append(
                KPI(
                    START_TIME=parts[0],
                    T=int(parts[1]),
                    NET_ELE=parts[2],
                    SECTOR_DETAIL=parts1[1],
                    SECTOR_NAME=parts2[0],
                    RRC_BUILD=int(parts2[1]),
                    RRC_REQUEST=int(parts2[2]),
                    RRC_RATE=float(parts2[3]),
                    RAB_SUCCESS=int(parts2[4]),
                    RAB_TRY=int(parts2[5]),
                    RAB_RATE=float(parts2[6]),
                    eNodeB_TIME=int(parts2[7]),
                    SECTOR_TIME=int(parts2[8]),
                    RAB_DROP_RATE=float(parts2[9]),
                    CONN_RATE=float(parts2[10]),
                    RESET_TIME= int(parts2[11]),
                    ABNORMAL_TIME=int(parts2[12]),
                    SUCCESS_TIME=int(parts2[13]),
                    WIRELESS_DROP_RATE= float(parts2[14]),
                    eNodeB_IN_DIF_SUCCESS =int(parts2[15]),
                    eNodeB_IN_DIF_TRY = int(parts2[16]),
                    eNodeB_IN_SIM_SUCCESS= int(parts2[17]),
                    eNodeB_IN_SIM_TRY= int(parts2[18]),
                    eNodeB_OUT_DIF_SUCCESS=int(parts2[19]),
                    eNodeB_OUT_DIF_TRY=int(parts2[20]),
                    eNodeB_OUT_SIM_SUCCESS=int(parts2[21]),
                    eNodeB_OUT_SIM_TRY= None if parts2[22]=='NIL' else int(parts2[22]),
                    eNodeB_IN_RATE=None if parts2[23]=='NIL' else float(parts2[23]),
                    eNodeB_OUT_RATE=None if parts2[24]=='NIL' else float(parts2[24]),
                    SIM_RATE=None if parts2[25]=='NIL' else float(parts2[25]),
                    DIF_RATE=None if parts2[26]=='NIL' else float(parts2[26]),
                    TOTAL_SUCCESS_RATE = float(parts2[27]),
                    UP_BIT = int(parts2[28]),
                    DOWN_BIT = int(parts2[29]),
                    RRC_REBUILD_REQUEST = int(parts2[30]),
                    RRC_REBUILD_RATE= float(parts2[31]),
                    REBUILD_SIM_IN_TIME = int(parts2[32]),
                    REBUILD_DIF_IN_TIME=int(parts2[33]),
                    REBUILD_SIM_OUT_TIME=int(parts2[34]),
                    REBUILD_DIF_OUT_TIME = int(parts2[35]),
                    eNB_REQUEST_TIME = int(parts2[36]),
                    eNB_TRY_TIME = int(parts2[37]),
                )
            )
            if y == 50:  # 在for line in f循环中判断 每组50行输入  最后一组可能不足50行  在for循环结束后
                KPI.objects.bulk_create(KPI_list)
                z = z + 1
                y = 0
                print('第' + str(z) + '组数据导入成功')
                KPI_list.clear()
        KPI.objects.bulk_create(KPI_list)
        f.close()

    elif request.GET['table'] == '3':
        print('table:3')
        PRB_list = []
        f = open(
            r'C:\Users\Administrator\Desktop\数据库系统原理课程设计-18\三门峡地区TD-LTE网络数据-2017-03\表13 优化区17日-19日每PRB干扰 查询-15分钟.csv',
            'r',
            encoding='utf-8')
        next(f)  # 将文件标记移到下一行
        for line in f:
            # print(line)
            parts1 = line
            parts1 = parts1.split('"')  # 第一次分割   将小区详细信息  分解出来为part1[0] part1[1] part1[2]
            parts = parts1[0].split(',')
            parts2 = parts1[2].split(',')
            for x in parts2:
                if x == '':
                    parts2.remove(x)
            # print(parts2)
           # all = PRB.objects.filter(START_TIME=parts[0], SECTOR_DETAIL=parts1[1])
            #触发器会自动判断是插入还是更新

            y = y + 1
            PRB_list.append(
                PRB(
                    START_TIME=parts[0],
                    T=int(parts[1]),
                    NET_ELE=parts[2],
                    SECTOR_DETAIL=parts1[1],
                    SECTOR_NAME=parts2[0],
                    PRB0=parts2[1],
                    PRB1=parts2[2],
                    PRB2=parts2[3],
                    PRB3=parts2[4],
                    PRB4=parts2[5],
                    PRB5=parts2[6],
                    PRB6=parts2[7],
                    PRB7=parts2[8],
                    PRB8=parts2[9],
                    PRB9=parts2[10],
                    PRB10=parts2[11],
                    PRB11=parts2[12],
                    PRB12=parts2[13],
                    PRB13=parts2[14],
                    PRB14=parts2[15],
                    PRB15=parts2[16],
                    PRB16=parts2[17],
                    PRB17=parts2[18],
                    PRB18=parts2[19],
                    PRB19=parts2[20],
                    PRB20=parts2[21],
                    PRB21=parts2[22],
                    PRB22=parts2[23],
                    PRB23=parts2[24],
                    PRB24=parts2[25],
                    PRB25=parts2[26],
                    PRB26=parts2[27],
                    PRB27=parts2[28],
                    PRB28=parts2[29],
                    PRB29=parts2[30],
                    PRB30=parts2[31],
                    PRB31=parts2[32],
                    PRB32=parts2[33],
                    PRB33=parts2[34],
                    PRB34=parts2[35],
                    PRB35=parts2[36],
                    PRB36=parts2[37],
                    PRB37=parts2[38],
                    PRB38=parts2[39],
                    PRB39=parts2[40],
                    PRB40=parts2[41],
                    PRB41=parts2[42],
                    PRB42=parts2[43],
                    PRB43=parts2[44],
                    PRB44=parts2[45],
                    PRB45=parts2[46],
                    PRB46=parts2[47],
                    PRB47=parts2[48],
                    PRB48=parts2[49],
                    PRB49=parts2[50],
                    PRB50=parts2[51],
                    PRB51=parts2[52],
                    PRB52=parts2[53],
                    PRB53=parts2[54],
                    PRB54=parts2[55],
                    PRB55=parts2[56],
                    PRB56=parts2[57],
                    PRB57=parts2[58],
                    PRB58=parts2[59],
                    PRB59=parts2[60],
                    PRB60=parts2[61],
                    PRB61=parts2[62],
                    PRB62=parts2[63],
                    PRB63=parts2[64],
                    PRB64=parts2[65],
                    PRB65=parts2[66],
                    PRB66=parts2[67],
                    PRB67=parts2[68],
                    PRB68=parts2[69],
                    PRB69=parts2[70],
                    PRB70=parts2[71],
                    PRB71=parts2[72],
                    PRB72=parts2[73],
                    PRB73=parts2[74],
                    PRB74=parts2[75],
                    PRB75=parts2[76],
                    PRB76=parts2[77],
                    PRB77=parts2[78],
                    PRB78=parts2[79],
                    PRB79=parts2[80],
                    PRB80=parts2[81],
                    PRB81=parts2[82],
                    PRB82=parts2[83],
                    PRB83=parts2[84],
                    PRB84=parts2[85],
                    PRB85=parts2[86],
                    PRB86=parts2[87],
                    PRB87=parts2[88],
                    PRB88=parts2[89],
                    PRB89=parts2[90],
                    PRB90=parts2[91],
                    PRB91=parts2[92],
                    PRB92=parts2[93],
                    PRB93=parts2[94],
                    PRB94=parts2[95],
                    PRB95=parts2[96],
                    PRB96=parts2[97],
                    PRB97=parts2[98],
                    PRB98=parts2[99],
                    PRB99=parts2[100],
                )
                )
            if y==50:  #在for line in f循环中判断 每组50行输入  最后一组可能不足50行  在for循环结束后
                PRB.objects.bulk_create(PRB_list)
                z = z + 1
                y = 0
                print('第'+str(z)+'组数据导入成功')
                PRB_list.clear()
        PRB.objects.bulk_create(PRB_list)
        f.close()

    elif request.GET['table'] == '4':
        print('table:4')
        MRO_list = []
        f = open(
            r'C:\Users\Administrator\Desktop\数据库系统原理课程设计-18\三门峡地区TD-LTE网络数据-2017-03\9. tbMROData.csv',
            'r',
            encoding='utf-8')
        next(f)  # 将文件标记移到下一行
        for line in f:
            # print(line)
            parts = line
            parts = parts.split(',')

            parts6 = "".join(parts[6].split())
            y = y + 1

            MRO_list.append(
                MRO(
                    _TimeStamp=parts[0],
                    ServingSector = parts[1],
                    InterferingSector = parts[2],
                    LteScRSRP = int(parts[3]),
                    LteNcRSRP = int(parts[4]),
                    LteNcEarfcn = int(parts[5]),
                    LteNcPci = int(parts6),
                    )
            )
            if y == 50:  # 在for line in f循环中判断 每组50行输入  最后一组可能不足50行  在for循环结束后
                MRO.objects.bulk_create(MRO_list)
                z = z + 1
                y = 0
                print('第' + str(z) + '组数据导入成功')
                MRO_list.clear()
        MRO.objects.bulk_create(MRO_list)
        f.close()
    #print("更新数据" + str(x) + "条,成功导入数据" + str(y) + "条")
    return render(request,'index.html', locals())



def data_in(request):
    if request.user.is_authenticated:
        return render(request, 'data_in.html', locals())
    else:
        return render(request, 'error.html', {'reason': '请先登录'})

def data_out(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'reason': '请先登录'})
    if request.method == 'GET':      #通过request的方式 做不同的处理
        return render(request, 'data_out.html', locals())
    else:
        if not request.POST['path']:
            return render(request, 'error.html', {'reason': '没有选择导出路径'})
        else:
            path = request.POST['path']
            if request.POST['table'] == '1':
                tbcell_list = tbCell.objects.all()
                if tbcell_list:
                    # 创建工作薄
                    ws = Workbook(encoding='utf-8')
                    w = ws.add_sheet(u"数据报表第一页")
                    w.write(0, 0, "CITY")
                    w.write(0, 1, "SECTOR_ID")
                    w.write(0, 2, "SECTOR_NAME")
                    w.write(0, 3, "ENODEBID")
                    w.write(0, 4, "ENODEB_NAME")
                    w.write(0,5, "EARFCN")
                    w.write(0,6, "PCI")
                    w.write(0,7, "PSS")
                    w.write(0,8, "SSS")
                    w.write(0,9, "TAC")
                    w.write(0,10, "VENDOR")
                    w.write(0,11, "LONGITUDE")
                    w.write(0,12, "LATITUDE")
                    w.write(0,13, "STYLE")
                    w.write(0,14, "AZIMUTH")
                    w.write(0, 15, "HEIGHT")
                    w.write(0, 16, "ELECTTILT")
                    w.write(0, 17, "MECHTILT")
                    w.write(0, 18, "TOTLETILT")
                    # 写入数据
                    excel_row = 1
                    for obj in tbcell_list:
                        w.write(excel_row, 0, obj.CITY)
                        w.write(excel_row, 1, obj.SECTOR_ID)
                        w.write(excel_row, 2, obj.SECTOR_NAME)
                        w.write(excel_row, 3, obj.ENODEBID)
                        w.write(excel_row, 4, obj.ENODEB_NAME)
                        w.write(excel_row, 5, obj.EARFCN)
                        w.write(excel_row, 6, obj.PCI)
                        w.write(excel_row, 7, obj.PSS)
                        w.write(excel_row, 8, obj.SSS)
                        w.write(excel_row, 9, obj.TAC)
                        w.write(excel_row, 10, obj.VENDOR)
                        w.write(excel_row, 11, obj.LONGITUDE)
                        w.write(excel_row, 12, obj.LATITUDE)
                        w.write(excel_row, 13, obj.STYLE)
                        w.write(excel_row, 14, obj.AZIMUTH)
                        w.write(excel_row, 15, obj.HEIGHT)
                        w.write(excel_row, 16, obj.ELECTTILT)
                        w.write(excel_row, 17, obj.MECHTILT)
                        w.write(excel_row, 18, obj.TOTLETILT)

                        excel_row += 1

                    ws.save(path+r"\1.tbcell.xls")
                return render(request, 'index.html', locals())

            elif request.POST['table'] == '2':
                kpi_list = KPI.objects.all()
                if kpi_list:
                    # 创建工作薄
                    ws = Workbook(encoding='utf-8')
                    w = ws.add_sheet(u"数据报表第一页")
                    w.write(0, 0, "START_TIME ")
                    w.write(0, 1, "T")
                    w.write(0, 2, "NET_ELE")
                    w.write(0, 3, "SECTOR_DETAIL")
                    w.write(0, 4, "ENODEB_NAME")
                    w.write(0, 5, "RRC_BUILD")
                    w.write(0, 6, "RRC_REQUEST")
                    w.write(0, 7, "RRC_RATE")
                    w.write(0, 8, "RAB_SUCCESS")
                    w.write(0, 9, "RAB_TRY")
                    w.write(0, 10, "RAB_RATE")
                    w.write(0, 11, "eNodeB_TIME")
                    w.write(0, 12, "SECTOR_TIME")
                    w.write(0, 13, "RAB_DROP_RATE")
                    w.write(0, 14, "CONN_RATE")
                    w.write(0, 15, "RESET_TIME")
                    w.write(0, 16, "ABNORMAL_TIME")
                    w.write(0, 17, "SUCCESS_TIME")
                    w.write(0, 18, "TOTLETILT")
                    w.write(0, 19, "eNodeB_IN_DIF_SUCCESS")
                    w.write(0, 20, "eNodeB_IN_DIF_TRY")
                    w.write(0, 21, "eNodeB_IN_SIM_SUCCESS")
                    w.write(0, 22, "eNodeB_IN_SIM_TRY")
                    w.write(0, 23, "eNodeB_OUT_DIF_SUCCESS")
                    w.write(0, 24, "eNodeB_OUT_DIF_TRY")
                    w.write(0, 25, "eNodeB_OUT_SIM_SUCCESS")
                    w.write(0, 26, "eNodeB_OUT_SIM_TRY")
                    w.write(0, 27, "eNodeB_IN_RATE")
                    w.write(0, 28, "eNodeB_OUT_RATE")
                    w.write(0, 29, "SIM_RATE")
                    w.write(0, 30, "DIF_RATE")
                    w.write(0, 31, "TOTAL_SUCCESS_RATE")
                    w.write(0, 32, "UP_BIT")
                    w.write(0, 33, "DOWN_BIT")
                    w.write(0, 34, "RRC_REBUILD_REQUEST")
                    w.write(0, 35, "RRC_REBUILD_RATE")
                    w.write(0, 36, "REBUILD_SIM_IN_TIME")
                    w.write(0, 37, "REBUILD_DIF_IN_TIME")
                    w.write(0, 38, "REBUILD_SIM_OUT_TIME")
                    w.write(0, 39, "REBUILD_DIF_OUT_TIME")
                    w.write(0, 40, "eNB_REQUEST_TIME")
                    w.write(0, 41, "eNB_TRY_TIME")
                    # 写入数据
                    excel_row = 1
                    for obj in kpi_list:
                        w.write(excel_row, 0, obj.START_TIME )
                        w.write(excel_row, 1, obj.T)
                        w.write(excel_row, 2, obj.NET_ELE)
                        w.write(excel_row, 3, obj.SECTOR_DETAIL)
                        w.write(excel_row, 4, obj.SECTOR_NAME)
                        w.write(excel_row, 5, obj.RRC_BUILD)
                        w.write(excel_row, 6, obj.RRC_REQUEST)
                        w.write(excel_row, 7, obj.RRC_RATE)
                        w.write(excel_row, 8, obj.RAB_SUCCESS)
                        w.write(excel_row, 9, obj.RAB_TRY)
                        w.write(excel_row, 10, obj.RAB_RATE)
                        w.write(excel_row, 11, obj.eNodeB_TIME)
                        w.write(excel_row, 12, obj.SECTOR_TIME)
                        w.write(excel_row, 13, obj.RAB_DROP_RATE)
                        w.write(excel_row, 14, obj.CONN_RATE)
                        w.write(excel_row, 15, obj.RESET_TIME)
                        w.write(excel_row, 16, obj.ABNORMAL_TIME)
                        w.write(excel_row, 17, obj.SUCCESS_TIME)
                        w.write(excel_row, 18, obj.WIRELESS_DROP_RATE)
                        w.write(excel_row, 19, obj.eNodeB_IN_DIF_SUCCESS)
                        w.write(excel_row, 20, obj.eNodeB_IN_DIF_TRY)
                        w.write(excel_row, 21, obj.eNodeB_IN_SIM_SUCCESS)
                        w.write(excel_row, 22, obj.eNodeB_IN_SIM_TRY)
                        w.write(excel_row, 23, obj.eNodeB_OUT_DIF_SUCCESS)
                        w.write(excel_row, 24, obj.eNodeB_OUT_DIF_TRY)
                        w.write(excel_row, 25, obj.eNodeB_OUT_SIM_SUCCESS)
                        w.write(excel_row, 26, obj.eNodeB_OUT_SIM_TRY)
                        w.write(excel_row, 27, obj.eNodeB_IN_RATE)
                        w.write(excel_row, 28, obj.eNodeB_OUT_RATE)
                        w.write(excel_row, 29, obj.SIM_RATE)
                        w.write(excel_row, 30, obj.DIF_RATE)
                        w.write(excel_row, 31, obj.TOTAL_SUCCESS_RATE)
                        w.write(excel_row, 32, obj.UP_BIT)
                        w.write(excel_row, 33, obj.DOWN_BIT)
                        w.write(excel_row, 34, obj.RRC_REBUILD_REQUEST)
                        w.write(excel_row, 35, obj.RRC_REBUILD_RATE)
                        w.write(excel_row, 36, obj.REBUILD_SIM_IN_TIME)
                        w.write(excel_row, 37, obj.REBUILD_DIF_IN_TIME)
                        w.write(excel_row, 38, obj.REBUILD_SIM_OUT_TIME)
                        w.write(excel_row, 39, obj.REBUILD_DIF_OUT_TIME)
                        w.write(excel_row, 40, obj.eNB_REQUEST_TIME)
                        w.write(excel_row, 41, obj.eNB_TRY_TIME)
                        excel_row += 1
                    ws.save(path + r"\2.kpi.xls")
                return render(request, 'index.html', locals())

            elif request.POST['table'] == '3':
                prb_list = PRB.objects.all()
                if prb_list:
                    # 创建工作薄
                    ws = Workbook(encoding='utf-8')
                    w = ws.add_sheet(u"数据报表第一页")
                    w.write(0, 0, "START_TIME ")
                    w.write(0, 1, "T")
                    w.write(0, 2, "NET_ELE")
                    w.write(0, 3, "SECTOR_DETAIL")
                    w.write(0, 4, "ENODEB_NAME")
                    w.write(0, 5, "PRB0")
                    w.write(0, 6, "PRB1")
                    w.write(0, 7, "PRB2")
                    w.write(0, 8, "PRB3")
                    w.write(0, 9, "PRB4")
                    w.write(0, 10, "PRB5")
                    w.write(0, 11, "PRB6")
                    w.write(0, 12, "PRB7")
                    w.write(0, 13, "PRB8")
                    w.write(0, 14, "PRB9")
                    w.write(0, 15, "PRB10")
                    w.write(0, 16, "PRB11")
                    w.write(0, 17, "PRB12")
                    w.write(0, 18, "PRB13")
                    w.write(0, 19, "PRB14")
                    w.write(0, 20, "PRB15")
                    w.write(0, 21, "PRB16")
                    w.write(0, 22, "PRB17")
                    w.write(0, 23, "PRB18")
                    w.write(0, 24, "PRB19")
                    w.write(0, 25, "PRB20")
                    w.write(0, 26, "PRB21")
                    w.write(0, 27, "PRB22")
                    w.write(0, 28, "PRB23")
                    w.write(0, 29, "PRB24")
                    w.write(0, 30, "PRB25")
                    w.write(0, 31, "PRB26")
                    w.write(0, 32, "PRB27")
                    w.write(0, 33, "PRB28")
                    w.write(0, 34, "PRB29")
                    w.write(0, 35, "PRB30")
                    w.write(0, 36, "PRB31")
                    w.write(0, 37, "PRB32")
                    w.write(0, 38, "PRB33")
                    w.write(0, 39, "PRB34")
                    w.write(0, 40, "PRB35")
                    w.write(0, 41, "PRB36")
                    w.write(0, 42, "PRB37")
                    w.write(0, 43, "PRB38")
                    w.write(0, 44, "PRB39")
                    w.write(0, 45, "PRB40")
                    w.write(0, 46, "PRB41")
                    w.write(0, 47, "PRB42")
                    w.write(0, 48, "PRB43")
                    w.write(0, 49, "PRB44")
                    w.write(0, 50, "PRB45")
                    w.write(0, 51, "PRB46")
                    w.write(0, 52, "PRB47")
                    w.write(0, 53, "PRB48")
                    w.write(0, 54, "PRB49")
                    w.write(0, 55, "PRB50")
                    w.write(0, 56, "PRB51")
                    w.write(0, 57, "PRB52")
                    w.write(0, 58, "PRB53")
                    w.write(0, 59, "PRB54")
                    w.write(0, 60, "PRB55")
                    w.write(0, 61, "PRB56")
                    w.write(0, 62, "PRB57")
                    w.write(0, 63, "PRB58")
                    w.write(0, 64, "PRB59")
                    w.write(0, 65, "PRB60")
                    w.write(0, 66, "PRB61")
                    w.write(0, 67, "PRB62")
                    w.write(0, 68, "PRB63")
                    w.write(0, 69, "PRB64")
                    w.write(0, 70, "PRB65")
                    w.write(0, 71, "PRB66")
                    w.write(0, 72, "PRB67")
                    w.write(0, 73, "PRB68")
                    w.write(0, 74, "PRB69")
                    w.write(0, 75, "PRB70")
                    w.write(0, 76, "PRB71")
                    w.write(0, 77, "PRB72")
                    w.write(0, 78, "PRB73")
                    w.write(0, 79, "PRB74")
                    w.write(0, 80, "PRB75")
                    w.write(0, 81, "PRB76")
                    w.write(0, 82, "PRB77")
                    w.write(0, 83, "PRB78")
                    w.write(0, 84, "PRB79")
                    w.write(0, 85, "PRB80")
                    w.write(0, 86, "PRB81")
                    w.write(0, 87, "PRB82")
                    w.write(0, 88, "PRB83")
                    w.write(0, 89, "PRB84")
                    w.write(0, 90, "PRB85")
                    w.write(0, 91, "PRB86")
                    w.write(0, 92, "PRB87")
                    w.write(0, 93, "PRB88")
                    w.write(0, 94, "PRB89")
                    w.write(0, 95, "PRB90")
                    w.write(0, 96, "PRB91")
                    w.write(0, 97, "PRB92")
                    w.write(0, 98, "PRB93")
                    w.write(0, 99, "PRB94")
                    w.write(0, 100, "PRB95")
                    w.write(0, 101, "PRB96")
                    w.write(0, 102, "PRB97")
                    w.write(0, 103, "PRB98")
                    w.write(0, 104, "PRB99")
                    # 写入数据
                    excel_row = 1
                    for obj in prb_list:
                        w.write(excel_row, 0, obj.START_TIME)
                        w.write(excel_row, 1, obj.T)
                        w.write(excel_row, 2, obj.NET_ELE)
                        w.write(excel_row, 3, obj.SECTOR_DETAIL)
                        w.write(excel_row, 4, obj.ENODEB_NAME)
                        w.write(excel_row, 5, obj.PRB0)
                        w.write(excel_row, 6, obj.PRB1)
                        w.write(excel_row, 7, obj.PRB2)
                        w.write(excel_row, 8, obj.PRB3)
                        w.write(excel_row, 9, obj.PRB4)
                        w.write(excel_row, 10, obj.PRB5)
                        w.write(excel_row, 11, obj.PRB6)
                        w.write(excel_row, 12, obj.PRB7)
                        w.write(excel_row, 13, obj.PRB8)
                        w.write(excel_row, 14, obj.PRB9)
                        w.write(excel_row, 15, obj.PRB10)
                        w.write(excel_row, 16, obj.PRB11)
                        w.write(excel_row, 17, obj.PRB12)
                        w.write(excel_row, 18, obj.PRB13)
                        w.write(excel_row, 19, obj.PRB14)
                        w.write(excel_row, 20, obj.PRB15)
                        w.write(excel_row, 21, obj.PRB16)
                        w.write(excel_row, 22, obj.PRB17)
                        w.write(excel_row, 23, obj.PRB18)
                        w.write(excel_row, 24, obj.PRB19)
                        w.write(excel_row, 25, obj.PRB20)
                        w.write(excel_row, 26, obj.PRB21)
                        w.write(excel_row, 27, obj.PRB22)
                        w.write(excel_row, 28, obj.PRB23)
                        w.write(excel_row, 29, obj.PRB24)
                        w.write(excel_row, 30, obj.PRB25)
                        w.write(excel_row, 31, obj.PRB26)
                        w.write(excel_row, 32, obj.PRB27)
                        w.write(excel_row, 33, obj.PRB28)
                        w.write(excel_row, 34, obj.PRB29)
                        w.write(excel_row, 35, obj.PRB30)
                        w.write(excel_row, 36, obj.PRB31)
                        w.write(excel_row, 37, obj.PRB32)
                        w.write(excel_row, 38, obj.PRB33)
                        w.write(excel_row, 39, obj.PRB34)
                        w.write(excel_row, 40, obj.PRB35)
                        w.write(excel_row, 41, obj.PRB36)
                        w.write(excel_row, 42, obj.PRB37)
                        w.write(excel_row, 43, obj.PRB38)
                        w.write(excel_row, 44, obj.PRB39)
                        w.write(excel_row, 45, obj.PRB40)
                        w.write(excel_row, 46, obj.PRB41)
                        w.write(excel_row, 47, obj.PRB42)
                        w.write(excel_row, 48, obj.PRB43)
                        w.write(excel_row, 49, obj.PRB44)
                        w.write(excel_row, 50, obj.PRB45)
                        w.write(excel_row, 51, obj.PRB46)
                        w.write(excel_row, 52, obj.PRB47)
                        w.write(excel_row, 53, obj.PRB48)
                        w.write(excel_row, 54, obj.PRB49)
                        w.write(excel_row, 55, obj.PRB50)
                        w.write(excel_row, 56, obj.PRB51)
                        w.write(excel_row, 57, obj.PRB52)
                        w.write(excel_row, 58, obj.PRB53)
                        w.write(excel_row, 59, obj.PRB54)
                        w.write(excel_row, 60, obj.PRB55)
                        w.write(excel_row, 61, obj.PRB56)
                        w.write(excel_row, 62, obj.PRB57)
                        w.write(excel_row, 63, obj.PRB58)
                        w.write(excel_row, 64, obj.PRB59)
                        w.write(excel_row, 65, obj.PRB60)
                        w.write(excel_row, 66, obj.PRB61)
                        w.write(excel_row, 67, obj.PRB62)
                        w.write(excel_row, 68, obj.PRB63)
                        w.write(excel_row, 69, obj.PRB64)
                        w.write(excel_row, 70, obj.PRB65)
                        w.write(excel_row, 71, obj.PRB66)
                        w.write(excel_row, 72, obj.PRB67)
                        w.write(excel_row, 73, obj.PRB68)
                        w.write(excel_row, 74, obj.PRB69)
                        w.write(excel_row, 75, obj.PRB70)
                        w.write(excel_row, 76, obj.PRB71)
                        w.write(excel_row, 77, obj.PRB72)
                        w.write(excel_row, 78, obj.PRB73)
                        w.write(excel_row, 79, obj.PRB74)
                        w.write(excel_row, 80, obj.PRB75)
                        w.write(excel_row, 81, obj.PRB76)
                        w.write(excel_row, 82, obj.PRB77)
                        w.write(excel_row, 83, obj.PRB78)
                        w.write(excel_row, 84, obj.PRB79)
                        w.write(excel_row, 85, obj.PRB80)
                        w.write(excel_row, 86, obj.PRB81)
                        w.write(excel_row, 87, obj.PRB82)
                        w.write(excel_row, 88, obj.PRB83)
                        w.write(excel_row, 89, obj.PRB84)
                        w.write(excel_row, 90, obj.PRB85)
                        w.write(excel_row, 91, obj.PRB86)
                        w.write(excel_row, 92, obj.PRB87)
                        w.write(excel_row, 93, obj.PRB88)
                        w.write(excel_row, 94, obj.PRB89)
                        w.write(excel_row, 95, obj.PRB90)
                        w.write(excel_row, 96, obj.PRB91)
                        w.write(excel_row, 97, obj.PRB92)
                        w.write(excel_row, 98, obj.PRB93)
                        w.write(excel_row, 99, obj.PRB94)
                        w.write(excel_row, 100, obj.PRB95)
                        w.write(excel_row, 101, obj.PRB96)
                        w.write(excel_row, 102, obj.PRB97)
                        w.write(excel_row, 103, obj.PRB98)
                        w.write(excel_row, 104, obj.PRB99)

                        excel_row += 1
                    ws.save(path + r"\3.prb.xls")
                return render(request, 'index.html', locals())

            elif request.POST['table'] == '4':
                mro_list = MRO.objects.all()
                if mro_list:
                    # 创建工作薄
                    ws = Workbook(encoding='utf-8')
                    w = ws.add_sheet(u"数据报表第一页")
                    w.write(0, 0, "_TimeStamp")
                    w.write(0, 1, "ServingSector")
                    w.write(0, 2, "InterferingSector")
                    w.write(0, 3, "LteScRSRP")
                    w.write(0, 4, "LteNcRSRP")
                    w.write(0, 5, "LteNcEarfcn")
                    w.write(0, 6, "LteNcPci")

                    # 写入数据
                    excel_row = 1
                    for obj in mro_list:
                        w.write(excel_row, 0, obj._TimeStamp)
                        w.write(excel_row, 1, obj.ServingSector)
                        w.write(excel_row, 2, obj.InterferingSector)
                        w.write(excel_row, 3, obj.LteScRSRP)
                        w.write(excel_row, 4, obj.LteNcRSRP)
                        w.write(excel_row, 5, obj.LteNcEarfcn)
                        w.write(excel_row, 6, obj.LteNcPci)

                        excel_row += 1

                    ws.save(path + r"\4.mro.xls")
                return render(request, 'index.html', locals())
            else:
                return render(request, 'error.html', {'reason': '没有选择要导出的表'})


def query(request):
    if request.user.is_authenticated:
        return render(request, 'query.html', locals())
    else:
        return render(request, 'error.html', {'reason': '请先登录'})


def query2(request):    #返回查询子页面和查询结果页面
    if request.method == 'GET':
        fina_list = []

        if request.GET['table']=='1':#value和value_list   value返回的查询集是 key value字典的集合


            name_list = tbCell.objects.distinct().values_list("SECTOR_NAME")
            for name in name_list:
                fina_list.append(name[0])
        elif request.GET['table'] == '2':
            name_list = tbCell.objects.distinct().values_list("ENODEB_NAME")
            for name in name_list:
                fina_list.append(name[0])
        elif request.GET['table'] == '3':
            name_list = KPI.objects.distinct().values_list("NET_ELE")
            for name in name_list:
                fina_list.append(name[0])
        elif request.GET['table'] == '4':
            name_list = PRB.objects.distinct().values_list("NET_ELE")
            for name in name_list:
                fina_list.append(name[0])
        else:
            return render(request, 'error.html', {'reason': '没有选择要查询的项目'})
        return render(request, 'query2.html', locals())
    elif request.method == 'POST':
        FLAG1 = []
        FLAG2 = []
        if request.GET['table'] == '1':
            list1=[]
            if request.POST['name']:
                if request.POST['name'] == 'none':
                    return render(request, 'error.html', {'reason': '没有选择要查询的小区'})

                else:

                    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='073819', db='TD-LTE',
                                           charset='utf8')

                    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
                    cursor.callproc('query2',(request.POST['name'],))#注意必须加逗号，不然会把字符串一个字符一个字符的分解为多个参数
                    result = cursor.fetchall()
                    print(result)
                    print(result[0])
                    fina_list = []
                    for key in result[0]:
                       fina_list.append(result[0][key])
                    print(fina_list)
                    #print(result[0])
                    #print(result[0]['id'])
                    #list1 = result[0].values()

                    #print(list1)
                    #for i in list1:
                    #    print(i)
                    #list1 = tbCell.objects.filter(SECTOR_NAME=request.POST['name'])

        elif request.GET['table'] == '2':
            list2 = []
            if request.POST['name']:
                if request.POST['name'] =='none':
                    return render(request, 'error.html', {'reason': '没有选择要查询的小区'})
                else:
                    list2 = tbCell.objects.filter(ENODEB_NAME=request.POST['name'])



        elif request.GET['table'] == '3':
            list3 = []
            if request.POST['name']!='1':#通过这个值来判断是第几次post请求
                list3 = KPI.objects.filter(NET_ELE=request.POST['name'])
                name2 = request.POST['name']
                return render(request, 'query2.html', locals())
            else:
                list4 = []
                kpi_list = []
                kpi_list = KPI.objects.filter(NET_ELE=request.POST['name2'])#通过名查询所有
                Point = namedtuple('Point', ['x', 'y'])#nametuple将两项数据合并起来
                for x in kpi_list:
                    data_value = getattr(x,request.POST['data'])
                    time_key = datetime.datetime.strptime(x.START_TIME, "%m/%d/%Y %H:%M:%S")#转换格式 str转为datetime
                    list4.append(Point(time_key,data_value))
                for i in list4:
                    if i.x < datetime.datetime.strptime(request.POST['start'],"%Y-%m-%d") or i.x > datetime.datetime.strptime(request.POST['end'],"%Y-%m-%d"):
                        list4.remove(i)
                return render(request, 'query_result2.html', locals())


        elif request.GET['table'] == '4':
            list5 = []
            if request.POST['name'] != '1':  # 通过这个值来判断是第几次post请求
                list5 = PRB.objects.filter(NET_ELE=request.POST['name'])
                name2 = request.POST['name']
                return render(request, 'query2.html', locals())
            else:
                list6 = []
                kpi_list = []
                kpi_list = PRB.objects.filter(NET_ELE=request.POST['name2'])
                Point = namedtuple('Point', ['x', 'y'])  # nametuple将两项数据合并起来
                for x in kpi_list:
                    data_value = getattr(x, request.POST['data'])
                    time_key = datetime.datetime.strptime(x.START_TIME, "%m/%d/%Y %H:%M:%S")  # 转换格式 str转为datetime
                    list6.append(Point(time_key, data_value))
                for i in list6:
                    if i.x < datetime.datetime.strptime(request.POST['start'],
                                                        "%Y-%m-%d") or i.x > datetime.datetime.strptime(
                            request.POST['end'], "%Y-%m-%d"):
                        list6.remove(i)
                return render(request, 'query_result2.html', locals())

        else:
            return render(request, 'error.html', {'reason': '没有选择要查询的表'})
    return render(request, 'query_result.html', locals())


def analyse(request):
    if  request.user.is_authenticated:
        return render(request, 'analyse.html', locals())
    else:
        return render(request, 'error.html', {'reason': '请先登录'})


def analyse2(request):
    fina_list = []
    if not request.method == 'POST':
        if request.GET['table']=='1':
            name_list = MRO.objects.distinct().values_list("ServingSector","InterferingSector")
            Point = namedtuple('Point', ['x', 'y'])
            for name in name_list:#先拿到所有(ServingSector, InterfereringSector)
                fina_list.append(Point(name[0],name[1]))



            #print(indextb.objects.all().aggregate(c2i_sd=StdDev('c2i'))['c2i_sd'])

            for i in fina_list:
                print()
                #indextb.objects.all().aggregate(c2i_sd=StdDev('c2i'))['c2i_sd']
                u =  MRO.objects.filter(ServingSector=i.x,InterferingSector=i.y).aggregate(C2I_mean = Avg('LteScRSRP')-Avg('LteNcRSRP'))['C2I_mean']
                o = MRO.objects.filter(ServingSector=i.x,InterferingSector=i.y).aggregate(C2I_SD=StdDev(F('LteScRSRP') - F('LteNcRSRP'), output_field=FloatField()))['C2I_SD']
                add = tbC2Inew(
                ServingSector=i.x,
                InterferingSector=i.y,
                mean =u,
                    #能直接像sql语句中的临时表一样，直接操作但是注意('字段名')要加括号
                standard_deviation=o,
                rate1 = cdfd(-10000,9,u,o),#a,b 为区间起始范围，u，o分别为正态分布的均值和标准差。
                rate2 = cdfd(-6,6,u,o)
                )
                add.save()

            return render(request, 'index.html', locals())
        elif request.GET['table'] == '2':
            return render(request, 'query3.html', locals())
    else:#post时

        if int(request.POST['x'])>100 or int(request.POST['x'])<0:
            return render(request, 'error.html', {'reason': '输入有误'})
        else:
            x = float(request.POST['x'])/100
            first_list = []
            sec_list = []
            third_list = []
            name_list = tbC2Inew.objects.distinct().values_list("ServingSector")
            print(name_list)
            for name in name_list:
                first_list.append(name[0])
            print(first_list)
            for i in first_list:  # 查询第i个主小区的所有邻区
                sec_list = tbC2Inew.objects.filter(ServingSector=i, rate2__gte=x)  # 注意是怎么表达的
                for name in sec_list:
                    third_list.append(name.InterferingSector)
                print(third_list)
                if sec_list:  # 判断两两是否为邻区，判断完的就移除 直到为空
                    for j in range(len(third_list)):
                        for k in range(j+1, len(third_list)):  # k与j错开一位
                            if tbC2Inew.objects.filter(ServingSector=third_list[j],
                                                       InterferingSector=third_list[k], rate2__gte=x):
                                # print(sec_list[j].ServingSector)
                                add = tbC2I3(
                                    sector1=i,
                                    sector2=third_list[k],
                                    sector3=third_list[j]

                                )
                                add.save()
                            elif tbC2Inew.objects.filter(ServingSector=third_list[k],
                                                         InterferingSector=third_list[j], rate2__gte=x):
                                add = tbC2I3(
                                    sector1=i,
                                    sector2=third_list[j],
                                    sector3=third_list[k]

                                )
                                add.save()


        return render(request, 'index.html', locals())
def log_reg(request):
    return render(request, 'log_reg.html', locals())

# 绘制随机字符
def generate_random_string(request):
    # 随机字符串
    chars = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 随机产生４个不同字符
    random_chars = "".join(random.sample(chars, 4))
    # 随机字符存储到session中
    request.session['verify_code'] = random_chars

    return random_chars


# 获得图片背景颜色
def draw_disturb_point(pen_for_image):
    for _ in range(100):
        # 随机生成干扰点位置
        pos = (random.randint(0, 100), random.randint(0, 30))
        # 随机生成点的颜色
        color = (random.randint(0, 255), 255, random.randint(0, 255))
        # 将点绘制到图片上
        pen_for_image.point(pos, color)


# 给图片绘制随机文字
def draw_random_string(pen_for_image, random_string):
    # 加载字体 字体所在目录:/usr/share/fonts/
    my_font = ImageFont.truetype("STATICFILES_DIRS/fonts/Roboto-Regular.ttf", 23)
    # 设置字符颜色
    my_color = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制字符
    for number, ch in enumerate(random_string):
        pen_for_image.text((5 + number * 20, 2), ch, my_color, my_font)


# 绘制基本图片
def create_base_image():
    # 定义图片背景颜色(RGB)
    bg_color = (random.randrange(20, 100), random.randrange(20, 100), 255)
    # 创建图片, 分别设置图片格式, 图片大小, 图片背景颜色
    verify_image = Image.new('RGB', (100, 30), bg_color)

    return verify_image

def verification_code(request):
    # 生成随机字符序列
    random_string = generate_random_string(request)
    # 创建图片对象
    verify_image = create_base_image()
    # 创建对图片(verify_image)的画笔
    pen_for_image = ImageDraw.Draw(verify_image)
    # 将随机字符绘制到图片上
    draw_random_string(pen_for_image, random_string)
    # 绘制图片干扰点
    draw_disturb_point(pen_for_image)

    # 将图片数据暂存到内存中
    image_data = BytesIO()
    verify_image.save(image_data, 'png')
    #print(random_string)
    request.session['captcha'] = random_string#记录到session中
    #print(request.session['captcha'])
    return HttpResponse(image_data.getvalue(), 'image/png')

#主页
def index(request):
    return render(request,'index.html',locals())


#登录
def do_login(request):
    try:
        if request.method == 'POST':  #方式是提交
            login_form = LoginForm(request.POST)  #forms实例化，request.POST是表单中的数据，刚开始为空
            if login_form.is_valid():  #校验表单
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]#request.session['captcha']
                captcha = login_form.cleaned_data["captcha"]
                user = authenticate(username=username,password=password)  #认证给出的用户名和密码，合法返回一个User对象，密码不合法返回None
                if user is not None:
                    #print(user.backend)
                    #user.backend = 'django.contrib.auth.backends.ModelBackend'
                    #通过附加 user.backend 属性来记录验证是被哪个配置的 backend 通过的。通常是 django.contrib.auth.backends.ModelBackend.
                    if user.is_active:
                        print(captcha)
                        print(request.session['captcha'])
                        if captcha == request.session['captcha']:    #is是比较地址？
                            login(request, user)
                            return render(request,'index.html')
                        else:
                            return render(request, 'error.html', {'reason': '验证码不正确'})
                else:
                    return render(request,'error.html',{'reason':'密码或用户名不正确'})
                #return redirect(request.POST.get('source_url')) #request。POST.get()获取login.html表单中的值：source_url
            else:
                return render(request,'error.html',{'reason':login_form.errors})
        else: #GET方法，如第一次进入登陆页面
            login_form = LoginForm()
    except Exception as e:
        pass
    return render(request,'login.html',locals())

#注册
def do_reg(request):
    try:
        if request.method == 'POST':  #POST方法
            reg_form = RegForm(request.POST)  #提取post的数据
            if reg_form.is_valid():  #校验表单                                                                                                            #cleaned_data['email']  读取name为‘email’的表单提交值，并赋予 email变量
                print(1)
                user = User.objects.create(username=reg_form.cleaned_data["username"],  #创建一个对象，并保存在user中
                                    email=reg_form.cleaned_data["email"],
                                    password = make_password(reg_form.cleaned_data["password"]),
                                    address=reg_form.cleaned_data["address"],
                                    phone=reg_form.cleaned_data["phone"],)
                user.is_active = True
                user.save()
                #注册后直接登录
                user = authenticate(username=reg_form.cleaned_data["username"],password=reg_form.cleaned_data["password"])
                print(1.2)
                if user is not None:
                    print(2)
                    #user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request,user)
                    #return redirect(request.POST.get('source_url'))
                    return render(request,'index.html',locals())
                else:
                    print(3)
                    return  render(request,'error.html','登陆失败')
            else:
                print(4)
                return render(request,'error.html',{'reason':reg_form.errors})
        else:
            print(5)
            reg_form=RegForm()
    except Exception as e:
        print('eror')
        pass
    return render(request,'register.html',locals())

#退出
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        pass
    return render(request, 'index.html', locals())
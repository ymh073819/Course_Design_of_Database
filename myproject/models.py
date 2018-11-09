from django.db import models
from django.contrib.auth.models import AbstractUser
#from myapp import ConnMySql
import pymysql
import time
import random

# 用户
class User(AbstractUser):#REQUIRED_FIELDS只有AbstractUser才有    这是另外一种拓展user的方法
    address = models.CharField(max_length=200, verbose_name='地址')
    phone = models.CharField(max_length=20, verbose_name='联系电话')

    class Meta:  # 定义元数据
        verbose_name = '用户'
        verbose_name_plural = verbose_name  # 设置后台模块
        ordering = ['-id']  # id降序排列

    def __str__(self):
        return self.username


class tbCell(models.Model):
    CITY = models.CharField(max_length=50)              #0
    SECTOR_ID =  models.CharField(max_length=50)        #1
    SECTOR_NAME = models.CharField(max_length=50)       #2
    ENODEBID = models.CharField(max_length=50)          #3
    ENODEB_NAME = models.CharField(max_length=50)       #4
    EARFCN = models.IntegerField()                      #5
    PCI = models.IntegerField()                         #6
    PSS = models.IntegerField()                         #7
    SSS = models.IntegerField()                         #8
    TAC = models.IntegerField()                         #9
    VENDOR = models.CharField(max_length=50)            #10
    LONGITUDE = models.FloatField()                     #11
    # null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
    # blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
    LATITUDE = models.FloatField()                      #12
    STYLE = models.CharField(max_length=50)             #13
    AZIMUTH = models.IntegerField()                     #14
    HEIGHT = models.IntegerField(null=True,blank=True)                      #15
    ELECTTILT = models.IntegerField(null=True,blank=True)                   #16
    MECHTILT = models.IntegerField(null=True,blank=True)                    #17
    TOTLETILT = models.IntegerField(null=True,blank=True)                   #18


class KPI(models.Model):
    START_TIME = models.CharField(max_length=50)#0   主键
    T = models.IntegerField()                        # 1
    NET_ELE = models.CharField(max_length=50)#network element name网元名称    2
    SECTOR_DETAIL = models.TextField(max_length=100) #3 主键
    SECTOR_NAME = models.CharField(max_length=50) #4
    RRC_BUILD = models.IntegerField()#5
    RRC_REQUEST = models.IntegerField()#6
    RRC_RATE = models.FloatField()#7
    RAB_SUCCESS = models.IntegerField()#8
    RAB_TRY = models.IntegerField()#9
    RAB_RATE = models.FloatField()#10
    eNodeB_TIME = models.IntegerField()#11
    SECTOR_TIME = models.IntegerField()#12
    RAB_DROP_RATE = models.FloatField()#13
    CONN_RATE = models.FloatField()#14
    RESET_TIME = models.IntegerField()#15
    ABNORMAL_TIME = models.IntegerField()#16
    SUCCESS_TIME = models.IntegerField()#17
    WIRELESS_DROP_RATE = models.FloatField()#18
    eNodeB_IN_DIF_SUCCESS = models.IntegerField()#19
    eNodeB_IN_DIF_TRY = models.IntegerField()#20
    eNodeB_IN_SIM_SUCCESS = models.IntegerField()#21
    eNodeB_IN_SIM_TRY = models.IntegerField()     #IN是内   OUT是间 22
    eNodeB_OUT_DIF_SUCCESS = models.IntegerField()#23
    eNodeB_OUT_DIF_TRY = models.IntegerField()#24
    eNodeB_OUT_SIM_SUCCESS = models.IntegerField()#25
    eNodeB_OUT_SIM_TRY = models.IntegerField()#26
    eNodeB_IN_RATE = models.FloatField(null=True,blank=True)#27
    eNodeB_OUT_RATE = models.FloatField(null=True,blank=True)#28
    SIM_RATE = models.FloatField(null=True,blank=True)  #同频切换成功率zsp (%)  29
    DIF_RATE = models.FloatField(null=True,blank=True)#30
    TOTAL_SUCCESS_RATE = models.FloatField()#31
    UP_BIT = models.BigIntegerField()  #小区PDCP层所发送的上行数据的总吞吐量 (比特)   32
    DOWN_BIT = models.BigIntegerField()#33
    RRC_REBUILD_REQUEST = models.IntegerField()#RRC重建请求次数 (无) 34
    RRC_REBUILD_RATE = models.FloatField()#35
    REBUILD_SIM_IN_TIME = models.IntegerField()#通过重建回源小区的eNodeB间同频切换出执行成功次数 (无)   36
    REBUILD_DIF_IN_TIME = models.IntegerField()#37
    REBUILD_SIM_OUT_TIME = models.IntegerField()#38
    REBUILD_DIF_OUT_TIME = models.IntegerField()#39
    eNB_REQUEST_TIME = models.IntegerField()#40
    eNB_TRY_TIME = models.IntegerField()#41



class PRB(models.Model):
    START_TIME = models.CharField(max_length=50)  # 0   主键
    T = models.IntegerField()  # 1
    NET_ELE = models.CharField(max_length=50)  # network element name网元名称    2
    SECTOR_DETAIL = models.TextField(max_length=100)  # 3 主键
    SECTOR_NAME = models.CharField(max_length=50)  # 4

    PRB0 = models.IntegerField()
    PRB1 = models.IntegerField()
    PRB2 = models.IntegerField()
    PRB3 = models.IntegerField()
    PRB4 = models.IntegerField()
    PRB5 = models.IntegerField()
    PRB6 = models.IntegerField()
    PRB7 = models.IntegerField()
    PRB8 = models.IntegerField()
    PRB9 = models.IntegerField()
    PRB10 = models.IntegerField()
    PRB11 = models.IntegerField()
    PRB12 = models.IntegerField()
    PRB13 = models.IntegerField()
    PRB14 = models.IntegerField()
    PRB15 = models.IntegerField()
    PRB16 = models.IntegerField()
    PRB17 = models.IntegerField()
    PRB18 = models.IntegerField()
    PRB19 = models.IntegerField()
    PRB20 = models.IntegerField()
    PRB21 = models.IntegerField()
    PRB22 = models.IntegerField()
    PRB23 = models.IntegerField()
    PRB24 = models.IntegerField()
    PRB25 = models.IntegerField()
    PRB26 = models.IntegerField()
    PRB27 = models.IntegerField()
    PRB28 = models.IntegerField()
    PRB29 = models.IntegerField()
    PRB30 = models.IntegerField()
    PRB31 = models.IntegerField()
    PRB32 = models.IntegerField()
    PRB33 = models.IntegerField()
    PRB34 = models.IntegerField()
    PRB35 = models.IntegerField()
    PRB36 = models.IntegerField()
    PRB37 = models.IntegerField()
    PRB38 = models.IntegerField()
    PRB39 = models.IntegerField()
    PRB40 = models.IntegerField()
    PRB41 = models.IntegerField()
    PRB42 = models.IntegerField()
    PRB43 = models.IntegerField()
    PRB44 = models.IntegerField()
    PRB45 = models.IntegerField()
    PRB46 = models.IntegerField()
    PRB47 = models.IntegerField()
    PRB48 = models.IntegerField()
    PRB49 = models.IntegerField()
    PRB50 = models.IntegerField()
    PRB51 = models.IntegerField()
    PRB52 = models.IntegerField()
    PRB53 = models.IntegerField()
    PRB54 = models.IntegerField()
    PRB55 = models.IntegerField()
    PRB56 = models.IntegerField()
    PRB57 = models.IntegerField()
    PRB58 = models.IntegerField()
    PRB59 = models.IntegerField()
    PRB60 = models.IntegerField()
    PRB61 = models.IntegerField()
    PRB62 = models.IntegerField()
    PRB63 = models.IntegerField()
    PRB64 = models.IntegerField()
    PRB65 = models.IntegerField()
    PRB66 = models.IntegerField()
    PRB67 = models.IntegerField()
    PRB68 = models.IntegerField()
    PRB69 = models.IntegerField()
    PRB70 = models.IntegerField()
    PRB71 = models.IntegerField()
    PRB72 = models.IntegerField()
    PRB73 = models.IntegerField()
    PRB74 = models.IntegerField()
    PRB75 = models.IntegerField()
    PRB76 = models.IntegerField()
    PRB77 = models.IntegerField()
    PRB78 = models.IntegerField()
    PRB79 = models.IntegerField()
    PRB80 = models.IntegerField()
    PRB81 = models.IntegerField()
    PRB82 = models.IntegerField()
    PRB83 = models.IntegerField()
    PRB84 = models.IntegerField()
    PRB85 = models.IntegerField()
    PRB86 = models.IntegerField()
    PRB87 = models.IntegerField()
    PRB88 = models.IntegerField()
    PRB89 = models.IntegerField()
    PRB90 = models.IntegerField()
    PRB91 = models.IntegerField()
    PRB92 = models.IntegerField()
    PRB93 = models.IntegerField()
    PRB94 = models.IntegerField()
    PRB95 = models.IntegerField()
    PRB96 = models.IntegerField()
    PRB97 = models.IntegerField()
    PRB98 = models.IntegerField()
    PRB99 = models.IntegerField()


class MRO(models.Model):
    _TimeStamp = models.CharField(max_length=50)
    ServingSector = models.CharField(max_length=50)
    InterferingSector = models.CharField(max_length=50)
    LteScRSRP = models.IntegerField()
    LteNcRSRP = models.IntegerField()
    LteNcEarfcn = models.IntegerField()
    LteNcPci = models.IntegerField()



class tbC2Inew(models.Model):
    ServingSector = models.CharField(max_length=50)
    InterferingSector = models.CharField(max_length=50)
    mean = models.FloatField()
    standard_deviation = models.FloatField()
    rate1 = models.FloatField()
    rate2 = models.FloatField()

class tbC2I3(models.Model):
    sector1 = models.CharField(max_length=50)
    sector2 = models.CharField(max_length=50)
    sector3 = models.CharField(max_length=50)
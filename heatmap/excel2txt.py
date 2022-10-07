# coding=gbk

import os
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import pandas as pd 
from datetime import datetime
from pandas import Series,DataFrame

df = pd.read_excel('test.xls')  #��Excel���
print(df) #��ӡ��������
print(df.shape)  #��ӡ����С
print(df.dtypes)  #��ӡ��������������
print(df.head(5))  #��ӡǰ��������

f = open('data.txt','w',encoding='utf-8')  #��data.txt�ļ������Ժ����ַ�д��
from xlrd import open_workbook
wb=open_workbook(r'test.xls')
tb=wb.sheets()[0]
data=[]
for r in range(tb.nrows):
    val=[]
    for c in range(tb.ncols):
        val.append(tb.cell_value(r,c))
    f.write(str(val)+'\n')
    data.append(tuple(val))
f.close()
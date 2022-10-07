# coding=gbk

import os
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import pandas as pd 
from datetime import datetime
from pandas import Series,DataFrame

df = pd.read_excel('test.xls')  #打开Excel表格
print(df) #打印所有数据
print(df.shape)  #打印表格大小
print(df.dtypes)  #打印表格各列数据类型
print(df.head(5))  #打印前五行数据

f = open('data.txt','w',encoding='utf-8')  #打开data.txt文件，并以汉字字符写入
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
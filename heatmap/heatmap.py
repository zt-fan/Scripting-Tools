# coding=gbk 
# @Time    : 2022/05/25 10:17
# @Author  : zt-fan
# @File    : heatmap.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_excel("/home/public_data/liyufeng_teacher/fzt_data/Tools/excel/heatmap.xlsx")
#sns.set(font_scale=1.25)#字符大小设定
print(df)
hm=sns.heatmap(df,vmin=0,vmax=100,cmap="RdBu_r")
plt.show()
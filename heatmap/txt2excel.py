# coding=gbk
#################
#��һ��ִ�еĴ���
import xlwt #д���ļ�
import xlrd #��excel�ļ�
 
fopen=open("/home/public_data/liyufeng_teacher/fzt_data/Tools/excel2txt/data.txt",'r')
lines=fopen.readlines()
#�½�һ��excel�ļ�
file=xlwt.Workbook(encoding='utf-8',style_compression=0)
#�½�һ��sheet
sheet=file.add_sheet('data')
 
############################
#д��д��a.txt��a.txt�ļ���20000���ļ�
i=0
for line in lines:
	sheet.write(i,0,line)
	i=i+1
 
#################################
#�ڶ���ִ�д��룬д��b.txt��
j=79 #��20001��д��
fopen2=open("/home/public_data/liyufeng_teacher/fzt_data/Tools/excel2txt/data.txt",'r')
lines2=fopen2.readlines()
for line in lines2:
	sheet.write(j,0,line)
	j=j+1
file.save('minni.xls')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 0003 上午 11:53
# @Author  : toby
# @Site    : 
# @File    : generate_result.py
# @Software: PyCharm
import sys ,os
import time
import csv
from lib.generate_html import write_csv_to_html


#生成测试报告

def generate_result(resultFileName,result):
    # filePath = os.getcwd()
    filePath = os.path.abspath(os.path.dirname(__file__))
    resultFilePath = os.path.join(os.path.dirname(filePath),'results',resultFileName)
    print('generate resultfilepath %s ' %resultFilePath)


    #写文件到csv中,使用的python3 环境 ,默认后面是有一个"\n" ,所以使用newline='' 表示不增加换行符
    csvFile = open(resultFileName, 'a+',encoding='utf-8',newline='')
    writer = csv.writer(csvFile)
    data = [result]
    writer.writerows(data)
    csvFile.close()

    html_result_path = os.path.join(os.getcwd(),'results',resultFileName+".html")
    write_csv_to_html(resultFilePath,html_result_path)


if __name__ == '__main__':
    filePath = os.getcwd()
    filePath1 = os.path.abspath(os.path.dirname(__file__))
    print(filePath)
    print(filePath1)
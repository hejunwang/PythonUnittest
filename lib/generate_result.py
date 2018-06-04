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


#生成测试报告

def generate_result(resultFileName,result):
    # filePath = os.getcwd()
    filePath = os.path.abspath(os.path.dirname(__file__))
    resultFilePath = os.path.join(os.path.dirname(filePath),'results',resultFileName)
    print('generate resultfilepath %s ' %resultFilePath)


    #写文件到csv中
    csvFile = open(resultFileName, 'a+')
    writer = csv.writer(csvFile)
    data = [result]
    writer.writerows(data)
    csvFile.close()


if __name__ == '__main__':
    filePath = os.getcwd()
    filePath1 = os.path.abspath(os.path.dirname(__file__))
    print(filePath)
    print(filePath1)
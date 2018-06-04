# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-06-02 15:04:36
# @Last Modified by:   Administrator
# @Last Modified time: 2018-06-02 21:32:55

import sys
import os

# 读取要执行的脚本文件
def read_selection():
    path  = os.path.abspath(os.path.dirname(__file__))
    print('read_selection path-->%s' %path)
    #当前文件的父路径
    father_path=os.path.abspath(os.path.dirname(path)+os.path.sep+".")
    #读取文件的绝对路径
    selectionFilepath  =os.path.join(father_path,'scripts','scripts_selection.txt')
    print("readselectionFilepath--->"+selectionFilepath)
    selecton = []

    for line in open(selectionFilepath):
        selecton.append(line.replace('\n',''))
        print('文件列表的名称: '+line)
    return selecton
        



if __name__ == '__main__':
    read_selection()


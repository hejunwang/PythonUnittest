#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 0003 上午 11:55
# @Author  : toby
# @Site    :
# @File    : __init__.py.py
# @Software: PyCharm

import os

# 使用本地的pip3  安装需要的库文件
if __name__ == '__main__':
    pathFile = os.getcwd()
    installFile = os.path.join(pathFile,'requirements.txt')

    commandline ='F:\Python36\Scripts\pip3.exe install -r'+installFile
    os.system(commandline)
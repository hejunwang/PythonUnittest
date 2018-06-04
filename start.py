# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-06-02 15:30:48
# @Last Modified by:   Administrator
# @Last Modified time: 2018-06-02 21:44:39



from lib.execute_selection import execute_selection
from scripts.create_selection import create_selection,create_selection_file

def createfile():
    create_selection_file(create_selection())

if __name__ == '__main__':
    #createfile()      #生成执行文件列表,先要执行生成文件列表,不能再这直接调用,否则直接使用的是本地的地址 会导致出错
    execute_selection()    #开始执行脚本
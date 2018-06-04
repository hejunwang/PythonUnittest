# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-06-02 15:34:13
# @Last Modified by:   Administrator
# @Last Modified time: 2018-06-02 21:12:23


import os
import time
import sys

def write_log(log):
    path = os.getcwd()
    print('write_log')

    #读取文件的绝对路径
    logFilePath = os.path.join(path,'logcat','log.txt')
    print(logFilePath)

    execTime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    with open(logFilePath,'a') as f:
        f.write(execTime+" "+log+"\n")
        print('a 是追加 ')

if __name__ == '__main__':
    write_log('logFilePath')
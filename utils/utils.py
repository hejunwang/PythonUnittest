#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 0003 下午 4:42
# @Author  : toby
# @Site    : 
# @File    : utils.py
# @Software: PyCharm


import time
import os,sys
import datetime

def get_local_time():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

def str_2_tuple(*str):
    return str

def get_specific_time():
    return datetime.datetime.now()


def memInfo():
    pass


def getCmdExecute(cmd):
    tmp = os.popen(cmd).read()
    return tmp



def apkList():
    cmd = "adb shell pm list packages"
    # cmd = "adb shell dumpsys"
    rs= os.popen(cmd).read().split()
    for each in rs:
        print("each -->{}".format(each))

    print(type(rs))



def pipinstall():

    import subprocess
    cmd = "adb devices"
    devices = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]

    serial_nos=[]
    pythonshell=[]
    for item in devices.split():
        filters = ['list','of','device','attached',"devices"]
        if str(item.lower(),encoding='utf-8') not in filters:
            serial_nos.append(str(item,encoding="utf-8"))
            print("item -->{}".format(str(item,encoding="utf-8")))


    for serial in serial_nos:
        print("serial {}".format(serial))
        pythonshell.append("adb -s %s version" %serial)
        pythonshell.append("adb -s %s pip install --pre uiautomator2" %serial)




    for command in pythonshell:
        print("command-->%s" %command)
        sb = subprocess.Popen(command.split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
        print("sb--->{}".format(sb))

if __name__ == '__main__':
    print("python version {}".format(sys.version))
    # pipinstall()
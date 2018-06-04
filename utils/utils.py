#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 0003 下午 4:42
# @Author  : toby
# @Site    : 
# @File    : utils.py
# @Software: PyCharm


import time
import os
import datetime

def get_local_time():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

def str_2_tuple(*str):
    return str

def get_specific_time():
    return datetime.datetime.now()
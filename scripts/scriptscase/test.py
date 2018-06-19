# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-06-02 12:06:18
# @Last Modified by:   Administrator
# @Last Modified time: 2018-06-02 17:32:52

import os
import sys
import time
def test1():
    print(sys.path[0])
    print('this is test1')
    time.sleep(2)
    i = 0
    while True:
        i+=1
        print(i)
        if i==10:
            print('test over  i: %s '%i )
            break
        time.sleep(1)

if __name__ == '__main__':
    test1()


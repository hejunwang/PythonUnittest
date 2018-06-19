# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-06-02 12:06:18
# @Last Modified by:   Administrator
# @Last Modified time: 2018-06-02 17:33:00


from time import *

def main():
    print('this is test2')

    for each in range(1,10):
        print('each %s %s ' %(each,ctime()))
        sleep(1)


if __name__ == '__main__':
    main()


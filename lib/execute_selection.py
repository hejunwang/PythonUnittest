# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-06-02 15:27:38
# @Last Modified by:   Administrator
# @Last Modified time: 2018-06-02 21:38:04


import os
from .read_selection import read_selection
from .write_log import write_log
from .exe_deco import exe_deco
from utils.utils import get_local_time,get_specific_time
from .generate_result import generate_result
from utils.utils import str_2_tuple


from time import ctime
def execute_selection():
    selection = read_selection()
    print('execute_selection list')

    curPath = os.getcwd()
    gettime = get_local_time()
    print('ctime--> %s' %ctime())
    resultFileName =gettime+"_test_result.csv"
    resutFilePath = os.path.join(curPath,'result',resultFileName)
    print('resutFilePath--> %s' %resutFilePath)

    #这里是向表里面写入了头文件
    generate_result(resutFilePath,('ScriptsPath','Detail','StartTime','Endtime','Duration'))

    #执行脚本

    for scriptPath in selection:
        path1 = str_2_tuple(scriptPath)
        starttime = get_specific_time()
        print('starttime :{}'.format(starttime))
        # ret 是装饰器返回的,返回的是元组
        ret = execute_script(scriptPath)
        print('ret 返回值: %s,类型是 %s ' %(ret,type(ret)))


        endtime = get_specific_time()
        print('endtime :{}'.format(endtime))
        duration = (endtime-starttime).microseconds * 0.00001
        #转化成元组
        fileResult = path1+ret+str_2_tuple(starttime)+str_2_tuple(endtime)+str_2_tuple(duration)

        generate_result(resutFilePath,fileResult)


@exe_deco
def execute_script(scriptPath):
    write_log('execute_script :' + scriptPath)
    print('开始执行脚本')
    #这里 有个bug就是,os.system执行的时间,如果有异常 , 装饰器已经把日志都写到了文件中
    # ,爆出来了错误,也没有办法写到日志中
    # os.system('python3 ' + scriptPath)
    re = os.popen('python3 ' + scriptPath).read()
    print('re-->{}'.format(re))   #这里得到的re 都是测试用例执行中的print 输出


if __name__ == '__main__':
    execute_selection()
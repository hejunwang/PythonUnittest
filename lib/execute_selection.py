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

def execute_selection():
    selection = read_selection()
    print('execute_selection list')

    curPath = os.getcwd()
    gettime = get_local_time()
    resultFileName =gettime+"_test_result.csv"
    resutFilePath = os.path.join(curPath,'result',resultFileName)
    print('resultFile--> %s' %resutFilePath)
    #这里是向表里面写入了头文件
    generate_result(resutFilePath,('ScriptsPath','Detail','StartTime','Endtime','Duration'))

    #执行脚本
    for scriptPath in selection:
        path1 = str_2_tuple(resutFilePath)
        starttime = get_specific_time()
        print(starttime)
        # ret 是装饰器返回的
        ret = execute_script(scriptPath)
        print(ret)
        print(type(ret))
        endtime = get_specific_time()
        print(endtime)
        duration = (endtime-starttime).microseconds*0.00001
        #转化成字符串形式
        # fileResult = (path1,str(ret),str(starttime),str(endtime),str(duration))
        fileResult = path1+ret+str_2_tuple(starttime)+str_2_tuple(endtime)+str_2_tuple(duration)

        generate_result(resutFilePath,fileResult)


@exe_deco
def execute_script(scriptPath):
    write_log('execute_script :' + scriptPath)
    os.system('python3 ' + scriptPath)


if __name__ == '__main__':
    execute_selection()
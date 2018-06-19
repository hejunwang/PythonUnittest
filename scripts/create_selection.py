# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-06-02 11:39:11
# @Last Modified by:   Administrator
# @Last Modified time: 2018-06-02 15:02:01

# 这个脚本 生成所有可以执行的脚本文件列表

import sys
import os

def create_selection():
	
	path = sys.path[0]
	print(path)
	print(os.getcwd())
	selection = []
	scriptPath =os.path.join(path,'scriptscase')
	print(scriptPath)
	#查找脚本文件
	for root,dirs,files in os.walk(scriptPath):
		print('root: %s' %root)
		print("dirs :%s" %dirs)
		print("files %s" %files)
		for fileName in files:
			if check_if_python(fileName):
				selection.append(os.path.join(scriptPath,fileName))
				
	cur_file =os.path.basename(sys.argv[0])
	print('cur_file-->'+cur_file)

	if os.path.join(path,cur_file) in selection:
		selection.remove(os.path.join(path,cur_file))

	if os.path.join(path,"__init__.py") in selection:
		selection.remove(os.path.join(path,"__init__.py"))

	return selection

# 判断是否是python文件
def check_if_python(fileName):
	if fileName.endswith('.py'):
		return True


def create_selection_file(selection):
    filePath = os.path.join(os.getcwd(),'scripts_selection.txt')
    print("filepath-->%s" %filePath)
    with open(filePath,'w') as f :
        for scriptPath 	in selection:
            f.write(scriptPath+"\n")


if __name__ == '__main__':
	selection = create_selection()
	create_selection_file(selection)







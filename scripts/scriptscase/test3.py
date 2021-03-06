#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 0002 下午 10:24
# @Author  : toby
# @Site    : 
# @File    : test3.py
# @Software: PyCharm


import unittest
import os

# def main():
#     print('this is test3')
#     try:
#         print('test3')
#         print('try')
#     except Exception as e:
#         print('except <> '+ e)

class Test3(unittest.TestCase):

    def setUp(self):
        print('\ncases before')
        pass

    def test_add(self):
        '''test add method'''
        print('add...')
        a = 3 + 4
        b = 7
        self.assertEqual(a, b)

    def test_sub(self):
        '''test sub method'''
        print('sub...')
        a = 10 - 5
        b = 5
        self.assertEqual(a, b)

    def tearDown(self):
        print('case after\n')
        pass

def main():
    test_dir = os.path.join(os.getcwd())
    print(test_dir)
    test_dir = "I:\PythonUnittest\scripts"
    # 2、自动搜索指定目录下的cas，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # 实例化TextTestRunner类
    runner = unittest.TextTestRunner()
    # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(discover)

if __name__ == '__main__':
    main()



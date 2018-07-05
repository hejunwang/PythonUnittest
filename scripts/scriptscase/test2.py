# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-06-02 12:06:18
# @Last Modified by:   Administrator
# @Last Modified time: 2018-06-02 17:33:00


from time import *
import unittest,os

# def main():
#     print('this is test2')
#
#     for each in range(1,10):
#         print('each %s %s ' %(each,ctime()))
#         sleep(1)

class Test2(unittest.TestCase):

    def setUp(self):
        print('\ncases2 before')
        pass

    def test_add(self):
        '''test add method'''
        print('add2...')
        a = 3 + 4
        b = 7
        self.assertEqual(a, b)

    def test_sub(self):
        '''test sub method'''
        print('sub2...')
        a = 10 - 5
        b = 5
        self.assertEqual(a, b)

    def tearDown(self):
        print('case after2\n')
        pass

def main():
    test_dir = os.path.join(os.getcwd())
    print(test_dir)
    # 2、自动搜索指定目录下的cas，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # 实例化TextTestRunner类
    runner = unittest.TextTestRunner()
    # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(discover)
if __name__ == '__main__':
    main()



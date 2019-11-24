import random
import unittest
from Page_modle import *

# 引用类 Test_login
class test_biz_login(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('完成测试')
    def test_account_update(self):

        Test_Page().user_login('格力供应商','18822029836')
        sleep(3)
        # 点击账户中心 ，银行账户管理
        Test_Page().index_tab('账户中心','银行账户管理')
        sleep(3)

        #修改银行账户
        Test_Page().mod_account('格力供应商')
        sleep(3)
        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()
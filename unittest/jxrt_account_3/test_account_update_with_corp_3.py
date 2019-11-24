import unittest
from Page_modle_3 import *

# 引用类 Test_login
class test_biz_login(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('完成测试')
    def test_account_update(self):

        Test_Page().user_login('中通钢构链条','13620001111')
        sleep(3)
        # 点击账户中心 ，银行账户管理
        Test_Page().index_tab('账户中心','账户管理','银行账户管理')

        #修改银行账户
        sleep(3)
        Test_Page().mod_account_core('中通钢构链条')
        sleep(3)
        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()
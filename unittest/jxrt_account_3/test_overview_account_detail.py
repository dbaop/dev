import unittest
from Page_modle_3 import *

# 引用类 Test_login
class test_biz_login(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('完成测试')
    def test_account_update(self):

        Test_Page().user_login('鱼香茄子','13621112003')
        sleep(3)
        # 点击账户中心 ，银行账户管理
        Test_Page().index_tab('账户中心','账户管理','资产总览')

        # 点击查看交易明细
        Test_Page().transaction_core_query('鱼香茄子', '2019-06-01', '2018-05-01', '100', '110')



        sleep(3)
        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()
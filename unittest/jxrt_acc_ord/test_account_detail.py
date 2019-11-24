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

        Test_Page().user_login('菜中建供应商公司五','13995005555')
        sleep(3)
        # 点击账户中心 ，银行账户管理
        Test_Page().index_tab_core('账户中心','账户明细查询')
        sleep(3)

        #查看我的账户页面
        Test_Page().query_account_detail('菜中建供应商公司五','2019-06-30','2019-06-09','1000','2000')
        sleep(3)

        # 刷新为了重新获取页面，此时再退出，可以正常退出
        sleep(3)
        driver.refresh()

        sleep(2)
        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()
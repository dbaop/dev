#此用例实现了以下几个场景
# 1. 2.0企业端点击缴费管理正常跳转
# 2. 查询条件能够正常筛选
# 3. 点击导出明细正常导出
# 4. 点击明细、缴费通知书正常显示
# 5. 排序是按时间由近及远排序
# 6. 批量下载凭证需要选择
# 7. 导出明细不需要选择，默认下载全部
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
        Test_Page().index_tab_core('账户中心','缴费管理')
        sleep(3)

        #查看我的缴费管理页面
        Test_Page().bill_query('菜中建供应商公司五')

        # 刷新为了重新获取页面，此时再退出，可以正常退出
        sleep(3)
        driver.refresh()

        sleep(2)
        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()
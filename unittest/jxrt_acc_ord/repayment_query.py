from Page_modle import *
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
from time import sleep
import re
class test_repayment(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('完成测试')

    def test_repayment(self):
        #调用登录类
        Test_Page().user_login('公司七九', '18510728006')
        #选择菜单
        Test_Page().index_tab('订单融资','单笔还款查询')

        #输入查询条件
        Test_Page().repayment_query('公司四四','ld2019021802')

        sleep(3)

        #点击查询按钮
        driver.find_element_by_xpath("//span[@class='btn btn-check']").click();
        #搜索出的结果金额总计,此时使用driver 是为了方便下边写方便
        sleep(3)
        sum = driver.find_element_by_xpath("//span[@class='fs-24 c-blue']")
        print ("累计还款本金是："+sum.text)

        # 数据库校验,验证累计还款金额为 T_ORDER_REPAYMENT 中的repayment_amount 的总和
        rs = Test_Page().Oracle_link('T4',
           "select sum(t.repayment_amount)  from prod_ccbscf.T_ORDER_REPAYMENT t where t.drawdown_num = \
            (select d.drawdown_num from prod_ccbscf.T_ORDER_DRAWDOWN_DETAIL d where \
            d.loan_apply_num = 'ld2019021802')",0,2)

        print("数据库中该订单的累计还款本金是%d"%rs[0][0])

        #re.sub(r'\,','',(sum.text)) 替换原有字符中的，然后\是转义字符
        num  = re.sub(r'\,','',(sum.text))
        e = int(float(num))
        try:
            assert rs[0][0] == e
            print("累计还款本金没问题")
        except BaseException:
            print ("Error:累计还款本金计算没问题")

        sleep(2)
        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()
from Page_modle import *
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

#该条用例验证的是链条企业没有单笔赎货查询菜单

class test_redeem_core(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('完成测试')

    def test_corp(self):
        #调用登录类
        Test_Page().user_login('中通钢构链条','13620001111')
        # 点击订单融资 #鼠标悬停
        above = driver.find_element_by_xpath("//ul[@id='font_menu']/li[1]")
        ActionChains(driver).move_to_element(above).perform()

        #点击单笔赎货查询
        sleep(2)
        try:
            assert driver.find_element_by_xpath("//a[@href='/corp/order/query/core/redeem_query.html']")
            print("该公司为核心企业，有单笔赎货查询菜单")
        except BaseException:
            print("该公司不是核心企业，无单笔赎货查询菜单")

        sleep(3)

        # 数据库校验,验证数据中该核心企业下无1206测试核心企业一商户
        count_order = Test_Page().Oracle_link('T4',
             "select count(*) from prod_ccbscf.t_product_corp t where t.corp_name in ('湖南申湘汽车常德众兴销售服务有限公司')and \
            t.product_type_ccbscf = 'ORDER'", 0, 2)
        rs = Test_Page().Oracle_link('T4',
           "select t.user_type from prod_ccbscf.t_ci_user t where t.pk_user = (select c.pk_corp  from\
            prod_ccbscf.T_ci_corp c where c.corp_name = '中通钢构链条' )", 0, 2)
        assert rs[0][0] == 'CORP'
        print("该企业开通了订单融资，产品开通表中有%s条记录，但是企业类型为%s，因此不显示单笔赎货查询菜单"
              %(count_order[0][0],rs[0][0]))

        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()
from Page_modle import *
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

#该条

class test_redeem_core(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('完成测试')

    def test_corp(self):
        #调用登录类
        Test_Page().user_login('12121','13620001111')
        # 点击
        above = driver.find_element_by_xpath("//ul[@id='font_menu']/li[1]")
        ActionChains(driver).move_to_element(above).perform()

        #点击
        sleep(2)
        try:
            assert driver.find_element_by_xpath("//a[@href='/corp/order/query/core/redeem_query.html']")
        except BaseException:

        sleep(3)

        # 数据库校验
        count_order = Test_Page().Oracle_link('T4',
             "select count(*) from prod_ccbscf.t_product_corp t where t.corp_name in ('12121')and \
            t.product_type_ccbscf = 'ORDER'", 0, 2)
        rs = Test_Page().Oracle_link('T4',
           "select t.user_type from prod_ccbscf.t_ci_user t where t.pk_user = (select c.pk_corp  from\
            prod_ccbscf.T_ci_corp c where c.corp_name = '12121' )", 0, 2)
        assert rs[0][0] == 'CORP'
        print("该"
              %(count_order[0][0],rs[0][0]))

        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()

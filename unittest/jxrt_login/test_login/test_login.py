#from Page_modle import *
from page_demo.Page_modle import *
import unittest
# 引用类 Test_login
#Test_login().user_login('格力集团','13621115001')

class test_login(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('完成测试')

    def test_corp(self):

        Test_Page().user_login('格力供应商', '18822029836')
        sleep(3)
        Test_Page().user_logout()

        assert driver.find_element_by_css_selector('[class="sub pointer"]')

        print("退出成功！")

if __name__ == '__main__':
    unittest.main()
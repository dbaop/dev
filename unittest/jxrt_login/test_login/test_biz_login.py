from page_demo.Page_modle import *
import unittest

class test_biz_login(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('完成测试')

    def test_biz(self):

        Test_Page().biz_user_login('18601086706','a1111111')
        sleep(3)
        Test_Page().biz_user_logout()

        print(driver.title)
        assert driver.title == '建信融通有限责任公司'

if __name__ == '__main__':
    unittest.main()
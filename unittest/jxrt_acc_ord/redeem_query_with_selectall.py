from Page_modle import *
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class test_select_all(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('完成测试')

    def test_corp(self):
        #调用登录类
        Test_Page().user_login('上海上汽大众汽车销售有限公司','13552317374')
        #选择菜单
        Test_Page().index_tab('订单融资','单笔赎货查询')

        #点击查询按钮 ,使用该企业做测试,空就不传,等待15s的原因是单笔赎货查询列表响应慢，导致后续窗口无法定位，后续优化下
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//span[@id='select-all']")))

        sleep(5)

        Test_Page().select_all()

        #刷新为了重新获取页面，此时再退出，可以正常退出
        sleep(3)
        driver.refresh()

        sleep(2)
        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()
from selenium import webdriver
import unittest, time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

driver = webdriver.Ie()

class YoudaoTest(unittest.TestCase):
    def setUp(self):
        print("开始有道")

    def test_youdao(self):
        driver.implicitly_wait(30)  # 隐性等待时间为30秒
        driver.get("http://www.youdao.com")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys(u"你好")
        driver.find_element_by_id("translateContent").submit()
        time.sleep(3)
        print("test2")

    def tearDown(self):
        print("结束有道")
        driver.quit()


if __name__ == "__main__":
    unittest.main()
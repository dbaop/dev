from selenium import webdriver
import unittest, time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

driver = webdriver.Ie()

class BaiduTest(unittest.TestCase):
    def setUp(self):
        print("百度开始")

    def test_baidu(self):
        driver.implicitly_wait(30)  # 隐性等待时间为30秒
        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        print("test1")

    def tearDown(self):
        print("百度结束")
        driver.quit()


if __name__ == "__main__":
    unittest.main()
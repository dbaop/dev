from selenium import webdriver
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

driver = webdriver.Ie()
corp_url = "test4.ccbscf.com/"
biz_url =  "test4.ccbscf.com/biz/"
#driver.get("test4.ccbscf.com/")
# 窗口最大化
driver.maximize_window()

class Test_login():
    def user_login(self,login_name,login_phone):
        driver.get(corp_url)
        # 输入企业全称
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(login_name)
        # s输入手机号码
        sleep(2)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(login_phone)
        sleep(2)
        #通过id 来点一下是否保存了密码
        driver.find_element_by_id('passwordInput').click()
        sleep(1)
        driver.find_element_by_id("password").clear()
        sleep(1)
        driver.find_element_by_id('password').send_keys('a1111111')
        #点击登录按钮
        driver.find_element_by_css_selector('[class="sub pointer"]').click()
        sleep(3)
    def biz_user_login(self,login_phone,login_password):

        driver.get(biz_url)
        # s输入手机号码
        sleep(2)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(login_phone)
        sleep(2)
        driver.find_element_by_xpath('//*[@id="form"]/div[3]/input[1]').click()
        #通过id 来点一下是否保存了密码
        driver.find_element_by_xpath('//*[@id="form"]/div[3]/input[1]').clear()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="form"]/div[3]/input[1]').send_keys(login_password)
        sleep(1)
        #点击登录按钮
        driver.find_element_by_css_selector('[class="button"]').click()
        sleep(3)
    def biz_user_logout(self):
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/p[1]').click()

    def user_logout(self):
        driver.find_element_by_class_name('quit').click()
        sleep(2)
        driver.find_element_by_link_text('确定').click()
        sleep(3)


    if __name__ == 'main':
        # login().user_login()
        # sleep(3)
        # login().user_logout()

        driver.quit()
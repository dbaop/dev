from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

driver = webdriver.Ie()
driver.get("www.baidu.com")
driver.implicitly_wait(5)

driver.find_element(By.ID,'kw').click()
driver.find_element(By.NAME,'wd').send_keys("Selenium")
#driver.find_element(By.CLASS_NAME,'s_ipt').send_keys('百度')
#driver.find_element(By.CSS_SELECTOR,"kw").send_keys('Python')

sleep(1)
driver.find_element(By.ID,'su').click()
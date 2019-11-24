from time import sleep
from selenium import webdriver
class Page():
    def __init__(self,driver):
        self.driver = driver
        self.base_url = "test4.ccbscf.com"
        self.timeout = 10

    def _open(self,url):
        url_ = self.base_url
        print("Page is %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        assert self.driver.current_url == url_,'Did not land on %s' %url_

    def open(self):
        self.open(self.url)
        #self.driver.get(url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def driver(self, browser):
        if browser == 'ie':
            driver = webdriver.Ie()
        if browser == 'chrome':
            driver = webdriver.Chrome(chrome_options=optons)
        if browser == 'firefox':
            driver = webdriver.Firefox()
        driver.maximize_window()
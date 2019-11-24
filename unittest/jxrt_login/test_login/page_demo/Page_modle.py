from selenium import webdriver
from time import sleep
import subprocess
import xlrd
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

# #以下方法可以启动chrome
optons=webdriver.ChromeOptions()
#浏览器启动配置
optons.add_argument('disable-infobars')
# #启动谷歌浏览器
# driver=webdriver.Chrome(chrome_options=optons)
# driver.get("http://test4.ccbscf.com/")

driver = webdriver.Ie()
corp_url = "test4.ccbscf.com/"
biz_url =  "test4.ccbscf.com/biz/"
# 窗口最大化
driver.maximize_window()

class Test_Page():
    #企业端登录和退出
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
    def user_logout(self):
        driver.find_element_by_class_name('quit').click()
        sleep(2)
        driver.find_element_by_link_text('确定').click()
        sleep(3)


    #平台端登录和退出
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

     #导出明细
    def export_detail(self):
        driver.find_element_by_css_selector("[class='btn bg-blue btn-180-50 fw-bold c-white mt30']").click()
        try:
            #请选择赎货明细  btn btn-border bg-blue btn-140-40 c-white fs-16
            driver.find_element_by_class_name('btn btn-border bg-blue btn-140-40 c-white fs-16').click()
            print("请选择赎货明细")
            driver.find_element_by_class_name('btn bg-blue btn-180-50 fw-bold c-white mt30').click()
        except BaseException:
            #driver.find_element_by_class_name('btn btn-border bg-blue btn-140-40 c-white fs-16').click()
            # a[1]是确定，a[2]是取消
            driver.find_element_by_xpath('//div[@class = "dialog-footer tar"]/a[1]').click()
            sleep(2)


    #通过选择菜单可以进入任意模块
    def index_tab(self,tab,Stab):

        # 点击订单融资 #鼠标悬停
        if tab == '订单融资':
            above = driver.find_element_by_xpath("//ul[@id='font_menu']/li[1]")
            ActionChains(driver).move_to_element(above).perform()
        if tab == '账户中心':
            above = driver.find_element_by_xpath("//ul[@id='font_menu']/li[6]")
            ActionChains(driver).move_to_element(above).perform()

        # 点击单笔赎货查询
        if Stab == '单笔赎货查询':
            sleep(2)
            above_1 = driver.find_element_by_xpath("//a[@href='/corp/order/query/core/redeem_query.html']")
        elif Stab == '单笔还款查询':
            sleep(2)
            above_1 = driver.find_element_by_xpath("//a[@href='/corp/order/query/core/repayment_query.html']")
        elif Stab == '银行账户管理':
            sleep(2)
            above_1 = driver.find_element_by_xpath("//a[@href='/corp/account/bank/account_maintain.html']")
        driver.execute_script("arguments[0].click();", above_1)



#关于数据库的一些操作，其中 Oracle_link 是关于 oracle 连接的，

# Oracle 使用cursor进行各种操作   释放cursor   self._DelCursor(cur)
    def Oracle_link(self,env,sql,nStart=0 , nNum=- 1):

        #连接数据库
        import cx_Oracle
        # conn=cx_Oracle.connect('t2_updscf/000000@12.0.216.142:1523/jxrtest')    #连接数据库
        conn = cx_Oracle.connect('prod_selscf/000000@12.0.216.136:1523/jxr2p')
        c = conn.cursor()  # 获取cursor
        x = c.execute('select sysdate from dual')
        x.fetchone()
        c.close()  # 关闭cursor
        conn.close()

        #查询数据库
        if env == 'T1':
            conn = cx_Oracle.connect('t_updscf/000000@12.0.216.142:1523/jxrtest')
        elif env == 'T2':
            conn = cx_Oracle.connect('t2_updscf/000000@12.0.216.142:1523/jxrtest')
        elif env == 'T4':
            conn = cx_Oracle.connect('prod_selscf/000000@12.0.216.136:1523/jxr2p')
        cur = conn.cursor()
        rt = []
        # 获取cursor
        if not cur:
            return rt
        # 查询到列表
        cur.execute(sql)
        # num 为1证明只看一条
        if (nStart == 0) and (nNum == 1):
            rt.append(cur.fetchone())
        else:
            # 如果不是0或者num=!1,默认是全部
            rs = cur.fetchall()
            # for x in rs:
            #     print(x)
            if nNum == - 1:
                rt.extend(rs[nStart:])
            else:
                rt.extend(rs[nStart:nStart + nNum])
        return rt

    # mongodb


    def Mongodb_link(self,env,db,collection,filters,results):
        import pymongo
        if env == 'T1':
            myclient = pymongo.MongoClient("mongodb://12.0.216.155:27017")
        elif env == 'T2':
            myclient = pymongo.MongoClient("mongodb://12.0.216.145:27017")
        #针对集群
        elif env == 'T4':
            #myclient = pymongo.MongoClient("mongodb://12.0.216.30:37017")
            myclient = pymongo.MongoClient('mongodb://ccbscf_app:mcsa2jxrtT#@12.0.216.30:37017')
        #选择数据库
        mydb = myclient[db]
        #查询缴费凭证表
        mycol = mydb[collection]
        result = []
        #除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。，查询条件已经默认是0
        for x in mycol.find(filters, results):
            #print(x)
            #print(x['billAmount'])
            result.append(x)
        return result

    if __name__ == 'main':
        driver.quit()
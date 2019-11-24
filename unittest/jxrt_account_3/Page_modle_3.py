from selenium import webdriver
#from BasePage import *
from time import sleep
import subprocess
import xlrd
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
env = 'prod_ccbscf'
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
        # driver.find_element_by_class_name('quit').click()
        # sleep(2)
        # driver.find_element_by_link_text('确定').click()
        # sleep(3)

        above=driver.find_element_by_css_selector("[class='ivu-icon ivu-icon-ios-arrow-down']")

        ActionChains(driver).move_to_element(above).perform()

        sleep(2)

        driver.find_element_by_xpath("//ul[@class='ivu-dropdown-menu']/li[1]").click()

        sleep(2)

        # driver.switch_to.frame(driver.find_element_by_id('_QD_STATUS_MANAGE_SOCKET_IFRAME'))
        # driver.switch_to.frame(driver.find_element_by_css_selector("[class='ivu-btn ivu-btn-primary']"))
        # js = 'document.getElementsByClassName("ivu-btn ivu-btn-primary")[0].click();'
        # driver.execute_script(js)
        driver.find_element_by_css_selector("[class='ivu-btn ivu-btn-primary']").click()
        # driver.find_element_by_link_text('确认').click()
        # driver.find_element_by_xpath("//button[contains(text(),'确认')]").click()
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

    # def index_tab(self,tab,Stab):
    #
    #     # 点击订单融资 #鼠标悬停
    #     if tab == '订单融资':
    #         above = driver.find_element_by_xpath("//ul[@id='font_menu']/li[1]")
    #         ActionChains(driver).move_to_element(above).perform()
    #     if tab == '账户中心':
    #         above = driver.find_element_by_xpath("//ul[@id='font_menu']/li[6]")
    #         ActionChains(driver).move_to_element(above).perform()
    #
    #     # 点击单笔赎货查询
    #     if Stab == '单笔赎货查询':
    #         sleep(2)
    #         above_1 = driver.find_element_by_xpath("//a[@href='/corp/order/query/core/redeem_query.html']")
    #     elif Stab == '单笔还款查询':
    #         sleep(2)
    #         above_1 = driver.find_element_by_xpath("//a[@href='/corp/order/query/core/repayment_query.html']")
    #     elif Stab == '银行账户管理':
    #         sleep(2)
    #         above_1 = driver.find_element_by_xpath("//a[@href='/corp/account/bank/account_maintain.html']")
    #     driver.execute_script("arguments[0].click();", above_1)

    #因为有的菜单tab个数不一样

    def index_tab(self,Ftab,Stab,Ttab):

        # 点击订单融资 #鼠标悬停
        if Ftab == '产品':
            above = driver.find_element_by_xpath("//ul[@id='font_menu']/li[1]")
            ActionChains(driver).move_to_element(above).perform()
        if Ftab == '供应商管理':
            above = driver.find_element_by_xpath("//ul[@id='font_menu']/li[4]")
            ActionChains(driver).move_to_element(above).perform()
        if Ftab == '账户中心':
            above = driver.find_element_by_xpath("//a[@href='/cv3/my/person-info/index']")
            above.click()

        # 点击二级菜单
        if Stab == '账户管理':
            sleep(2)
            driver.find_element_by_xpath("//ul[@class='ivu-menu ivu-menu-light ivu-menu-vertical']/li[2]").click()
        elif Stab == '单笔还款查询':
            sleep(2)
            above_1 = driver.find_element_by_xpath("//a[@href='/corp/order/query/core/repayment_query.html']")

        # 点击三级菜单
        if Ttab == '资产总览':
            sleep(2)
            finance = driver.find_element_by_xpath("//a[@href='/cv3/my/account/overview']")
            finance.click()
        elif Ttab == '账户明细查询':
            sleep(2)
            transaction = driver.find_element_by_xpath("//a[@href='/cv3/my/account/transaction']")
            transaction.click()
        elif Ttab == '银行账户管理':
            sleep(2)
            above=driver.find_element_by_xpath("//a[@href='/cv3/my/account/info']")
            above.click()
        elif Ttab == '凭证管理':
            sleep(2)
            receipt = driver.find_element_by_xpath("//a[@href='/cv3/my/account/receipt']")
            receipt.click()
    def core_name(self, core_name):
        # 输入企业全称，依次点击查询，选择
        driver.find_element_by_class_name('input-btn').click()
        sleep(3)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div[7]/div/div[1]/div/div/div[1]/span[2]/input").send_keys(core_name)
        driver.find_element_by_xpath("//span[@class='btn bg-blue btn-108-38 c-white fs-14 ml20']").click()
        sleep(2)
        driver.find_element_by_xpath("//span[@class='btn bg-blue btn-auto-30 c-white']").click()
        try:
            # 没有有效合同
            driver.find_element_by_class_name('fs-16')
            # pl_name = driver.find_element_by_link_text('1206测试核心企业一')
            # print(pl_name.text)
            print("该商户没有有效合同，请选择其他商户")
            sleep(2)
            driver.find_element_by_xpath("//div[@class='dialog-footer tar']/"
                                         "a[@class='btn btn-border bg-blue btn-140-40 c-white fs-16']").click();
            # 数据库校验,验证数据中该核心企业下无1206测试核心企业一商户
            rs = Test_Page().Oracle_link('T4',
               "select count(*) from prod_ccbscf.t_ebs_contract_downstream t where t.corp_name = '公司四四' and \
               t.counterparty_name = '1206测试核心企业一T4';", 0, 2)
            assert rs[0][0] == 0
            print(core_name + "核心企业下无该商户的赎货")
        except BaseException:
            print(core_name + "有有效合同")

    def core_query(self, order_no, guaranty_num, goods_name):
        # 订单编号、仓单编号、授信品种、货物名称、申请日期,默认是流贷
        driver.find_element_by_xpath('// input[ @ placeholder = "请输入订单编号"]').send_keys(order_no)
        driver.find_element_by_xpath('// input[ @ placeholder = "请输入仓单编号"]').send_keys(guaranty_num)
        driver.find_element_by_xpath('// input[ @ placeholder = "请输入货物名称"]').send_keys(goods_name)
        driver.find_element_by_xpath('// span[ @ class = "ivu-select-placeholder"]').click()
        # li[1]是电票，li[2]是流贷
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div[4]/span[2]/div/div[2]/ul[2]/li[2]').click()
        # 申请日期起始时间结束时间就不写了，太麻烦
        # driver.find_element_by_xpath('// input[ @ placeholder = "开始"]').send_keys(goods_name)
    # 账户明细查询
    def transaction_core_query(self,corp_name, data_end, date_start, s_amount,b_amount):
        # 跳转到账户明细查询页面
        sleep(2)
        transaction = driver.find_element_by_xpath("//a[@href='/cv3/my/account/transaction']")
        transaction.click()
        #统计总共多少条
        rs = Test_Page().Oracle_link('T4',
             "select count(*) from %s.t_account_detail t where t.FK_ACCOUNT in (select a.pk_account from \
             %s.t_account a where a.FK_ACCOUNT_PARENT = (select t.PK_ACCOUNT from %s.t_account t \
             where t.account_name = '%s' and t.account_type in ('VMF', 'VMC')))  \
             order by t.trade_time asc"%(env,env,env,corp_name), 0, 2)
        sleep(2)
        total = driver.find_element_by_xpath("//span[@class='ivu-page-total']")
        print(total.text)
        # 判断页面条数为数据库总的条数
        print("共 %s 条"%rs[0][0])
        assert "共 %s 条"%rs[0][0] == total.text
        # 验证查询条件
        driver.find_element_by_xpath('// input[ @ placeholder = "结束"]').send_keys(data_end)
        driver.find_element_by_xpath('// input[ @ placeholder = "开始"]').send_keys(date_start)
        driver.find_element_by_xpath('// input[ @ placeholder = "大于"]').send_keys(s_amount)
        driver.find_element_by_xpath('// input[ @ placeholder = "小于"]').send_keys(b_amount)
        sleep(2)
        driver.find_element_by_css_selector("[class='btn current ivu-btn ivu-btn-default']").click()

        # 查询明细
        qd = Test_Page().Oracle_link('T4',
             "select t.amount,t.balance,t.trade_type,t.remark from prod_ccbscf.t_account_detail t where t.FK_ACCOUNT in (select a.pk_account from \
             prod_ccbscf.t_account a where a.FK_ACCOUNT_PARENT = (select t.PK_ACCOUNT from prod_ccbscf.t_account t \
             where t.account_name = '%s' and t.account_type in ('VMF', 'VMC'))) \
             and t.amount >= %s and t.amount <= %s and t.trade_time >= TO_DATE('%s', 'YYYY-MM-DD') and \
             t.trade_time <= TO_DATE('%s', 'YYYY-MM-DD')order by t.trade_time asc" % (corp_name,s_amount,b_amount,date_start,data_end), 0, 2)
        qd_c = Test_Page().Oracle_link('T4',
             "select count(*) from prod_ccbscf.t_account_detail t where t.FK_ACCOUNT in (select a.pk_account from \
             prod_ccbscf.t_account a where a.FK_ACCOUNT_PARENT = (select t.PK_ACCOUNT from prod_ccbscf.t_account t \
             where t.account_name = '%s' and t.account_type in ('VMF', 'VMC')))\
             and t.amount >= %s and t.amount <= %s and t.trade_time >= TO_DATE('%s', 'YYYY-MM-DD') and \
             t.trade_time <= TO_DATE('%s', 'YYYY-MM-DD')order by t.trade_time asc" % (corp_name,s_amount,b_amount,date_start,data_end), 0, 2)

        print("该条件下的总条数为%s"%(qd_c[0][0]))
        #点击导出明细 ，目前导出明细为筛选条件之前的所有明细，产品说暂时不改。
        driver.find_element_by_css_selector("[class='fr ivu-btn ivu-btn-primary']").click()
        sleep(5)

        file_pathB = r'C:\Users\dbaop\Desktop\picture\corp_account.xlsx'
        cmd = 'D:/pythonTest/StudyPythonC/testC.exe' + ' ' + file_pathB
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
        out, err = p.communicate()

        sleep(3)
        book = xlrd.open_workbook(r'C:\Users\dbaop\Desktop\picture\corp_account.xlsx')
        sheet = book.sheet_by_index(0)  # 根据顺序获取sheet
        sheet2 = book.sheet_by_name('Sheet1')  # 根据sheet页名字获取sheet
        for i in range(sheet.nrows):  # 0 1 2 3 4 5
            print(sheet.row_values(i))  # 获取第几行的数据

        print("导出的数据为所有的数据！")

    # 修改银行账户，包括查询转账计划，反向汇款认证、账户信息

    def mod_account(self):

        #查询修改之前的银行账户，通过 oracle
        rs = Test_Page().Oracle_link('T4',
           "select account_code from prod_ccbscf.t_account\
           where account_name = '格力供应商' and pk_account = (select fk_account from prod_ccbscf.t_account_owner\
           where fk_user_owner = (select pk_corp from prod_ccbscf.t_ci_corp where corp_name = '格力供应商')\
           and account_usage_type = 'COLLECT')", 0, 100)
        print("修改之前的银行账户是%s" % rs[0][0])
        #点击修改按钮
        driver.find_element_by_css_selector('[class = "btn btn-140-40 c-white bg-blue"]').click()

        # 生成随机数
        # account_num = 62170000 + random.randint(1, 100)
        #account_num = '11001018700053004936'  以后放款记得改成这个贷转存账号，建行那边埋数了
        account_num = '6217000011112222' + str(random.randint(1000, 9999))

        print("修改之后的账户是%s" %account_num)
        sleep(3)
        driver.find_element_by_css_selector("[class ='inp fs-14']").clear()
        driver.find_element_by_css_selector("[class ='inp fs-14']").send_keys(account_num)

        # 下边那样写会报错 Compound class names not permitted
        #driver.find_element_by_class_name('inp fs-14').send_keys('12345678')
        driver.find_element_by_css_selector("[class ='btn btn-140-40 c-white bg-blue']").click()
        sleep(3)

        #调用 autoit 函数
        cmd='D:/pythonTest/StudyPythonC/UKEY.exe'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.returncode == 0:
            print('银行账户修改成功！')
        sleep(5)

        #点击银行账户修改成功弹出框的确定按钮
        driver.find_element_by_css_selector("[class ='btn bg-blue btn-140-40 c-white fs-16']").click()

        #查询 mongodb 数据库,链条企业进行了反向汇款认证
        rs_m = Test_Page().Mongodb_link('T4', 'ccbscf-biz-payment', 'accountVerifyInfoDO',
            {"accountCode": account_num},{"_id": 1, "accountVerifyState": 1, "accountCode": 1})
        print(rs_m)
        print(rs_m[0]['accountCode'])
        assert rs_m[0]['accountCode'] == account_num

        # 查询 Oracle 数据库,账号修改成功，此时需要转下
        rs_o = Test_Page().Oracle_link('T4',
           "select account_code from prod_ccbscf.t_account\
           where account_name = '格力供应商' and pk_account = (select fk_account from prod_ccbscf.t_account_owner\
           where fk_user_owner = (select pk_corp from prod_ccbscf.t_ci_corp where corp_name = '格力供应商')\
           and account_usage_type = 'COLLECT')", 0, 100)
        rs_v = Test_Page().Oracle_link('T4',
           "select t.account_code_cr,t.amount from prod_ccbscf.t_account_transfer t where \
           t.account_name_cr = '格力供应商' order by t.trade_time desc", 0, 10)
        #print(rs)
        print("反向汇款认证的账号是%s,给该账号汇了%s元" %(rs_v[0][0],rs_v[0][1]))
        assert rs_o[0][0] == rs_v[0][0]
        assert rs_v[0][1] == 0.01

    # 修改银行账户，包括查询转账计划，反向汇款认证、账户信息,但是对于核心企业不发生反向汇款

    def mod_account_core(self,corp_name):

        #查询修改之前的银行账户，通过 oracle
        rs = Test_Page().Oracle_link('T4',
           "select account_code from prod_ccbscf.t_account\
           where account_name = '%s' and pk_account = (select fk_account from prod_ccbscf.t_account_owner\
           where fk_user_owner = (select pk_corp from prod_ccbscf.t_ci_corp where corp_name = '%s')\
           and account_usage_type = 'COLLECT')"%(corp_name,corp_name), 0, 100)
        print("修改之前的银行账户是%s" % rs[0][0])
        #点击修改按钮
        driver.find_element_by_css_selector('[class = "btn current ivu-btn ivu-btn-primary"]').click()

        # 生成随机数,由于数据库是 str 型，需要改成 str 型的
        # account_num = 62170000 + random.randint(1, 100)
        account_num = '6217000011112222' + str(random.randint(1000, 9999))

        print("修改之后的账户是%s" %account_num)
        sleep(3)
        driver.find_element_by_css_selector("[class ='ivu-input']").clear()
        driver.find_element_by_css_selector("[class ='ivu-input']").send_keys(account_num)

        #验证开户支行全称可以手输,点击第一个父类是为了定位到输入框，然后再删除
        driver.find_element_by_css_selector("[class ='ivu-input-wrapper ivu-input-wrapper-default"
            " ivu-input-type ivu-input-group ivu-input-group-default ivu-input-group-with-append"
            " ivu-input-hide-icon']").click()
        driver.find_element_by_css_selector("[class ='ivu-input ivu-input-default']").clear()
        driver.find_element_by_css_selector("[class ='ivu-input ivu-input-default']").send_keys('建行北京支行')

        # 下边那样写会报错 Compound class names not permitted
        #driver.find_element_by_class_name('inp fs-14').send_keys('12345678')
        driver.find_element_by_css_selector("[class ='btn current mr10 ivu-btn ivu-btn-primary']").click()
        sleep(3)

        #调用 autoit 函数
        cmd='D:/pythonTest/StudyPythonC/UKEY.exe'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.returncode == 0:
            print('银行账户修改成功！')
        sleep(5)

        #点击银行账户修改成功弹出框的确定按钮
        driver.find_element_by_css_selector("[class ='ivu-btn ivu-btn-primary ivu-btn-large']").click()

        #查询 mongodb 数据库,核心企业不进行反向汇款认证
        rs_m = Test_Page().Mongodb_link('T4', 'ccbscf-biz-payment', 'accountVerifyInfoDO',
            {"accountCode": account_num},{"_id": 1, "accountVerifyState": 1, "accountCode": 1})
        print(rs_m)
        print("该账号在库中的记录为%s,并没有进行反向汇款认证" %(rs_m))

        # 查询 Oracle 数据库,账号修改成功，此时需要转下
        rs_o = Test_Page().Oracle_link('T4',
           "select account_code from prod_ccbscf.t_account\
           where account_name = '%s' and pk_account = (select fk_account from prod_ccbscf.t_account_owner\
           where fk_user_owner = (select pk_corp from prod_ccbscf.t_ci_corp where corp_name = '%s')\
           and account_usage_type = 'COLLECT')"%(corp_name,corp_name), 0, 100)
        rs_v = Test_Page().Oracle_link('T4',
           "select count(*) from prod_ccbscf.t_account_transfer t where t.account_name_cr = '%s' \
       and t.ACCOUNT_CODE_CR = '%s' order by t.trade_time desc"%(corp_name,account_num), 0, 10)
        #print(rs)
        print("该账号在库中的记录为%s,并没有转一分钱." %(rs_v[0][0]))
        assert rs_v[0][0] == 0

        # 由于链条企业账号有时候在建行埋数了，所以改过之后尽量再改回来 ， 点击修改按钮
        sleep(2)
        driver.find_element_by_css_selector('[class = "btn current ivu-btn ivu-btn-primary"]').click()
        sleep(3)
        driver.find_element_by_css_selector("[class ='ivu-input']").clear()
        driver.find_element_by_css_selector("[class ='ivu-input']").send_keys(rs[0][0])

        driver.find_element_by_css_selector("[class ='btn current mr10 ivu-btn ivu-btn-primary']").click()
        sleep(3)
        # 调用 autoit 函数
        cmd = 'D:/pythonTest/StudyPythonC/UKEY.exe'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.returncode == 0:
            print('银行账户修改成功！')
        sleep(5)
        # 点击银行账户修改成功弹出框的确定按钮
        driver.find_element_by_css_selector("[class ='ivu-btn ivu-btn-primary ivu-btn-large']").click()

        print("账户再次修改成功，修改后的账号是%s" % (rs[0][0]))

    #选择全选按钮，适用于导出明细
    def select_all(self):
        sleep(3)
        driver.find_element_by_xpath("//span[@id='select-all']").click()
        account = driver.find_element_by_xpath("//div[@class = 'fr mt15']/span[5]")
        select_account = driver.find_element_by_xpath("//div[@class = 'fl ml50 mt15']/span[5]")

        print("全选的金额是" + select_account.text + ",货物总计的金额是" + account.text)

        Test_Page().export_detail()

        # 调用 autoit 实现另存为
        # 为防止出现因IO引起的死等，官方推荐的做法是使用communicate，比如这样：
        # 相当于linux exit code) subprocess.check_call()父进程等待子进程完成返回0检查退出信息，如果returncode不为0,则举出错误
        # file_path=r'C:\Users\dbaop\Desktop\picture'
        # cmd='D:/pythonTest/StudyPythonC/test.exe'+' ' +file_path

        file_pathB = r'C:\Users\dbaop\Desktop\picture\goods_0.xlsx'
        cmd = 'D:/pythonTest/StudyPythonC/testC.exe' + ' ' + file_pathB
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
        out, err = p.communicate()

        sleep(3)
        book = xlrd.open_workbook(r'C:\Users\dbaop\Desktop\picture\goods_0.xlsx')
        sheet = book.sheet_by_index(0)  # 根据顺序获取sheet
        sheet2 = book.sheet_by_name('Sheet1')  # 根据sheet页名字获取sheet
        for i in range(sheet.nrows):  # 0 1 2 3 4 5
            print(sheet.row_values(i))  # 获取第几行的数据

        print("导出的数据为全选的数据！")

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

    #企业端单笔赎货查询选择经销商

    def core_name(self,core_name):
        # 输入企业全称，依次点击查询，选择
        driver.find_element_by_class_name('input-btn').click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[7]/div/div[1]/div/div/div[1]/span[2]/input").send_keys(core_name)
        driver.find_element_by_xpath("//span[@class='btn bg-blue btn-108-38 c-white fs-14 ml20']").click()
        sleep(2)
        driver.find_element_by_xpath("//span[@class='btn bg-blue btn-auto-30 c-white']").click()
        try:
            #没有有效合同
            driver.find_element_by_class_name('fs-16')
            # pl_name = driver.find_element_by_link_text('1206测试核心企业一')
            # print(pl_name.text)
            print("该商户没有有效合同，请选择其他商户")
            sleep(2)
            driver.find_element_by_xpath("//div[@class='dialog-footer tar']/"
                                         "a[@class='btn btn-border bg-blue btn-140-40 c-white fs-16']").click();
            # 数据库校验,验证数据中该核心企业下无1206测试核心企业一商户
            rs = Test_Page().Oracle_link('T4',
               "select count(*) from prod_ccbscf.t_ebs_contract_downstream t where t.corp_name = '公司四四' and \
               t.counterparty_name = '1206测试核心企业一T4';", 0, 2)
            assert rs[0][0] == 0
            print(core_name+"核心企业下无该商户的赎货")
        except BaseException:
            print(core_name+"有有效合同")


    #企业端单笔赎货查询输入查询条件

    def core_query(self, order_no,guaranty_num,goods_name):
        # 订单编号、仓单编号、授信品种、货物名称、申请日期,默认是流贷
        driver.find_element_by_xpath('// input[ @ placeholder = "请输入订单编号"]').send_keys(order_no)
        driver.find_element_by_xpath('// input[ @ placeholder = "请输入仓单编号"]').send_keys(guaranty_num)
        driver.find_element_by_xpath('// input[ @ placeholder = "请输入货物名称"]').send_keys(goods_name)
        driver.find_element_by_xpath('// span[ @ class = "ivu-select-placeholder"]').click()
        # li[1]是电票，li[2]是流贷
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[4]/span[2]/div/div[2]/ul[2]/li[2]').click()
        #申请日期起始时间结束时间就不写了，太麻烦
        #driver.find_element_by_xpath('// input[ @ placeholder = "开始"]').send_keys(goods_name)

    # 企业端单笔还款查询输入查询条件

    # def repayment_query(self, name, order_num, start_date,end_date):
    def repayment_query(self, name, order_num):
        # 订单编号、仓单编号、授信品种、货物名称、申请日期,默认是流贷
        driver.find_element_by_xpath('// input[ @ placeholder = "请输入商户名称"]').send_keys(name)
        driver.find_element_by_xpath('// input[ @ placeholder = "请输入订单编号"]').send_keys(order_num)
        #开始时间
        js = 'document.getElementsByName("date-time")[0].removeAttribute("readonly")'
        driver.execute_script(js)
        js_value_start = 'document.getElementsByName("date-time")[0].value="2016-12-25"'
        driver.execute_script(js_value_start)
        sleep(2)

        #结束时间
        js = 'document.getElementsByName("date-time")[1].removeAttribute("readonly")'
        driver.execute_script(js)
        js_value_end = 'document.getElementsByName("date-time")[1].value="2019-12-26"'
        driver.execute_script(js_value_end)
        sleep(2)

#关于数据库的一些操作，其中 Oracle_link 是关于 oracle 连接的，

# Oracle 使用cursor进行各种操作   释放cursor   self._DelCursor(cur)
    def Oracle_link(self,env,sql,nStart=0 , nNum=- 1):

        #连接数据库
        import cx_Oracle
        # conn=cx_Oracle.connect('t2_updscf/000000@12.0.216.142:1523/jxrtest')    #连接数据库
        conn = cx_Oracle.connect('P_DUBAOPING/IZWZrw7#@12.0.216.136:1523/jxr2p')
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
            conn = cx_Oracle.connect('P_DUBAOPING/IZWZrw7#@12.0.216.136:1523/jxr2p')
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
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

    def test_filters(self):
        #调用登录类
        Test_Page().user_login('上海上汽大众汽车销售有限公司','13552317374')
        #选择菜单
        Test_Page().index_tab('订单融资','单笔赎货查询')

        #点击查询按钮 ,使用该企业做测试,空就不传,等待15s的原因是单笔赎货查询列表响应慢，导致后续窗口无法定位，后续优化下
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//span[@id='select-all']")))

        sleep(5)

        # 点击查询按钮 ,使用该企业做测试,空就不传,等待15s的原因是单笔赎货查询列表响应慢，导致后续窗口无法定位，后续优化下
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@id='select-all']")))

        # 输入查询条件
        Test_Page().core_name('1206测试核心企业一T4')
        Test_Page().core_name('湖南申湘汽车常德众兴销售服务有限公司')
        Test_Page().core_query('p50814001', '', '')
        sleep(1)
        driver.find_element_by_xpath("//span[@class='btn btn-check']").click();
        sleep(2)

        driver.find_element_by_xpath("//span[@id='select-all']").click();
        sum_account = driver.find_element_by_xpath("//div[@class = 'fr mt15']/span[5]")
        select_sum_account = driver.find_element_by_xpath("//div[@class = 'fl ml50 mt15']/span[5]")
        print("该订单编号下的货物金额是：" + sum_account.text)
        print("当前页选中的货物金额是：" + select_sum_account.text)

        # # #re.sub(r'\,','',(sum.text)) 替换原有字符中的，然后\是转义字符
        num = re.sub(r'\,', '', (sum_account.text))
        sum_account = int(float(num))
        select_num = re.sub(r'\,', '', (select_sum_account.text))
        select_sum_account = int(float(select_num))

        # # 数据库校验,验证赎货数量和货物金额
        rs = Test_Page().Oracle_link('T4',
           "select sum(t.remand_amount),sum(t.repayment_amount) from prod_ccbscf.T_ORDER_GUARANTY_PICKUP t where t.core_name in \
            (select o.core_name  from prod_ccbscf.T_ORDER_DRAWDOWN_DETAIL o where o.product_type = 'SHORT_TERM_WORKING_CAPTIAL_LOAN'\
            and o.core_name = '上海上汽大众汽车销售有限公司') and  t.pledgeor_name = '湖南申湘汽车常德众兴销售服务有限公司'and t.guaranty_storage_state = 'OUT_STORAGE' and \
            t.loan_apply_num = 'p50814001'", 0, 2)
        print("数据库中查询到的赎货数量是%s箱,赎货金额是%s元" % (rs[0][0], rs[0][1]))

        try:
            assert rs[0][1] == select_sum_account
            print("金额没问题")
        except BaseException:
            print("Error:金额计算有问题")

        sleep(2)
        Test_Page().user_logout()

if __name__ == '__main__':
    unittest.main()
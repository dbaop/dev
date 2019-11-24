import unittest
from Page_modle_3 import *


Test_Page().user_login('鱼香茄子','13621112003')
sleep(3)
# 点击账户中心 ，银行账户管理
Test_Page().index_tab('账户中心','账户管理','凭证管理')

# 点击缴费凭证
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]'
                             '/div/div/div[2]/div[1]/div/div/div/div/div[5]').click()
sleep(3)
# 点击预览凭证，然后关闭
# #driver.find_element_by_link_text('预览凭证').click()
# driver.find_element_by_xpath('//div[@class = "ivu-btn ivu-btn-default action-button"]/span[1]').click()
# sleep(5)
# # 可以定位到pdf 中的融信编号
# driver.find_element_by_xpath('//*[@id="viewer"]/div/div[2]/span[2]').click()
# driver.find_element_by_css_selector("[class='ivu-icon ivu-icon-ios-close']").click()

# 点击导出明细 ，目前导出明细为筛选条件之前的所有明细，产品说暂时不改。
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
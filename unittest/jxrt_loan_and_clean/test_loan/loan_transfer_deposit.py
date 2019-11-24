from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
from loan_page.Page_loan_test_DB import *

# 贷转存(前提条件是已经签了合同)：
# 1、执行 5528sql 脚本使得白条状态变成FI5,然后有相应数据(如果正常交互，和建行联调，无法自动化)
# 2、插入oracle 流水，mongodb 中相应账单信息，通过 CCBSCF_BANK_SERIAL_NO 和 SUMMARY_CODE 关联起来
# 3、执行账单的自动匹配(流水账单自动匹配，平台端账单信息查询中可看到该白条已匹配)
# 4、执行代发工资白条匹配处理(此时白条状态变为FID)

# 执行定时任务

# Test_Page().exec_5528('DFGZEXT-20190522-002-000001')
# sleep(2)
# Test_Page().xxl_job('T4','白条服务','根据反馈结果更新融资进度状态任务')
# sleep(2)
# Test_Page().xxl_job('T4','价格服务','推送账单服务')
#
#
# #Test_Page().xxl_job('T4','价格服务','确认账单服务')
# #test_interface().Interface('xxl-job-admin/jobinfo/pageList')
#
# Test_Page().xxl_job('T4','支付结算','代发工资白条匹配处理')

# Test_Page().match('DGGAA-20190621-014-000001')
Test_Page().match_depo('SHJGYJJT-20190801-001-000001')

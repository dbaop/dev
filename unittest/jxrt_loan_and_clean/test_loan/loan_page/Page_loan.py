from selenium import webdriver
import decimal
from time import sleep
import subprocess
import xlrd
import time
import datetime
from dateutil import parser
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

Env = 'prod_ccbscf'

driver = webdriver.Ie()
corp_url = "test4.ccbscf.com/"
biz_url =  "test4.ccbscf.com/biz/"
# # 窗口最大化
driver.maximize_window()

class Test_Page_1():
    def exec_5528(self,credit_no):

        # 设置 voucher_no
        v_no = "jkcs1533887171891"+str(random.randint(1000, 9999))
        ccbs = "depo1533887171891" + str(random.randint(1000, 9999))
        serial = 99999 + random.randint(10, 1000)

        #查询企业编号、企业名称、合同、是否是贷转存、品牌号  t_ebs_financing
        co = Test_Page().Oracle_link('T4',
             "select FK_CORP, CORP_NAME, CONTRACT_CODE,IS_LOAN_TRANSFER_DEPOSIT,MARKETING_BRAND\
              from %s.t_ebs_financing  WHERE fk_credit = '%s'" % (Env, credit_no), 0, 100)
        print("该白条的链条企业用户编号是"+co[0][0]+",链条企业名字是"+co[0][1]+",合同编号是"+co[0][2])

        # 查询链条企业的账号，因为如果是贷转存，放款到企业账号内  t_account
        account_code = Test_Page().Oracle_link('T4',
             "select account_code from %s.t_account  where account_name = (select \
             corp_name from %s.t_ebs_financing  where fk_credit = '%s' \
             and account_type = 'BC')"% (Env,Env, credit_no), 0, 100)

        # 查询过渡户，即95533  T_ACCOUNT 表
        bamt = Test_Page().Oracle_link('T4',
             "select t.account_code from %s.T_ACCOUNT t where t.remark = '过渡户'"% (Env), 0, 100)

        # 查询代发工资账户，即类型为CFA的账户
        cfa = Test_Page().Oracle_link('T4',
             "select t.ACCOUNT_CODE from %s.t_account t where t.pk_account IN (select o.fk_account from \
             %s.t_account_owner o where o.FK_USER_OWNER = (select fk_corp from %s.t_ebs_financing \
             where fk_credit = '%s')) AND t.account_type = 'CPA'"% (Env,Env,Env,credit_no), 0, 100)

        # 查询 t_credit 表，判断是否是代发工资，查询付款日期、金额、以及白条类型BUSI_TYPE
        rs = Test_Page().Oracle_link('T4',
           "select MATURITY_DATE,MATURITY_AMOUNT,BUSI_TYPE from %s.t_credit  WHERE pk_credit \
           = '%s'"%(Env,credit_no), 0, 100)
        print(rs[0][2])

        #查询账单个数
        c_depo = Test_Page().Oracle_link('T4',
           "select count(distinct(t.fk_bill)) from %s.t_price_fee_plan t where t.fk_price_snapshot_detail in \
            (select t2.pk_snapshot_detail from %s.T_PRICE_SNAPSHOT_DETAIL t2 where t2.fk_snapshot in \
            (select t1.pk_snapshot from %s.T_PRICE_SNAPSHOT t1 where t1.fk_credit='%s')) and \
            t.trade_state = 'DONE' and t.is_paid = '0'"%(Env,Env,Env,credit_no), 0, 100)
        print(c_depo[0][0])

        #判断 5528 中 t_ebs_drawdown 是否有数据
        c_ebs = Test_Page().Oracle_link('T4',
           "select COUNT(*) from %s.T_EBS_DRAWDOWN e  WHERE e.fk_credit = '%s'"%(Env,credit_no), 0, 100)
        print(c_ebs[0][0])

        # 插入融资进度voucher_no
        Test_Page().Oracle_insert('T4',
            "UPDATE %s.t_ebs_financing  SET voucher_no = '%s' WHERE fk_credit \
            = '%s'" % (Env, v_no, credit_no))

        # 格式转换，需要将查出的 datetime.datetime 类型转换成 str 类型才可以传给 t_ebs_drawdown 使用
        c_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        new_format = datetime.datetime.strptime(c_date, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
        print(c_date)
        print(new_format)
        print(rs[0][2], rs[0][0], rs[0][1])
        maturity = rs[0][0].strftime("%Y-%m-%d")
        print(type(rs[0][0]))
        print(rs[0][0])
        print(type(maturity))
        print(maturity)
        print(type(new_format))

        # 如果是代发工资条，则 BUSI_TYPE 为 PAYROLL_CREDIT  比如cfa 写成CFA 就会提示 ‘列在此处不允许’ ，%s 尽量加引号
        if c_ebs[0][0] == 0:
            if rs[0][2] == 'PAYROLL_CREDIT':
                print("白条 " + credit_no + " 是代发工资条")
                Test_Page().Oracle_insert('T4',
                  "insert into %s.t_ebs_drawdown (SEQUENCE_NO, PK_SERIAL, FK_CORP, CORP_NAME, CONTRACT_CODE,\
                  CURRENCY,FK_CREDIT, MATURITY_DATE, LOAN_AMOUNT_PLAN, LOAN_AMOUNT, LOAN_TIME,IS_RELATED_LOAN_DETAILS, \
                  IS_LOAN_SUCCESSFUL, FAIL_REASON, VOUCHER_NO,DRAWDOWN_CODE, IS_RELATED_FINANCING_PROCESS,\
                  IS_LOAN_TRANSFER_DEPOSIT,INNER_ACCOUNT_CODE, MARKETING_BRAND, LOAN_TO_DEPOSIT_CUST_ACC_CODE,\
                  LOAN_TO_DEPOSIT_CUST_ACC_TYPE, FREEZE_AFFAIR_SERIAL_NUMBER, SALABLE_PRODUCT_CODE)\
                  values (%s.seq_t_ebs_drawdown.nextval, '%s', '%s', '%s','%s', '156', '%s', to_date('%s','yyyy-mm-dd'),\
                  %s, %s, to_date('%s','yyyy-mm-dd'),'0', '1', null, '%s',%s.seq_t_ebs_drawdown.nextval, '1',\
                  '1', null, '%s', '%s', '09', '1', '1111')" % (Env, Env, serial, co[0][0], co[0][1],
                  co[0][2],credit_no, maturity, rs[0][1], rs[0][1], new_format, v_no, Env,co[0][4],cfa[0][0]))

            elif rs[0][2] == 'STANDARD':
                print("白条 " + credit_no + " 不是代发工资条")

                #明确不是代发工资条之后，再判断是不是贷转存
                is_d = Test_Page().Oracle_link('T4',
                     "select t.IS_LOAN_TRANSFER_DEPOSIT from %s.t_ebs_financing t where t.fk_credit = %s" % (Env, credit_no), 0, 100)
                print(is_d[0][0])

                if is_d[0][0] == '1':
                    print("白条 " + credit_no + " 是贷转存条")
                    Test_Page().Oracle_insert('T4',
                      "insert into %s.t_ebs_drawdown (SEQUENCE_NO, PK_SERIAL, FK_CORP, CORP_NAME, CONTRACT_CODE,\
                      CURRENCY,FK_CREDIT, MATURITY_DATE, LOAN_AMOUNT_PLAN, LOAN_AMOUNT, LOAN_TIME,IS_RELATED_LOAN_DETAILS, \
                      IS_LOAN_SUCCESSFUL, FAIL_REASON, VOUCHER_NO,DRAWDOWN_CODE, IS_RELATED_FINANCING_PROCESS,\
                      IS_LOAN_TRANSFER_DEPOSIT,INNER_ACCOUNT_CODE, MARKETING_BRAND, LOAN_TO_DEPOSIT_CUST_ACC_CODE,\
                      LOAN_TO_DEPOSIT_CUST_ACC_TYPE, FREEZE_AFFAIR_SERIAL_NUMBER, SALABLE_PRODUCT_CODE)\
                      values (%s.seq_t_ebs_drawdown.nextval, '%s', '%s', '%s','%s', '156', '%s', to_date('%s','yyyy-mm-dd'),\
                      %s, %s, to_date('%s','yyyy-mm-dd'),'0', '1', null, '%s',%s.seq_t_ebs_drawdown.nextval, '1',\
                      '1', null, '%s', '%s', '01', '0', '00112939')" % (Env, Env, serial, co[0][0],
                      co[0][1],co[0][2],credit_no, maturity, rs[0][1], rs[0][1], new_format, v_no, Env,co[0][4],account_code[0][0]))

                    # 插入 mongodb 流水，是为了账单的自动匹配, accout-detail 插流水

                    post_data = \
                        {
                            "_id": credit_no,
                            "_class": "com.ccbscf.biz.payment.mongo.model.DepositFeeFeedbackInfoDO",
                            "serialNo": serial,
                            "corpName": co[0][1],  # 链条企业名称
                            "corpOrgCode": "43843937-9",
                            "coreOrgCode": "21478012-9",
                            "contractId": "RZBH110660000201900243",
                            "feeAmount": "381.63",
                            "tradeTime": parser.parse("2019-06-28T12:50:41.000Z"),
                            "feeAccountCode": account_code[0][0],
                            "expdtrId": "ZXZY110660000201900600",
                            "feeSuccess": 'true',
                            "vchrNo": "CS22440000000000896",
                            "feeReceiverAccountCode": bamt[0][0],
                            "receivableMgtFee": "0",
                            "processState": "WAIT",
                            "createTime": parser.parse("2019-04-29T07:58:33.626Z"),
                            "ccbEBankSerial": ccbs
                        }

                    Test_Page().Mongodb('T4', 'ccbscf-biz-payment', 'depositFeeFeedbackInfoDO', post_data)


                #对于普通白条
                elif is_d[0][0] != '1':
                    print("白条 " + credit_no + " 是普通条")
                    Test_Page().Oracle_insert('T4',
                        "insert into prod_ccbscf.T_EBS_DRAWDOWN(SEQUENCE_NO, PK_SERIAL, FK_CORP, CORP_NAME, CONTRACT_CODE,\
                        CURRENCY,FK_CREDIT, MATURITY_DATE, LOAN_AMOUNT_PLAN, LOAN_AMOUNT, LOAN_TIME,IS_RELATED_LOAN_DETAILS, \
                        IS_LOAN_SUCCESSFUL, FAIL_REASON, VOUCHER_NO,DRAWDOWN_CODE, IS_RELATED_FINANCING_PROCESS,\
                        IS_LOAN_TRANSFER_DEPOSIT,INNER_ACCOUNT_CODE, MARKETING_BRAND, LOAN_TO_DEPOSIT_CUST_ACC_CODE,\
                        LOAN_TO_DEPOSIT_CUST_ACC_TYPE, FREEZE_AFFAIR_SERIAL_NUMBER, SALABLE_PRODUCT_CODE)\
                        values(%s.seq_t_ebs_drawdown.nextval, '%s', '%s', '%s','%s', '156', '%s', to_date('%s', 'dd-mm-yyyy'),\
                            %s, %s, to_date(SYSDATE(), 'dd-mm-yyyy'), '1', '1', null, '%s','%s.seq_t_ebs_drawdown.nextval', '1',\
                            '0', null, '%s', '%s', '01', '0', '00112939')"
                        % (Env, serial, co[0][0], co[0][1], co[0][2], credit_no,rs[0][0],rs[0][1],rs[0][1], v_no,Env,co[0][4],bamt[0][0]))

            elif c_ebs[0][0] == 1:
                print("该白条"+credit_no + "已经有放款反馈信息")

    def match(self,credit_no):

        # 设置 voucher_no
        v_no = "jkcs1533887171891"+str(random.randint(1000, 9999))
        ccbs = "depo1533887171891" + str(random.randint(1000, 9999))
        serial = 99999 + random.randint(10, 1000)

        #查询企业编号、企业名称、合同、是否是贷转存、品牌号  t_ebs_financing
        co = Test_Page().Oracle_link('T4',
             "select FK_CORP, CORP_NAME, CONTRACT_CODE,IS_LOAN_TRANSFER_DEPOSIT,MARKETING_BRAND\
              from %s.t_ebs_financing  WHERE fk_credit = '%s'" % (Env, credit_no), 0, 100)
        print("该白条的链条企业用户编号是"+co[0][0]+",链条企业名字是"+co[0][1]+",合同编号是"+co[0][2])

        # 查询链条企业的账号，因为如果是贷转存，放款到企业账号内  t_account
        account_code = Test_Page().Oracle_link('T4',
             "select account_code from %s.t_account  where account_name = (select \
             corp_name from %s.t_ebs_financing  where fk_credit = '%s' \
             and account_type = 'BC')"% (Env,Env, credit_no), 0, 100)

        # 查询过渡户，即95533  T_ACCOUNT 表
        bamt = Test_Page().Oracle_link('T4',
             "select t.account_code from %s.T_ACCOUNT t where t.remark = '过渡户'"% (Env), 0, 100)

        # 查询缴费户，即 398  T_ACCOUNT 表
        bamf = Test_Page().Oracle_link('T4',
             "select t.account_name,t.account_code from %s.T_ACCOUNT t where t.remark = '缴费户'"% (Env), 0, 100)

        # 查询代发工资账户，即类型为CFA的账户
        cfa = Test_Page().Oracle_link('T4',
             "select t.ACCOUNT_CODE from %s.t_account t where t.pk_account IN (select o.fk_account from \
             %s.t_account_owner o where o.FK_USER_OWNER = (select fk_corp from %s.t_ebs_financing \
             where fk_credit = '%s')) AND t.account_type = 'CPA'"% (Env,Env,Env,credit_no), 0, 100)

        # 查询 t_credit 表，判断是否是代发工资，查询付款日期、金额、以及白条类型BUSI_TYPE
        rs = Test_Page().Oracle_link('T4',
           "select MATURITY_DATE,MATURITY_AMOUNT,BUSI_TYPE from %s.t_credit  WHERE pk_credit \
           = '%s'"%(Env,credit_no), 0, 100)
        print(rs[0][2])

        #查询账单个数
        c_depo = Test_Page().Oracle_link('T4',
           "select count(distinct(t.fk_bill)) from %s.t_price_fee_plan t where t.fk_price_snapshot_detail in \
            (select t2.pk_snapshot_detail from %s.T_PRICE_SNAPSHOT_DETAIL t2 where t2.fk_snapshot in \
            (select t1.pk_snapshot from %s.T_PRICE_SNAPSHOT t1 where t1.fk_credit='%s')) and \
            t.trade_state = 'DONE' and t.is_paid = '0'"%(Env,Env,Env,credit_no), 0, 100)
        print(c_depo[0][0])

        # 查询 mongodb 数据库,该白条下对应的账单
        rs_m = Test_Page().Mongodb_link('T4', 'ccbscf-biz-payment', 'billInfoDO',
            {"creditDetails.fkCredit": 'BMYY-20190705-004-000001'},
            {"_id": 1, "loanTransferDepositBill": 1, "creditDetails.feeAmount": 1,"corpName":1})
        print(rs_m)
        print(rs_m[0]['_id'])
        # rs_m[0]['creditDetails'][0]['feeAmount'] 为账单需缴金额
        print(rs_m[0]['loanTransferDepositBill'])
        print(rs_m[0]['creditDetails'][0]['feeAmount'])
        print(rs_m[1]['creditDetails'][0]['feeAmount'])

        # 格式转换，需要将查出的 datetime.datetime 类型转换成 str 类型才可以传给 t_ebs_drawdown 使用
        c_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        new_format = datetime.datetime.strptime(c_date, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
        print(c_date)
        print(new_format)
        print(rs[0][2], rs[0][0], rs[0][1])
        maturity = rs[0][0].strftime("%Y-%m-%d")
        print(type(rs[0][0]))
        print(rs[0][0])
        print(type(maturity))
        print(maturity)
        print(type(new_format))

        # 如果是代发工资条，则 BUSI_TYPE 为 PAYROLL_CREDIT  比如cfa 写成CFA 就会提示 ‘列在此处不允许’ ，%s 尽量加引号
        if c_depo[0][0] >= 0:
            if rs[0][2] == 'PAYROLL_CREDIT':
                print("白条 " + credit_no + " 是代发工资条")
                Test_Page().Oracle_insert('T4',
                  "insert into %s.t_account_detail (SEQUENCE_NO, PK_DETAIL, FK_ACCOUNT, ACCOUNT_CODE, ACCOUNT_NAME,\
                   BANK_NAME, FK_ACCOUNT_CP, ACCOUNT_CODE_CP, ACCOUNT_NAME_CP, BANK_NAME_CP, ACCOUNT_DIRECTION, CURRENCY, \
                   AMOUNT, TRADE_TIME, CCBSCF_TIME, CCBSCF_BANK_NAME,CCBSCF_BANK_DATE, CCBSCF_BANK_SERIAL_NO, \
                   CCBSCF_BANK_RESPONSE_CODE, BALANCE, TRADE_TYPE, REMARK, IS_PROCESSED, SUMMARY, SUMMARY_CODE, CNAPS_CODE_CP,\
                   AMOUNT_AVAILABLE,CUSTOMER_SERIAL_NO,STATUS_REFUND)\
                   values (%s.seq_t_account_detail.nextval, sys_guid(), '837a763d-426a-48f2-b9e7-748d041e0e75', \
                           '%s', '%s','CCB', null, '20181011000001', '%s', '建行北京兴融支行', \
                           'CR', '156', '${pay_amount_1}', to_date('20-06-2019 16:20:25', 'dd-mm-yyyy hh24:mi:ss'), \
                           to_date('10-11-2017 18:42:20', 'dd-mm-yyyy hh24:mi:ss'), null, to_date('14-02-2018 16:20:25', \
                           'dd-mm-yyyy hh24:mi:ss'), sys_guid(), null,1223493.16, 'OTHER', '测试插入数据', '0', null, '123456',\
                           null,'${pay_amount_1}',null,'UNREFUND')" % (Env, Env,bamf[0][1],bamf[0][0],rs_m[0]['corpName']))

            elif rs[0][2] == 'STANDARD':
                print("白条 " + credit_no + " 不是代发工资条")

                #明确不是代发工资条之后，再判断是不是贷转存
                is_d = Test_Page().Oracle_link('T4',
                     "select t.IS_LOAN_TRANSFER_DEPOSIT from %s.t_ebs_financing t where t.fk_credit = %s" % (Env, credit_no), 0, 100)
                print(is_d[0][0])
                is_dd = Test_Page().Mongodb_link()

                if is_d[0][0] == '1':
                    print("白条 " + credit_no + " 是贷转存条")
                    Test_Page().Oracle_insert('T4',
                      "insert into %s.t_ebs_drawdown (SEQUENCE_NO, PK_SERIAL, FK_CORP, CORP_NAME, CONTRACT_CODE,\
                      CURRENCY,FK_CREDIT, MATURITY_DATE, LOAN_AMOUNT_PLAN, LOAN_AMOUNT, LOAN_TIME,IS_RELATED_LOAN_DETAILS, \
                      IS_LOAN_SUCCESSFUL, FAIL_REASON, VOUCHER_NO,DRAWDOWN_CODE, IS_RELATED_FINANCING_PROCESS,\
                      IS_LOAN_TRANSFER_DEPOSIT,INNER_ACCOUNT_CODE, MARKETING_BRAND, LOAN_TO_DEPOSIT_CUST_ACC_CODE,\
                      LOAN_TO_DEPOSIT_CUST_ACC_TYPE, FREEZE_AFFAIR_SERIAL_NUMBER, SALABLE_PRODUCT_CODE)\
                      values (%s.seq_t_ebs_drawdown.nextval, '%s', '%s', '%s','%s', '156', '%s', to_date('%s','yyyy-mm-dd'),\
                      %s, %s, to_date('%s','yyyy-mm-dd'),'0', '1', null, '%s',%s.seq_t_ebs_drawdown.nextval, '1',\
                      '1', null, '%s', '%s', '01', '0', '00112939')" % (Env, Env, serial, co[0][0],
                      co[0][1],co[0][2],credit_no, maturity, rs[0][1], rs[0][1], new_format, v_no, Env,co[0][4],account_code[0][0]))

                    # 插入 mongodb 流水，是为了账单的自动匹配, accout-detail 插流水

                    post_data = \
                        {
                            "_id": credit_no,
                            "_class": "com.ccbscf.biz.payment.mongo.model.DepositFeeFeedbackInfoDO",
                            "serialNo": serial,
                            "corpName": co[0][1],  # 链条企业名称
                            "corpOrgCode": "43843937-9",
                            "coreOrgCode": "21478012-9",
                            "contractId": "RZBH110660000201900243",
                            "feeAmount": "381.63",
                            "tradeTime": parser.parse("2019-06-28T12:50:41.000Z"),
                            "feeAccountCode": account_code[0][0],
                            "expdtrId": "ZXZY110660000201900600",
                            "feeSuccess": 'true',
                            "vchrNo": "CS22440000000000896",
                            "feeReceiverAccountCode": bamt[0][0],
                            "receivableMgtFee": "0",
                            "processState": "WAIT",
                            "createTime": parser.parse("2019-04-29T07:58:33.626Z"),
                            "ccbEBankSerial": ccbs
                        }

                    Test_Page().Mongodb('T4', 'ccbscf-biz-payment', 'depositFeeFeedbackInfoDO', post_data)




                #对于普通白条
                elif is_d[0][0] != '1':
                    print("白条 " + credit_no + " 是普通条")
                    Test_Page().Oracle_insert('T4',
                        "insert into prod_ccbscf.T_EBS_DRAWDOWN(SEQUENCE_NO, PK_SERIAL, FK_CORP, CORP_NAME, CONTRACT_CODE,\
                        CURRENCY,FK_CREDIT, MATURITY_DATE, LOAN_AMOUNT_PLAN, LOAN_AMOUNT, LOAN_TIME,IS_RELATED_LOAN_DETAILS, \
                        IS_LOAN_SUCCESSFUL, FAIL_REASON, VOUCHER_NO,DRAWDOWN_CODE, IS_RELATED_FINANCING_PROCESS,\
                        IS_LOAN_TRANSFER_DEPOSIT,INNER_ACCOUNT_CODE, MARKETING_BRAND, LOAN_TO_DEPOSIT_CUST_ACC_CODE,\
                        LOAN_TO_DEPOSIT_CUST_ACC_TYPE, FREEZE_AFFAIR_SERIAL_NUMBER, SALABLE_PRODUCT_CODE)\
                        values(%s.seq_t_ebs_drawdown.nextval, '%s', '%s', '%s','%s', '156', '%s', to_date('%s', 'dd-mm-yyyy'),\
                            %s, %s, to_date(SYSDATE(), 'dd-mm-yyyy'), '1', '1', null, '%s','%s.seq_t_ebs_drawdown.nextval', '1',\
                            '0', null, '%s', '%s', '01', '0', '00112939')"
                        % (Env, serial, co[0][0], co[0][1], co[0][2], credit_no,rs[0][0],rs[0][1],rs[0][1], v_no,Env,co[0][4],bamt[0][0]))

            elif c_ebs[0][0] == 1:
                print("该白条"+credit_no + "已经有放款反馈信息")

    #xxl_job 定时任务执行
    def xxl_job(self,xxl_env,xxl_group,xxl_job):
        # T1环境
        if xxl_env == 'T1':
            driver.get("http://12.0.216.155:28080/xxl-job-admin/toLogin")


        # T2环境
        elif xxl_env == 'T2':
            driver.get("http://12.0.216.145:28080/xxl-job-admin/toLogin")

        # T4环境
        elif xxl_env == 'T4':
            driver.get("http://12.0.216.196:28080/xxl-job-admin/toLogin")

        # 手动添加 cookie
        driver.add_cookie(
            {
                'name': 'XXL_JOB_LOGIN_IDENTITY',
                'value': '6333303830376536353837616465323835626137616465396638383162336437'
            }
        )
        sleep(2)
        driver.refresh()

        # 执行定时任务组
        if xxl_group == '支付结算':
            driver.get("http://12.0.216.196:28080/xxl-job-admin/jobinfo?jobGroup=10")
        elif xxl_group == '价格服务':
            driver.get("http://12.0.216.196:28080/xxl-job-admin/jobinfo?jobGroup=11")
        elif xxl_group == '白条服务':
            driver.get("http://12.0.216.196:28080/xxl-job-admin/jobinfo?jobGroup=6")

        #执行定时任务
        sleep(1)
        if xxl_job == '代发工资白条匹配处理':
            driver.find_element_by_xpath('//*[@id="86"]/button[1]').click()
        elif xxl_job == '放款批量':
            driver.find_element_by_xpath('//*[@id="48"]/button[1]').click()
        elif xxl_job == '建行放款匹配':
            driver.find_element_by_xpath('//*[@id="job_list_paginate"]/ul/li[3]/a').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="46"]/button[1]').click()
        elif xxl_job == '账单的自动匹配':
            driver.find_element_by_xpath('//*[@id="job_list_paginate"]/ul/li[3]/a').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="41"]/button[1]').click()
        elif xxl_job == '根据反馈结果更新融资进度状态任务':
            driver.find_element_by_xpath('//*[@id="69"]/button[1]').click()
        elif xxl_job == '推送账单服务':
            driver.find_element_by_xpath('//*[@id="42"]/button[1]').click()
        elif xxl_job == '确认账单服务':
            driver.find_element_by_xpath('//*[@id="43"]/button[1]').click()
        #第一个定位是点击执行确认执行，第二个定位是执行成功后弹出的执行成功弹框，都是点击确定按钮
        driver.find_element_by_xpath("//div[@class='layui-layer-btn layui-layer-btn-']/"
             "a[@class='layui-layer-btn0']").click()
        sleep(2)
        driver.find_element_by_xpath("//div[@class='layui-layer-btn layui-layer-btn-']/"
             "a[@class='layui-layer-btn0']").click()

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

        # # 获取打开的多个窗口句柄
        # windows = driver.window_handles
        # # 切换到当前最新打开的窗口
        # driver.switch_to.window(windows[-1])

        # js = 'document.getElementsByClassName("ivu-btn ivu-btn-primary")[0].click();'
        # driver.execute_script(js)
        driver.find_element_by_css_selector("[class='ivu-btn ivu-btn-primary']").click()
        # driver.find_element_by_link_text('确认').click()
        sleep(2)

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



#关于数据库的一些操作，其中 Oracle_link 是关于 oracle 连接的，

# Oracle 使用cursor进行各种操作   释放cursor   self._DelCursor(cur)
    def Oracle_link(self,env,sql,nStart=0 , nNum=- 1):

        #连接数据库
        import cx_Oracle
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
    # oracle 新增、更新数据
    def Oracle_insert(self,env,sql):

        #连接数据库
        import cx_Oracle
        #查询数据库
        if env == 'T1':
            conn = cx_Oracle.connect('t_updscf/000000@12.0.216.142:1523/jxrtest')
        elif env == 'T2':
            conn = cx_Oracle.connect('t2_updscf/000000@12.0.216.142:1523/jxrtest')
        elif env == 'T4':
            conn = cx_Oracle.connect('P_DUBAOPING/IZWZrw7#@12.0.216.136:1523/jxr2p')
        cur = conn.cursor()
        # 查询到列表
        cur.execute(sql)
        conn.commit()
        
        cur.close()
        conn.close()

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
    def Mongodb(self, env, db, collection, sql):
        import pymongo
        if env == 'T1':
            client = pymongo.MongoClient("mongodb://12.0.216.155:27017")
        elif env == 'T2':
            client = pymongo.MongoClient("mongodb://12.0.216.145:27017")
        # 针对集群
        elif env == 'T4':
            # myclient = pymongo.MongoClient("mongodb://12.0.216.30:37017")
            client = pymongo.MongoClient('mongodb://ccbscf_app:mcsa2jxrtT#@12.0.216.30:37017')
        # 选择数据库
        mydb = client[db]
        # 查询缴费凭证表
        mycol = mydb[collection]
        result = []
        # 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。，查询条件已经默认是0
        for x in mycol.insert(sql):
            # print(x)
            # print(x['billAmount'])
            result.append(x)
        return result

    def Mongodb_count(self, env, db, collection, sql):
        import pymongo
        if env == 'T1':
            client = pymongo.MongoClient("mongodb://12.0.216.155:27017")
        elif env == 'T2':
            client = pymongo.MongoClient("mongodb://12.0.216.145:27017")
        # 针对集群
        elif env == 'T4':
            # myclient = pymongo.MongoClient("mongodb://12.0.216.30:37017")
            client = pymongo.MongoClient('mongodb://ccbscf_app:mcsa2jxrtT#@12.0.216.30:37017')
        # 选择数据库
        mydb = client[db]
        # 查询缴费凭证表
        mycol = mydb[collection]
        result = []
        # 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。，查询条件已经默认是0
        # 用 range 是为了解决 list 中'int' object is not iterable
        # Python写循环程序的时候遇到 TypeError: ‘int’ object is not iterable，原因是循环中使用的应该是一组数。
        for x in range(mycol.count(sql)):
            # print(x)
            # print(x['billAmount'])
            result.append(x)
        return result

    if __name__ == 'main':
        driver.quit()
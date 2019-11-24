from interface.test_interface import *

#test_interface().Interface({"jobGroup":'10'},'http://12.0.216.196:28080/xxl-job-admin/jobinfo/pageList')

#test_interface().Interface({'id':'41'},'http://12.0.216.196:28080/xxl-job-admin/jobinfo/trigger')

test_interface().Interface_biz('T1',{},'http://test1.ccbscf.com/api/web/biz/v1/match/bills/list')
# oracle 插入
# env = 'prod_ccbscf'
# credit_no = 'DFGZEXT-20190215-005-000001'
# co = Test_Page().Oracle_link('T4',
#      "select t.SUMMARY_CODE from %s.t_account_detail t where t.pk_detail = '88b599f6-8ae9-43ae-bbd4-5b1e277d8a8d'" % (env), 0, 100)
#
# Test_Page().Oracle_insert('T4',
#   "insert into %s.t_account_detail (SEQUENCE_NO, PK_DETAIL, FK_ACCOUNT, ACCOUNT_CODE, ACCOUNT_NAME, BANK_NAME, FK_ACCOUNT_CP,\
#  ACCOUNT_CODE_CP, ACCOUNT_NAME_CP, BANK_NAME_CP, ACCOUNT_DIRECTION, CURRENCY, AMOUNT, TRADE_TIME, CCBSCF_TIME, CCBSCF_BANK_NAME,\
#   CCBSCF_BANK_DATE, CCBSCF_BANK_SERIAL_NO, CCBSCF_BANK_RESPONSE_CODE, BALANCE, TRADE_TYPE, REMARK, IS_PROCESSED, SUMMARY, SUMMARY_CODE, CNAPS_CODE_CP)\
# values (%s.seq_t_account_detail.nextval, sys_guid(), '837a763d-426a-48f2-b9e7-748d041e0e75', '11001085200059507029-100010', '鱼香茄子',\
#  'CCB', null, '20181011000001', '鱼香茄子', '建行北京兴融支行', 'CR', '156', 3500, to_date('11-01-2018 16:20:25', 'dd-mm-yyyy hh24:mi:ss'),\
#   to_date('10-11-2017 18:42:20', 'dd-mm-yyyy hh24:mi:ss'), null, to_date('05-05-2019 16:20:25', 'dd-mm-yyyy hh24:mi:ss'),'1100012010N7Python',\
#  null,1223493.16, 'OTHER', '测试插入数据', '0', null, '%s', null)"% (env,env,co[0][0]))
# print(co[0][0])
# print("打印成功")

# c_date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# new_format = datetime.datetime.strptime(c_date, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
# print(c_date)
# print(new_format)
#
# credit_no = 'DFGZEXT-20190215-005-000001'
# co = Test_Page().Oracle_link('T4',
#              "select FK_CORP, CORP_NAME, CONTRACT_CODE from %s.t_ebs_financing  WHERE\
#              fk_credit = '%s'" % (Env, credit_no), 0, 100)
#
# print("该白条的链条企业用户编号是"+co[0][0]+",链条企业名字是"+co[0][1]+",合同编号是"+co[0][2])
#
# # 设置 voucher_no
# v_no = "jkcs1533887171891"+str(random.randint(1000, 9999))
# serial = 999999 + random.randint(1, 100)
# # 判断是否是代发工资
# rs = Test_Page().Oracle_link('T4',
#    "select MATURITY_DATE,MATURITY_AMOUNT,BUSI_TYPE from %s.t_credit  WHERE pk_credit \
#    = '%s'"%(Env,credit_no), 0, 100)
#
# # 格式转换，需要将查出的 datetime.datetime 类型转换成 str 类型才可以传给 t_ebs_drawdown 使用
# print(rs[0][2],rs[0][0],rs[0][1])
# MATURITY_DATE = rs[0][0].strftime("%Y-%m-%d")
# print(type(rs[0][0]))
# print (rs[0][0])
# print(type(MATURITY_DATE))
# print(MATURITY_DATE)
#
# print(type(new_format))
#
# Test_Page().Oracle_insert('T4',
#     "UPDATE %s.t_ebs_financing  SET voucher_no = '%s' WHERE fk_credit \
#     = '%s'" % (Env, v_no, credit_no))
#
# #如果是代发工资   TO_DATE(to_timestamp('"+lastDate+"','%%Y-%%m-%%d %%H:%%M:%%S')
# if rs[0][2] == 'PAYROLL_CREDIT':
#     print("白条 "+credit_no+" 是代发工资条")
#     #select to_date('2009-12-25 14:23:31','yyyy-mm-dd,hh24:mi:ss') from dual  取时间   ('27-06-2019 18:42:20', 'dd-mm-yyyy hh24:mi:ss')
#     Test_Page().Oracle_insert('T4',
#         "insert into %s.t_ebs_drawdown (SEQUENCE_NO, PK_SERIAL, FK_CORP, CORP_NAME, CONTRACT_CODE,\
#         CURRENCY,FK_CREDIT, MATURITY_DATE, LOAN_AMOUNT_PLAN, LOAN_AMOUNT, LOAN_TIME,IS_RELATED_LOAN_DETAILS, \
#         IS_LOAN_SUCCESSFUL, FAIL_REASON, VOUCHER_NO,DRAWDOWN_CODE, IS_RELATED_FINANCING_PROCESS,\
#         IS_LOAN_TRANSFER_DEPOSIT,INNER_ACCOUNT_CODE, MARKETING_BRAND, LOAN_TO_DEPOSIT_CUST_ACC_CODE,\
#         LOAN_TO_DEPOSIT_CUST_ACC_TYPE, FREEZE_AFFAIR_SERIAL_NUMBER, SALABLE_PRODUCT_CODE)\
#         values (%s.seq_t_ebs_drawdown.nextval, '%s', '%s', '%s','%s', '156', '%s', to_date('%s','yyyy-mm-dd'),\
#         %s, %s, to_date('%s','yyyy-mm-dd'),'0', '1', null, '%s',%s.seq_t_ebs_drawdown.nextval, '1',\
#         '1', null, 'MB00013', '13001635208050503076', '01', '4', '10266090')"% (Env,Env,serial,co[0][0],co[0][1],co[0][2],
#         credit_no,MATURITY_DATE,rs[0][1],rs[0][1],new_format,v_no,Env))

# mongodb 插入
# print(type(decimal.Decimal("381.63")))
#
# post_data = \
#     {
#         "_id": "GZMTGS-20199999-005-000001",
#         "_class": "com.ccbscf.biz.payment.mongo.model.DepositFeeFeedbackInfoDO",
#         "serialNo": "188000",
#         "corpName": 'KY测试企业幺幺',  # 核心企业名称
#         "corpOrgCode": "43843937-9",
#         "coreOrgCode": "21478012-9",
#         "contractId": "RZBH110660000201900243",
#         "feeAmount": float(decimal.Decimal("381.63")),
#         "tradeTime": parser.parse("2019-06-28T12:50:41.000Z"),
#         "feeAccountCode": "42250133240100000070",
#         "expdtrId": "ZXZY110660000201900600",
#         "feeSuccess": 'true',
#         "vchrNo": "CS22440000000000896",
#         "feeReceiverAccountCode": "11001085200059507029-100010",
#         "receivableMgtFee": "0",
#         "processState": "WAIT",
#         "createTime": parser.parse("2019-04-29T07:58:33.626Z"),
#         "ccbEBankSerial": "1100003010NAP0IP777"
#     }
#
# Test_Page().Mongodb('T4', 'ccbscf-biz-payment', 'depositFeeFeedbackInfoDO', post_data)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import subprocess
import datetime


def date():
    now_date = datetime.date.today()
    goal_date = now_date+datetime.timedelta(1)
    return goal_date

def comp(commond):
    i = 0
    res_att = subprocess.Popen(commond, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = res_att.stdout.readlines()
    for lines in result:
        i = i+1
        if i == len(result):
            look_data = lines
    print(look_data)
    print(type(look_data))
    look_result = look_data.find("success")
    return look_result

if __name__ == '__main__':
    #d = raw_input("请输日目标日期: ")

    #goal = date()
    currentDate = input("please input the date:")
    goalDate = datetime.datetime.strptime(currentDate, "%Y-%m-%d").date()
    pre_goal = goalDate + datetime.timedelta(days=-1)
    pre_goal_str = pre_goal.strftime('%Y%m%d')
    goal_str = goalDate.strftime('%Y%m%d')
    #string_date = "date -s " + str(goal)
    # os.system(string_date)
    #print(string_goal)
    #string_closed = r"/home/byxf-sch/jetty/smyx-scheduler-core/bin/stop.sh"
    #关闭集群调度任务
    #string_start = r"/home/byxf-sch/jetty/smyx-scheduler-core/bin/start.sh"
    #开启集群调度任务

    #os.system(string_closed)

    #执行acs 传参数
    control_sp = [
        r"ChannelCompensateHandler",
        r"changeTransDateHandler0",
        r"acsRepayDayEndProcessHandler0",
        r"accrualOfInterestCapitalHandler0 0000000000",
        r"accrualInterestNewCapitalHandler0 0000000000",
        r"feeAndIntersetCapitalHandler0 0000000000",
        r"acsRepayPlanStatusHandler0 0000000000",
        r"acsOrderLoanStatusHandler0 0000000000",
        r"loanAndRepayAccountingHandler0 0000000000",
        r"accoutingGeneralFileHandler0 0000000000",

        r"accrualOfInterestCapitalHandler0 1000000001",
        r"accrualInterestNewCapitalHandler0 1000000001",
        r"feeAndIntersetCapitalHandler0 1000000001",
        r"acsRepayPlanStatusHandler0 1000000001",
        r"acsOrderLoanStatusHandler0 1000000001",
        r"loanAndRepayAccountingHandler0 1000000001",
        r"accoutingGeneralFileHandler0 1000000001",

        r"loanOtherHandler0 1000000001",
        r"businessAccountingHandler0 1000000001",
        r"changeAccountDateHandler0",

    ]

    # 执行cts
    control = [
       # r"RepayDayEndProcess",
        r"AccrualInterestNewHandler",
        r"TrxOrderBalanceDayEndProcess",
        r"AccountBalanceDayEndProcess",
        r"CTSLimitDealingHandler",
        r"ctsGetRepayStatusCheckHandler",
        r"ctsRepayPlanStatusHandler",
        r"ctsAccountLoanStatusHandler,ctsOrderLoanStatusHandler",
        r"AccrualOfInterestHandler",
       # r"ctsChannelAccountReconcileHandler",
        r"ctsPersonalAccountInfoSchedule",
        r"ctsChannelAccountInfoSchedule",
        r"ctsAccountCurrDayAmtCheckHandler",
        r"ctsFeeAndIntersetHandler",
        #r"fdpcreateFdpOrderInfoSchedule",
        #r"fdpcreateFdpRepayInfoSchedule",
        #r"fdpdealWithOverduePlanSchedule",
        #r"fdporderSynchSchedule,fdprepayInfoSyncSchedule,fdprepayPlanSynchSchedule,fdpUploadFileHandler",
        #r"fdpCalInterestSchedule",
        r"groupFdpStatisticsInfoSchedule",
        #r"ChannelSettleHandler",
        #r"MerchantSettleHandler",
        r"channelHandFeeCheckAccountHandler",
        r"ctsOrderCheckAccountHandler",
        r"ctsRepayDetailCheckAccountHandler",
        r"ctsUploadChannelFileHandler",
       # r"ComputeRepayAccoutingNewHandler,TrxOrderAccoutingHandler,ComputeRepayAccoutingHandler,AccoutingGeneralFileHandler",
       # r"ComputeRepayAccoutingHandler",
        #r"fdpBusinessAccountFileCreateSchedule",
        r"ctsNeedRepayTipHandler,ctsSmsDetailSendHandler",
        r"channelBailDateTask",
        r"cifPersonalAccountInfoSchedule",
        r"ctsChannelAccountInfoSchedule"
    ]
    # "对公账户信息采集":"ctsChannelAccountInfoSchedule",
    # "对私客户信息采集":"cifPersonalAccountInfoSchedule",
    # "平账AccountReconcileHander": "ctsGetRepayStatusCheckHandler",
    # "还款计划形态转移RepayPlanStatusHandler":"ctsRepayPlanStatusHandler",
    #  "账户形态转移accountLoanStatusHandler":"ctsAccountLoanStatusHandler,ctsOrderLoanStatusHandler",
    #  "利息计提": "AccrualOfInterestHandler",
    # "虚拟账户平账及核对":"ctsChannelAccountReconcileHandler",
    # "对私账户信息采集":"ctsPersonalAccountInfoSchedule",
    # "渠道账户信息采集":"ctsChannelAccountInfoSchedule",
    # "发生额核对AccountCurrDayAmtCheckHandler":"ctsAccountCurrDayAmtCheckHandler",
    # "结息计费FeeAndIntersetHandler":"ctsFeeAndIntersetHandler",
    # "资金方借据生成":"fdpcreateFdpOrderInfoSchedule",
    # "资金方还款记录":"fdpcreateFdpRepayInfoSchedule",
    # "资金方逾期代偿":"fdpdealWithOverduePlanSchedule",
    # "资金方借据文件":"fdporderSynchSchedule,fdprepayInfoSyncSchedule,fdprepayPlanSynchSchedule,fdpUploadFileHandler",
    # "资金方每日计息":"fdpCalInterestSchedule",
    # "资金方入账":"groupFdpStatisticsInfoSchedule",
    # "渠道结算":"ChannelSettleHandler",
    # "商户结算":"MerchantSettleHandler",
    # "渠道手续费对账文件":"channelHandFeeCheckAccountHandler",
    # "渠道放款对账文件":"ctsOrderCheckAccountHandler",
    # "渠道对账-还款明细":"ctsRepayDetailCheckAccountHandler",
    # "渠道对账文件上传任务":"ctsUploadChannelFileHandler",
    # "核算日终":"ComputeRepayAccoutingNewHandler,TrxLimitAcitiveAccountingHandler,TrxOrderAccoutingHandler,ComputeRepayAccoutingHandler,AccoutingGeneralFileHandler",
    # "资金方核算文件生成":"fdpBusinessAccountFileCreateSchedule"
    # "短信调度":"ctsNeedRepayTipHandler,ctsSmsDetailSendHandler",
    # "保证金扣款统计":"channelBailDateTask",
        
    #goal = date()
    #string_today = datetime.date.today().strftime('%Y-%m-%d')
    #string_goal = goal.strftime('%Y-%m-%d')
    #string_date = "date -s " + str(goal)
    string_day = goalDate.strftime('%d')
    #string_backup_date = goal.strftime('%Y%m%d')
    string_backup = r"/root/script/python_b2b/change_service_date/calldump.sh " + pre_goal_str

    try:
        for control_sp_name in control_sp:
            _tmp = control_sp_name.split(" ")
            _tmp_sp_name = _tmp[0]
            _temp_param = ""
            if(_tmp.__len__() > 1):
                _temp_param = _tmp[1]

            string_control_sp = r"java -jar scheduler_run/lib/scheduler-1.0.jar " + _tmp_sp_name + " " + pre_goal_str + " " + _temp_param
            print (string_control_sp)
            look_result_sp = comp(string_control_sp)
            if look_result_sp<0:
                print(string_control_sp + " is failed")

            else:
                print(string_control_sp + " is success")

    except Exception as e:
        print(e)

    #os.system(string_goal)
    time.sleep(5)

    try:
        for control_name in control:
            string_control = r"java -jar scheduler_run/lib/scheduler-1.0.jar " + control_name + " " + goal_str
            print(string_control)
            look_result = comp(string_control)
            print(look_result)
            if look_result<0:
                print(string_control + " is failed")
            else:
                print(string_control + " is success")

    except Exception as e:
        print(e)


    time.sleep(2)
    #os.system(string_backup)
    print(string_backup)

    if string_day == '01':

        string_adjust = 'java -jar scheduler_run/lib/scheduler-1.0.jar rdfOrderInfoHandler,rdfRepayPlan' \
                        'Handler,rdfRepayDetailHandler,rdfProdSubInfoHandler,rdfFeeInfoHandler,' \
                        'rdfMerchantInfoHandler,rdfAgreementInfoHandler,rdfFiveStatusHandler,' \
                        'rdfCrsApplyInfoSchedule,uploadFileHandler'



        look_adjust = comp(string_adjust)
        if look_adjust < 0:
            print(string_adjust + " is failed")
        else:
            print(string_adjust + " is success")

    #os.system(string_start)


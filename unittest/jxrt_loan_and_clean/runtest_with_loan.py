import unittest
#from HTMLTestRunner import HTMLTestRunner

from BSTestRunner import BSTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(latest_report):
    f = open(latest_report,'rb')
    mail_content = f.read()
    f.close()

    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "test_unittest@163.com"  # 用户名
    # 其实是授权码，不是密码
    mail_pass = "jxrttest123"
    sender = 'test_unittest@163.com'

    # 接收邮件的邮箱
    receivers = ['dbaop@163.com','dubaoping@ccbtrust.com.cn']

    subject = 'Web Selenium 自动化测试报告'
    #content = '<html><hl style="color:red">建信融通！</hl></html>'
    message = MIMEText(mail_content, 'html', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = 'A <test_unittest@163.com>'  # 发送者
    message['To'] = ','.join(receivers)  # 接受者

    try:
        smtpObj = smtplib.SMTP()
        # 25 为 smtp 端口号
        smtpObj.connect("smtp.163.com", 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error:无法发送邮件")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    #print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file


# unittest.defaultTestLoader(): defaultTestLoader()类，通过该类下面的discover()方法可自动根据
# 测试目录start_dir匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，
# 因此可以直接通过run()方法执行discover。


if __name__ == '__main__':

    test_dir = './test_login'
    discovery = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    #存放报告的文件夹  ./是当前目录  ../是父级目录    /是根目录
    #report_dir='./test_report'
    report_dir = '../test_report'
    #报告命名时间格式化
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #报告文件完整路径
    report_name = report_dir+'/'+now+'result.html'
    #打开文件在报告文件写入测试结果 stream=f 要写入的文件
    with open(report_name,'wb')as f:
        runner = BSTestRunner(stream=f, title="Test Report", description='Test case result')
        runner.run(discovery)

    f.close()
    #获取最新
    latest_report = latest_report(report_dir)
    #发送邮件
    send_email(latest_report)
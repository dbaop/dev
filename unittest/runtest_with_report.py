import unittest
#from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner
import time

# StartEnd.py ---setup 与 teardown 管理
# calculator.py ---加减法运算方法的实现
# test_add.py --- 加法测试用例
# test_sub.py --- 减法测试用例
# runtest.py  --- 用例执行管理
# test_dir = './' 表示测试的路径是当前路径
# import sys
# sys.path.append('..')
test_dir = './jxrt_acc_ord'
# unittest.defaultTestLoader(): defaultTestLoader()类，通过该类下面的discover()方法可自动根据
# 测试目录start_dir匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，
# 因此可以直接通过run()方法执行discover。
discovery = unittest.defaultTestLoader.discover(test_dir,pattern="*test*.py")

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(discovery)
    #存放报告的文件夹
    report_dir='./test_report'
    #报告命名时间格式化
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #报告文件完整路径
    report_name = report_dir+'/'+now+'result.html'
    #打开文件在报告文件写入测试结果 stream=f 要写入的文件
    with open(report_name,'wb')as f:
        #runner = HTMLTestRunner(stream=f,title="Test Report",description='Test case result')
        runner = BSTestRunner(stream=f, title="Test Report", description='Test case result')
        runner.run(discovery)

    f.close()
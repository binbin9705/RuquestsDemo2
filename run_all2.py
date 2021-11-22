from selenium import webdriver
import time
import unittest
import HTMLTestRunner
from case import test_case1
from case import test_case2
if __name__ == '__main__':
    pass
    # 当前时间
    # now=time.strftime('%Y-%m-%d %H_%M_%S')
    # runner=HTMLTestRunner.HTMLTestRunner(title='自动化测试报告',description='用例执行清空',stream=open(reportpath+'\\'+now+'HTMLReport.html','wb'),verbosity=2)
    # print(suite)
    #自动搜索该模块下所有test开头的测试方法
    # unittest.main()

    # #创建测试套件TestSuite
    # suite=unittest.TestSuite()
    # #添加需要运行的脚本具体到方法addTest
    # suite.addTest(test_case1.Test1('test_01'))
    # suite.addTest(test_case1.Test1('test_02'))
    # #实例化TextTestRunner
    # runner=unittest.TextTestRunner()
    # #使用run方法运行测试套件
    # runner.run(suite)

    # #创建测试套件TestSuite
    # suite=unittest.TestSuite()
    # #添加需要运行的脚本具体到方法addTests
    # suite.addTests([test_case1.Test1('test_01'),test_case1.Test1('test_02'),test_case2.Test2('test_01')])
    # #实例化TextTestRunner
    # runner=unittest.TextTestRunner(verbosity=2)
    # #使用run方法运行测试套件
    # runner.run(suite)


    #使用defaultTestLoader discover方法查找测试用例文件
    #创建用例存放地址
    # path1='./case'
    # pattern='test*.py' 规定测试集文件开头命名为test，也可以是pattern='test_*.py'
    # discover方法找到path 目录下所有文件到的测试用例组装到测试套件
    #start_dir：用例存放路径
    # suite=unittest.defaultTestLoader.discover(path1,pattern='test*.py')
    #实例化TextTestRunner
    # runner=unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # # 使用defaultTestLoader discover方法查找测试用例文件
    # # 创建用例存放地址
    # path='case'
    # # 规定测试集文件开头命名为test，也可以是pattern='test_*.py'
    # pathcase='test*.py'
    # # discover方法找到path 目录下所有文件到的测试用例组装到测试套件
    # # start_dir：用例存放路径
    # suite=unittest.defaultTestLoader.discover(path,pathcase)
    # # 当前时间
    # now=time.strftime('%Y-%m-%d %H_%M_%S')
    # #定义测试报告存放路径 绝对路径/
    # piluginpath='plugins/'+now+'自动化测试报告.html'
    # #写入执行数据到测试报告中 open wb
    # piluginpathopen=open(piluginpath,'wb')
    # #设置测试报告详情 stream写入 title description列表头 verbosity详细程度
    # runner=HTMLTestRunner.HTMLTestRunner(stream=piluginpathopen,description='详细结果',title='自动化测试报告',verbosity=2)
    # #调用HTML类下的run方法运行测试套件
    # runner.run(suite)
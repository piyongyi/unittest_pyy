from common import MyHTMLReport
import os, unittest, time, smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr


# 定义发送邮件
def sentemail(file_new):
    from_addr = '1172163596@qq.com'  # 邮件发送账号
    to_addrs = "1172163596@qq.com"  # 接收邮件账号，字符串，多个账号用逗号分隔
    authorization_code = 'zzbcfkbpjxbqgggi'  # 授权码代替QQ密码
    smtp_server = 'smtp.qq.com'  # 固定的SMTP服务器
    smtp_port = 465  # 固定端口

    # 配置服务器
    stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    stmp.login(from_addr, authorization_code)

    # 创建一个带附件的实例
    subject = 'webUI自动化测试报告'
    message = MIMEMultipart()
    message['From'] = formataddr(["自动化测试", from_addr])  # 发件人
    message['To'] = to_addrs  # 收件人
    message['Subject'] = Header(subject, 'utf-8')  # 邮件标题
    message.attach(MIMEText('附件report.html为测试报告，请下载后打开查阅！！！', 'plain', 'utf-8'))  # 邮件正文内容

    # 增加HTML附件
    atthtml = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')  # 文件放在同一路径，不放在同一路径改一下比如'D:\\test\\report.html
    atthtml["Content-Type"] = 'application/octet-stream'
    atthtml["Content-Disposition"] = 'attachment;filename = "report.html"'
    message.attach(atthtml)

    try:
        stmp.sendmail(from_addr, to_addrs.split(','), message.as_string())  # 发送邮件,split分割后产生列表
    except Exception as e:
        print('邮件发送失败T_T' + str(e))
    print('邮件发送成功!!!')


# 查找测试报告，调用收发邮件功能
def sendreport():
    result_dir = u'../web_tester/report/'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "/" + fn)
    if not os.path.isdir(result_dir + "/" + fn) else 0)
    # 打印文件名
    # print (u'最新测试生成的报告:'+lists[-1])
    # print (u'最新测试生成的报告:'+lists[-2])

    # 找到最新生成的文件
    # file_new = os.path.join(result_dir, lists[-1])
    file_new = os.path.join(result_dir, lists[-2])
    print(u'最新生成的测试报告:', file_new)
    sentemail(file_new)


# from Case import Test004_方圆间老官网
# 测试套件
# suite = unittest.TestSuite()
# # 测试用例加载器
# loader = unittest.TestLoader()
# # 把测试用例加载到测试套件中
# suite.addTests(loader.loadTestsFromTestCase(Test004_方圆间老官网.Test_guanwang))


test_case_path = "../web_tester/Case/"
pattern = "Test*.py"
#pattern = "Test005_official_website.py"
suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
filename = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

# 测试用例执行器
if __name__ == '__main__':
    runner = MyHTMLReport.HTMLReport.TestRunner(report_file_name=filename,  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                                output_path='report',  # 保存文件夹名，默认“report”
                                                title='测试报告',  # 报告标题，默认“测试报告”
                                                description='webUI自动化测试',  # 报告描述，默认“测试描述”
                                                thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                                thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                                                sequential_execution=False,  # 是否按照套件添加(addTests)顺序执行，
                                                # 会等待一个addTests执行完成，再执行下一个，默认 False
                                                # 如果用例中存在 tearDownClass ，建议设置为True，
                                                # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                                # lang='en'
                                                lang='cn'  # 默认中文
                                                )
    # 执行测试用例套件
    runner.run(suite)
    #测试完成后发送邮件
    sendreport()

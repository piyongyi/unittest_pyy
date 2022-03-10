# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.MyHTMLReport import logger, AddImage
from common.location_path import test_login_url
from common.login import login
from common.login import username, password


class Test_Bceam(unittest.TestCase):

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        logger().info("测试开始")
        self.driver.get(test_login_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")
        login(self.driver, username, password)  # 登录
        time.sleep(5)
        # 点测试企业
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]").click()
        logger().info(f"点击选择企业-创富港")
        time.sleep(1)
        # 点应用
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[3]/a").click()
        logger().info(f"点击应用")
        time.sleep(1)


    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        self.driver.quit()
        logger().info(f"测试结束")

    def test_001_众邦电子账户充值(self):
        '''点击众邦电子账户充值'''
        # 点击电子账户管理
        self.driver.find_element_by_css_selector("#app > div.mainContainer > div > div.rightBox > div > div:nth-child(9) > div:nth-child(2)").click()
        logger().info("点击电子账户管理")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("iframe")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".companyAccountList:nth-child(1) span:nth-child(1)").click()
        logger().info("点击充值按钮")
        time.sleep(1)
        t001 = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[11]/div/div[1]/span").text
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertIn("请通过其他银行网银转账方式向此账号转入金额", t001)

    def test_002_众邦电子账户提现(self):
        '''点击众邦电子账户提现'''
        # 点击电子账户管理
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[9]/div[2]").click()
        logger().info("点击电子账户管理")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("iframe")
        time.sleep(1)

        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[7]/span[2]").click()

        logger().info("点击众邦电子账户提现")
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        t002=self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div["
                                               "4]/div/div/section/div/div[1]/div[1]/div[2]/div[1]").text
        print(t002)
        self.assertIn("账户提现", t002, msg="众邦电子账户充值按钮点击出错")

    def test_003_众邦电子账户修改密码(self):
        '''点击众邦电子账户更多操作修改密码'''
        #点击电子账户管理
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[9]/div[2]").click()
        logger().info("点击电子账户管理")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("iframe")
        time.sleep(1)

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[7]/div").click()
        time.sleep(1)
        logger().info("点击更多操作")
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[7]/div/div/div[1]").click()

        time.sleep(1)
        logger().info("点击电子修改密码")
        t003 = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div["
                                                 "5]/div/div/section/div/div[1]/div[2]/div[6]/div[1]").text
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertIn("确认交易密码", t003)  # 断言

    def test_004_众邦电子账户重置密码(self):
        '''点击众邦电子账户更多操作重置密码'''
        #点击电子账户管理
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[9]/div[2]").click()
        logger().info("点击电子账户管理")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("iframe")
        time.sleep(1)

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[7]/div").click()
        time.sleep(1)
        logger().info("点击更多操作")
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[7]/div/div/div[2]").click()
        logger().info("点击重置密码")
        time.sleep(1)
        t004 = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div["
                                                 "6]/div/div/section/div/div[1]/div[2]/div[7]/div[1]").text
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertIn("确认交易密码", t004)  # 断言


    def test_005_众邦电子账户自动做账(self):
        '''点击众邦电子账户更多操作自动做账'''
        #点击电子账户管理
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[9]/div[2]").click()
        logger().info("点击电子账户管理")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("iframe")
        time.sleep(1)

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[7]/div").click()
        time.sleep(1)
        logger().info("点击更多操作")
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[7]/div/div/div[3]").click()
        logger().info("点击自动做账")
        time.sleep(1)
        t005 = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div["
                                                 "7]/div/div/section/div/div[1]/div[1]").text
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertIn("自动做账管理", t005)  # 断言


    def test_006_众邦电子账户交易明细(self):
        '''点击众邦电子账户更多操作交易明细'''
        #点击电子账户管理
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[9]/div[2]").click()
        logger().info("点击电子账户管理")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("iframe")
        time.sleep(1)

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[7]/div").click()
        time.sleep(1)
        logger().info("点击更多操作")
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[7]/div/div/div[4]").click()
        logger().info("点击交易明细")
        time.sleep(1)
        t006 = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[10]/div/div["
                                                 "2]/div/div[2]/div[1]/div[2]").text
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertIn("交易详情", t006)  # 断言


    def test_007_点击电子账户管理发放记录(self):
        '''点击电子账户管理发放记录'''
        #点击电子账户管理
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[9]/div[2]").click()
        logger().info("点击电子账户管理")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("iframe")
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div[1]/div[2]").click()
        time.sleep(1)
        logger().info("点击发放记录")
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/input").send_keys("5.31test 5月份众邦银行")
        logger().info("输入工资表名称5.31test")
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/div[1]/div[3]").click()
        logger().info("点击搜索")
        time.sleep(1)
        t007 = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]").text
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertIn("5.31test 5月份众邦银行", t007)  # 断言



    def test_008_点击电子账户分配(self):
        '''点击电子账户分配'''
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[9]/div[2]").click()
        logger().info("点击电子账户管理")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("iframe")
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div[1]/div[3]").click()
        time.sleep(1)
        logger().info("点击电子账户分配")
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[7]/div[8]/span[1]").click()
        time.sleep(1)
        logger().info("点击分配账户")
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div/div[2]/div[1]").click()
        time.sleep(1)
        logger().info("点击确认按钮")
        AddImage(self.driver.get_screenshot_as_base64())
        t008 = self.driver.find_element_by_xpath("/html/body/div[2]/p").text #获取页面提示文本
        print(t008)
        time.sleep(1)
        if t008 == u'操作成功':
            print("账户分配操作成功")
        else:
            print("用例失败，请检查")

        #self.assertIn("操作成功", t008)  # 断言

if __name__ == '__main__':
    unittest.main()

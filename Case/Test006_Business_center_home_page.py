# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from common.MyHTMLReport import logger
from common.location_path import test_login_url
from common.login import login
from common.login import username, password
time1 = 5

class Test_Bchp(unittest.TestCase):

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        logger().info("测试开始")
        self.driver.get(test_login_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")
        login(self.driver, username, password)  # 登录
        time.sleep(time1)
        # 点测试企业
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]").click()
        logger().info(f"点击选择企业-创富港")
        time.sleep(1)

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        self.driver.quit()
        logger().info(f"测试结束")

    def test_001_首页常用应用报修中心(self):
        """点击打开首页常用应用报修中心"""
        self.driver.find_element_by_id("153").click()
        logger().info(f"点击报修中心")
        time.sleep(1)
        t001 = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[1]").text
        self.assertIn("预算审批权限设置", t001, msg="常用应用进入报修中心失败！")

    def test_002_首页常用应用薪资管理(self):
        """点击打开首页常用应用薪资管理"""
        self.driver.find_element_by_id("111").click()
        logger().info(f"点击薪资管理")
        time.sleep(3)
        self.driver.switch_to.frame("iframe")
        t = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[4]").text
        self.assertIn("查找", t, msg="常用应用进入薪资管理失败！")

    def test_003_首页常用应用电子账户管理(self):
        """点击打开首页常用应用电子账户管理"""
        self.driver.find_element_by_id("121").click()
        logger().info(f"点击电子账户管理")
        time.sleep(3)
        self.driver.switch_to.frame("iframe")
        t = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[1]/div[1]").text
        self.assertIn("众邦电子账户", t, msg="常用应用进入电子账户管理失败！")

    def test_004_首页常用应用工资条推送(self):
        """点击打开首页常用应用工资条推送"""
        self.driver.find_element_by_id("143").click()
        logger().info(f"点击工资条推送")
        time.sleep(3)
        t = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[1]/button").text
        self.assertIn("推送工资条", t, msg="常用应用进入工资条推送失败！")

    def test_005_首页常用应用通知公告(self):
        """点击打开首页常用应用通知公告"""
        self.driver.find_element_by_id("109").click()
        logger().info(f"点击通知公告")
        time.sleep(3)
        self.driver.switch_to.frame("iframe")
        t = self.driver.find_element_by_xpath(
            "//*[@id=\"section-content\"]/section/div[2]/div/div/div[1]/div/span").text
        self.assertIn("新建通知公告", t, msg="常用应用进入通知公告失败！")

    def test_006_首页常用应用区块链发票(self):
        """点击打开首页常用应用区块链发票"""
        self.driver.find_element_by_id("165").click()
        logger().info(f"点击区块链发票")
        time.sleep(3)
        t = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/form/div/div[1]/div[5]/button").text
        self.assertIn("开票", t, msg="常用应用进入区块链发票失败！")

    def test_007_首页常用应用报销(self):
        """点击打开首页常用应用报销"""
        self.driver.find_element_by_id("155").click()
        logger().info(f"点击报销")
        time.sleep(3)
        t = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/section/aside/div[1]").text
        self.assertIn("报销申请", t, msg="常用应用进入报销失败！")

    def test_008_首页常用应用审批及申请(self):
        """点击打开首页常用应用审批及申请"""
        self.driver.find_element_by_id("103").click()
        logger().info(f"点击审批及申请")
        time.sleep(3)
        self.driver.switch_to.frame("iframe")
        t = self.driver.find_element_by_xpath("//*[@id=\"col-left\"]/ul/li[1]/a").text
        self.assertIn("审批模板", t, msg="常用应用进入审批及申请失败！")


if __name__ == '__main__':
    unittest.main()

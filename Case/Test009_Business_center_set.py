# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from common.MyHTMLReport import logger
from common.location_path import test_login_url
from common.login import login
from common.login import username, password
from selenium.webdriver.common.action_chains import ActionChains
time1 = 5


class Test_Bcs(unittest.TestCase):

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

    def test_001_企业设置页面(self):
        """点击进入企业设置"""
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[4]/a").click()
        logger().info(f"点击设置")
        time.sleep(1)
        t = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[1]/div[1]").text
        self.assertIn("企业信息", t, msg="进入设置失败！")

    def test_002_查看企业启动页面(self):
        """点击进入企业设置启动页面"""
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[4]/a").click()
        logger().info(f"点击设置")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[1]/div[2]").click()
        logger().info(f"点击启动页面")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div/div[4]/span").click()
        logger().info(f"点击《自定义企业开机启动图规则》")
        time.sleep(1)
        t = self.driver.find_element_by_xpath(
            "//*[@id=\"app\"]/div[2]/div/div[2]/div/div/div[7]/div/div[2]/div/div[1]").text
        self.assertIn("方圆间用户协议", t, msg="进入启动页面失败！")

    def test_003_查看企业权限管理(self):
        """点击进入企业设置权限管理"""
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[4]/a").click()
        logger().info(f"点击设置")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[1]/div[3]").click()
        logger().info(f"点击权限管理")
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@id=\"app\"]/div[2]/div/div[2]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/div[1]/button/span").click()
        logger().info(f"点击超级管理员分配用户")
        time.sleep(1)
        t = self.driver.find_element_by_xpath(
            "//*[@id=\"app\"]/div[2]/div/div[2]/div/div/div[2]/div[2]/table/thead/tr/th[2]/div").text
        self.assertIn("手机号", t, msg="进入权限管理失败！")

    def test_004_查看企业工作台开关(self):
        """点击进入企业设置工作台开关"""
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[4]/a").click()
        logger().info(f"点击设置")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[1]/div[4]").click()
        logger().info(f"点击工作台开关")
        time.sleep(1)
        # el = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/span[2]")
        # ActionChains(self.driver).double_click(el).perform()  # 鼠标双击
        self.driver.find_element_by_xpath(
            "//*[@id=\"app\"]/div[2]/div/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/span[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@id=\"app\"]/div[2]/div/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/span[2]").click()

        logger().info(f"点击开启/停用审批和申请工作台开关")
        t = self.driver.find_element_by_xpath("/html/body/div[2]/p").text
        self.assertIn("操作成功", t)


if __name__ == '__main__':
    unittest.main()

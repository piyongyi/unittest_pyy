# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from common.MyHTMLReport import logger
from common.location_path import  test_login_url
from common.login import login
from common.login import username, password
time1 = 5

class Test_Bco(unittest.TestCase):

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

    def test_001_组织架构页面(self):
        """点击进入组织架构"""
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[2]/a").click()
        logger().info(f"点击组织")
        time.sleep(1)
        t = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div[1]/div[2]/button[1]/span").text
        self.assertIn("新增员工", t, msg="进入组织失败！")

if __name__ == '__main__':
    unittest.main()

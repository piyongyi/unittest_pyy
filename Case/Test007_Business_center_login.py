# -*- coding: utf-8 -*-
import time
import unittest
from random import random
import random
from selenium import webdriver
from common.MyHTMLReport import logger
from common.location_path import test_login_url
from common.login import login
from common.login import username, password
time1 = 5

class Test_Bcl(unittest.TestCase):

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        logger().info("测试开始")
        self.driver.get(test_login_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        self.driver.quit()
        logger().info(f"测试结束")

    def test_001_企业中心账号验证码登录(self):
        """登录功能测试"""
        login(self.driver, username, password)  # 登录
        time.sleep(time1)

    def test_002_企业中心退出登录(self):
        """退出登录功能测试"""
        login(self.driver, username, password)  # 登录
        time.sleep(time1)
        element = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div/img")
        self.driver.execute_script("arguments[0].click();", element)
        logger().info(f"点击退出登录按钮")
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button[1]/span").click()
        time.sleep(1)
        logger().info(f"点击取消退出")
        element1 = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div/img")
        self.driver.execute_script("arguments[0].click();", element1)
        logger().info(f"再次点击退出登录按钮")
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button[2]/span").click()
        time.sleep(5)
        logger().info(f"点击确定按钮，退出到登录页")
        t = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[3]/div[3]/button/span").text
        self.assertIn("登录", t, msg="退出登录失败！")


    def test_003_企业中心创建新企业功能测试(self):
        """创建新企业功能测试"""
        login(self.driver, username, password)  # 登录
        time.sleep(time1)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[3]/div/button/span").click()
        time.sleep(1)
        logger().info(f"点击创建新企业")

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        characters = "".join(random.sample(alphabet, 3))

        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[2]/div[1]/div[2]/div/input").send_keys(
            characters)
        logger().info(f"企业名称输入随机文本")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[3]/div/button").click()
        logger().info(f"点击确定按钮，等待创建")
        time.sleep(5)
        t = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[1]/div[1]/div[1]").text
        self.assertIn("企业信息", t, msg="创建新企业失败！")

if __name__ == '__main__':
    unittest.main()

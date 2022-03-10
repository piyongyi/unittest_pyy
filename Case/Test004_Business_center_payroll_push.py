# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from common.MyHTMLReport import logger, AddImage
from common.location_path import salary_path,test_login_url
from common.login import login
from common.login import username, password

class Test_Bcpp(unittest.TestCase):

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

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        self.driver.quit()
        logger().info(f"测试结束")

    def test_001_工资条推送(self):
        '''工资条推送测试'''
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[3]/a").click()  # 点应用
        logger().info("点击应用")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[11]/div[2]").click()
        logger().info("点击工资条推送模块")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[1]/button").click()
        logger().info("点击推送工资条按钮")
        time.sleep(1)
        # input标签上传文件
        upload = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div[2]/div[2]/div/div/input")
        time.sleep(1)
        upload.send_keys(salary_path)
        logger().info("上传工资单测试文件")
        print(upload.get_attribute('value'))
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div[3]/button[2]").click()
        logger().info("点击导入按钮")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[1]/div[2]/button[1]").click()
        logger().info("点击立即推送")
        AddImage(self.driver.get_screenshot_as_base64())
        text = self.driver.find_element_by_xpath("/html/body/div[2]/p").text #获取页面提示文本
        print(text)
        self.assertIn("推送成功",text)  # 断言


if __name__ == '__main__':
    unittest.main()

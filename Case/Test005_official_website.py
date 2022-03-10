# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from common.MyHTMLReport import logger, AddImage
from common.location_path import ow_url

class Test_own(unittest.TestCase):

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        logger().info("测试开始")

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        self.driver.quit()
        logger().info("测试结束")

    def test_001_母公司创富港首页(self):
        '''从方圆间官网跳转至创富港官网首页'''
        self.driver.get(ow_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        js = "var q=document.documentElement.scrollTop=1000"  # 下拉滚动条至底部
        self.driver.execute_script(js)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"footer\"]/div/div/div[1]/div[1]/ul/li[2]/a").click()  # 点击创富港
        logger().info(f"点击母公司-创富港")
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 在新标签中打开，进入新窗口
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertEqual("办公室出租_共享办公_深圳众创空间", self.driver.title, msg="无法打开创富港首页")

    def test_002_首页(self):
        '''点击方圆间官网首页按钮'''
        a = self.driver.get(ow_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul/li[1]/a").click()
        logger().info(f"点击首页")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"hd\"]/div/div/div/div[1]/a/img").click()
        logger().info(f"点击方圆间logo")
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertEqual("方圆间", self.driver.title, msg="无法打开关于我们页面")

    def test_003_商务合作(self):
        '''从方圆间官网打开商务合作页面'''
        self.driver.get(ow_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul/li[2]/a").click()
        logger().info(f"点击商务合作")
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        t = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/p").text
        self.assertEqual("方圆间诚邀各服务商进行商务合作。", t, msg="无法打开商务合作页面")

    def test_004_加入我们(self):
        '''从方圆间官网打开加入我们页面'''
        self.driver.get(ow_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul/li[3]/a").click()
        logger().info(f"点击加入我们")
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        t = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/p").text
        self.assertEqual("我们努力为人才打造公正、公平、透明的成长环境，人尽其才，各施所长。", t, msg="无法打开加入我们页面")

    def test_005_关于我们(self):
        '''从方圆间官网打开关于我们页面'''
        self.driver.get(ow_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul/li[4]/a").click()
        logger().info(f"点击关于我们")
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        t = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/p").text
        self.assertEqual("我们只追求服务好每一家企业，成为他们坚实的后盾", t, msg="无法打开关于我们")

    def test_006_企业中心(self):
        '''从方圆间官网打开企业中心页面'''
        self.driver.get(ow_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"companycenter\"]").click()
        logger().info(f"点击企业中心")
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 在新标签中打开，进入新窗口
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertEqual("企业中心", self.driver.title, msg="无法打开企业中心")

    def test_007_帮助文档(self):
        '''从方圆间官网打开帮助文档页面'''
        self.driver.get(ow_url)  # 打开测试页面
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/div/a[2]").click()
        logger().info(f"点击帮助文档")
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 在新标签中打开，进入新窗口
        logger().info(f"打开网址：{self.driver.current_url}")
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertEqual("方圆间平台帮助手册 · 方圆间", self.driver.title, msg="无法打开帮助文档")



if __name__ == '__main__':
    unittest.main()

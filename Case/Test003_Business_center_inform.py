# -*- coding: utf-8 -*-
import os
import time
import unittest
from selenium import webdriver
from common.location_path import test_login_url
from common.MyHTMLReport import logger, AddImage
from common.login import login
from common.login import username, password

class Test_Bci(unittest.TestCase):
    # 定义一个保存截图函数
    def save_img(self, img_name):
        self.driver.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath("D:/projects/web_tester/img/"), img_name, 'rb'))

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



    def test_001_新增一条通知公告(self):
        '''新增新增一条通知公告测试'''
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[3]/a").click()  # 点应用
        logger().info(f"点击应用")
        time.sleep(2)
        # 点通知公告
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[4]/div[2]").click()
        logger().info(f"点击通知公告")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("iframe")
        time.sleep(1)
        # 点新建通知公告
        self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/div[2]/div/div/div[1]/div/span").click()
        self.driver.implicitly_wait(5)
        logger().info(f"点击新建通知公告")
        # # 点发布类型下拉框
        self.driver.find_element_by_xpath("//*[@id=\"dLabe2\"]").click()
        logger().info(f"点击选择发布类型")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/div[1]/div/ul/li[2]").click()  # 行政通知
        time.sleep(1)
        logger().info(f"点击行政通知")
        self.driver.find_element_by_xpath("//*[@id=\"dLabe2\"]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/div[1]/div/ul/li[3]").click()  # 会议通知
        time.sleep(1)
        logger().info(f"点击会议通知")
        self.driver.find_element_by_xpath("//*[@id=\"dLabe2\"]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/div[1]/div/ul/li[1]").click()  # 通知公告
        time.sleep(1)
        logger().info(f"点击通知公告")
        # 点添加
        self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/div[2]/span").click()
        time.sleep(1)
        logger().info(f"点击添加按钮")
        # 选中通知人员 测试124234
        self.driver.find_element_by_xpath(
            "//*[@id=\"noticeMember\"]/div/div/div[2]/div[1]/div/div/div[4]/span[2]").click()
        logger().info(f"选中通知人员：测试124234")
        # 点确认
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"noticeMember\"]/div/div/div[3]/button[1]").click()
        logger().info(f"点击确认")
        # 输入通知标题
        time.sleep(1)
        # self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/input").send_keys("测试通知")
        # time.sleep(1)
        # 从模板中选择
        self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/button").click()
        time.sleep(1)
        logger().info(f"从模板中选择")
        # 选中方圆间版本更新
        self.driver.find_element_by_xpath(
            "//*[@id=\"attend-detail\"]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[1]").click()
        logger().info(f"选中方圆间版本更新模板")
        # click_locxy(self.driver, 550, 610)
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("iframe")
        # iframe1= self.driver.find_element_by_id("ueditor_8")
        # self.driver.switch_to.frame(iframe1)
        # 点确认
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"attend-detail\"]/div/div/div[3]/div[2]/button[1]").click()
        logger().info(f"确认")
        js = "var q=document.documentElement.scrollTop=500"  # 下拉滚动条
        self.driver.execute_script(js)
        time.sleep(1)
        # 点预览
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/div[9]/button[2]").click()
        logger().info(f"预览")
        # 点关闭预览
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"attend-detail-yulan\"]/div/div/div[1]/button").click()
        logger().info(f"关闭预览")
        # 点发布
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/div[9]/button[1]").click()
        logger().info(f"点击发布")
        time.sleep(1)
        AddImage(self.driver.get_screenshot_as_base64())
        t001=self.driver.find_element_by_xpath("//*[@id=\"section-content\"]/section/div[2]/div/div/table/tbody/tr[1]/td[2]/div[1]").text
        print(t001)
        self.assertIn("方圆间版本更新", t001, msg="发布通知公告失败！")


if __name__ == '__main__':
    unittest.main()

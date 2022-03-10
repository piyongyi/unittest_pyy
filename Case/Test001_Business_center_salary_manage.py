# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from common.MyHTMLReport import logger, AddImage
from common.location_path import test_login_url
from common.login import login
from common.login import username, password

class Test_Bcsm(unittest.TestCase):

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

    def test_001_新建工资表(self):
        '''新建工资表测试'''
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[3]/a").click()  # 点应用
        logger().info("点击应用")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[5]/div[2]").click()  # 点薪资管理
        self.driver.implicitly_wait(5)
        logger().info("点击薪资管理")
        self.driver.switch_to.frame("iframe")
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[5]").click()  # 点新建工资表
        logger().info("点击新建工资表")
        time.sleep(1)
        # 选择月份
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/input").click()
        logger().info("点击选择月份")
        time.sleep(1)
        # 选九月
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[2]/table[3]/tbody/tr[3]/td[1]/div/a").click()
        time.sleep(1)
        logger().info("点击选择九月份")
        # 输入工资单001
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/input").clear()
        time.sleep(1)

        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/input").send_keys("工资单001")
        time.sleep(1)
        logger().info("输入工资单名称001")
        # 引入历史数据
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div/input").click()
        time.sleep(1)
        logger().info("引入历史数据")
        # 选择testp模板
        self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[1]").click()
        logger().info("选择testp模板")
        time.sleep(1)
        # 点击下一步
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]").click()
        time.sleep(1)
        logger().info("点击下一步")
        # 点添加员工
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/button[5]/span").click()
        time.sleep(1)
        logger().info("点添加员工")
        # 输入姓名 皮永宜 查询
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[6]/div[2]/div/input").send_keys(
            "皮永宜")
        logger().info("输入姓名 皮永宜 查询")
        time.sleep(1)
        # 选中 皮
        self.driver.find_element_by_css_selector(
            "body > div > div > div.appMain > div.managementHome > div.right > div > div.selPP > div.PPbox > div > "
            "div.el-tree-node.is-expanded.is-focusable > div.el-tree-node__children > "
            "div.el-tree-node.is-expanded.is-focusable > div.el-tree-node__children > "
            "div.el-tree-node.is-expanded.is-focusable > div.el-tree-node__children > div:nth-child(8) > div > label "
            "> span > span").click()
        logger().info("选中 皮永宜 ")
        time.sleep(1)
        # 确定
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/div[6]/div[4]/div").click()
        time.sleep(1)
        logger().info("点击确定 ")
        # 输入基本工资
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div["
                                          "3]/table/tbody/tr/td[8]/div/div/input").send_keys("0.01")
        time.sleep(1)
        logger().info("输入基本工资0.01元")
        AddImage(self.driver.get_screenshot_as_base64())
        t001=self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/button[2]/span").text
        print(t001)
        self.assertIn("修改工资表信息", t001, msg="创建工资单失败！")


    def test_002_工资表提交审核(self):
        '''工资表提交审核测试'''
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[3]/a").click()  # 点应用
        logger().info("点击应用")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[5]/div[2]").click()  # 点薪资管理
        self.driver.implicitly_wait(5)
        logger().info("点击薪资管理")
        self.driver.switch_to.frame("iframe")
        time.sleep(1)
        # 点编辑
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div["
                                          "6]/span[3]").click()
        logger().info("点击审核")
        js = "var q=document.documentElement.scrollTop=300"  # 下拉滚动条
        self.driver.execute_script(js)
        time.sleep(1)
        # 提交审核
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[5]/button[1]").click()
        logger().info("点击提交审核")
        time.sleep(1)
        # 输入姓名 皮 查询
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[10]/div/div[2]/div/input").send_keys(
            "皮永宜")
        logger().info("输入姓名 皮永宜 查询")
        time.sleep(1)
        # 选中 皮
        self.driver.find_element_by_css_selector(
            "body > div > div > div.appMain > div.managementHome > div.right > div > div.subpeople > div > div.PPbox "
            "> div > div.el-tree-node.is-expanded > div.el-tree-node__children > div.el-tree-node.is-expanded > "
            "div.el-tree-node__children > div.el-tree-node.is-expanded > div.el-tree-node__children > div:nth-child("
            "8) > div > label > span > span").click()
        time.sleep(1)
        logger().info("选择 皮永宜")

        # 确定
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[10]/div/div[4]/div").click()
        time.sleep(1)
        logger().info("点击确定")
        # alert = driver.switch_to.alert  # 切到弹出框
        # print(alert.text)
        # alert.accept()  # 确定 取消为 alert.dismiss()
        # 确定提交审核
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button[2]/span").click()
        time.sleep(1)
        logger().info("确定提交审核")
        # 点审核工资表
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]").click()
        logger().info("点击审核工资表")
        t002 = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[4]").text
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertIn("查找", t002, msg="提交审核失败！")

    def test_003_工资表提交发放(self):
        '''工资表提交发放测试'''
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/div[3]/a").click()  # 点应用
        logger().info("点击应用")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div[2]/div/div[5]/div[2]").click()  # 点薪资管理
        self.driver.implicitly_wait(5)
        logger().info("点击薪资管理")
        self.driver.switch_to.frame("iframe")
        time.sleep(1)
        # 点审核工资表
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]").click()
        logger().info("点击审核工资表")
        time.sleep(1)
        # 点审核按钮
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[6]/span").click()
        logger().info("点击审核按钮")
        time.sleep(1)
        js = "var q=document.documentElement.scrollTop=300"  # 下拉滚动条
        self.driver.execute_script(js)
        time.sleep(1)
        # 提交发放
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[5]/button[2]").click()
        logger().info("点击提交发放")
        time.sleep(2)
        # 输入姓名 皮 查询
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[7]/div/div[2]/div/input").send_keys(
            "皮永宜")
        logger().info("输入姓名 皮永宜 查询")
        time.sleep(1)
        # 选中 皮
        self.driver.find_element_by_css_selector(
            "body > div > div > div.appMain > div.managementHome > div.right > div > div.subpeople > div > div.PPbox "
            "> div > div.el-tree-node.is-expanded > div.el-tree-node__children > div.el-tree-node.is-expanded > "
            "div.el-tree-node__children > div.el-tree-node.is-expanded > div.el-tree-node__children > div:nth-child("
            "8) > div > label > span > span").click()
        logger().info("选中 皮永宜")
        time.sleep(1)

        # 确定
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[7]/div/div[4]/div").click()
        logger().info("点击确定")
        time.sleep(1)
        # alert = driver.switch_to.alert  # 切到弹出框
        # print(alert.text)
        # alert.accept()  # 确定 取消为 alert.dismiss()
        # 确定提交发放
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button[2]/span").click()
        time.sleep(1)
        logger().info("确定提交发放")
        # 点审核工资表
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]").click()
        t003 = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[4]").text
        AddImage(self.driver.get_screenshot_as_base64())
        self.assertIn("查找", t003, msg="提交发放失败")


if __name__ == '__main__':
    unittest.main()

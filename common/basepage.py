# -*- coding:UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#显性等待
# WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,value)))
# self.driver.find_element_by_xpath().click(value)


class locations():

    def __init__(self,driver):
        self.driver = driver
        #等待時長
        self.timeout = 10

    # 打开网页功能
    def open(self, url):
        self.driver.get(url)
        # 隐性等待,最长等待5秒
        self.driver.implicitly_wait(5)

    # 关闭网页功能
    def close(self):
        # 强制等待
        time.sleep(1)
        self.driver.quit()

    # 定位元素功能
    def locateElement(self, types, value):
        global el
        if types == "id":
            el = WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element_by_id(value))
        elif types == "name":
            el = WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element_by_name(value))
        elif types == "class_name":
            el = WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element_by_class_name(value))
        elif types == "tag_name":
            el = WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element_by_tag_name(value))
        elif types == "link_text":
            el = WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element_by_link_text(value))
        elif types == "partial_link_text":
            el = WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element_by_partial_link_text(value))
        elif types == "xpath":
            el = WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element_by_xpath(value))
        elif types == "css_selector":
            el = WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element_by_css_selector(value))
        return el

    # 点击元素功能
    def click(self, types, value):
        # 调用locateElement定位元素
        el = self.locateElement(types, value)
        # 调用click()进行点击操作
        el.click()

    # 对定位到元素进行输入
    def input_data(self, types, value, data):
        # 调用locateElement定位元素
        el = self.locateElement(types, value)
        # 调用send_keys进行输入
        el.send_keys(data)

    # 获取定位到的元素中的文本内容<a>text</a>
    def getText(self, types, value):
        # 调用locateElement定位元素
        el = self.locateElement(types, value)
        # 返回文本内容
        return el.text

    # 获取定位到的元素中的标签值
    def getAttribute(self, types, value, name):
        # 调用locateElement定位元素
        el = self.locateElement(types, value)
        # 返回文本内容
        return el.get_attribute(name)




# 如果是引用该类则不执行该方法
if __name__ == "__main__":
    test = locations(webdriver.Chrome())
    url = "https://test.chuangfuka.com/web/companycenter/#/login"
    test.open(url)
    test.input_data("xpath", "//*[@id=\"app\"]/div[2]/div/div/div[3]/div[2]/div[1]/div[3]/div/input", "19968151428")
    test.input_data("xpath", "//*[@id=\"app\"]/div[2]/div/div/div[3]/div[2]/div[2]/div[2]/div/input", "a123456")
    test.click("xpath", "//*[@id=\"app\"]/div[2]/div/div/div[3]/div[3]/button")
    test.close()


from common.MyHTMLReport import logger
from selenium.webdriver.remote.webdriver import WebDriver
import time

username = 19968151428
password = 888888

def login(driver: WebDriver, username, password):

    driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[3]/div[2]/div[1]/div[3]/div/input").send_keys(username)
    logger().info(f"输入手机号码:{username}")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[3]/div[2]/div[2]/div[2]/div/input").send_keys(password)
    logger().info(f"输入密码:{password}")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[3]/div[3]/div/div/div[1]/label/span[1]/span").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[3]/div[3]/button").click()
    time.sleep(1)
    logger().info(f"点击登录")

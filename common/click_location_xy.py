from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def click_locxy(dr, x, y, left_click=True):
    '''
    dr:浏览器
    x:页面x坐标
    y:页面y坐标
    left_click:True为鼠标左键点击，否则为右键点击
    '''
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前

if __name__ == "__main__":
    dr = webdriver.Chrome()
    dr.get('http://www.baidu.com')
    click_locxy(dr, 100, 0) # 左键点击
    click_locxy(dr, 100, 100, left_click=False) # 右键点击
    # click_locxy(self.driver, 800, 240)  # 左键点击 800,240坐标点

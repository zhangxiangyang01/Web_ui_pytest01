from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base():

    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_ele(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))
    # 点击元素
    def base_click(self, loc):
        self.base_find_ele(loc).click()
    # 输入方法
    def base_input(self,loc,text):
        el = self.base_find_ele(loc)
        el.clear()
        el.send_keys(text)

    def base_get_toast(self, message):
        # loc = (By.XPATH, "//*[contains(@text,'"+message+"')]")
        loc = (By.XPATH, "//*[contains(@text,'%s')]" % message)
        return self.base_find_ele(loc, poll=0.1).text

    def base_get_text(self, loc):
        return self.base_find_ele(loc).text

    def base_drag_and_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)

    def base_get_iamge(self):
        path = "./Image/faild.png"
        self.driver.get_screenshot_as_file(path)
from selenium.webdriver.common.by import By
from Base.base import Base
btn = By.XPATH,"//*[@text='登录']"
class PageToast(Base):
    def page_click_login_btn(self):
        self.base_click(btn)
# from selenium.webdriver.common.by import By
from Base.base import Base
import Page

class PageLogin(Base):

    def page_click_skip(self):
        self.base_click(Page.login_click_skip)

    def page_click_me(self):
        self.base_click(Page.login_click_me)

    def page_click_go_login(self):
        self.base_click(Page.login_go_login)

    # 输入用户名
    def page_input_username(self, text):
        self.base_input(Page.login_input_user, text)

    # 输入密码
    def page_input_password(self, text):
        self.base_input(Page.login_input_pwd, text)

    # 点击登陆
    def page_click_login_btn(self):
        self.base_click(Page.login_click_button)

    # 登录后，获取昵称
    def page_get_self_name(self):
        return self.base_get_text(Page.login_get_user_nikename)

    def page_click_setting(self):
        self.base_click(Page.login_click_setting)

    def page_drag_and_drop(self):
        el1 = self.base_find_ele(Page.login_msg_push)
        el2 = self.base_find_ele(Page.login_revise_pwd)
        self.base_drag_and_drop(el1, el2)

    def page_click_loginout(self):
        self.base_click(Page.login_loginout_button)

    def page_click_loginout_ok(self):
        self.base_click(Page.login_click_ok)








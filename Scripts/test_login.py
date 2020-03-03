import os
import sys
sys.path.append(os.getcwd())

from time import sleep
import pytest
from Page.page_in import PageIn
from Base.read_login_yaml import get_yaml
from Base.read_login_txt import red_login_txt

def get_yaml_data():
    arrs = []
    for i in get_yaml().values():
        arrs.append((i.get("username"), i.get("pwd"), i.get("expect_resoult"), i.get("expect_toast") ))
        # arrs.append((i.get("username"), i.get("pwd"), i.get("expect_resoult")))
    return arrs

def get_txt_data():
   return red_login_txt("login_data.txt")

# @allure.severity(allure.severity_level.CRITICAL)
class TestLogin():

    # 初始化方法
    def setup_class(self):

        # ------ 实例化 PageLogin
        # self.login = PageLogin(get_driver())
        # self.toast = PageToast(get_driver())
        self.login = PageIn().page_get_login()
        self.toast = PageIn().page_get_toast()
        #
        self.login.page_click_skip()
        self.login.page_click_me()
        self.login.page_click_go_login()

    # 结束方法
    def teardown_class(self):
        # 关闭驱动对象

        # self.driver.quit()
        self.login.driver.quit()

    # @pytest.mark.parametrize("username,pwd",[("18339052997@163.com", "123456"),("2222222@163.com","222222")])

    # @allure.step("登录测试")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.parametrize("username, pwd, nickname", [("18339052997", "Zz0103", "lq_0223094916_yxe"), (" 1833", "22222", "此用户不存在")])

    # --- 以yaml读取
    @pytest.mark.parametrize("username, pwd, expect_resoult, expect_toast", get_yaml_data())

    # 以txt读取
    # @pytest.mark.parametrize("username, pwd, expect_resoult, expect_toast", get_txt_data())
    def test_login(self, username, pwd, expect_resoult, expect_toast):
        if expect_resoult:
            try:
                self.login.page_input_username(username)
                self.login.page_input_password(pwd)
                self.login.page_click_login_btn()

                assert expect_resoult in self.login.page_get_self_name()
                self.login.page_click_setting()
                self.login.page_drag_and_drop()
                self.login.page_click_loginout()
                self.login.page_click_loginout_ok()
                self.login.page_click_me()
                self.login.page_click_go_login()
            except:
                self.login.base_get_iamge()
                raise
        else:
            try:
                self.login.page_input_username(username)
                self.login.page_input_password(pwd)
                self.login.page_click_login_btn()
                assert expect_toast in self.login.base_get_toast(expect_toast)
            except:
                self.login.base_get_iamge()
                raise

        # try:
        #     self.login.page_click_skip()
        #     self.login.page_click_me()
        #     self.login.page_click_go_login()
        #             # allure.attach("描述：","输入用户名")
        #     self.login.page_input_username(username)
        #
        #             # allure.attach("描述：", "输入密码")
        #     self.login.page_input_password(pwd)
        #
        #     self.login.page_click_login_btn()
        #             # toast--调用
        #             # self.toast.page_click_login_btn()
        #     assert nickname in self.login.page_get_self_name()
        # except:
        #     self.login.base_get_iamge()
            # self.login.page_click_setting()
            # self.login.page_drag_and_drop()
            # self.login.page_click_loginout()
            # self.login.page_click_loginout_ok()




if __name__ == '__main__':
    pytest.main("-s test_login.py")
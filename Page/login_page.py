import time

import yaml
from selenium.webdriver.common.by import By

from c2_cms.Page.base_page import BasePage


class LoginPage(BasePage):
    _BASE_URL = 'https://msi-c2-cms.fooyo.shop/#/login'
    email = 'huyang@fooyo.sg'
    psd = '11111111'
    __ENG = (By.CSS_SELECTOR, '[class="login__language__text"]')
    __USERNAMR = (By.CSS_SELECTOR,'[placeholder="Please Input The Email"]')
    __PASSWORD = (By.CSS_SELECTOR, '[placeholder="Please Input The Password"]')
    __BTN_LOGIN = (By.CSS_SELECTOR, '[class="el-button login-btn el-button--primary el-button--small"]')

    def login(self):
        time.sleep(2)
        self.wait_element_until_visible(self.__ENG)
        self.do_find(self.__ENG).click()
        self.wait_element_until_visible(self.__USERNAMR)
        self.wait_element_until_visible(self.__PASSWORD)
        self.do_send_keys(self.email,self.__USERNAMR)
        self.do_send_keys(self.psd,self.__PASSWORD)
        self.do_find(self.__BTN_LOGIN).click()
        time.sleep(5)
        # 获取 Session Storage 只需将 localStorage 修改为 sessionStorage，修改获取的值为 token_bk 即可
        user = self.driver.execute_script("return localStorage.getItem('user')")
        print(user)
        time.sleep(3)
        with open('../Data/user.yaml', "w") as f:
            # 第一个参数是要写入的数据，第二个字段是要进行数据操作的资源文件
            yaml.safe_dump(user, f)
        print("保存成功")
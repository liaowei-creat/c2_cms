import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Public:

    __ENG = (By.CSS_SELECTOR, '[class="login__language__text"]')

    def local_storage(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(chrome_options=options)
        # driver = webdriver.Chrome()
        driver.implicitly_wait(60)
        driver.get('https://msi-c2-cms.fooyo.shop')
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(self.__ENG))
        driver.find_element(By.CSS_SELECTOR, '[class="login__language__text"]').click()
        # 定义cookie,从文件中获取
        user = yaml.safe_load(open('../Data/user.yaml'))
        # print(user)
        # self.driver.execute_script('return window.localStorage.setItem("token", "value");')
        driver.execute_script(f'localStorage.setItem("user", {[user]});')
        # 再次访问
        driver.get('https://msi-c2-cms.fooyo.shop')
        time.sleep(5)
        yield driver
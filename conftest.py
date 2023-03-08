import time

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

_BASE_URL = 'https://msi-c2-cms.fooyo.shop/#/login'
email = 'huyang@fooyo.sg'
psd = '11111111'
__ENG = (By.CSS_SELECTOR, '[class="login__language__text"]')
__USERNAMR = (By.CSS_SELECTOR,'[placeholder="Please Input The Email"]')
__PASSWORD = (By.CSS_SELECTOR, '[placeholder="Please Input The Password"]')
__BTN_LOGIN = (By.CSS_SELECTOR, '[class="el-button login-btn el-button--primary el-button--small"]')



@pytest.fixture(scope='session')
def login():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://msi-c2-cms.fooyo.shop')
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(__ENG))
    driver.find_element(By.CSS_SELECTOR, '[class="login__language__text"]').click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(__USERNAMR))
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(__PASSWORD))
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Please Input The Email"]').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Please Input The Password"]').send_keys(psd)
    driver.find_element(By.CSS_SELECTOR,
                        '[class="el-button login-btn el-button--primary el-button--small"]').click()
    time.sleep(5)
    # 获取 Session Storage 只需将 localStorage 修改为 sessionStorage，修改获取的值为 token_bk 即可
    user = driver.execute_script("return localStorage.getItem('user')")
    # print(user)
    with open('../Data/user.yaml', "w") as f:
        # 第一个参数是要写入的数据，第二个字段是要进行数据操作的资源文件
        yaml.safe_dump(user, f)
    # print("保存成功")
    yield driver
    driver.quit()



@pytest.fixture(scope='session')
def local_storage():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.Chrome()
    driver.implicitly_wait(60)
    driver.get('https://msi-c2-cms.fooyo.shop')
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(__ENG))
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
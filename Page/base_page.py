from time import sleep, time

import allure
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    _BASE_URL = ''

    def __init__(self,driver=None):
        if driver:
            self.driver = driver
        else:
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("start-maximized")
            self.options.add_argument("disable-infobars")
            self.options.add_argument("--disable-extensions")
            driver = webdriver.Chrome(chrome_options=self.options)
            #默认打开开发者工具
            # self.option = webdriver.ChromeOptions()
            # self.option.add_argument("--auto-open-devtools-for-tabs")

            #设置为手机模式
            # mobile_emulation = {"deviceName": "iPhone 12 Pro"}
            #
            # option.add_experimental_option("mobileEmulation", mobile_emulation)
            # option.add_argument('–user-agent=iphone XR')
            # # option.add_argument('--window-size=1920,1080')
            # option.add_argument('--start-maximized')
            # option.add_argument("--auto-open-devtools-for-tabs")
            # self.driver = webdriver.Chrome(options=self.option)

            self.driver = webdriver.Chrome()
            # self.driver.set_window_size(1920,1080)
            self.driver.implicitly_wait(10)
            # self.driver.maximize_window()
            # self.driver.get(self._BASE_URL)
                # 再次访问
        self.driver.get(self._BASE_URL)

    def do_find(self, by, locator=None):
        #获取单个元素
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        #获取多个元素
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        ele = self.do_find(by, locator)
        ele.clear()
        ele.send_keys(value)

    def do_send_files(self, file, by, locator=None):
        ele = self.do_find(by, locator)
        ele.send_keys(file)

    def do_quit(self):
        self.driver.quit()

    def get_screen(self):
        timestamp = int(time())
        image_path = f"./images/image_{timestamp}.PNG"
        #截图
        self.driver.save_screenshot(image_path)
        #将截图放到报告的数据中
        allure.attach.file(image_path,name='picture',attachment_type=allure.attachment_type.PNG)

    def wait_element_until_visible(self, locator:tuple):
        return WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(locator))

    def wait_element_until_clickable(self, locator:tuple):
        return WebDriverWait(self.driver, 40).until(expected_conditions.element_to_be_clickable(locator))

    def do_scroll_from_origin(self,x,y):
        self.action = ActionChains(self.driver)
        self.action.scroll_by_amount(x,y)
        # self.action.scroll(0,1000)
        self.action.perform()

    #滑动
    def do_swipe(self,ele):
        # 将滚动条移动到页面的底部
        # self.action = TouchAction(self.driver)
        # self.action.press(x=500,y=1890)
        # self.action.move_to(x=500,y=485)
        # self.action.release()
        # self.action.perform()'arguments[0].scrollIntoView({block: "end"}
        # js1 =  'window.scroll(0, document.documentElement.scrollHeight)'
        # js2 = 'arguments[0].scrollIntoView({block: "end"})'
        js = "driver.execute_script('arguments[0].scrollIntoView();', driver.find_elements('id', 'kw')[0])"
        # ks3 =   '3'
        self.driver.execute_script('arguments[0].scrollIntoView();', self.do_find(ele))

    #鼠标悬停并点击
    def hover(self, locator:tuple):
        ele = self.do_find(locator)
        # ele = self.driver.switch_to().activeElement()
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()


    #键盘
    def action_send_key(self, value):
        ActionChains(self.driver).send_keys(value).perform()

    #获取当前页面的url
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url
import time

import yaml
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from c2_cms.Page.base_page import BasePage


class SkuPage(BasePage):
    _BASE_URL = 'https://msi-c2-cms.fooyo.shop/#/skus'
    #sku列表页面
    __BTN_EXPORT = (By.XPATH,"//span[text()=' Export ']/..")
    __Export_info = (By.CSS_SELECTOR,"[class='el-message__content']")
    __BTN_EDIT = (By.XPATH, "//div[@style='top: 40px; max-height: 760px;']//tr[1]/td[last()]/div/button[2]")
    __CONFIRM_INFO = (By.XPATH, "//*[text()='Operate Success!']")
    #edit页面
    __IPT_NAME_CN = (By.CSS_SELECTOR, 'div[placeholder="Name(CN)"]')
    __BTN_DEL = (By.XPATH, '//i[@class="el-input__icon el-icon-circle-close el-input__clear"]')
    __BTN_CONFIRM = (By.XPATH, "//*[text()='Confirm']")


    '''sku列表页面'''

    #点击导出按钮
    def click_sku_export(self):
        self.wait_element_until_visible(self.__BTN_EXPORT)
        self.do_find(self.__BTN_EXPORT).click()
        return self

    #点击其中一个sku的编辑按钮修改里面的信息
    def click_edit(self):
        self.wait_element_until_visible(self.__BTN_EDIT)
        self.do_find(self.__BTN_EDIT).click()
        return self

    #点击view按钮
    def click_view(self, SKU_No):
        __BTN_VIEW = (By.XPATH,
                      f'//div[@class="el-table__body-wrapper is-scrolling-none"]//*[text()="{SKU_No}"]/../../../..//*[text()="View"]')
        self.hover(__BTN_VIEW)
        # self.do_find(__BTN_VIEW).click()
        return self

    #导出成功的信息
    def get_infomation(self):
        self.wait_element_until_visible(self.__Export_info)
        text = self.do_find(self.__Export_info).text
        return text

    #confirm成功的信息
    def confirm_info(self):
        self.wait_element_until_visible(self.__CONFIRM_INFO)
        text = self.do_find(self.__CONFIRM_INFO).text
        return text

    '''sku的编辑页面'''
    def edit_name_zn(self,name):
        # js = f"document.getElementsByClassName('el-input__inner')[1].value='123'"
        # self.driver.execute_script(js)
        # print('11')
        # self.wait_element_until_visible(self.__IPT_NAME_CN)
        # self.do_find(self.__IPT_NAME_CN).get_attribute('hogwarts')
        print('12')
        # time.sleep(5)
        # ele = self.do_find(self.__IPT_NAME_CN)
        # print(ele)
        self.hover(self.__IPT_NAME_CN)
        self.hover(self.__BTN_DEL)
        self.action_send_key(name)
        print('13')
        # ele = self.do_find(self.__IPT_NAME_CN).get_attribute('value')
        # for i in ele:
        #     ActionChains(self.driver).send_keys(Keys.BACK_SPACE).perform()
        # ActionChains(self.driver).send_keys('uio').perform()
        return self

    #点击确认按钮
    def click_btn_confirm(self):
        self.wait_element_until_visible(self.__BTN_CONFIRM)
        self.do_find(self.__BTN_CONFIRM).click()
        return self



    '''sku的详情页面'''
    def get_sku_info(self,sku_info):
        __INFO = (By.XPATH, f"//span[text()='SKU: {sku_info}']")
        # __INFO = (By.CSS_SELECTOR, '[class="marginBottom8"]')
        # js = "document.getElementsByClassName('marginBottom8')[0].innerText"
        # text = self.driver.execute_script(js)
        # print(self.driver.execute_script("document.getElementsByClassName('marginBottom8')"))
        ele = self.do_find(__INFO)
        # self.wait_element_until_visible(__INFO)
        # text = self.do_find(__INFO).get_attribute('textContent')
        # text = self.do_find(__INFO).get_attribute('innerHTML')
        time.sleep(2)
        content = ele.text
        # print(content)
        return content

import re
import time

from selenium.webdriver.common.by import By

from c2_cms.Page.base_page import BasePage


class PromotionPage(BasePage):
    _BASE_URL = 'https://msi-c2-cms.fooyo.shop/#/promotions'
    # 列表页面
    __CREATE_PROMOTION = (By.XPATH, "//*[text()=' Create New ']")
    __CONFIRM_INFO = (By.XPATH, "//*[text()='Operate Success!']")
    # 编辑页面
    __IPT_NAME_CN = (
        By.XPATH, '//*[@class="el-collapse formily-element-form-collapse"]/div[1]//input[@ placeholder="Name(CN)"]')
    __IPT_NAME_EN = (
        By.XPATH, '//*[@class="el-collapse formily-element-form-collapse"]/div[1]//input[@ placeholder="Name(EN)"]')
    __IPT_SHOP = (By.CSS_SELECTOR, 'input[placeholder="Shop"]')
    __IPT_CHANNEL = (By.CSS_SELECTOR, 'input[placeholder="Channel"]')
    __IPT_PROMOTION_TYPE = (By.CSS_SELECTOR, 'input[placeholder="Promotion Type"]')
    __IPT_SELLABLE_TYPE = (By.CSS_SELECTOR, 'input[placeholder="Sellable Type"]')
    __BTN_SELLABLE_TYPE = (By.XPATH, "//span[text()=' Set ']")
    __BTN_DEL = (By.XPATH, '//*[@class="el-input__icon el-icon-circle-close el-input__clear"]')
    __BTN_CONFIRM_SECOND_PAGE = (By.XPATH, "//*[text()=' Confirm ']")
    __IPT_DISSCOUNT_TYPE = (By.CSS_SELECTOR, 'input[placeholder="Discount Type"]')
    __PERCENTAGE = (By.CSS_SELECTOR, 'input[placeholder="Percentage off(%)"]')
    __APPLICATION_METHOD = (By.CSS_SELECTOR, 'input[placeholder="Application Method"]')
    __BTN_SUBMIT = (By.CSS_SELECTOR, 'button[data-test="submit"]')
    __BTN_CONFIRM = (By.XPATH, '//*[@class="el-message-box"]/div[3]/button[2]')
    '''列表页面'''
    #点击新建按钮
    def click_create_promotion(self):
        self.wait_element_until_clickable(self.__CREATE_PROMOTION)
        self.do_find(self.__CREATE_PROMOTION).click()
        return self

    # 点击其中一个promotion的编辑按钮修改里面的信息
    def click_promotion_edit(self, name):
        __BTN_EDIT = (
        By.XPATH, f"//*[@class='createtable']/div[2]/div[3]/table//*[text()='{name}']/../../../..//*[text()='Edit']")
        # print(self.do_find(__BTN_EDIT))
        self.hover(__BTN_EDIT)
        # self.wait_element_until_visible(__BTN_EDIT)
        # self.do_find(__BTN_EDIT).click()
        return self

    # 点击view按钮
    def click_view(self, promotion_name):
        __BTN_VIEW = (By.XPATH,
                      f"//*[@class='createtable']/div[2]/div[3]/table//*[text()='{promotion_name}']/../../../..//*[text()='View']")
        self.hover(__BTN_VIEW)
        # self.do_find(__BTN_VIEW).click()
        return self


    # confirm成功的信息
    def confirm_info(self):
        self.wait_element_until_visible(self.__CONFIRM_INFO)
        text = self.do_find(self.__CONFIRM_INFO).text
        return text

    '''编辑页面'''

    def edit_name_zn(self, name):
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

    # 点击确认按钮
    def click_btn_confirm(self):
        self.wait_element_until_visible(self.__BTN_SUBMIT)
        self.do_find(self.__BTN_SUBMIT).click()
        self.wait_element_until_clickable(self.__BTN_CONFIRM)
        self.do_find(self.__BTN_CONFIRM).click()
        return self

    #创建promotion
    def fill_in_promotion(self, name_en, name_cn):
        __SHOP = (By.XPATH, "//span[text()='Ulu Ulu eShop']")
        __CHANNEL = (By.XPATH, "//span[text()='App']")
        __PROMOTION_TYPE = (By.XPATH, "//span[text()='Discount Promotion']")
        __SELLABLE_TYPE = (By.XPATH, '//*[@class="el-select-dropdown__item select-option-item-el"]/span[text()="Product"]')
        __IPT_BOX = (By.XPATH, "//span[text()='青菜']/../../../../td[1]//label")
        __IPT_DISSCOUNT_TYPE = (By.XPATH, "//*[text()='Percentage off(%)']")
        __APPLICATION_METHOD = (By.XPATH, "//*[text()='Automatic']")
        self.hover(self.__IPT_NAME_EN)
        self.action_send_key(name_en)
        self.hover(self.__IPT_NAME_CN)
        self.action_send_key(name_cn)
        self.hover(self.__IPT_SHOP)
        time.sleep(1)
        self.hover(__SHOP)
        # self.action_send_key('Ulu Ulu eShop')
        time.sleep(1)
        self.hover(self.__IPT_CHANNEL)
        # self.action_send_key('App')
        self.hover(__CHANNEL)
        self.hover(self.__IPT_PROMOTION_TYPE)
        # self.action_send_key('Discount Promotion')
        self.hover(__PROMOTION_TYPE)
        self.hover(self.__IPT_SELLABLE_TYPE)
        # self.action_send_key('Product')
        self.hover(__SELLABLE_TYPE)
        self.hover(self.__BTN_SELLABLE_TYPE)
        self.hover(__IPT_BOX)
        # self.hover(__IPT_BOX)
        # self.do_find(self.__IPT_BOX).click()
        self.wait_element_until_visible(self.__BTN_CONFIRM_SECOND_PAGE)
        self.do_find(self.__BTN_CONFIRM_SECOND_PAGE).click()
        self.hover(self.__IPT_DISSCOUNT_TYPE)
        self.hover(__IPT_DISSCOUNT_TYPE)
        self.hover(self.__PERCENTAGE)
        self.action_send_key('10')
        self.hover(self.__APPLICATION_METHOD)
        self.hover(__APPLICATION_METHOD)
        time.sleep(5)
        return self



    '''详情页面'''

    def get_promotion_info(self):
        __INFO = (By.XPATH, '//div[@class="display-between"]/span')
        current = self.get_current_url()
        promotion_id = re.search(r"[0-9]*$", current).group()
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
        print(content)
        print(promotion_id)
        return content, str(promotion_id)

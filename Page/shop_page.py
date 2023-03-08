import re
import time

from selenium.webdriver.common.by import By

from c2_cms.Page.base_page import BasePage


class ShopPage(BasePage):
    _BASE_URL = 'https://msi-c2-cms.fooyo.shop/#/shops'
    # 列表页面
    __CONFIRM_INFO = (By.XPATH, "//*[text()='Operate Success!']")
    __CREATE_SHOP = (By.XPATH, "//*[text()=' Create New ']")
    __BTN_LIST_CONFIRM = (By.XPATH, "//*[contains(text(),'Confirm')]")
    # 编辑页面
    __IPT_NAME_CN = (
        By.XPATH, '//*[@class="el-collapse formily-element-form-collapse"]/div[1]//input[@ placeholder="Name(CN)"]')
    __IPT_NAME_EN = (By.XPATH, '//*[@class="el-collapse formily-element-form-collapse"]/div[1]//input[@ placeholder="Name(EN)"]')
    __BTN_DEL = (By.XPATH, '//*[@class="el-input__icon el-icon-circle-close el-input__clear"]')
    __INT_PICTURE = (By.CSS_SELECTOR, '[class="el-upload__input"]')
    __BTN_CONFIRM = (By.XPATH, "//*[text()='Confirm']")

    '''列表页面 '''

    # 点击其中一个shop的编辑按钮修改里面的信息
    def click_shop_edit(self, name):
        __BTN_EDIT = (
            By.XPATH,
            f"//*[@class='createtable']/div[2]/div[3]/table//*[text()='{name}']/../../../..//*[text()='Edit']")
        print(self.do_find(__BTN_EDIT))
        self.hover(__BTN_EDIT)
        # self.wait_element_until_visible(__BTN_EDIT)
        # self.do_find(__BTN_EDIT).click()
        return self

    # 点击view按钮
    def click_shop_view(self, name):
        __BTN_VIEW = (By.XPATH,
                      f"//*[@class='createtable']/div[2]/div[3]/table//*[text()='{name}']/../../../..//*[text()='View']")
        self.hover(__BTN_VIEW)
        # self.do_find(__BTN_VIEW).click()
        return self

    # confirm成功的信息
    def confirm_info(self):
        self.wait_element_until_visible(self.__CONFIRM_INFO)
        text = self.do_find(self.__CONFIRM_INFO).text
        return text

    #点击创建shop的按钮
    def click_create_shop(self):
        self.wait_element_until_clickable(self.__CREATE_SHOP)
        self.do_find(self.__CREATE_SHOP).click()
        return self

    #点击删除按钮
    def click_delete_shop(self,name):
        __BTN_DELETE = (By.XPATH,
                      f"//*[@class='createtable']/div[2]/div[3]/table//*[text()='{name}']/../../../..//*[text()='Delete']")
        # self.wait_element_until_clickable(__BTN_DELETE)
        # self.do_find(__BTN_DELETE).click()
        self.hover(__BTN_DELETE)
        return self

    #点击restore按钮
    def click_restore_shop(self, name):
        __BTN_RESTORE = (By.XPATH, f"//*[@class='createtable']/div[2]/div[3]/table//*[text()='{name}']/../../../..//*[text()='Restore']")
        self.hover(__BTN_RESTORE)
        return self

    #点击下架按钮
    def click_inactive_shop(self, name):
        __INACTIVE = (By.XPATH, f"//*[@class='createtable']/div[2]/div[3]/table//*[text()='{name}']/../../../../td[5]//input")
        self.hover(__INACTIVE)
        return self

    #切换不同的tab
    def click_top_tab(self, name):
        __TAB = (By.XPATH, f"//*[@class='el-tabs__nav is-top']//*[contains(text(),'{name}')]")
        # self.wait_element_until_clickable(__TAB)
        # self.do_find(__TAB).click()
        self.hover(__TAB)
        return self

    #得到不同的shop名
    def get_shop_name(self, name):
        __NAME = (By.XPATH, f"//*[@class='createtable']/div[2]/div[3]/table//*[text()='{name}']")
        self.wait_element_until_visible(__NAME)
        content = self.do_find(__NAME).text
        return content

    #点击确认按钮
    def click_list_confirm(self):
        self.wait_element_until_clickable(self.__BTN_LIST_CONFIRM)
        self.do_find(self.__BTN_LIST_CONFIRM).click()
        return self

    '''编辑页面'''
    #编辑名字
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
        self.wait_element_until_visible(self.__BTN_CONFIRM)
        self.do_find(self.__BTN_CONFIRM).click()
        return self

    # 创建shop
    def fill_create_shop(self,name_en,name_cn):
        self.hover(self.__IPT_NAME_EN)
        self.action_send_key(name_en)
        self.hover(self.__IPT_NAME_CN)
        self.action_send_key(name_cn)
        self.do_send_files('/Users/liaowei/PycharmProjects/MSI/c2_cms/Data/sell.jpeg' ,self.__INT_PICTURE)
        time.sleep(4)
        return self



    '''详情页面'''
    #获取详情页面的数据
    def get_shop_info(self):
        __INFO = (By.XPATH, '//div[@class="display-between"]/span')
        current = self.get_current_url()
        shop_id = re.search(r"[0-9]*$", current).group()
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
        print(shop_id)
        return content, shop_id



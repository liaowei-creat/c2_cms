import re
import time

from selenium.webdriver.common.by import By

from c2_cms.Page.base_page import BasePage


class ChannelPage(BasePage):
    _BASE_URL = 'https://msi-c2-cms.fooyo.shop/#/channels'
    # 列表页面
    __CONFIRM_INFO = (By.XPATH, "//*[text()='Operate Success!']")
    # 编辑页面
    __IPT_NAME_CN = (
        By.XPATH, '//*[@class="el-collapse formily-element-form-collapse"]/div[1]//input[@ placeholder="Name"]')
    __BTN_DEL = (By.XPATH, '//*[@class="el-input__icon el-icon-circle-close el-input__clear"]')
    __BTN_CONFIRM = (By.XPATH, "//*[text()='Confirm']")

    '''列表页面'''

    # 点击其中一个channel的编辑按钮修改里面的信息
    def click_channel_edit(self, name):
        __BTN_EDIT = (
            By.XPATH,
            f"//*[@class='createtable hiddenCheckAll']/div[2]/div[3]/table//*[text()='{name}']/../../../..//*[text()='Edit']")
        print(self.do_find(__BTN_EDIT))
        self.hover(__BTN_EDIT)
        # self.wait_element_until_visible(__BTN_EDIT)
        # self.do_find(__BTN_EDIT).click()
        return self

    # 点击view按钮
    def click_channel_view(self, name):
        __BTN_VIEW = (By.XPATH,
                      f"//*[@class='createtable hiddenCheckAll']/div[2]/div[3]/table//*[text()='{name}']/../../../..//*[text()='View']")
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
        self.wait_element_until_visible(self.__BTN_CONFIRM)
        self.do_find(self.__BTN_CONFIRM).click()
        return self

    '''详情页面'''

    def get_channel_info(self):
        __INFO = (By.XPATH, '//div[@class="display-between"]/span')
        current = self.get_current_url()
        channel_id = re.search(r"[0-9]*$", current).group()
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
        print(channel_id)
        return content, channel_id
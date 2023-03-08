import os
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Utils:

    @classmethod
    def get_yaml_data(cls, file):
        '''
        封装yaml读取
        :param file_path: 文件路径
        :return: 返回yaml数据体
        '''
        with open(Utils.get_data_root_path() + '/' + file, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def get_data_root_path(self):
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Data'
        # return os.path.abspath(__file__)


if __name__ == '__main__':
    print(Utils.get_data_root_path())
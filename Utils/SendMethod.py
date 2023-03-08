"""
文件名: SendMethod.py
根据接口文档,分析具体使用的方法
- 请求地址
- 请求方式: GET POST
- 请求参数:
    GET请求参数: requests.get(url,params)
    POST请求参数:
        - 无参数: requests.post(url)
        - x-www-form-urlencoded: requests.post(url,data)
        - json: requests.post(url,json)
- 返回值
    response.json()
"""

import requests


class SendMethod:
    @staticmethod
    def send_method(method, url, params=None, data=None, json=None, headers=None):
        """
        封装项目请求方式
        :param method: 请求方式
        :param url: 请求地址
        :param params: 接收GET请求参数
        :param data: 接收POST请求x-www-form-urlencoded格式参数
        :param json: 接收POST请求json格式数据
        :param headers: 请求头
        :return:响应结果
        """
        # 1. 封装请求方式
        if method == "get":  # 请求方式为get
            # response接收请求返回
            if params is not None:
                response = requests.get(url=url, params=params, headers=headers)
            else:
                response = requests.get(url=url, headers=headers)  # get请求不带参数
        elif method == "post":  # 请求方式为post
            if data is None and json is None:  # 不带参数的post请求
                response = requests.post(url=url, headers=headers)
            elif data is not None and json is None:  # 请求参数为x-www-form-urlencoded
                response = requests.post(url=url, data=data, headers=headers)
            elif data is None and json is not None:  # 请求参数为json
                response = requests.post(url=url, json=json, headers=headers)
            else:
                print('请求参数错误')
                return None
        else:
            print('请求方式错误')
            return None

        # 2. 获取响应
        result = dict()
        result['status_code'] = response.status_code  # 状态码
        result['body'] = response.json()  # 响应体
        result['headers'] = response.headers  # 响应头
        result['response_time'] = int(response.elapsed.microseconds / 1000)  # 响应时间
        return result


if __name__ == '__main__':
    method = "post"
    url = 'http://139.159.146.104:8082/admin/login'
    payload = {
        "password": "macro123",
        "username": "admin"
    }
    print(SendMethod.send_method(method=method, url=url, json=payload))

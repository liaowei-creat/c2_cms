"""
文件名：GetKeyword.py
作用：获取json格式返回值中具体字段值
1.根据字典键获取对应的值
2.使用jsonpath库   pip install jsonpath
    jsonpath    专门用来获取json格式数据中的字段值
    jsonpath.jsonpath(数据源，jsonpath表达式)
        - 数据源：json格式的数据
        - jsonpath表达式：$..字段名称   $..token    $..code
"""
import jsonpath


class GetKeyword:
    @staticmethod
    def get_keyword(source_data, keyword):
        """
        获取关键字对应的值，如果有多个值，默认取第一个，如果没有就返回False
        :param source_data: 数据源
        :param keyword: 关键字
        :return:
        """
        try:
            return jsonpath.jsonpath(source_data, f'$..{keyword}')[0]
        except:
            print(f'关键字{keyword}不存在')
            return False

    @staticmethod
    def get_keywords(source_data, keyword):
        """
        获取关键字对应的所有值
        :param source_data: 数据源
        :param keyword: 关键字
        :return:
        """
        try:
            return jsonpath.jsonpath(source_data, f'$..{keyword}')
        except:
            print(f'关键字{keyword}不存在')
            return False


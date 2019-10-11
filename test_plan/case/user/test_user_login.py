import unittest  # 导入unittest
import requests
from lib.read_excel import *
import json,os
from lib.case_log import *
from config.config import *
from test_plan.case.basecase import BaseCase

class TestUserLogin(BaseCase):  # 类必须Test开头，继承TestCase才能识别为用例类
    #url = 'http://115.28.108.130:5000/api/user/login/'
    data_file = os.path.join(data_path,'test_case.xlsx')
    # @classmethod
    # def setUpClass(cls):
    #     cls.data_list = excel_to_list(os.path.join(data_path,'test_case.xlsx'),cls.__name__)

    def test_user_login_normal(self):  # 一条测试用例，必须test_开头
        '''level1:正常登录'''
        case_data = self.get_case_data('test_user_login_normal')

        if not case_data:
            #print('测试用例不存在')
            logging.error('测试用例不存在')
        self.send_request(case_data)
        # url = case_data.get('url')
        # data = case_data.get('data')
        # expect_res = case_data.get('expect_res')
        # res = requests.post(url=url, data=json.loads(data))
        # log_case_info('test_user_login_normal',url,data,expect_res,res.text)
        # self.assertEqual(expect_res, res.text)  # 断言
    #@unittest.skip('hh')
    def test_user_login_password_wrong(self):
        '''level2:异常登录'''
        case_data = self.get_case_data('test_user_login_password_wrong')
        if not case_data:
            #print('测试用例不存在')
            logging.error('测试用例不存在')
        self.send_request(case_data)
        # data = {"name": "张三", "password": "1234567"}
        # res = requests.post(url=self.url, data=data)
        # self.assertIn('登录失败', res.text)  # 断言


if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)  # 运行本测试类所有用例,verbosity为结果显示级别
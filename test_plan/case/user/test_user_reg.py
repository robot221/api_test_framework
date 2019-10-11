import unittest,requests,json,os
from lib.db import DB
from config.config import *
from test_plan.case.basecase import BaseCase

class TestUserReg(BaseCase):
    #url = 'http://115.28.108.130:5000/api/user/reg/'
    db = DB()
    data_file = os.path.join(data_path,'test_case.xlsx')
    def test_user_reg_normal(self):
        case_data = self.get_case_data('test_user_reg_normal')
        user_name = json.loads(case_data.get('args')).get('name')

        #环境检查
        if self.db.check_user(user_name):
            self.db.del_user(user_name)
        #发送数据

        self.send_request(case_data)
        # data = {'name':NOT_EXIST_USER,'password':'123456'}
        # res = requests.post(url=self.url,json=data)
        # #print(res.json())
        # except_res = {
        #     "code": "100000",
        #     "msg": "成功",
        #     "data": {
        #         "name": NOT_EXIST_USER,
        #         "password": "e10adc3949ba59abbe56e057f20f883e"
        #     }
        # }
        #
        # #响应断言
        # self.assertDictEqual(res.json(),except_res)

        #数据库断言
        self.assertTrue(db.check_user(user_name))

        # 环境清理（由于注册接口向数据库写入了用户信息）
        db.del_user(user_name)

    def test_user_reg_exist(self):
        case_data = self.get_case_data('test_user_reg_exist')
        user_name = json.loads(case_data.get('args')).get('name')
        #环境检查
        if not self.db.check_user(user_name):
            self.db.add_user(user_name)

        # 发送数据

        self.send_request(case_data)
        # data = {'name': EXIST_USER, 'password': '123456'}
        # res = requests.post(url=self.url, json=data)
        # #print(res.json())
        # # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        # except_res = {
        #     "code": "100001",
        #     "msg": "失败，用户已存在",
        #     "data": {
        #         "name": EXIST_USER,
        #         "password": "e10adc3949ba59abbe56e057f20f883e"
        #     }
        # }
        #
        # # 响应断言
        # self.assertDictEqual(res.json(), except_res)

        # 数据库断言(没有注册成功，数据库没有添加新用户)

        # 环境清理（无需清理）

if __name__ == '__main__':
    unittest.main(verbosity=2)
import unittest
import sys
sys.path.append("../..")
from test_plan.case.user.test_user_reg import TestUserReg
from test_plan.case.user.test_user_login import TestUserLogin

smoke_suite = unittest.TestSuite()
smoke_suite.addTests([TestUserLogin('test_user_login_normal'), TestUserReg('test_user_reg_normal')])

def get_suite(suite_name):    # 获取TestSuite方法
    return globals().get(suite_name)

if __name__ == '__main__':
    print(get_suite('smoke_suite'))
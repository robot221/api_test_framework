from config.config import *
import json

def log_case_info(case_name,url,data,expect_res,res_txt):
    '''

    :param case_name: 用例名称
    :param url: 请求地址
    :param data: 请求数据
    :param expect_res: 期望结果
    :param res_txt: 实际结果
    :return: None
    '''
    logging.info(f'测试用例：{case_name}')
    logging.info(f'url：{url}')
    logging.info(f'请求参数：{data}')
    logging.info(f'期望结果：{expect_res}')
    logging.info(f'实际结果：{res_txt}')
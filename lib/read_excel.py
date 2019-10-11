import xlrd

def excel_to_list(data_file,sheet_name):
    book = xlrd.open_workbook(data_file)
    sheet = book.sheet_by_name(sheet_name)
    rows = sheet.nrows
    cols = sheet.ncols
    headers = sheet.row_values(0)
    data_list = []
    for row in range(1,rows):
        data_list.append(dict(zip(headers,sheet.row_values(row))))

    return data_list

def get_test_data(data_list,case_name):
    for case_item in data_list:
        if case_item['case_name'] == case_name:
            return case_item

    return None

if __name__ == '__main__':   # 测试一下自己的代码
    data_list = excel_to_list("test_case.xlsx", "TestUserLogin")  # 读取excel，TestUserLogin工作簿的所有数据
    case_data = get_test_data(data_list, 'test_user_login_normal')  # 查找用例'test_user_login_normal'的数据
    print(case_data)
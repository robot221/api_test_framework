import logging
import os,time
from optparse import OptionParser

today = time.strftime('%Y%m%d',time.localtime())
now = time.strftime('%Y%m%d_%H%M%S',time.localtime())
# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的绝对路径的上一级，__file__指当前文件

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test_plan')  # 测试目录
case_path = os.path.join(test_path, 'case')  # 用例目录
log_file = os.path.join(prj_path, 'log', 'log_{}.txt'.format(today))  # 也可以每天生成新的日志文件
report_file = os.path.join(prj_path, 'report', 'report_{}.html'.format(now))  # 也可以每次生成新的报告
testlist_file = os.path.join(test_path, 'testlist.txt')
last_fails_file = os.path.join(case_path, 'last_fails.txt')

#日志配置
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s,%(lineno)d] %(message)s', #log格式
                    datefmt='%Y-%m-%d %H:%M:%S', # 日期格式
                    filename=log_file, # 日志输出文件
                    filemode='a' # 追加模式
)

# 数据库配置
db_host = '127.0.0.1'   # 自己的服务器地址
db_port = 3306
db_user = 'rib'
db_passwd = 'rib'
db = 'icop_xxgj'

# 邮件配置

smtp_server = 'smtp.163.com'
smtp_user = 'dxs86@163.com'
smtp_password = 'dxs8806'

sender = smtp_user  # 发件人
receiver = '282497745@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题

send_email_after_run = False
#命令行选项
parser = OptionParser()
parser.add_option('--collect-only',action='store_true',dest='collect_only',help='仅列出所有用例')
parser.add_option('--rerun-fails',action='store_true',dest='rerun_fails',help='运行上次失败的用例')
parser.add_option('--testlist',action='store_true',dest='testlist',help='运行test/testlist.txt列表指定用例')

parser.add_option('--testsuite',action='store',dest='testsuite',help='运行指定的TestSuite')
parser.add_option('--tag',action='store',dest='tag',help='运行指定tag的用例')

(options,arges) = parser.parse_args()

if __name__ == '__main__':
    print(prj_path)

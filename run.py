import unittest,time
from HTMLTestRunner import HTMLTestRunner
from config.config import *
from lib.send_mail import send_email
from test_plan.suite.test_suites import *
import pickle
def discover():
    suite = unittest.defaultTestLoader.discover(case_path)
    return suite
def save_failures(result,file):
    suite = unittest.TestSuite()
    for case_failure in result.failures:
        suite.addTest(case_failure[0])
    with open(file,'wb') as f:
        pickle.dump(suite,f)

def run(suite):
    logging.info("================================== 测试开始 ==================================")
    # suite = unittest.defaultTestLoader.discover(case_path)  # 从配置文件中读取用例路径

    with open(report_file, 'wb') as f:  # 从配置文件中读取
        result = HTMLTestRunner(stream=f, title="Api Test", description="测试描述").run(suite)
    if result.failures:
        save_failures(result,last_fails_file)
    if send_email_after_run:
        send_email(report_file)  # 从配置文件中读取
    logging.info("================================== 测试结束 ==================================")

def run_all():
    run(discover())

def run_suite(suite_name):
    suite = get_suite(suite_name)
    run(suite)

def rerun_fails():
    with open(last_fails_file,'rb') as f:
        suite = pickle.load(f)
    run(suite)

def collect():
    suite = unittest.TestSuite()

    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)

    _collect(discover())
    return suite

def collect_only():
    '''仅列出用例列表，不执行'''
    start = time.time()
    cases = collect()
    for i,case in enumerate(cases):
        print('{}.{}'.format(str(i+1),case.id()))
    print('----------------------------------')
    print('Collect {} tests is {:.3f}s'.format(cases.countTestCases(),time.time()-start))


def makesuite_by_testlist(testlist_file):
    suite = unittest.TestSuite()
    with open(testlist_file,'r') as f:
        list = f.readlines()
    list = [i.strip() for i in list if not i.startswith('#')]

    for case in collect():
        if case._testMethodName in list:
            suite.addTest(case)

    return suite

def makesuite_by_tag(tag):
    suite = unittest.TestSuite()
    allcases = collect()
    for case in allcases:
        if case._testMethodDoc and tag in case._testMethodDoc:
            suite.addTest(case)
    return suite

# def run_testlist(testlist_file):
#     suite = makesuite_by_testlist(testlist_file)
#     run(suite)

def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.testlist:
       run(makesuite_by_testlist(testlist_file))
    elif options.testsuite:
        run_suite(options.testsuite)
    elif options.tag:
        run(makesuite_by_tag(options.tag))
    else:
        run_all()

if __name__ == '__main__':
    main()
    #run_suite('smoke_suite')
    #rerun_fails()
    #collect_only()
    #print(makesuite_by_testlist(testlist_file))
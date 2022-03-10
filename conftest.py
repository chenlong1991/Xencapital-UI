# -*-coding:utf-8 -*-
import os

import allure
import pytest
from os import environ

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from pageobjects.login_page import LoginPage
from common.basepage import BasePage

from common.tools import logger, conf_get

_driver = None


@pytest.fixture(scope='function')
def lambdatest_driver(request):
    # desired_caps = {}
    #
    # browser = {
    #     "platform": "Windows 10",
    #     "browserName": "chrome",
    #     "version": "73"
    # }
    #
    # desired_caps.update(browser)
    # test_name = request.node.name
    # build = '测试001'
    # username = environ.get('LT_USERNAME', None)
    # access_key = environ.get('LT_ACCESS_KEY', None)
    #
    # selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    # desired_caps['build'] = build
    # desired_caps['name'] = test_name
    global _driver
    desired_caps = {
        "platform": "Windows 10",
        "browserName": "chrome",
        "version": "73",
        'build': '测试001',
        'name': request.node.name
    }

    username = environ.get('LT_USERNAME', None)
    access_key = environ.get('LT_ACCESS_KEY', None)

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    if _driver is None:
        _driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=desired_caps
        )
    yield _driver

    def fin():
        if request.node.rep_call.failed:
            _driver.execute_script("lambda-status=failed")
        else:
            _driver.execute_script("lambda-status=passed")
            _driver.quit()

    request.addfinalizer(fin)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数,添加用例失败截图功能实现
    :param item: 测试用例
    :param call: 测试步骤
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode, encoding='utf-8') as f:
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write((rep.nodeid + extra + "\n"))
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('用例执行失败时，添加失败截图...'):
                logger.error("用例执行失败，捕获当前页面......")
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


def pytest_collection_modifyitems(items):
    # 解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


# @pytest.fixture(scope='class')
# def _driver():
#     global _driver
#     try:
#         if _driver is None:
#             chrome_options = webdriver.ChromeOptions()
#             # 无浏览器模式
#             chrome_options.add_argument('--headless')
#             chrome_options.add_argument('--disable-dev-shm-usage')
#             # 以最高权限运行
#             chrome_options.add_argument('--no-sandbox')
#             # 谷歌文档提到需要加上这个属性来规避bug
#             chrome_options.add_argument('--disable-gpu')
#             # 最大化启动
#             # chrome_options.add_argument('--start - maximized')
#             chrome_options.add_argument('window-size=1920x1080')
#             _driver = webdriver.Chrome(chrome_options=chrome_options)
#             # 隐式等待
#             _driver.implicitly_wait(10)
#             logger.info('初始化driver')
#             logger.info(_driver)
#
#         yield _driver
#         logger.info('关闭浏览器')
#         _driver.quit()
#     except Exception as e:
#         logger.error('初始化driver错误{}'.format(e))
#         raise

@pytest.fixture(scope='session')
def driver():
    global _driver
    try:
        # options = webdriver.ChromeOptions()
        # options.add_argument('window-size=1680x1050')
        # _driver = webdriver.Chrome(chrome_options=options)
        _driver = webdriver.Chrome()
        _driver.set_window_size(1680, 1050)
        # 最大化浏览器
        # _driver.maximize_window()
        # 隐式等待
        _driver.implicitly_wait(10)
        logger.info('初始化driver')
        yield _driver
        # logger.info('关闭浏览器')
        _driver.quit()
    except Exception as e:
        logger.error('初始化driver错误{}'.format(e))
        raise


@pytest.fixture()
def admin_driver(driver):
    """
    admin用户登录
    """
    email = conf_get('arocarret', 'admin_email')
    password = conf_get('arocarret', 'admin_password')
    logger.info('读取用户名:{}，密码:{}'.format(email, password))
    LoginPage(driver).login(email, password)
    yield driver


@pytest.fixture()
def investor_driver(driver):
    """
    investor用户登录
    """
    email = conf_get('arocarret', 'investor_email')
    password = conf_get('arocarret', 'investor_password')
    logger.info('读取用户名: {}，密码: {}'.format(email, password))
    LoginPage(driver).login(email, password)
    yield driver

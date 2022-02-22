# -*-coding:utf-8 -*-
import os

import allure
import pytest
from os import environ

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from common.tools import logger

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
    获取每个用例状态的钩子函数
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
        with open("failures", mode) as f:
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


@pytest.fixture(scope='class')
def driver():
    global _driver
    try:
        if _driver is None:
            chrome_options = webdriver.ChromeOptions()
            # 以最高权限运行
            chrome_options.add_argument('--no-sandbox')
            # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--disable-gpu')
            # 最大化启动
            chrome_options.add_argument('--start - maximized')
            _driver = webdriver.Chrome()
            # 隐式等待
            _driver.implicitly_wait(10)
            logger.info('初始化driver')
        yield _driver
        logger.info('关闭浏览器')
        _driver.quit()
    except Exception as e:
        logger.info('初始化driver错误{}'.format(e))
        raise

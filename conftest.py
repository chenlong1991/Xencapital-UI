# -*-coding:utf-8 -*-
import pytest
from os import environ

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from common.tools import logger


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
    browser = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=desired_caps
    )
    yield browser

    def fin():
        if request.node.rep_call.failed:
            browser.execute_script("lambda-status=failed")
        else:
            browser.execute_script("lambda-status=passed")
            browser.quit()

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


@pytest.fixture(scope='class')
def driver():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        logger.info('初始化driver')
        yield driver
        logger.info('关闭浏览器')
        driver.quit()
    except Exception as e:
        logger.info('初始化driver错误{}'.format(e))
        raise

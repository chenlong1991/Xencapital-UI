# -*-coding:utf-8 -*-

"""
登录测试用例
"""
import allure
import pytest
from pagelocator.login_page_loc import LoginPageLoc as loc
from testdata.login_data import data
from common.tools import logger
import time
from pageobjects.login_page import LoginPage


@allure.feature('登录功能')
class TestLogin:
    @pytest.mark.parametrize('title, email, password, checkpoint', data)
    @allure.story('老用户登录')
    @allure.title('{title}')
    @allure.testcase('https://www.baidu.com', name='对应功能测试用例')
    @allure.severity("normal")
    def test_login(self, driver, title, email, password, checkpoint):
        login_page = LoginPage(driver)
        login_page.login(email, password)
        logger.info('断言预期结果')
        assert login_page.wait_ele_visible(checkpoint, timeout=10)

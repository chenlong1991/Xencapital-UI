# -*-coding:utf-8 -*-

"""
登录测试用例
"""
import allure
import pytest
from testdata.auth_data import test_login_data
from common.tools import logger
from pageobjects.login_page import LoginPage


@allure.feature('Auth')
class TestAuth:
    @pytest.mark.parametrize('title, email, password, checkpoint', test_login_data)
    @allure.story('Old user login')
    @allure.title('{title}')
    @allure.testcase(r'http://www.baidu.com', name='对应功能测试用例')
    @allure.severity("normal")
    def test_login(self, driver, title, email, password, checkpoint):
        login_page = LoginPage(driver)
        login_page.login(email, password)
        logger.info('断言预期结果')
        assert login_page.wait_ele_visible(checkpoint, timeout=10)

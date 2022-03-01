# -*-coding:utf-8 -*-
"""
登录页面
"""
import allure

from common.basepage import BasePage
from pagelocator.login_page_loc import LoginPageLoc as loc
from common.tools import logger


class LoginPage(BasePage):

    def login(self, email, password):
        """
        输入邮件密码登录操作
        :param email: 账号
        :param password: 密码
        :return:
        """
        logger.info('-------------------执行登录操作------------------')
        with allure.step("打开网址：{}".format(loc.url)):
            self.open_url(loc.url)
        with allure.step("输入账号"):
            self.wait_ele_visible(loc.email_address)
            self.input_text(loc.email_address, email)
        with allure.step("输入密码"):
            self.input_text(loc.password, password)
        with allure.step("点击登录按钮"):
            self.click(loc.login_button)

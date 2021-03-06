# -*-coding:utf-8 -*-
"""
登录页面元素定位
"""
from common.tools import url


class LoginPageLoc:
    # 登录地址
    url = r'https://accounts.stg.xencapital.com/login?locale=en&originId=arocarret&redirect_url=https%3A%2F%2F{}%2F%23%2F'.format(url)
    email_address = ('xpath', "//div[@label='Input your email address']//input")
    password = ('xpath', '//input[@autocomplete="new-password"]')
    login_button = ('xpath', "//button[@type='submit']")

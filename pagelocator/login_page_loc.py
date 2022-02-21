# -*-coding:utf-8 -*-
"""
登录页面元素定位
"""


class LoginPageLoc:
    # 登录地址
    url = 'https://accounts.stg.xencapital.com/login?locale=en&originId=arocarret&redirect_url=https%3A%2F%2Farocarret.uat.xencapital.com%2F%23%2F'

    # 账号文本框
    email_address = ('xpath', "//div[@label='Input your email address']//input")

    # 密码文本框
    password = ('xpath', "//input[@id='input-38']")

    # 登录按钮
    login_button = ('xpath', "//button[@type='submit']")

    # 错误信息
    error_message = ('xpath', "//div[@class='v-snack__wrapper v-sheet theme--dark error']")

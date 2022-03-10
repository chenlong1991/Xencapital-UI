# -*-coding:utf-8 -*-
"""
登录相关测试数据
"""

# 测试用例：test_login 测试登录
test_login_data = [
    ('正确账号，密码', 'jack@xencapital.com', 'Pass1234_', ('xpath', "//span[@class='account-name']")),
    ('不填写密码', 'jack@xencapital.com', '', ('xpath', "//div[@label='Password']//div[text()='Mandatory field']")),
    ('账号为空', '', 'Pass1234_', ('xpath', "//div[@label='Input your email address']//div[text()='Mandatory field']")),
    ('账号格式不正确', '11111', 'Pass1234_', ('xpath', "//div[@label='Input your email address']//div[text()='Incorrect email format']"))
]

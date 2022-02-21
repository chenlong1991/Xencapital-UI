# -*-coding:utf-8 -*-


data = [
    ('正确账号，密码', 'jack@xencapital.com', 'Pass1234_', ('xpath', "//span[@class='account-name']")),
    ('不填写密码', 'jack@xencapital.com', '', ('xpath', "//div[@class='v-messages__message message-transition-enter-to' and text()='Mandatory field']")),
    ('账号为空', '', 'Pass1234_', ('xpath', "//div[@class='v-messages__message message-transition-enter-to' and text()='Mandatory field']")),
    ('账号格式不正确', '11111', 'Pass1234_', ('xpath', "//div[contains(text(),'Incorrect email format1')]"))
]

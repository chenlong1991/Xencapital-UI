# -*-coding:utf-8 -*-
"""
公共文件路径
"""

import os

# 当前项目路径
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


# log路径
def log_path():
    path = os.path.join(base_path, 'logs')
    if not os.path.exists(path):
        os.mkdir(path)
    return path


# 配置文件路径
conf_path = os.path.join(base_path, 'conf')

# 测试数据路径
test_data_path = os.path.join(base_path, 'testdata')

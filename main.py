# -*-coding:utf-8 -*-
import os

import pytest

if __name__ == '__main__':
    # report_path()
    pytest.main(['-s', '-v', '--alluredir', './report', '--clean-alluredir'])
    os.system('allure generate -c -o ./report/result ./report')
    os.system('allure open ./report/result')

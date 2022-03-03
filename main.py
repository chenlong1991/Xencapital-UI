# -*-coding:utf-8 -*-
import os

import pytest

if __name__ == '__main__':
    # report_path()
    pytest.main(['-k', 'test_create_products_check_required', '-s', '-v', '--alluredir', './report', '--clean-alluredir'])
    os.system('allure generate -c -o ./report/result ./report')
    os.system('allure open ./report/result')

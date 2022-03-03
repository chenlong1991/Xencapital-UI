# -*-coding:utf-8 -*-

"""
Products测试用例
"""
import allure
import pytest
from testdata.products_data import test_create_products_check_required, test_create_products
from common.tools import logger
from pageobjects.products_list_page import ProductsDetailsPage
from pageobjects.products_details_page import ProductsPage
from pagelocator.products_details_page_loc import ProductsDetailsPageLoc as loc


@allure.feature('Products')
class TestProducts:
    @pytest.mark.parametrize('title, data', test_create_products_check_required)
    @allure.story('Create Products')
    @allure.title('{title}')
    @allure.testcase(r'https://xentesting.testrail.io/index.php?/tests/view/96&group_by=cases:section_id&group_order=asc&group_id=7', name='对应功能测试用例')
    @allure.severity("critical")
    def test_create_products_check_required(self, admin_driver, title, data):
        """
        创建Products，校验必填项
        """
        pdp = ProductsDetailsPage(admin_driver)
        pp = ProductsPage(admin_driver)
        pdp.create_products(data['products_type'], data['products_name'])
        for i in data['products_value']:
            pp.edit_products_details(i[0])
            assert pp.wait_ele_visible(i[1])
            logger.info('断言预期结果')

    @pytest.mark.parametrize('title, data', test_create_products)
    @allure.story('Create Products')
    @allure.title('{title}')
    @allure.testcase(r'https://xentesting.testrail.io/index.php?/tests/view/96&group_by=cases:section_id&group_order=asc&group_id=7', name='对应功能测试用例')
    @allure.severity("critical")
    def test_create_products(self, title, admin_driver, data):
        """
        创建Products并发布，校验是否成功
        """
        pdp = ProductsDetailsPage(admin_driver)
        pp = ProductsPage(admin_driver)
        pdp.create_products(data['products_name'], data['products_name'])

        pp.edit_products_details(data['fund_value'])
        logger.info('断言预期结果')
        assert pp.wait_ele_visible(loc.but_publish)

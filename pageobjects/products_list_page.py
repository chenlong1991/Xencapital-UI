# -*-coding:utf-8 -*-
"""
Products 列表页
"""

import allure

from common.basepage import BasePage
from pagelocator.products_list_page_loc import ProductsListPageLoc as loc
from common.tools import logger


class ProductsDetailsPage(BasePage):

    def create_products(self, products_type, products_name):
        """
        创建Products,不包括Products详情
        """
        logger.info('-------------------执行创建Products操作，不包括详情------------------')
        with allure.step("点击【create】按钮。选择{}，输入Products名称，点击【create】".format(products_type)):
            self.wait_ele_visible(loc.menu_products)
            self.open_url(loc.url)
            self.wait_ele_clickable(loc.btn_create)
            self.click(loc.btn_create)
            if products_type == 'Fund':
                self.click(loc.btn_fund)
            else:
                self.click(loc.btn_company)
            self.input_text(loc.input_productName, products_name)
            self.click(loc.btn_create_)

    def search_products(self, product_name):
        """
        根据product_name查询列表
        """
        logger.info('-------------------执行查找Products操作------------------')
        with allure.step("根据名称查找Products"):
            self.wait_ele_visible(loc.menu_products)
            self.open_url(loc.url)
            self.click(loc.but_search_product_name)
            self.input_text(loc.but_search_product_name, product_name)
            self.click(loc.but_search)
            if self.get_text(loc.list_product_name) == product_name:
                logger.info('查找到{}'.format(product_name))
                return loc.list_product_name
            else:
                logger.info('没有查找到{}'.format(product_name))
                return False

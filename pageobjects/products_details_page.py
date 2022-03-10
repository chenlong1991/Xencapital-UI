# -*-coding:utf-8 -*-
"""
Products 详情页面
"""
import allure

from common.basepage import BasePage
from pagelocator.products_details_page_loc import ProductsDetailsPageLoc as loc
from common.tools import logger
import time


class ProductsPage(BasePage):

    def edit_products_details(self, products_info):
        """
        填写Products详细信息
        :param products_info: 字典格式，key元组格式，里面是控件类型和控件元素，value为输入的值或下拉列表的元素
        :return:
        """
        logger.info('------------------执行填写Products详细信息操作------------------')
        with allure.step("填写Products信息"):
            self.wait_ele_visible(loc.drop_assetClass)
            try:
                # 遍历edit Products详情页面元素
                for key, value in products_info.items():
                    # 判断值如果是空字符串执行清除文本操作
                    # 判断如果是文本框执行输入操作，如果是下拉框执行选择操作
                    self.sliding_window(key[1])
                    if key[0] == 'input':
                        if value == '':
                            self.backspace_all(key[1])
                        else:
                            self.input_text(key[1], value)
                    elif key[0] == 'drop':
                        if value == '':
                            self.backspace_all(key[1])
                            self.click(loc.box_products_details)
                        else:
                            self.click(key[1])
                            self.click(value)
                    elif key[0] == 'check':
                        self.click(key[1])
                        if value == '':
                            self.backspace(key[2])
                        else:
                            self.click(value)
                        self.click(key[1])
                    else:
                        logger.error('控件类型错误')
            except Exception as e:
                logger.error('填写Products信息错误：{}'.format(e))
                raise

        with allure.step("点击Save按钮"):
            self.click(loc.but_save)

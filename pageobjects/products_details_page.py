# -*-coding:utf-8 -*-
"""
Products 详情页面
"""
import allure

from common.basepage import BasePage
from pagelocator.products_details_page_loc import ProductsDetailsPageLoc as loc
from common.tools import logger


class ProductsPage(BasePage):

    def input_fund_details(self, products_value):
        """
        填写Products详细信息
        :param products_value:列表，输入值或者下拉列表元素
        :return:
        """
        logger.info('------------------执行填写Fund详细信息操作------------------')
        products_loc = [
            ('input', loc.input_productName),
            ('drop', loc.drop_assetClass),
            ('drop', loc.drop_currency),
            ('input', loc.input_fundSize),
            ('drop', loc.drop_focus),
            ('input', loc.input_closingDate),
            ('drop', loc.drop_symbol),
            ('input', loc.input_expectedReturn),
            ('input', loc.input_minHoldingPeriod),
            ('input', loc.input_minimumInvestment),
            ('input', loc.input_vintage),
            ('input', loc.input_website),
            ('input', loc.input_fundManager),
            ('input', loc.input_vehicle),
            ('input', loc.input_minimumIncrement),
            ('drop', loc.drop_tags),
            ('input', loc.input_templateIdIndividual),
            ('input', loc.input_descriptionIndividual_en),
            ('input', loc.input_descriptionIndividual_ch),
            ('input', loc.input_templateIdEntity),
            ('input', loc.input_descriptionEntity_en),
            ('input', loc.input_descriptionEntity_ch)
        ]
        try:
            fund_info = dict(zip(products_loc, products_value))
        except Exception as e:
            logger.error('合并数据错误:{}'.format(e))
            raise

        with allure.step("填写Products信息"):
            self.wait_ele_visible(loc.drop_assetClass)
            # 遍历edit products详情页面元素
            for key, value in fund_info.items():
                if value == '':
                    self.clean_text(key[0])
                elif not value:
                    pass
                else:
                    if key[0] == 'input':
                        self.input_text(key[1], value)
                    else:
                        self.click(key[1])
                        self.click(value)
        with allure.step("点击Save按钮"):
            self.click(loc.but_save)

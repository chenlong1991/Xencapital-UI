# -*-coding:utf-8 -*-
"""
Products List Page元素定位
"""
from common.tools import url


class ProductsListPageLoc:
    url = r'https://{}/#/partners/fund-managers/listings?page=1&itemsPerPage=30'.format(url)
    menu_products = ('xpath', '//a[@href="#/partners/fund-managers/listings"]')
    btn_create = ('xpath', "//div[@class='main-box']/div/div/button")
    btn_fund = ('xpath', "//span[text()='Funds']")
    btn_company = ('xpath', "//span[. = 'Private Company']")
    btn_create_ = ('xpath', "//div[@role='document']//span[text()='Create']")
    input_productName = ('xpath', "//div[@label='Fund/Private Company Name']//input")
    but_search_product_name = ('xpath', "//div[text()='Product Name']")
    input_search_productName = ('xpath', "//div[@class='v-text-field__slot']")
    but_search = ('xpath', "//span[text()='Search']")
    list_product_name = ('xpath', "//span[contains(text(), 'Search')]")

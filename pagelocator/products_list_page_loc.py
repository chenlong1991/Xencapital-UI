# -*-coding:utf-8 -*-
"""
Products List Page元素定位
"""


class ProductsListPageLoc:

    url = 'https://arocarret.uat.xencapital.com/#/partners/fund-managers/listings?page=1&itemsPerPage=30'
    menu_products = ('xpath', '//a[@href="#/partners/fund-managers/listings"]')
    btn_create = ('xpath', "//div[@class='main-box']/div/div/button")
    btn_fund = ('xpath', "//span[contains(text(), 'Funds')]")
    btn_company = ('xpath', "//span[. = 'Private Company']")
    btn_create_ = ('xpath', "//div[@role='document']//span[contains(text(), 'Create')]")
    input_productName = ('xpath', "//div[@label='Fund/Private Company Name']//input")
    but_search_product_name = ('xpath', "//div[contains(text(),'Product Name')]")
    input_search_productName = ('xpath', "//div[@class='v-text-field__slot']")
    but_search = ('xpath', "//span[contains(text(), 'Search')]")
    list_product_name = ('xpath', "//span[contains(text(), 'Search')]")


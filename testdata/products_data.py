# -*-coding:utf-8 -*-
"""
Products测试相关数据
"""
from pagelocator.products_details_page_loc import ProductsDetailsPageLoc as loc
from common.tools import faker

# 正常的fund数据
test_create_products = [
    ('正常填写Fund信息',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'products_value':
          [
              None, loc.drop_assetClass_list1, loc.drop_currency_list1, 12000000, loc.drop_focus_list1, 25122025,
              loc.drop_symbol_list1, 12, 1000, 2022, 'xencapital.com', 'gary@xen.io', '1234', 100,
              '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '个人英文描述', '个人中文描述', '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '公司英文描述', '公司中文描述'
          ]
      })]

# 错误的fund数据
test_create_fund_check_required = [
    ('不选择assetClass',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'products_value':
          [
              None, None, loc.drop_currency_list1, 12000000,
              loc.drop_focus_list1, 25122025,
              loc.drop_symbol_list1, 12,
              1000, 2012, 'xencapital.com', 'gary@xen.io', '1234', 100, '9d00463a-e04d-43ca-a8d9-13b57fa62ea2',
              '个人英文描述', '个人中文描述', '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '公司英文描述', '公司中文描述'
          ],
      'checkpoint': loc.err_assetClass}),

    ('不选择currency',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'products_value':
          [
              None, loc.drop_assetClass_list1, None, 12000000,
              loc.drop_focus_list1, 25122025,
              loc.drop_symbol_list1, 12,
              1000, 2012, 'xencapital.com', 'gary@xen.io', '1234', 100, '9d00463a-e04d-43ca-a8d9-13b57fa62ea2',
              '个人英文描述', '个人中文描述', '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '公司英文描述', '公司中文描述'
          ],
      'checkpoint': loc.err_currency}),

    ('不填写Fund Size',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'products_value':
          [
              None, loc.drop_assetClass_list1, loc.drop_currency_list1, None,
              loc.drop_focus_list1, 25122025,
              loc.drop_symbol_list1, 12,
              1000, 2012, 'xencapital.com', 'gary@xen.io', '1234', 100, '9d00463a-e04d-43ca-a8d9-13b57fa62ea2',
              '个人英文描述', '个人中文描述', '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '公司英文描述', '公司中文描述'
          ],
      'checkpoint': loc.err_fundSize}),

    ('不选择Focus',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'products_value':
          [
              None, loc.drop_assetClass_list1, loc.drop_currency_list1, 12000000,
              None, 25122025,
              loc.drop_symbol_list1, 12,
              1000, 2012, 'xencapital.com', 'gary@xen.io', '1234', 100, '9d00463a-e04d-43ca-a8d9-13b57fa62ea2',
              '个人英文描述', '个人中文描述', '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '公司英文描述', '公司中文描述'
          ],
      'checkpoint': loc.err_focus}),

    ('不选择Symbol',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'products_value':
          [
              None, loc.drop_assetClass_list1, loc.drop_currency_list1, 12000000,
              loc.drop_focus_list1, 25122025,
              None, 12,
              1000, 2012, 'xencapital.com', 'gary@xen.io', '1234', 100, '9d00463a-e04d-43ca-a8d9-13b57fa62ea2',
              '个人英文描述', '个人中文描述', '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '公司英文描述', '公司中文描述'
          ],
      'checkpoint': loc.err_symbol}),

    ('不填写Expected Return',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'products_value':
          [
              None, loc.drop_assetClass_list1, loc.drop_currency_list1, 12000000,
              loc.drop_focus_list1, 25122025,
              loc.drop_symbol_list1, None,
              1000, 2012, 'xencapital.com', 'gary@xen.io', '1234', 100, '9d00463a-e04d-43ca-a8d9-13b57fa62ea2',
              '个人英文描述', '个人中文描述', '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '公司英文描述', '公司中文描述'
          ],
      'checkpoint': loc.err_expectedReturn}),

    ('不填写Minimum Investment',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'products_value':
          [
              None, loc.drop_assetClass_list1, loc.drop_currency_list1, 12000000,
              loc.drop_focus_list1, 25122025,
              loc.drop_symbol_list1, 12,
              None, 2012, 'xencapital.com', 'gary@xen.io', '1234', 100, '9d00463a-e04d-43ca-a8d9-13b57fa62ea2',
              '个人英文描述', '个人中文描述', '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '公司英文描述', '公司中文描述'
          ],
      'checkpoint': loc.err_minimumInvestment}),
]

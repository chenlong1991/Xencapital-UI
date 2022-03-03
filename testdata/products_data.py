# -*-coding:utf-8 -*-
"""
Products测试相关数据
"""
from pagelocator.products_details_page_loc import ProductsDetailsPageLoc as loc
from common.tools import faker

# 创建 Products 并发布
test_create_products = [
    ('正常填写Fund信息',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'fund_value':
          [
              None, loc.drop_assetClass_HedgeFunds, loc.drop_currency_USD, 12000000, loc.drop_focus_Caribbean, 25122025,
              loc.drop_symbol_big, 12, 12, 2022, 'xencapital.com', 'gary@xen.io', '1234', 100,
              '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '个人英文描述', '个人中文描述', '9d00463a-e04d-43ca-a8d9-13b57fa62ea2', '公司英文描述', '公司中文描述'
          ]
      })]

# 创建 Products 校验必填项
test_create_products_check_required = [
    ('创建 Fund 校验必填项',
     {'products_type': 'Fund',
      'products_name': faker().company(),
      'products_value':
          [
              [
                  {
                      ('drop', loc.drop_currency): loc.drop_currency_USD,
                      ('input', loc.input_fundSize): 12000000,
                      ('drop', loc.drop_focus): loc.drop_focus_Caribbean,
                      ('drop', loc.drop_symbol): loc.drop_symbol_big,
                      ('input', loc.input_expectedReturn): 12,
                      ('input', loc.input_minHoldingPeriod): 12,
                      ('input', loc.input_minimumInvestment): 10000
                  }, loc.err_assetClass
              ],
              [
                  {
                      ('drop', loc.drop_assetClass): loc.drop_assetClass_HedgeFunds,
                      ('drop', loc.drop_currency): ''
                  }, loc.err_currency
              ],
              [
                  {
                      ('drop', loc.drop_currency): loc.drop_currency_USD,
                      ('input', loc.input_fundSize): ''
                  }, loc.err_fundSize
              ],
              [
                  {
                      ('input', loc.input_fundSize): 12000000,
                      ('drop', loc.drop_focus): ''
                  }, loc.err_focus
              ],
              [
                  {
                      ('drop', loc.drop_focus): loc.drop_focus_Caribbean,
                      ('drop', loc.drop_symbol): ''
                  }, loc.err_symbol
              ],
              [
                  {
                      ('drop', loc.drop_symbol): loc.drop_symbol_big,
                      ('input', loc.input_expectedReturn): ''
                  }, loc.err_expectedReturn
              ],
              [
                  {
                      ('input', loc.input_expectedReturn): 12,
                      ('input', loc.input_minHoldingPeriod): ''
                  }, loc.err_minHoldingPeriod
              ],
              [
                  {
                      ('input', loc.input_minHoldingPeriod): 12,
                      ('input', loc.input_minimumInvestment): ''
                  }, loc.err_minimumInvestment
              ]
          ]
      }
     ),
    ('创建 Company 校验必填项',
     {'products_type': 'Company',
      'products_name': faker().company(),
      'products_value':
          [
              [
                  {
                      ('drop', loc.drop_currency): loc.drop_currency_USD,
                      ('input', loc.input_valuation): 12000000,
                      ('drop', loc.drop_fundingRound): loc.drop_fundingRound_Pre_seed,
                      ('check', loc.check_industries, loc.check_industries_input): loc.check_industries_Administrative,
                      ('drop', loc.drop_headquarters): loc.drop_headquarters_China,
                      ('input', loc.input_minimumInvestment): 10000
                  }, loc.err_assetClass
              ],
              [
                  {
                      ('drop', loc.drop_assetClass): loc.drop_assetClass_DirectInvestment,
                      ('drop', loc.drop_currency): ''
                  }, loc.err_currency
              ],
              [
                  {
                      ('drop', loc.drop_currency): loc.drop_currency_USD,
                      ('input', loc.input_valuation): ''
                  }, loc.err_valuation
              ],
              [
                  {
                      ('input', loc.input_valuation): 12000000,
                      ('drop', loc.drop_fundingRound): '',
                  }, loc.err_fundingRound
              ],
              [
                  {
                      ('drop', loc.drop_fundingRound): loc.drop_fundingRound_Pre_seed,
                      ('check', loc.check_industries, loc.check_industries_input): '',
                  }, loc.err_industries
              ],
              [
                  {
                      ('check', loc.check_industries, loc.check_industries_input): loc.check_industries_Administrative,
                      ('drop', loc.drop_headquarters): '',
                  }, loc.err_headquarters
              ],
              [
                  {
                      ('drop', loc.drop_headquarters): loc.drop_headquarters_China,
                      ('input', loc.input_minimumInvestment): ''
                  }, loc.err_minimumInvestment
              ]
          ]
      }
     )
]

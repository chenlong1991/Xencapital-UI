# -*-coding:utf-8 -*-
"""
Products Details Page元素定位
"""


class ProductsDetailsPageLoc:
    # fund详情页填写元素
    input_productName = ('xpath', "//div[@label='＊ Product Name']//input")

    drop_assetClass = ('xpath', "//label[contains(text(),'＊ Asset Class')]/following-sibling::input[1]")
    drop_assetClass_list1 = ('xpath', "//div[contains(text(),'Hedge Funds')]")
    err_assetClass = ('xpath', "//div[@label='＊ Asset Class']//div[text()='Field is required']")

    drop_currency = ('xpath', "//div[@label='＊ Currency']//input[1]")
    drop_currency_list1 = ('xpath', "//div[contains(text(),'USD')]")
    err_currency = ('xpath', "//div[@label='＊ Currency']//div[text()='Field is required']")

    input_fundSize = ('xpath', "//div[@label='＊ Fund Size']//input")
    err_fundSize = ('xpath', "//div[@label='＊ Fund Size']//div[text()='Field is required']")

    drop_focus = ('xpath', "//div[@label='＊ Focus']//input[1]")
    drop_focus_list1 = ('xpath', "//div[contains(text(),'Caribbean')]")
    err_focus = ('xpath', "//div[@label='＊ Focus']//div[text()='Field is required']")

    input_closingDate = ('xpath', "//div[@placeholder='DD/MM/YYYY']//input")

    drop_symbol = ('xpath', "//div[@label='＊ Symbol']//input[1]")
    drop_symbol_list1 = ('xpath', "//div[contains(text(),'>')]")
    err_symbol = ('xpath', "//div[@label='＊ Symbol']//div[text()='Field is required']")

    input_expectedReturn = ('xpath', "//div[@label='＊ Expected Return']//input")
    err_expectedReturn = ('xpath', "//div[@label='＊ Expected Return']//div[text()='＊ Expected Return is required']")

    input_minHoldingPeriod = ('xpath', "//div[@label='＊ Holding Period (Min)']//input")
    err_minHoldingPeriod = ('xpath', "//div[@label='＊ Holding Period (Min)']//div[text()='＊ Holding Period (Min) is required']")

    input_minimumInvestment = ('xpath', "//div[@label='＊ Minimum Investment']//input")
    err_minimumInvestment = ('xpath', "//div[contains(text(),'Minimum Investment Amount should be greater than 0')]")

    input_vintage = ('xpath', "//div[@label='Vintage']//input")
    input_website = ('xpath', "//div[@label='Website']//input")
    input_fundManager = ('xpath', "//div[@label='Fund Manager']//input")
    input_vehicle = ('xpath', "//div[@label='Vehicle Details']//input")
    input_minimumIncrement = ('xpath', "//div[@label='Minimum Increment']//input")

    drop_tags = ('xpath', "//div[@label='Tags']//div//div//i[1]")
    drop_tags_list1 = ('xpath', "//div[contains(text(),'Growth')]")

    input_templateIdIndividual = ('xpath', "//div[@label='DocuSign Template ID - Individual Client']//input")
    input_descriptionIndividual_en = ('xpath', "//div[@label='DocuSign Description (English) - Individual Client']//textarea")
    input_descriptionIndividual_ch = ('xpath', "//div[@label='DocuSign Description (Chinese) - Individual Client']//textarea")
    input_templateIdEntity = ('xpath', "//div[@label='DocuSign Template ID - Entity Client']//input")
    input_descriptionEntity_en = ('xpath', "//div[@label='DocuSign Description (English) - Entity Client']//textarea")
    input_descriptionEntity_ch = ('xpath', "//div[@label='DocuSign Description (Chinese) - Entity Client']//textarea")

    but_save = ('xpath', "// span[contains(text(), 'Save')]")
    but_publish = ('xpath', "//span[text()='Publish']")

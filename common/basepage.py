# -*-coding:utf-8 -*-
"""
    此类封装所有webdriver操作，所有页面继承该类
"""

from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from common.tools import logger
from common.tools import conf_get


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 打开网页
    def open_url(self, url):
        logger.info('打开网页：{}'.format(url))
        self.driver.get(url)

    # 判断元素是否存在
    def wait_ele_existence(self, loc, timeout=20, poll_frequency=0.5):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :return:None
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
            logger.info('元素存在,定位方式:{}'.format(loc))
            return True
        except Exception as e:
            logger.exception('{}元素不存在：{}'.format(loc, e))
            return False

    # 等待元素可见
    def wait_ele_visible(self, loc, timeout=20, poll_frequency=0.5):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :return:None
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
            logger.info('等待元素可见,定位方式:{}'.format(loc))
            return True
        except Exception as e:
            logger.exception('等待{}元素可见失败：{}'.format(loc, e))
            return False

    # 等待元素不可见
    def wait_ele_no_visible(self, loc, timeout=20, poll_frequency=0.5):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :return:None
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until_not(EC.visibility_of_element_located(loc))
            logger.info('等待元素消失,元素定位:{}'.format(loc))
            return True
        except Exception as e:
            logger.exception('等待{}元素消失失败:{}'.format(loc, e))
            return False

    # 判断元素是否可点击
    def wait_ele_clickable(self, loc, timeout=20, poll_frequency=0.5):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :return:None
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(loc))
            logger.info('等待元素可以点击,元素定位:{}'.format(loc))
            return True
        except Exception as e:
            logger.exception('元素{}不可点击:{}'.format(loc, e))
            return False

    # 查找一个元素element
    def find_element(self, loc):
        try:
            ele = self.driver.find_element(*loc)
            logger.info('查找元素，元素定位:{}'.format(loc))
            return ele
        except Exception as e:
            logger.exception('查找元素失败:{}'.format(e))
            raise

    # 查找多个元素elements
    def find_elements(self, loc):

        try:
            ele = self.driver.find_elements(*loc)
            logger.info('查找多个元素，元素定位:{}'.format(loc))
            return ele
        except Exception as e:
            logger.exception('查找多个元素失败:{}'.format(e))
            raise

    # 输入操作
    def input_text(self, loc, text):
        # 查找元素
        ele = self.find_element(loc)
        # 输入操作
        try:
            ele.send_keys(text)
            logger.info('文本框输入{}'.format(text))
        except Exception as e:
            logger.exception('输入操作失败:{}'.format(e))
            raise

    # 清除文本操作
    def clean_text(self, loc):
        ele = self.find_element(loc)
        # 清除操作
        try:
            ele.clear()
            logger.info('清除文本')
        except Exception as e:
            logger.exception('清除操作失败:{}'.format(e))
            raise

    def backspace(self, loc):
        ele = self.find_element(loc)
        # 退格操作
        try:
            ele.send_keys(Keys.BACKSPACE)
            logger.info('退格操作')
        except Exception as e:
            logger.exception('退格操作失败:{}'.format(e))
            raise

    def select_all(self, loc):
        ele = self.find_element(loc)
        # 全选操作
        try:
            if 'OS' in conf_get('lambdatest_conf', 'platform'):
                ele.send_keys(Keys.COMMAND + 'a')
                logger.info('MAC系统全选操作')
            else:
                ele.send_keys(Keys.CONTROL + 'a')
                logger.info('Windows系统全选操作')
        except Exception as e:
            logger.exception('全选操作失败:{}'.format(e))
            raise

    def backspace_all(self, loc):
        # 全选退格操作
        logger.info('全选退格操作')
        self.select_all(loc)
        self.backspace(loc)

    # 点击操作
    def click(self, loc):
        # 先查找元素在点击
        ele = self.find_element(loc)
        # 点击操作
        try:
            ele.click()
            logger.info('点击元素')
        except Exception as e:
            logger.exception('点击失败:{}'.format(e))
            raise

    # 获取文本内容
    def get_text(self, loc):
        # 先查找元素在获取文本内容
        ele = self.find_element(loc)
        # 获取文本
        try:
            text = ele.text
            logger.info('获取元素文本内容为:{}'.format(text))
            return text
        except Exception as e:
            logger.exception('获取元素文本内容失败:{}'.format(loc))
            raise

    # 获取元素属性值
    def get_element_attribute(self, loc, name):
        # 先查找元素在去获取属性值
        ele = self.find_element(loc)
        # 获取元素属性值
        try:
            ele_attribute = ele.get_attribute(name)
            logger.info('获取到元素{}属性值为：{}'.format(name, ele_attribute))
            return ele_attribute
        except Exception as e:
            logger.exception('获取元素属性失败:{}'.format(e))
            raise

    # 上下滑动窗口让元素可见
    def sliding_window(self, loc):
        ele = self.find_element(loc)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            logger.info('滑动窗口让元素可见')
        except Exception as e:
            logger.error('滑动窗口让元素可见失败：{}'.format(e))
            raise

    # iframe 切换
    def switch_iframe(self, frame_refer, timeout=30, poll_frequency=0.5):
        # 等待 iframe 存在
        logger.info('iframe 切换操作:')
        try:
            # 切换 == index\name\id\WebElement
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(frame_refer))
            sleep(0.5)
            logger.info('切换成功')
        except Exception as e:
            logger.exception('iframe 切换失败!!!')
            raise

    # 窗口切换 = 如果是切换到新窗口,new. 如果是回到默认的窗口,default
    def switch_window(self, name, cur_handles=None, timeout=20, poll_frequency=0.5):
        """
        调用之前要获取window_handles
        :param name: new 代表最新打开的一个窗口. default 代表第一个窗口. 其他的值表示为窗口的 handles
        :param cur_handles: 当前窗口句柄
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :return:
        """
        try:
            if name == 'new':
                if cur_handles is not None:
                    logger.info('切换到最新打开的窗口')
                    WebDriverWait(self.driver, timeout, poll_frequency).until(EC.new_window_is_opened(cur_handles))
                    window_handles = self.driver.window_handles
                    self.driver.switch_to.window(window_handles[-1])
                else:
                    logger.exception('切换失败,没有要切换窗口的信息!!!')
                    raise
            elif name == 'default':
                logger.info('切换到默认页面')
                self.driver.switch_to.window(cur_handles)
            else:
                logger.info('切换到为 handles 的窗口')
                self.driver.switch_to.window(name)
        except Exception:
            logger.exception('切换窗口失败!!!')
            raise

    def screenshot(self):
        """
        截图功能
        :return:
        """
        return self.driver.get_screenshot_as_png()

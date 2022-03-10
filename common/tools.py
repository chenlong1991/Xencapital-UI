# -*-coding:utf-8 -*-
import logging
import os
import datetime
from configparser import ConfigParser

from faker import Faker
from common.basepath import log_path, conf_path


class Logger(logging.Logger):
    """
    日志操作类
    """

    def __init__(self, path, name='root', level='INFO'):
        """
        初始化日志类
        :param path: 日志文件路径
        :param name:
        :param level: 日志等级，默认INFO
        """
        super().__init__(name, level)
        datefmt = '%Y-%m-%d %H:%M:%S'
        fmt = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        log_format = logging.Formatter(fmt, datefmt)
        file_log = logging.FileHandler(path, encoding='utf-8')
        console = logging.StreamHandler()
        file_log.setFormatter(log_format)
        console.setFormatter(log_format)
        self.addHandler(file_log)
        self.addHandler(console)


now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
paths = os.path.join(log_path(), '{}.log'.format(now_time))
logger = Logger(path=paths)


def conf_get(section, option, name='config.ini'):
    """
    获取config文件数据
    :param name: 配置文件名称，默认config.ini
    :param section:
    :param option:
    :return:
    """

    conf = ConfigParser()
    try:
        path = os.path.join(conf_path, name)
        conf.read(path, encoding='utf-8')
        value = conf.get(section, option)
        return value
    except Exception as e:
        logger.info('读取配置文件错误：{}'.format(e))
        raise


# 测试域名
url = conf_get('ip', 'arocarret')


def faker(language='en_US'):
    """
    创建假数据
    :param language: 语言默认英文，可选zh_CN、ja_JP、zh_TW
    :return:
    """
    fakers = Faker(locale=language)
    return fakers


def now_time(days=0):
    """
    获取当前时间之前或之后的日期
    :param days: 正数表示之后多少天，负数表示之前
    :return:
    """
    now_date = datetime.datetime.now().strftime('%d%m%Y')
    time = datetime.datetime.strptime(now_date, '%d%m%Y')
    delta = datetime.timedelta(days=days)
    n_time = (time + delta).strftime('%d%m%Y')
    return n_time


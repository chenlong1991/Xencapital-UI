# -*-coding:utf-8 -*-
import logging
from datetime import datetime
from common.basepath import log_path
import json
import os


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


now_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
paths = os.path.join(log_path(), '{}.log'.format(now_time))
logger = Logger(path=paths)

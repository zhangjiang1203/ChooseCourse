#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 5:26 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : manager.py
# @Software: PyCharm
import time
from conf import my_logging
import logging

logger = logging.getLogger(__name__)

# 加载logging配置
my_logging.load_my_logging_cfg()
logger.debug("start logging time {}".format(time.time()))

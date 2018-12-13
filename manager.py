#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 5:26 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : manager.py
# @Software: PyCharm
import time
import logging
from interface import school,schoolPerson,course
from db import db_handler

logger = logging.getLogger(__name__)

# 设置debug的bug
logger.debug("start logging time {}".format(time.time()))

db_handler.create_course_school()

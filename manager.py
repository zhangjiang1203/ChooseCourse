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

logger = logging.getLogger(__name__)

# 设置debug的bug
logger.debug("start logging time {}".format(time.time()))

#创建课程
linux = course.Course("linux","3个月",15000)
python = course.Course("python","4个月",17000)
go = course.Course("go","4个月",18000)

# 创建学校
beijingSchool = school.School("北京大学","北京","北京",[linux,python])
shanghaiSchool = school.School("上海大学","上海","上海",[go])




print(beijingSchool.name)

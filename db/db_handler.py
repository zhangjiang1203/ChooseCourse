#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : db_handler.py
# @Author: zhangjiang
# @Date  : 2018/12/13
# @Desc  :

'''
创建课程和学校 作为默认数据
'''

from interface import school,course,grade,schoolPerson
from  conf import setting
import pickle
import os

def create_course_school():
    file_name = os.path.join(setting.BASE_DBDIR,'School.db')
    if os.path.exists(file_name) :
        with open(file_name,'rb') as f_read:
            return pickle.load(f_read)
    else:
        # 创建课程
        linux = course.Course("linux", "3个月", 15000)
        python = course.Course("python", "4个月", 17000)
        go = course.Course("go", "4个月", 18000)

        # 创建班级
        grade1 = grade.Grade("三年二班")
        grade2 = grade.Grade('三年五班')
        grade3 = grade.Grade('二年一班')

        # 创建学校
        beijingSchool = school.School("北京理工大学", "北京", "北京", [linux, python],[grade1,grade2])
        shanghaiSchool = school.School("上海交通大学", "上海", "上海", [go],[grade3])

        #保存信息
        with open(file_name,'wb') as f_write:
            pickle.dump([beijingSchool,shanghaiSchool],f_write)
            return [beijingSchool,shanghaiSchool]


if __name__ == '__main__':
    data = create_course_school()
    beijing = data[0]
    print(beijing.name,beijing.province)
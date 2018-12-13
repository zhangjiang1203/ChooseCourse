#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 5:28 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : schoolPerson.py
# @Software: PyCharm


class SchoolPerson:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex



class Teacher(SchoolPerson):
    def __init__(self,name,age,sex,job_title):
        SchoolPerson.__init__(name,age,sex)
        self.job_title = job_title
        #开始设置自己的值
        self.course = []
        #学生
        self.students = []



class Student(SchoolPerson):
    def __init__(self,name,age,sex,course):
        SchoolPerson.__init__(name,age,sex)
        self.course = course

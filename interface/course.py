#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 5:29 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : course.py
# @Software: PyCharm


class Course:
    def __init__(self,name,period,price):
        self.name = name
        self.period = period
        self.price = price


    def tell_info(self):
        print("<%s %s %s>" %(self.name,self.period,self.price))


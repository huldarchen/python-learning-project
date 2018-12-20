#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:huldar
@file: lambda.py
@time: 2018/12/20
"""
# 2. 写一个lambda表达式，求两个变量的最大值

lambda_max = lambda x, y: max(x, y)
print(lambda_max(1, 2))
# 写一个lambda 表达式，判断这个数的2次方+1是否能被5整除，如果能被整除返回True, 否则返回False
lambda_test = lambda x: (x ** 2 + 1) % 5 == 0

print(lambda_test(2))
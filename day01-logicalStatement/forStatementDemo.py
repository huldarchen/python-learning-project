#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
for语句语法的使用
@author:huldar
@file: forStatementDemo.py
@time: 2018/12/19
"""
# 释义
"""
for 语句
  作用:
    用来遍历可迭代对象的数据元素
      可迭代对象是指能依次获取数据元素的对象
for 语法:
  for 变量列表 in 可迭代对象:
      语句块１
  else:
      语句块2
"""
# range函数
"""
range 函数
  range(stop) 用来生成0~stop区间内的整数，直到stop为止(不包含stop)
  range(start, stop[, step])  用来生成start~stop区间内的整数,直到stop为止(不包含stop),每次生成整数后移动step
"""
# for语句变量可能不被创建的问题
for x in range(4, 0):
    print(x)  # x不能被绑定 打印结果是空
"""
continue 语句
  作用:
    用于循环语句(while,for)中,不再执行本次循环continue之后的语句,重新开始一次新的循环
  语法:
    continue
  说明:
    1. 在while语句中执行continue,将会直接跳转到while语句的真值表达式处重新判断循环条件
    2. 在 for 语句中执行continue语句,将会从可迭代对象中取下一个元素,绑定变量后再次进行循环
"""
# 练习
"""
求: 100以内有哪儿些数与自身+1的乘积再对 11 求余等于8?
      x * (x+1)  % 11 == 8
"""
y = 0
for x in range(100):
    if y * (y + 1) % 11 == 8:
        print(y)
    y += 1

#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:huldar
@file: whileStatementDemo.py
@time: 2018/12/18
"""

# 循环语句:
# 有两中循环语句while,for
"""
while 语句:
  作用:
    根据一定条件,重复的执行一条语句或多条语句

  语法:
    while 真值表达式:
        语句块1
    else:
        语句块2
  说明:
    1.先判断真值表达式,为True或False
    2. 如果为True,则执行语句块1,再回到第一步
    3. 如果为False,则执行语句块2,然后结束此while的执行
    4. else 子句部可以省略(同if类似)
"""
# 1. 打印 1 ~ 20 的整数,打印在一行内
# 1 2 3 4 5 6 .... 18 19 20
j = 1
while j < 10:
    i = 1
    while i <= 20:
        print(i, end=' ')
        i += 1
    else:
        print()
    j += 1
# 2. 打印 1 ~ 20 的整数,每行打印5个,打印四行,
# 定义一个变量来记录每行的个数
rowNum = 5
# 定义一个变量来记录每次打印的每行的标记
fromIndex = 1
maxIndex = 20
while fromIndex <= maxIndex:
    print(fromIndex, end=' ')
    if fromIndex % rowNum == 0:
        print()
    fromIndex += 1

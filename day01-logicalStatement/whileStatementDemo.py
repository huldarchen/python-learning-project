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
"""
while 语句注意事项:
  要控制循环真值表达式的值来防止死循环
  通常用真值表达式内的循环变量来控制循环条件
  通常在循环语句块内改变循环变量来控制循环次数和变量走向

while 语句的嵌套
  while 语句本身是语句,和其它语句一样,可以嵌套到任何复合语句中

示意:
  while 真值表达式:
      ...
      while 真值表达式2:
          ...
      else:
          ...
  else:
      ...

"""

# 练习:
# 输入一个整数代表正方形的宽度,用变量n绑定,
# 打印指定宽度的正方形
sideLen = int(input("请输入正方形的边长:"))
for i in range(1,sideLen+1):
    for y in range(1,sideLen+1):
        print(y, end=' ')
    print()
"""

break 语句
  作用:
    用于循环语句(while, for语句)中,用来终止当前循环语句的执行
  语法:
    break
  说明:
    1. 当break语句执行后,此循环语句break之后的语句将不再执行
    2. break语句通常和if语句组合使用
    3. break语句终止循环时else子句的语句将不会执行
    4. break语句只能终止当前循环语句的执行,如果有循环嵌套时,不会跳出嵌套的外重循环

  死循环
    死循环是指条件一直成立的循环
    死循环通常用break语句来终止循环
    死循环的else子句永远不会执行

"""
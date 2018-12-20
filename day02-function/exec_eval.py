#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
exec and eval 练习
@author:huldar
@file: exec_eval.py
@time: 2018/12/20
"""

# exec(source, globals=None, locals=None) 把一个字符串source 当成程序来执行
exec_str = """
print("hello world!")
x = 100
x += 200
print('x=', x)
"""
exec(exec_str)
# eval(source, globals=None, local=None)  把一个字符串 source 当成一个表达式来执行，返回表达式执行的结果

x = 100
y = 200

a = eval('x + y')
print(a)  # 300

a = eval('x + y', {'x': 1, 'y': 2})
print(a)  # 3

a = eval('x + y',
         {'x': 1, 'y': 2},
         {'x': 10, 'y': 20})
print(a)  # 30

a = eval('x + y',
         {'x': 1, 'y': 2},
         {'x': 10})
print(a)  # 12


# 输入表达式执行表达式  这个类型与交互页面
while True:
    s = input("请输入表达式: ")
    if not s:
        break
    a = eval(s)
    print(a)

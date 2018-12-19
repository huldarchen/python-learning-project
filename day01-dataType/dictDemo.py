#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Python数据类型之字典(dict)
@author:huldar
@file: dictDemo.py
@time: 2018/12/19
"""
# 基本概念
"""
什么是字典:
    1. 字典是一种可变的容器，可以存储任意类型的数据
    2. 字典中的每个数据都是用'键'(key)进行索引的，而不像序列可以用索引下标进行索引
    3. 字典中的数据没有先后顺序关系,字典的存储是无序的
    4. 字典中的数据以键-值对(key-value)对形式进行映射存储
    5. 字典的键不能重复,且只能用不可变类型作为字典的键
"""
# 字典的字面值
"""
 字典的字面值表示方法:
    以{} 括起来,以冒号(:) 分隔键-值对,各键值对用逗号分隔开

  创建空字典:
    d = {}  # {} 表达式用来创建一个空的字典
  创建非空字典:
    d = {'name': 'weimingze', 'age': 35}
    d = {'a': 100}
    d = {'a': tuple("ABC")}
    d = {'abc': list("ABC")}
    d = {'a': {'b':100, 'c':200}}
    d = {True:'真值', False: '假值', None:'空', 100:'一百'}
    d = {(1970, 1, 1): '计算机元年'}
"""
# 字典的构造方法
"""
字典的构造函数 dict
  dict()  创建一个空的字典,等同于{}
  dict(iterable)  用可迭代对象创建一个新的字典
  dict(**kwargs)  用关键字传参形式创建一个新的字典

示例:
  d = dict()
  d = dict([('name', 'tarena'), ('age', 15)])
  d = dict((['name', 'weimingze'], "AB"))
  d = dict(name='Tarena', age=15)
"""
# 字典的操作
"""
字典的操作
  字典的键索引
    用[] 运算符可以获取字典内'键'对应的'值'
  语法:
    v = 字典[键]
  示例:
    d = {'name': 'tarena', 'age': 15}
    print(d['name'], '今年', d['age'], '岁')

添加/修改字典的元素
  语法:
    字典[键] = 表达式
  示例:
    d = {}
    d['name'] = 'tarena'  #创建新的键'name'同时关联值
    d['age'] = 15  # 创建键并绑定15
    d['age'] = 16  # 修改原来的键'age',重新绑定为16
  说明:
    键不存在,创建键,并绑定值
    键存在,修改键的绑定关系
  
删除字典元素 del语句
  del 字典[键]
  示例:
    d = {1:'一', 'hello': 'world', False:'假值'}
    del d['hello']



字典的 in / not in 运算符
  in用来判断一个键是否存在于字典中,如果存在返回 True,否则返回False
  not in 的返回结果与in 相反

示例:
  d = {'name': '小张', 'age': 20}
  'name' in d  # True
  'age' not in d  # False
  '小张' in d   # False  (只判断键,不判断值)
  20 not in d  # True
"""
# 练习
"""
  1.写程序,实现以下要求:
    1) 将如下数据形成一个字典 seasons
      键             值
      1          '春季有1,2,3月'
      2          '夏季有4,5,6月'
      3          '秋季有7,8,9月'
      4          '冬季有10,11,12月'
    2)  让用户输入一个整数代表这个季度,打印这个季度有信息
      如果用户输入的信息不在字典中,则打印"信息不存在"
"""
seasons = {1: "春季有1,2,3月", 2: "夏季有4,5,6月", 3: "秋季有7,8,9月", 4: "冬季有10,11,12月"}
inputNum = int(input("请输入一个整数:"))
if inputNum in seasons:
    print(seasons[inputNum])
else:
    print("信息不存在")
# 字典迭代
"""
字典的迭代访问
  字典是可迭代对象,字典只能对'键'进行访问
"""
# d = {'aaa': 111, 'bbb': 222, 'ccc': 333}
# for k in d:
#     print(k)  # 结果是 aaa bbb ccc
# 只对键进行迭代


# 字典的方法
"""
字典的方法
  方法名       说明
  D.clear()   清空字典
  D.pop(key)  移除键,同时返回此键对应的值
  D.copy()  返回字典D的副本(浅拷贝)
  D.update(D2)  将字典D2合并到D中,如果键相同,则此键的值取D2的值为为新值
  D.get(key, default=None)  返回键key所对应的值,如果没有此键,则返回Default的值

  D.keys()  返回可迭代的dict_keys集合对象
  D.values() 返回可迭代的dict_value集合对象
  D.items()  返回可迭代的dict_item对象
"""
# 练习
"""
练习:
  输入任意一段字符串,打印出这个字符串中出现过的字符及出现过的次数:
    如:
      输入: ABCDABCABA
    打印如下:
      A: 4次
      B: 3次
      D: 1次
      C: 2次
    注: 不要求打印的顺序
"""
# inputStr = input("请输入一个字符串")
# wordTuple = {}
# for i in inputStr:
#     if i in wordTuple:
#         wordTuple[i] += 1
#     else:
#         wordTuple[i] = 1
# print(wordTuple)
# 字典推导式
"""
字典推导式
  是用可迭代对象生成字典的表达式
  语法:
    {键表达式 : 值表达式 for 变量 in 可迭代对象[if 真值表达式]}
    注: []表示其中的内容可省略
  示例:
    # 生成一个字典,键为数字 1 ~ 9,值为键的平方
    d = {x : x ** 2 for x in range(1, 10)}
"""
# 推导式练习
'''
    已知有如下字符串列表
    L = ['tarena', 'xiaozhang', 'abc']
    生成如下字典:
    d = {'tarena': 6, 'xiaozhang': 9, 'abc': 3}
    注: 字典的值为键的长度
'''
listStr = ['tarena', 'xiaozhang', 'abc']
print({x: len(x) for x in listStr})

"""
  2. 已知有如下两个列表:
    nos = [1001, 1002, 1005, 1008]
    names = ['Tom', 'Jerry', 'Spike', 'Tyke']
    用上述两个列表生成如下字典:
    {1001: 'Tom', 1002: 'Jerry', 1005: 'Spike', 1008: 'Tyke'}
"""
nos = [1001, 1002, 1005, 1008]
names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# print({x: y for x in nos for y in names})

print({nos[i]: names[i] for i in range(len(nos))})
#字典VS列表
"""
字典 VS 列表
  1. 都是可变对象
  2. 索引方式,列表用整数索引,字典用键索引
  3. 字典的插入,删除,修改的速度可能会快行列表(重要)
  4. 列表的存储是有序的,字典的存储是无序的
"""
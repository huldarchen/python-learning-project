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

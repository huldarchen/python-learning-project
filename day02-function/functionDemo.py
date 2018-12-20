#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Python的函数学习笔记
@author:huldar
@file: functionDemo.py
@time: 2018/12/19
"""
# 基本概念
"""
函数 function
  什么是函数:
    函数是可以重复执行的语句块，可以重复调用
  作用:
    1. 用于封装语句块，提高代码的重用性
    2. 定义用户级别的函数

  语法:
    def 函数名(形参列表):
        语句块
  说明:
    1. 函数的名字就是语句块的名称
    2. 函数名的命名规则与变量名相同（函数名必须是标识符）
    3. 函数名是一个变量(不要轻易对其赋值)
    4. 函数有自己的名字空间，在函数外部不可以访问函数内部的变量，在函数内可以访问函数外部的变量,但不能修改此变量.
    5. 函数如果不需要传入参数，形参列表可以为空
    6. 语句部分不能为空，如果为空需要填充pass
  示例见:
    function.py

函数调用
  函数名(实际调用传递参数)
    注:实际调用传递参数，以后简称实参

  说明:
    1. 函数调用是一个表达式
    2. 如果函数内部没有return语句，函数调用完毕后返回None对象
    3. 如果函数需要返回其它的对象需要用到 return 语句
"""
# 练习
"""
练习：
  1. 写一个函数myadd, 此函数中的参数列表里有两个参数x, y
    此函数的功能是打印 x + y 的和
"""


# 无返回值
def myAdd(x, y):
    print(x + y)


# return
"""
return 语句
  语法:
    return [表达式]
    注: []  代表可省略
  作用:
    用于函数中，结束当前函数的执行，返回到调用该函数的地方，同时返回一个对象的引用关系

  return 语句说明
    1. return 语句后跟的表达式可以省略，省略后相 当于return None
    2. 如果函数内没有return 语句，则函数执行完最后一条语句后返回None(相当于在最后加了一条return None语句)
"""


def myAdd2(x, y) -> int:
    return x + y


myAdd(1, 4)
print(myAdd2(1, 3))
# 函数的参数
"""
函数的参数传递
  传递方式:
    位置传参
      序列传参
    关键字传参
      字典关键字传参

位置传参:
  实际参数(实参) 的对应关系与形式参数(形参)的对应关系是按位置来依次对应的
"""


# 此示例示意位置传参
def myfun1(a, b, c):
    # 这是一个函数的传参示例，此函数以后不会改变代码
    print('a 的值是:', a)
    print('b 的值是:', b)
    print('c 的值是:', c)


myfun1(1, 2, 3)

myfun1(4, 5, 6)

# 注意事项
# 说明:
# 实参和形参通过位置进行传递和匹配
# 实际参数的个数必须与形式参数的个数相同
"""
序列传参:
  序列传参是指在函数调用过程中，用 * 将序列拆解后按位置进行传递的传参方式

  说明:
    序列传参时，序列拆解的位置将与形参－－对应
    序列的位置信息对应相应的形参位置
"""


# 此示例示意序列传参
def myfun1(a, b, c):
    # 这是一个函数的传参示例，此函数以后不会改变代码
    print('a 的值是:', a)
    print('b 的值是:', b)
    print('c 的值是:', c)


s1 = [11, 22, 33]
myfun1(*s1)  # 相当于 myfun1(11, 22, 33)
# myfun1(s1[0], s1[1], s1[2])
t1 = (44, 55, 66)
myfun1(*t1)
myfun1(*"ABC")
"""
关键字传参
  关键字传参是指传参时，按着形参的名称给形参赋值
  实参和形参按形参名进行匹配
"""


# 此示例示意关键字传参
def myfun1(a, b, c):
    # 这是一个函数的传参示例，此函数以后不会改变代码
    print('a 的值是:', a)
    print('b 的值是:', b)
    print('c 的值是:', c)


# 以下是关键传参
myfun1(b=22, c=33, a=11)
myfun1(c=666, b=555, a=444)
# 字典关键字传参
"""
字典关键字传参
  是指实参为字典，将字典用　'**' 拆解后再进行关键字传参的传参方式

  说明:
    字典的键名和形参名必须一致
    字典的键名必须为字符串(标识符)
    字典的键名要在形参中存在
"""

# 综合传参
"""
函数的综合传参
  函数的传参方式在能确定形参能唯一匹配到相应实参的情况下可以任意组合

  说明:
    位置传参(序列传参) 要在 关键字传参(字典关键字传参)的左侧
  示例:
    def myfun1(a, b, c):
        pass
    # 调用时:
    myfun1(100, *[200, 300])
    myfun1(*(100, 200), 300)
    myfun1(*[100], 200, *(300,))
    myfun1(100, c=300,b=200) # 正确
    myfun1(c=300, b=200, 100)  # 错误
    myfun1(100, **{'c':300, 'b':200})
"""


def info(name, age=1, address='未填定'):
    print('我叫', name, '我今年', age,
          '岁， 我家住址:', address)


"""
函数的缺省参数:
  语法:
    def 函数名(形参名=默认实参1, 形参名2=默认实参2, ...):
        语句块

  示例见:
    default_args.py

  说明:
    缺省参数必须自右至左依次存在，如果一个参数有缺省参数，则其右侧的所有参数都必须有缺省参数
     如:
       def fe(a, b=10, c):  # 错误
            pass
"""
info("魏明择", 35, "北京市朝阳区")
info("Tarena", 15)
info('张飞')
# info()  # 出错
info('小张', age=20)
# 函数形参的定义方式
"""
  1. 位置形参
  2. 星号元组形参
  3. 命名关键字形参
  4. 双星号字典形参
"""


def positional_parameter(*args):
    print("参数的个数是:", len(args))
    print("args:", args)


positional_parameter()
positional_parameter(1, 2, 3, 4, 5)
positional_parameter(*"ABC", 1, 2, 3, 4, None, False)  # ('A', 'B', 'C', 1, 2, 3, 4, None, False)

"""
函数形参的定义方式:
  1. 位置形参
  2. 星号元组形参
  3. 命名关键字形参
  4. 双星号字典形参

位置形参:
  语法:
    def 函数名(形参名1, 形参名2, ...):
        语句块

星号元组形参
  语法:
    def 函数名(*元组形参名):
       语句块
  作用:
    收集多余的位置传参
命名关键字形参:
  语法:
    def 函数名(*, 命名关键字形参):
      语句块 
    或
    def 函数名(*args, 命名关键字形参):
      语句块 
  作用:
    强制所胡的参数都必须用关键字传参或字典关键字传参
双星号字典形参
  语法:
    def 函数名(**字典形参名):
       语句块
  作用:
    收集多余的关键字传参
  说明:
    字典形参名通常命名为'kwargs'
"""
def def_sum(*args):
    sumNum = 0
    for i in args:
        if type(i) == int:
            sumNum += i
        else:
            print("数据", i, "的类型不正确,", type(i), "数据类型应该是int")
    return sumNum


print(def_sum())
print(def_sum(1, 2, 3))
print(def_sum(123, "a"))


#参数说明
"""
函数的参数说明:
  位置形参，缺省参数，星号元组形参，双星号字典形参可以混合使用
  
  函数形参自左至右的顺序为:
    位置形参
    星号元组形参
    命名关键字形参
    双星号字典形参
  示例:
    def fx(a, b, *args, c, **kwargs):
         pass
    fx(100, 200, 300, 400, c="C", d="D", e="E")

函数的不定长参数:
  星号元组形参, 双星号字典形参

  说明:
    可以接收任意的位置传参和关键字传参
  示例:
    def fn(*args, **kwargs):
        pass
"""

# def process_item(self, item, spider):
#     if isinstance(item, WhoscoredNewItem):
#         table_name = item.pop('table_name')
#         col_str = ''
#         row_str = ''
#         for key in item.keys():
#             col_str = col_str + " " + key + ","
#             row_str = "{}'{}',".format(row_str, item[key] if "'" not in item[key] else item[key].replace("'", "\\'"))
#             sql = "insert INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE ".format(table_name, col_str[1:-1], row_str[:-1])
#         for (key, value) in six.iteritems(item):
#             sql += "{} = '{}', ".format(key, value if "'" not in value else value.replace("'", "\\'"))
#         sql = sql[:-2]
#         self.cursor.execute(sql) #执行SQL
#         self.cnx.commit()# 写入操作
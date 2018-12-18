#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
字符串学习demo
@author:huldar
@file: stringDemo.py
@time: 2018/12/18
"""
"""
Python字符串类型学习
 作用:
    用来记录文字信息
  表示方法:
    在非注释中凡是用引号括起来的部分都是字符串
    '    单引号
    "    双引号
    '''  三单引号
    \"\"\"  三双引号
单引号和双引号的区别:
  单引号内的双引号不算结束符
  双引号内的单引号不算结束符
三引号字符串
  以'''或\"\"\"开头,以'''或\"\"\"结尾的字符串
  作用:
    三引号字符串中的换行会自动转换为换行符'\n'
    三引号内可以包含单引号和双引号
    用转义序列代表特殊字符
  字符串字面值中用字符反斜杠 \ 后跟一些字符代表特殊的一个字符
转义字符表:
   \'  代表一个单引号
   \"  代表一个双引号
   \n  代表一个换行符
   \\  代表一个反斜杠
   \r  返回光标至行首
   \t  水平制表符
   \f  换页
   \v  垂直制表符
   \b  倒退(backspace)
   \0  字符串,字符值为0
   \0oo  oo为两位八进制表示的字符
   \\xXX  XX为两位十六进制表示的字符
   \\uXXXX Unicode 16的十六进制的字符
   \\UXXXXXXXX Unicode 32 的十六进制表示的字符
字符串函数练习
"""
'len函数  返回字符串的字符个数'
a = len("abc")
print(a)  # 打印结果是3

'''
raw函数  让转义字符无效
'''

print("C:\newfile\test.py")
"""打印结果是
C:
ewfile	est.py
"""
print(r"C:\newfile\test.py")  # 打印结果是C:\newfile\test.py

"""
字符串运算符  +   +=  *  *=
+ 加号运算符用于拼接字符串
+= 用于拼接运算后改变原变量的绑定关系
* 运算符生成重复的字符串
*= 生成重复的字符串并改变原变量的绑定关系
"""
concastLeft = "abcd"
concastRight = "efgh"

print(concastLeft + concastRight)  # 打印结果 abcdefgh
concastLeft += concastRight
concastedString = concastLeft  # concastLeft 就被赋值为abcdefgh
print(concastedString)
print(concastLeft)
# 还原
concastLeft = "abcd"
# print(concastLeft * concastRight) error :TypeError: can't multiply sequence by non-int of type 'str'
# 原因是字符串只能和数字相乘

print(concastLeft * 2)  # abcdabcd 数字代表重复原字符串多少次

"""
字符串的比较运算  < <= > >= == !=
    示例:
    'A' < 'B'  # True
    'AB' <= 'AC'  # True
    'ABC' > 'ACB'  # False
    'AD'  > 'ABC'  # True
    'AB'  < 'ABC'  # True
    'ABC'  == 'abc'  # False
    'ABCD' != 'DCBA'  # True
"""

"""
in / not in 运算符
  作用:
    in 用于序列,字典,集合中,用于判断某个值是否存在于容器中,如果存在返回True, 否则返回False
  说明:
    not in 返回结果与in 相反
  格式:
    对象 in 序列
  示例:
    x = 'welcome to tarena!'
    'to' in x  # True
    'e t' in x  # True
    'hello' in x  # False
    'hello' not in x  # True
"""
# inputString = input("请输入一个字符串:")
# inputName = input("请输入一个名字:")
# if inputName in inputString:
#     print("您的名字在字符串中出现了!")
# else:
#     print("字符串中没有出现您的名字!")

# ----------------------------------------------
"""
索引 index
  python字符串是不可以改变的序列, 
  所有的序列都可以通过索引来获取其中的数据元素
    语法:
      字符串[整数表达式]
    说明:
      1. 序列的正向索引是从0开始的,第二个索引为1,最后一个索引为len(s)-1
      2. 序列的反向索引是从-1开始的,-1代表最后一个,-2代表倒数第二个,以此类推,第一个是-len(s)
"""

"""
切片 slice
  从字符串序列中取出相应的元素重新组成一个字符串序列

  语法:
    s[(开始索引b):(结束索引e)(:(步长s))]
    注: 小括号() 括起的部分代表可省略

  说明:
    1. 开始索引b是切片切下的位置,0代表第一个元素,1代表第二个元素 -1代表最后一个元素...
    2. 结束索引是切片的终止索引(但不包含终止点)
    3. 步长是切片每次获取完当前元素后移动的方向和偏移量
      3.1 没有步长,相应于步长为1(默认为1)
      3.2 当步长为正整数时,取正向切片,开始索引默认为0,结束索引为最后一个元素的下一个位置
      3.3 当步长为负数时,取反向切片.
         反向切片时,默认的起始位置为最后一个元素.终止位置是第一个元素的前一个位置
"""
sliceString = "ABCDE"

# print(sliceString.s[1:4])  # AttributeError: 'str' object has no attribute 's'
# 含前不含后
print(sliceString[1:4])  # BCD
print(sliceString[1:4:2])  # BD
print(sliceString[1:])  # BCDE
print(sliceString[0:2])  # AB
print(sliceString[:])  # ABCDE
print(sliceString[4:0:-1])  # EDCB
print(sliceString[::-1])  # EDCBA
print(sliceString[4::-2])  # ECA

# 练习:输入任意一个字符串,判断这个字符串是否是回文
# 思路:将字符串反转 判断盘转后的字符串和反转前的字符串是否相同 利用字符串切片的功能实现
# 切片步长为负数时候反向切片
# moslemsString = input("判断是否是回文.输入一个字符串:")
# if moslemsString == moslemsString[::-1]:
#     print(moslemsString + "是回文!")
# else:
#     print(moslemsString + "不是回文!")
"""
python 3中能用于字符串的函数

  len(x)  返回字符串的长度
  max(x)  返回字符串串中编码值最大的字符
  min(x)  返回最小值的字符
  ord(c)  返回一个字符c的Unicode编码值
  chr(i)  返回i这个值所对应的字符
  bin(i)  将整数转换为二进制字符串
  oct(i)  将整数转换为八进制字符串
  hex(i)  将整数转换为十六进制字符串
  str(obj='')   将对象转换为字符串
"""

"""
练习:
  输入一个字符串:
    1. 判断您输入的字符串有几个空格
    2. 将源字符串左右空白字符去掉,打印出有效的字符的个数
    3. 判断您输入的是否是数字
      3.1 如果是数字,判断您输入的数字是否大于100

"""
# inputString = input("请输入一个字符串:")
# print("您输入的字符串是" + inputString + "其中空格的数量是:" + inputString.count(' ') + "个.")
# trimString = inputString.strip()
# print("去掉空格后的字符串是:" + trimString)
#
# if inputString.isdigit():
#     print("您输入的字符串是数字!")
#     if int(inputString) > 100:
#         print("你输入的字符串大于100")

"""
  1. 用字符串 * 运算符打印三角形
    要求输入一个整数,此整数代表最长的一行星离左侧的字节数
  如:
    请输入离左侧的距离: 3
  打印如下:
      *
     ***
    *****
   *******
"""
leftOffset = int(input("请输入一个整数:"))
asteriskNumber = 1
while leftOffset > 0:
    print(' ' * leftOffset + '*' * asteriskNumber)
    leftOffset -= 1
    asteriskNumber += 2
"""
输入一个字符串,把输入的字符串中的空格全部去掉.打印出处理后的字符串的长度和字符串内容
"""
trimingStr = input("请输入一个字符串:")
# 去掉字符串中的所有空格
trimedStr = trimingStr.replace(' ', '')
print("处理后的字符串是:%s,他的长度是:%s" % (trimedStr, len(trimedStr)))
"""
 输入三行文字,让这三行文字在一个方框内居中显示
    如输入(不要输入中文)
    hello!
    I'm studing python!
    I like python
     打印如下:
   +---------------------+
   |       hello!        |
   | I'm studing python! |
   |    I like python    |
   +---------------------+
"""
# 定义输入的行数
rowNum = int(input("请输入一个整数,代表行数:"))
# 定义一个列表接收输入的句子
rowList = []
# 获取字符串最大的长度
max_len = -1
for i in range(rowNum):
    sentence = input("请输入第%s句,总共%s句:" % (i + 1, rowNum))
    rowList.append(sentence)
    if max_len < len(sentence):
        max_len = len(sentence)
# 构建收尾句
firstAndEnd = '+' + '-' * (max_len + 2) + '+'
print(firstAndEnd)
# 遍历输入的句子并输入出
for sentence in rowList:
    print("|", sentence.center(max_len), "|")
print(firstAndEnd)

# 字符串格式化表达式
"""
  作用:
    生成一定格式的字符串
  运算符:
    %
  语法格式:
    格式字符串  % 参数值
    或
    格式字符串  % (参数值1, 参数值2, ...)
  说明:
    % 左侧为格式字符串
    % 右侧为参数值,当有多个参数值是用括号() 括起来,并用逗号(,)分隔
    格式化字符串中以%开头的为占位符,占位符的位置将用参数值替换
  示例:
    fmt = "name: %s, age: %d"
    s = fmt % ('weimingze', 35)
    print(s)  # name: weimingze, age: 35
    "温度:__%d__" % 32
----------------------------------------------------------------
格式化字符串中的占位符和类型码
   %s   字符串,使用 str(x) 将x转换为字符串
   %r   字符串,使用 repr(x) 将x转换为字符串
   %c   整数转为单个字符
   %d   转为十进制整数
   %o   转为八进制整数
   %x   十六制进整数(字符a-f小写)
   %X   十六制进整数(字符A-F大写)
   %e   指数型浮点数(e小写), 如2.9e+10
   %E   指数型浮点数(E大写), 如2.9E+10
   %f, %F 浮点数(小数形式)
   %g, %G  十进制浮点数或指数浮点自动转换
   %%   等同于一个%字符

占位符和类型码之间的格式化语法:
  % [- + 0 宽度.精度] 类型码
  -   : 左对齐
  +   : 显示正号
  0   : 左侧空白位置补零
  宽度 : 整个字符串的字符个数
  精度 : 保留小数点后多少位(默认6位)
 
示例:
  "%10d"  % 123    # '       123'
  "%+10d" % 123    # '      +123'
  "%-10d" % 123    # '123       '
  "%10s"  % 'abc'  # '       abc'
  "%-5s"  % 'abc'  # 'abc  '
  "%010d" % 123    # '0000000123'
  "%7.3f" % 3.141592535897932  # '  3.141'
  "%07.2f" % 3.141592535897932  # '0003.14'
"""

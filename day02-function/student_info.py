#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
学生信息管理系统
@author:huldar
@file: student_info.py
@time: 2018/12/20
"""
# 需求
"""
# 4 实现带有界面的学生信息管理系统
#   程序启动时先弹出操作菜单:
#     +-------------------------+
#     | 1)  添加学生信息          |
#     | 2)  显示学生信息          |
#     | 3)  删除学生信息          |
#     | 4)  修改学生成绩          |
#     | q)  退出                 |
#     +-------------------------+
#     请选择: 1
#   要求 ：
#       每个选择都要有一个函数来实现

"""


def show_menu():
    print('+-------------------------+')
    print('| 1)  添加学生信息        |')
    print('| 2)  显示学生信息        |')
    print('| 3)  删除学生信息        |')
    print('| 4)  修改学生成绩        |')
    print('| q)  退出                |')
    print('+-------------------------+')


"""
输入学生信息
@:return 返回学生信息字典
"""


def input_student() -> list:
    student_list = []
    while True:
        name = input("请输入学生姓名:")
        if not name:
            break
        age = int(input("请输入%s学生的年龄:" % name))
        score = float(input("请输入%s学生的成绩:" % name))
        student_dict = {'name': name, 'age': age, 'score': score}
        student_list.append(student_dict)
    return student_list


"""
打印收集的信息
@:param 封装的学生的序列
"""


def output_student(student_list):
    print("+-----------------+----------+----------+")
    print("|     name        |   age    |   score  |")
    print("+-----------------+----------+----------+")
    for student in student_list:
        n = student['name'].center(15)
        a = str(student['age']).center(10)
        s = str(student['score']).center(10)
        print("|%s|%s|%s|" % (n, a, s))

    print("+---------------+----------+----------+")

    # 主函数


def main():
    # 定义一个变量用于存放学生信息的空列表
    docs = []
    while True:
        show_menu()
        option = input("请输入您的选择:")
        if option == '1':
            docs += input_student()
        elif option == '2':
            output_student(docs)
        elif option == '3':
            print("开始删除")
        elif option == '4':
            print("开始修改成绩")
        elif option == 'q':
            break


main()

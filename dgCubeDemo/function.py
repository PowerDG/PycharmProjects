# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:

# def add(x, y):
#
#
#     z = x + y
#
#     return z
#
# a = 1
#
# b = 2
#
# c = add(a, b)

# print('相加结果是：', c)
# 13.2、函数参数：

# 使用函数，参数是不可变数据类型（字符吕，元组，数值）：传递的只是该数据类型的值（相当于复制一份）


def changeInt(a):
    a = a + 1


b = 1

print('调用函数之前b的值是：', b)

changeInt(a=b)

print('调用函数之后b的值是', b)


# 13.3、函数：可变数据类型
#
# 使用函数，参数是可变数据类型：传递是该变量的引用地址

def changeList(inputList):
    inputList.append('奶茶妹妹')


nameList = ['小张', '小李', '小王']

print('调用函数之前的值：', nameList)

changeList(nameList)

print('调用函数之后的值', nameList)

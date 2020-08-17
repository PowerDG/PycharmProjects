# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:

# 12.1、单字符串循环
print('12.1、单字符串循环')

eatList = ['吃第1次饭', '吃第2次饭', '吃第3次饭']

for i in eatList:
    print(i)

# 12.2、对字典进行循环
print('12.2、对字典进行循环')

gafataDict = {'腾讯': 'HK:00700',

              '阿里巴巴': 'BABA',

              '苹果': 'apple',

              '谷歌': 'GOOGLE',

              '脸书': 'FB',

              '亚马逊': 'AMZA'}

for key, value in gafataDict.items():
    newValue = value.upper()

    gafataDict[key] = newValue

print(gafataDict)

# 12.3、continue跳出当前循环

print('12.3、continue跳出当前循环')

# 以下例子是会把所有的数据读取完，只是当判断条件=苹果这条数据时，停止了循环读取数据。

gafataDict = {'腾讯': 'HK:00700',

              '阿里巴巴': 'BABA',

              '苹果': 'apple',

              '谷歌': 'GOOGLE',

              '脸书': 'FB',

              '亚马逊': 'AMZA'}

for key, value in gafataDict.items():

    if key == '苹果':
        continue

    print(gafataDict)

# 12.4、break用于退同整个循环

print('12.4、break用于退同整个循环：')

gafataDict = {'腾讯': 'HK:00700',

              '阿里巴巴': 'BABA',

              '苹果': 'apple',

              '谷歌': 'GOOGLE',

              '脸书': 'FB',

              '亚马逊': 'AMZA'}

number = 0

for key, value in gafataDict.items():

    number = number + 1

    if key == '苹果':
        # print('查找', key, '公司的股票代码是：', value)

        break

print('当前公司：', key, '当前股票代码是：', value)

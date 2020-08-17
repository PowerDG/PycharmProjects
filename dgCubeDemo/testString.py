# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:


# 我是中国人


"""
https://zhuanlan.zhihu.com/p/52770875
我是中国人，

那你呢
"""

str1 = '我叫 %s,俺爹是 %s' % ('小王', '老王')

print(str1)
nameStr = '马爸爸'

moneyStr = '有钱'

print('用+将字符串合并，', nameStr + moneyStr)
#  ===  列表----[ ]
nameList = ['猴子', '马云', '王健林', '马化腾']

nameLen = len(nameList)

print(nameLen)
nameList.append('刘强东')

print('增加1个元素的列表是', nameList)
del nameList[1]

print('删除第2个元素后的列表是', nameList)
name1 = nameList[0]

print('查询列表的第一个元素是：', name1)
print('修改之前的列表是', nameList)

nameList[0] = '孙悟空'

print('修改之后的列表是', nameList)

# ===   定义元组

gafataTuple = ('腾讯', '阿里巴巴', '苹果', '谷歌', 'FB', '亚马逊')

# 元组的长度

gafataLen = len(gafataTuple)

print('元组的长度是：', gafataLen)

# 查询元组元素

print('第1个元素的值', gafataTuple[0])

# === 7、集合----花括号{ }  定义：集合（sets）是不重复的容器
#
# List有序、可重复，Set无序，不能重复的

gafataSets = {'腾讯', '阿里巴巴', '苹果', '谷歌', 'FB', '亚马 逊', '亚马逊'}

print(gafataSets)

stockSets = set()

# 使用update()增加元素

stockSets.update(['腾讯', '阿里巴巴', '京东'])

print(stockSets)
# （2）删除

stockSets.discard('京东')

print(stockSets)

# （3）查找

txBool = '京东' in stockSets

print(txBool)

# （#4）修改

stockSets.discard('京东')

stockSets.update(['京东'])

print(stockSets)

# 8、字典（映射（键值对））----{ }

# 定义字典

patientDic = {'001': ['猴子', 29, '1型糖尿病', '较差'], '002': ['马云', 34, '2型糖尿病', '好转'], '003': ['王健林', 28, '1型糖尿病', '显著好转'],
              '004': ['马化腾', 52, '型糖尿病', '好转'], '005': ['王思聪', 30, '1型糖尿病', '好转']}

# ===   字典的操作：

# （1）增加

print(patientDic)

# （2）删除

del patientDic['005']

print(patientDic)

# （3）查询

valueList = patientDic['001']

print(valueList)
# （4）修改

print('修改之前的，病人信息：', patientDic)

patientDic['001'] = ['猴子', 29, '1型糖尿病', '好转']

print('修改之后的，病人信息：', patientDic)

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:

import sys
import pandas as pd
from collections import deque
import collections
pathList = sys.path

print('python的路径为:', pathList)
def ppd(a ) :
    fileNameStr = "F:\大数据\中级\第2关：零基础掌握人工智能核心语言Python\数据\病历数据.xlsx"

    xl = pd.ExcelFile(fileNameStr)

    patientDf = xl.parse('Sheet1')

    print(patientDf)
    print(a)


queue=deque(['001','002','003','004','005'])

queue.append('006')

print(queue)

#出队

queue.popleft()

print(queue)



stack=deque(['知乎动态','知乎回答','知乎文章'])

#进栈

print(stack)

stack.appendleft('知乎专栏')

print(stack)

#出栈

stack.pop()

print(stack)


# 16、python默认的字典
# 
# 16.1、有序


gafataDict={'谷歌':'GOOG','亚马逊':'AMZN','Facebook':'FB',

'苹果':'AAPL','阿里巴巴':'BABA','腾讯':'0700'}

print(gafataDict)

# 16.2、无序
# 
# OrderedDict:按照插入顺便，对字典进行排序

gafataDict2= collections.OrderedDict({'腾讯':'0700','阿里巴巴':'BABA','亚马逊':'AMZN','Facebook':'FB',})

print(gafataDict2)


# 
# 17、计算器


from collections import Counter

cDict=Counter('有一种势头是永远也遮挡不住的它的光芒,因为它们实在是太亮了,太光亮了')

print(cDict)

print(cDict.most_common(3))
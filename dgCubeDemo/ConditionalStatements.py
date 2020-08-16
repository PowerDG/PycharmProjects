# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:


# switch = {"valueA":functionA,"valueB":functionB,"valueC":functionC}
# try:
#　　switch["value"]() #执行相应的方法。
# except KeyError as e:
#       pass 或 functionX #执行default部分

switch = {
    "a":lambda x:x*2,
    "b":lambda x:x*3,
    "c":lambda x:x**x
}
try:
    print(switch["a"](6))
    print(switch["b"](6))
    print(switch["c"](6))
except KeyError as e:
    pass


# （1）值比较

#通过电影豆瓣评分，来判断是否要看

scoreNum=9.1

if scoreNum >=8:

    print('我要去看电影')

else:

    print('电影评分太低，不去看了')
# （2）逻辑比较


nameList=['猴子','马云','张三','李四']

if '猴子' not in nameList:

    print('没有这个人')

else:

    print('有这个人')

# （3）多个条件判断

age=int(input('请输入你家狗狗的年龄，按Enter键获取计算结果： '))

if age < 0 :

    print('狗狗年龄不能小于0')

elif age == 1:

    print('相当于14岁的人')

elif age ==2:

    print('相当于22岁的人')

else:

    human=22+(age-2)*5

print('对应人类年龄', human)

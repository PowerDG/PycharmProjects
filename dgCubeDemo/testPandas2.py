# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:


from collections import deque
import collections
# 2、二维数据分析
# 2.1、创建二维数组


# 引入包
import numpy as np
import pandas as pd

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
# 查询元素
print('查询元素', a[0, 2])
print('获取第1行', a[0, :])
print('获取第1列', a[:, 0])

# 2.1、Numpy数轴参数

# 引入包
import numpy as np
import pandas as pd

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
# axis=1,按行计算，axis=0,按列计算
print('按轴计算每一行', a.mean(axis=1))

# 引入包
import numpy as np
import pandas as pd

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
# axis=1,按行计算，axis=0,按列计算
print('按轴计算每一行', a.mean(axis=1))

# 2.2、字典类型的二维分析

# 创建字典类型数据
salesDict = {
    '购药时间': ['2018-01-01 星期五', '2018-02-01 星期六', '2018-03-01 星期天'],
    '社保卡号': ['001616528', '001616528', '0012602828'],
    '商品编码': [236701, 236701, 236701],
    '商品名称': ['强力VC银翘片', '清热解毒口服液', '感康'],
    '销售数量': [6, 1, 2],
    '应收金额': [82.8, 28, 16.8],
    '实收金额': [69, 24.64, 15]
}
# 导入有序字典
salesOrderDict = collections.OrderedDict(salesDict)
# 定义数据框，传入字典
salesDf = pd.DataFrame(salesOrderDict)
print(salesDf)
# 计算平均值
print(salesDf.mean())

# 2.3、iloc属性：索引位置查找值

# 引入包
import numpy as np
import pandas as pd
from collections import OrderedDict

# 创建字典类型数据
salesDict = {
    '购药时间': ['2018-01-01 星期五', '2018-02-01 星期六', '2018-03-01 星期天'],
    '社保卡号': ['001616528', '001616528', '0012602828'],
    '商品编码': [236701, 236701, 236701],
    '商品名称': ['强力VC银翘片', '清热解毒口服液', '感康'],
    '销售数量': [6, 1, 2],
    '应收金额': [82.8, 28, 16.8],
    '实收金额': [69, 24.64, 15]
}
# 导入有序字典
salesOrderDict = OrderedDict(salesDict)
# 定义数据框，传入字典
salesDf = pd.DataFrame(salesOrderDict)
print('查询元素是：', salesDf.iloc[0, 1])
print('获取第1行是：', salesDf.iloc[0, :])
print('获取第1列是：', salesDf.iloc[:, 0])

# 2.4、loc:索引名称查找值

# 引入包
import numpy as np
import pandas as pd
from collections import OrderedDict

# 创建字典类型数据
salesDict = {
    '购药时间': ['2018-01-01 星期五', '2018-02-01 星期六', '2018-03-01 星期天'],
    '社保卡号': ['001616528', '001616528', '0012602828'],
    '商品编码': [236701, 236701, 236701],
    '商品名称': ['强力VC银翘片', '清热解毒口服液', '感康'],
    '销售数量': [6, 1, 2],
    '应收金额': [82.8, 28, 16.8],
    '实收金额': [69, 24.64, 15]
}
# 导入有序字典
salesOrderDict = OrderedDict(salesDict)
# 定义数据框，传入字典
salesDf = pd.DataFrame(salesOrderDict)
print('查询元素是：', salesDf.loc[0, '商品编码'])
print('获取第1行是：', salesDf.loc[0, :])
print('获取第1列是：', salesDf.loc[:, '商品名称'])

# 2.5、其它查询方法

# 引入包
import numpy as np
import pandas as pd
from collections import OrderedDict

# 创建字典类型数据
salesDict = {
    '购药时间': ['2018-01-01 星期五', '2018-02-01 星期六', '2018-03-01 星期天'],
    '社保卡号': ['001616528', '001616528', '0012602828'],
    '商品编码': [236701, 236701, 236701],
    '商品名称': ['强力VC银翘片', '清热解毒口服液', '感康'],
    '销售数量': [6, 1, 2],
    '应收金额': [82.8, 28, 16.8],
    '实收金额': [69, 24.64, 15]
}
# 导入有序字典
salesOrderDict = OrderedDict(salesDict)
# 定义数据框，传入字典
salesDf = pd.DataFrame(salesOrderDict)
print('查询某几列:', salesDf[['商品名称', '销售数量']])
print('通过切片查询指定范围:', salesDf.loc[:, '购药时间':'销售数量'])

# 2.6、通过条件判断筛选

# 引入包
import numpy as np
import pandas as pd
from collections import OrderedDict

# 创建字典类型数据
salesDict = {
    '购药时间': ['2018-01-01 星期五', '2018-02-01 星期六', '2018-03-01 星期天'],
    '社保卡号': ['001616528', '001616528', '0012602828'],
    '商品编码': [236701, 236701, 236701],
    '商品名称': ['强力VC银翘片', '清热解毒口服液', '感康'],
    '销售数量': [6, 1, 2],
    '应收金额': [82.8, 28, 16.8],
    '实收金额': [69, 24.64, 15]
}
# 导入有序字典
salesOrderDict = OrderedDict(salesDict)
# 定义数据框，传入字典
salesDf = pd.DataFrame(salesOrderDict)
# 通过条件判断筛选
# 第1步:构建查询条件
querySer = salesDf.loc[:, '销售数量'] > 1
print(type(querySer))
print(querySer)

print(' 2.6、查看数据集描述统计信息')

# 2.6、查看数据集描述统计信息

# 引入包
import numpy as np
import pandas as pd
from collections import OrderedDict


def print():
    # 读取文件
    fileNameStr = 'F:\大数据\中级\第3关：数据分析的基本过程\朝阳医院2018年销售数据.xlsx'
    # 解析文件
    xls = pd.ExcelFile(fileNameStr)
    # 确认分析的数据源
    salesDf = xls.parse('Sheet1')
    # 打印表格数据
    print(salesDf.head(3))
    print('查看记录数是:', salesDf.shape)
    print('查看这一列的数据类型:', salesDf.loc[:, '销售数量'].dtype)
    print('查看数据的统计数值', salesDf.describe())

# 四、通过一个案例理解pandas、numpy
#
# 在分析前，需要在CMD环境中下载xlrd的包

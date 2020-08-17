# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:
# 引入包
import numpy as np
import pandas as pd

#
# 1.一维数据分析
# 1.1、一维数据分析
# 创建一维数组
a = np.array([2, 3, 4, 5])
# 查询元素
print('查询元素:', a[0])
# 切片访问
print('切片访问', a[1:3])
# 循环访问
for i in a:
    print('元素是:', i)
print('数据类型:', a.dtype)

# 1.2、统计功能

# 引入包
import numpy as np
import pandas as pd

# 创建一维数组
a = np.array([2, 3, 4])
print('平均值：', a.mean())
print('标准差：', a.std())

# 1.3、向量化计算

# 引入包
import numpy as np
import pandas as pd

b = np.array([1, 2, 3])
c = b * 4
print(c)

# 1.4、一维数据分析
#
# （1）创建一维数据结构：

# 引入包
import numpy as np
import pandas as pd

# 定义：pandas一维数据结构：Series
# 存放6家公司某一天的股价
stockS = pd.Series([54.74, 190.9, 173.14, 1050.3, 181.86, 1139.49],
                   index=['腾讯', '阿里巴巴', '苹果', '谷歌', 'Facebook', '亚马逊'])
print(stockS)

# （2）获取描述统计信息

# 引入包
import numpy as np
import pandas as pd

# 定义：pandas一维数据结构：Series
# 存放6家公司某一天的股价
stockS = pd.Series([54.74, 190.9, 173.14, 1050.3, 181.86, 1139.49],
                   index=['腾讯', '阿里巴巴', '苹果', '谷歌', 'Facebook', '亚马逊'])
print('获取描述统计信息')
# print(stockS)
# 获取描述统计信息
print(stockS.describe())

# （3）关键字iloc:根据索引值获取值

# 引入包
import numpy as np
import pandas as pd

# 定义：pandas一维数据结构：Series
# 存放6家公司某一天的股价
stockS = pd.Series([54.74, 190.9, 173.14, 1050.3, 181.86, 1139.49],
                   index=['腾讯', '阿里巴巴', '苹果', '谷歌', 'Facebook', '亚马逊'])
# iloc属性用于根据索引位置获取值
print('iloc属性用于根据索引位置获取值')
print(stockS.iloc[0])

# （4）关键字loc：根据索引值获取值

import pandas as pd

# 定义：pandas一维数据结构：Series
# 存放6家公司某一天的股价
stockS = pd.Series([54.74, 190.9, 173.14, 1050.3, 181.86, 1139.49],
                   index=['腾讯', '阿里巴巴', '苹果', '谷歌', 'Facebook', '亚马逊'])
# loc属性用于根据索引获取值
print(stockS.loc['腾讯'])

# （5）向量化计算：向量相加

# 引入包
import numpy as np
import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'e', 'f'])
s3 = s1 + s2
print(s3)

# 上面的计算中有出NaN，所以这里我们需要对缺失值进行处理
#
# （6）缺失值处理
#
# 删除缺失值

# 引入包
import numpy as np
import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'e', 'f'])
s3 = s1 + s2
print('删除缺失值')
print(s3.dropna())

# 将缺失值进行填充

# 引入包
import numpy as np
import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'e', 'f'])
s3 = s1.add(s2, fill_value=0)

print('将缺失值进行填充')
print(s3)

# -*-coding:utf-8-*-

# -------------------
# pandas 两种数据结构：Series和DataFrame
# -------------------

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

'''
pandas 功能：
    数据丢失
    插入和删除
    数据对齐
    数据分组
    数据转换
    索引、切片
    数据集的合并
    时间序列
'''

'''
    Series:一个类似于一维的数组对象，包含一个数组的数据和一个与数组关联的数据标签，标签也叫索引
    DataFrame:一个DataFrame就是一个表格，类似电子表格的数据结构，包含一个经过排序的列表集；
              DataFrame有行和列的索引，可以被看作是一个series的字典。
              在底层，数据是作为一个或多个二维数组存储的，而不是列表，字典。
'''
# 一个简单的Series
obj = Series([4, 7, -5, 3])
print obj  # 左边为索引，右边为值
print obj.values  # 值
print obj.index  # 索引
print
print '-----------------------------------'
# 创建一个带索引的series
obj = Series([83, 43, 54, 23], index=['a', 'b', 'c', 'd'])
print obj
print obj.index
print
'''
    Series是一个定长的，有序的字典，因为它把索引和值映射起来了。
'''
data = {'mich': 35000, 'tex': 71000, 'utah': 16000, 'jack': 45000}
obj = Series(data)
print obj
print
print '-----------------------------------'
# 一个简单的DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print frame
print DataFrame(data, columns=['year', 'pop', 'state'])  # 对列进行排序
print

dates = pd.date_range('20130101', periods=6)
print dates
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('abcd'))
print df
print

dd = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo'
})
print dd
print dd.dtypes

print dd.head()
print dd.tail(3)
print dd.index
print dd.values

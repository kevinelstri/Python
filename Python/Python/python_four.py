# -*-coding:utf-8-*-

# -----------------
# 高级特性
# -----------------

# 构造一个列表
L = []
n = 1
while n < 99:
    L.append(n)
    n = n + 2
print L

# ----------
#    切片
# ----------

L = ['mich', 'sara', 'tracy', 'bob', 'jack']
# 方法1：使用循环，获取前三个元素
r = []
n = 3
for i in range(n):
    r.append(L[i])
print r
# 方法2：直接获取
print L[0:3]
print L[:3]
print L[-1:]  # 获取最后一个元素
# 创建数列
L = range(100)
print L
print L[-10]
print L[-10:]
print L[10:20]
print L[::5]  # 每5个数取一个
print L[:10:2]  # 取10个数，每两个取一个

# --------
#   迭代
# --------
# 使用for循环来遍历这个list或tuple，这种遍历称为迭代
# python中，迭代时通过for...in来实现的

# 迭代key
d = {'a': 1, 'b': 2}  # 字典使用的是key-value键值对
for key in d:
    print key

# 迭代value
d = {'a': 1, 'b': 2}
for value in d.itervalues():
    print value

# 同时迭代key和value
d = {'a': 1, 'b': 2}
for k, v in d.iteritems():
    print k, ':', v

'''
判断是否可迭代，通过collections模块的iterable类型来判断
'''
from collections import Iterable

print isinstance('abc', Iterable)
print isinstance([abs], Iterable)

'''
列表生成式
'''
# 创建list生成式
print range(1, 11)

L = []
for x in range(1, 11):
    L.append(x * x)
print L

print [x * x for x in range(1, 11)]  # 直接使用列表生成式进行生成list

print [x * x for x in range(1, 11) if x % 2 == 0]


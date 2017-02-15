# -*-coding:utf-8-*-

# ----------------
# Numpy：科学计算，主要是矩阵运算
# ----------------

#    THE BASICS

import numpy as np

'''
    Numpy的数组称为ndarry，也可以使用array来表示
函数说明：
    ndarray.ndim:矩阵的维数
    ndarray.shape:矩阵的行列
    ndarray.size:矩阵的元素个数
    ndarray.dtype:矩阵的元素类型
    ndarray.itemsize:矩阵中每个元素的位数（64位：64/8=8，32位：32/8=4）
    ndarray.data:矩阵中的元素缓冲区的数目，一般使用不到
'''
a = np.arange(15).reshape(3, 5)  # 创建一个长度为15的数组，将其转换成3行5列的矩阵
print a
print a.shape  # 矩阵的行列（3行5列）
print a.ndim  # 矩阵的维数（二维矩阵）
print a.dtype  # 矩阵元素的类型
print a.itemsize
print a.size  # 矩阵的元素个数
print type(a)
b = np.array([3, 4, 5])
print b
print type(b)
print '----------------------------'

'''
    创建数组：
'''
a = np.array([2, 3, 4])
print a
print a.dtype
b = np.array([1.2, 3.5, 5.1])
print b
print b.dtype
c = np.array([(1, 2, 3, 4), (2, 3, 4, 5)])  # 创建二维矩阵
print c
d = np.array([[1, 2], [3, 4]], dtype=complex)
print d

# 创建全0数组
print np.zeros((3, 4))

# 创建全1数组
print np.ones((2, 3, 4))

# 创建空数组
print np.empty((2, 3))

# 创建一个数字序列，使用arange
print np.arange(10, 30, 5)
print np.arange(0, 2, 0.3)

print '-----------------------'

from numpy import pi

print np.linspace(0, 2, 9)  # 起点为0，终点为2，输出0和2之间的9个数，平均获取
x = np.linspace(0, 2 * pi, 100)  # 起点为0，终点为2*pi，输出中间的100个数
print x
f = np.sin(x)  # 对100个数求三角函数
print f
print '------------------------'

# random随机函数
print np.random.rand(3, 2)  # 随机输出3行2列的矩阵
print
print np.random.randn(3, 2)  # 随机输出3行2列的矩阵，并且具有标准正态分布
print '------------------------'

'''
    基本操作：
'''
# + - * / 等操作,一维数组的运算
a = np.array([20, 30, 40, 50])
print a
b = np.arange(4)
print b
print a * b
print a + b
print a - b
print b / a
print b ** 2
print 10 * np.sin(a)
print '-------------------------'
# 矩阵运算
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print A * B  # 矩阵相乘
print A.dot(B)  # 矩阵点乘
# += *=
a = np.ones((2, 3), dtype=int)
b = np.random.random((2, 3))
a *= 3
print a
b += a
print b
print '-------------------------'
'''
    数学函数
'''
a = np.arange(3)
print a
print np.exp(a)  # e的次幂
print np.sqrt(a)  # 开方
c = np.array([2, -1, 4])
print np.add(a, c)  # 数组相加，求和
print '-------------------------'

'''
索引、切片和迭代
'''
a = np.arange(10) ** 3
print a
print a[2]
print a[2:5]
print a[::-1]  # 逆序输出


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)  # 产生一个矩阵
print b
print b[2, 3]
print b[0:5, 1]
print b[:, 1]
print b[1:3, :]

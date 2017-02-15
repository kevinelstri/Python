# -*-coding:utf-8-*-

import cmath
import math


#################################################
# x = pi
# abs(x)  返回数字的绝对值
# cmath.sqrt(x)  # 返回平方根，也适用于负数
# float(x)  # 转换成浮点数
# input()  # 用于用户输入
# int()  # 转换成整数
# long(x)  # 转换成长整数
# math.ceil(x)  # 返回数的上入整数，返回值类型为浮点数
# math.floor(x)  # 返回数的下舍整数，返回值类型为浮点数
# math.sqrt(x)  # 返回平方根，不适用于负数
# pow(x, 2)  # 次幂计算
# raw_input()  # 获取用户输入
# repr(x)  # 返回值的字符串表示形式
# round(x)  # 对数字进行四舍五入
# str(x)  # 将值转换成字符串形式

# cmp(x, y)  比较两个值
# len(seq)  返回序列的长度
# list(seq)  把序列转换成列表
# max()  返回序列中的最大值
# min()  返回序列中的最小值
# reversed(seq)  对序列进行反向迭代
# sorted(seq)  返回已排序的元素的列表
# tuple(seq)  将序列转换成元组

# dict(seq) 使用键值对来建立字典

# chr(n)  返回n所代表的包含一个字符的字符串
# eval()  将字符串作为表达式计算，并且返回值
# enumerate(seq) 产生用于迭代的（索引、值）对
# ord(c)  返回单字符字符串的int值
# range()  创建整数的列表
# reversed(seq) 产生seq中值的反向版本，用于迭代
# sorted() 返回seq中值排序后的列表
# xrange()  创建xrange对象用于迭代
# zip()  创造用于并行迭代的新序列
#################################################

def function():
    # 并行迭代
    names = ['anne', 'beth', 'george', 'damon']
    ages = [12, 45, 32, 102]
    for i in range(len(names)):  # 标准迭代做法
        print names[i], 'is', ages[i], 'years old'

    # 使用内建zip函数来进行并行迭代，可以把两个序列进行压缩在一起，返回一个元组的列表
    print zip(names, ages)
    for name, age in zip(names, ages):
        print name, 'is', age, 'years old'

    # zip函数也可以用于任意多的序列
    print zip(range(5), xrange(100000000))  # output:[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

    # range,返回的是一个列表
    print range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print range(2, 10)
    print range(2, 10, 2)
    print type(range(10))  # <type 'list'>

    # xrange，返回的是一个生成器
    print xrange(10)  # xrange(10)
    print xrange(2, 10)
    print xrange(2, 10, 2)
    print type(xrange(10))  # <type 'xrange'>

    # enumerate 函数用于遍历序列中的元素以及它们的下标：
    for i, j in enumerate(('a', 'b', 'c')):
        print i, j

if __name__ == '__main__':
    function()

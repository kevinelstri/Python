# -*-coding:utf-8-*-

# -----------------
# 函数
# -----------------

print abs(-100)  # abs函数：取绝对值
print cmp(1, 2)  # cmp函数，比较大小，如果x<y,返回-1，如果x=y,返回0，如果x>y，返回1

# ---------------
# 数据类型转换：
#     数据的不同类型之间的转换
# ---------------
print int('123')  # int()可以将其他类型转换为整数类型
print int(12.35)
print float('12.36')
print str(12.37)
print unicode(100)
print bool(1)
print bool(0)


# -------------------
# 函数定义，使用def进行函数定义
# -------------------
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print my_abs(12)


# -------------------
# 函数参数
# -------------------

def power(x):  # 一个参数
    return x * x


print power(100)


def powern(x, n):  # 两个参数
    s = 1
    while n >= 1:
        s = s * x
        n = n - 1
    return s


print powern(2, 3)


def new_list(l=[]):  # 函数中使用list元组
    return l


print new_list([1, 2, 3])


def cal(number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


print cal([1, 2, 3, 4, 5])
print cal((1, 3, 5, 6))


def calc(*number):  # 可变参数
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


print calc(1, 3, 5, 6)


# ---------------
# 默认参数一定要用不可变对象，如果是可变对象，就会出现逻辑错误!
# *args 是可变参数，args接受的是一个tuple
# **kw是关键字参数，kw接受的是一个dict
# 可变参数既可以直接传入：func(1,2,3),又可以先组装list或tuple,再通过*args传入：func(*(1,2,3))
# 关键字参数既可以直接传入：func(a=1,b=2),又可以先组装dict，再通过**kw传入：func(**{'a':1,'b':2})
# ---------------


# -----------------
# 递归函数
# -----------------
def fact(n):  # 使用递归来求阶乘n!
    if n == 1:
        return 1
    return n * fact(n - 1)


print fact(5)


# -----------------
# 使用递归函数需要注意防止栈溢出，函数调用是通过栈这种数据结构来实习的，每当进入一个函数调用，栈就会加一层栈帧，
# 每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多。
#
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，
# -----------------

# 尾递归调用，仍然会导致栈溢出问题
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print fact(100)

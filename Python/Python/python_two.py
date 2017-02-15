# -*-coding:utf-8-*-

# ---------
# python基础
# ---------

# ---------
# 数据类型
#    整数：
#    浮点数：可以使用科学记数法表示，1.23，3.14，-9.01
#    字符串：
#    布尔值：and or not运算，True,False
#    空值：None
#    变量：
#    常量：
# ---------

# ------------
# 在计算机内存中，统一使用unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为utf-8编码
# 用记事本编辑的时候，从文件读取的utf8字符被转换为unicode字符到内存里，编辑完成后，保存的时候再把unicode转换为utf8保存到文件。
# 浏览网页的时候，服务器会把动态生成的unicode内容转换为utf8再传输到浏览器
# ------------

# ---------
# u'xxx'只能是unicode编码，字符串'xxx'虽然是ascii编码，但也可以看成是utf8编码
# 把u'xxx'转换为utf8编码的'xxx'使用encode('utf8')方法：
# ---------

print u'abc'.encode('utf-8')  # unicode编码转换成utf8编码
print u'中文'.encode('utf-8')
print len(u'abc')
print len(u'中文')

print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')  # 把utf8编码转换为unicode字符串

# ---------
# 格式化字符串,使用%来表示字符串的格式化形式
#    %d:整数
#    %f:浮点数
#    %s:字符串
#    %x:十六进制
# ---------

print 'hello, %s' % 'world'
print '%2d-%02d' % (3, 1)
print '%2.2f-%10.3f' % (43.673278, 3.141582657)
print 'Age:%s, Gender:%s' % (25, True)

# ---------
# 使用list和tuple
# list是一种有序的集合，可以随时进行添加和删除其中的元素
# ---------

classmates = ['hello', 'bob', 'mach']
print classmates
print len(classmates)  # 查看list长度
print classmates[1]  # 使用索引来查找元素
classmates.pop()  # pop()方法删除list末尾的元素
print classmates
classmates[1] = 'jack'
print classmates

# --------
# tuple 有序列表，一旦初始化就不能修改
# --------
classmates = ('Mich', 'Bob', 'Tracy')
print classmates[2]
t = (1,)
print t
t = ('a', 'b', 'c', ['A', 'B'])
print t
print t[1]
print t[3][1]

# ------------
# list和tuple是内置的有序集合，list是可变的，tuple是不可变的
# ------------

# ------------
# 条件判断和循环：
#    使用if、else,for循环
# ------------

# if选择结构
age = 6
if age <= 10:
    print "your age is : ", age
else:
    print 'adult'

# for循环结构
names = ['mich', 'bob', 'tracy']
for name in names:
    print name

# 变量运算
sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + i
print sum

# 整数序列生成器：range
for i in range(10):
    print i

sum = 0
for i in range(101):
    sum = sum + i
print sum

# while循环
sum = 0
n = 1
while n < 101:
    sum = sum + n
    n = n + 1
print sum

# 输入操作raw_input
# birth = int(raw_input('birth:'))
# if birth < 2000:
#     print '00前'
# else:
#     print '00后'


    # -------------------
    # 使用dict和set
    # -------------------

#----------------
# dict字典，类似于其他语言的map，使用键值对（key-value）存储，具有极快的存储速度
#----------------

# 使用dict将名字和成绩对应起来，构成名字-成绩键值对
names = ['mich', 'bob', 'tracy']
scores = [98, 67, 76]
d = {}  # 创建字典
for i in range(len(names)):
    d.setdefault(names[i], scores[i])
print d
d.pop('bob')  # 使用pop来删除字典，注意pop中必须指定字典的元素
print d
# items = [('mich', 'bob', 'tracy'), (98, 67, 76)]
# dd = dict(items)
# print dd


# ------------
# set集合，也是一组key的集合，但不存储value，由于key值不能重复，所以在set中，没有重复的元素
# ------------
s = set([1,2,3])
print s

s.add(4)
print s

s.remove(3)
print s
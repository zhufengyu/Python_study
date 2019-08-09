# 2.1变量的命名与使用

iVariable = 10
cVariable = 'Hello World'
bVariable = True
fVariable = 1.12
print('整型为：',iVariable)
print('字符串为：',cVariable)
print('布尔型为：',bVariable)
print('浮点型为：',fVariable)

#   1.变量名只能为字母（A-Z,a-z）、数字（0-9）
#   2.第一个字母不能是数字，如：2iVariable
#   3.不能是python关键字，如：class这个单词来命名一个变量
#   4.区分大小写，如：iA和ia是不同的变量

#   命名规范：
#             1.单词首字母大写，并在单词前加上变量类型，如：iVariable
#             2.多单词组成变量名，每个单词首字母大写，单词直接拼接，并在单词前加上变量类型，如：iMyVariable
#             3.如果不想在变量前加变量类型，变量首字母小写，如果多个单词拼接，则拼接单词首字母大写，如：variable、myVariable
#   变量输出前必须赋值，否则该变量不会被创建，运行报错，如：NameError: name 'iVariable' is not defined
#   Python支持多变量赋值，有两种方式：
#             1.先创建一个对象，值为1，然后对变量a、b、c进行赋值，例：
a = b = c = 1
print('a is ', a)
print('b is ', b)
print('c is ', c)

#             2.分别创建三个不同类型的对象，然后分别赋值给变量d、e、f，例：
d , e , f = 10 , 'hello' , True
print('d is ', d)
print('e is ', e)
print('f is ', f)


# Python关键字表(不可用作变量名）
# False        True        None         class      Type       and
#
# def           Del        if           elif       Else      as
#
# break       Continue     for          from      import     in
#
# pass         Not        is            or        Return      try
#
# except       While      assert      finally     Nonlocal     lambda
#
# raise        With       yield
#
#




# 2.2 变量的深浅拷贝

# 变量的拷贝定义：对变量进行数据处理时为了保留数据处理前的变量而重新定义新的变量，简单来说就是将一个变量数据复制到另一个变量里面

# 浅拷贝

# 例：
a1 = 'hello world'
a2 = a1
print(a2)
# 程序输出hello world
# 通过a2 = a1这种方式将字符串hello world分别赋值给a1、a2

# 变量拷贝分为浅拷贝和深拷贝，这两种拷贝主要用于数据类型为列表和字典的变量。
# import 是Python里面导入功能模块
import copy
# 生成list_1列表，列表有4个元素
list_1 = [1,2,'a',3]
# 通过拷贝的方式赋值给变量list_2(浅拷贝）
list_2 = list_1
# copy.copy是函数方法，该函数来自import copy。
# list_2 = copy.copy(list_1)      (浅拷贝）
# 修改 list_2某个元素的值
list_2[2] = 'b'
# 分别输出 list_1和 list_2,观察变化
print(list_1)
print(list_2)
# 输出结果：
# [1, 2, 'b', 3]
# [1, 2, 'b', 3]


# 上述代码讲述变量list_1值为列表或字典时，通过 list_2 = list_1 的浅拷贝，当某个变量的列表元素产生变化时，另一个列表元素同时改变
# 结论：如果变量a是一个列表或字典时，通过浅拷贝的方式生成变量b，当其中一个变量发生改变时，另一个变量也会随之改变。

# 深拷贝

# 定义：如果变量a是一个列表或字典时，通过深拷贝的方式生成变量b，当其中一个变量发生改变时，另一个变量不会随之改变。
# 例：

import copy
list_3 = [1,2,'a',3]
#变量 list_3 深拷贝到变量 list_4
list_4 = copy.deepcopy(list_3)
# 修改 list_4某个元素的值
list_4[2] = 'b'
# 分别输出 list_3和 list_4,观察变化
print(list_3)
print(list_4)

# 输出结果：
# [1, 2, 'a', 3]
# [1, 2, 'b', 3]





# 2.3  运算符使用

# 分类
# 算术运算符：计算两个变量的加减乘除等计算法则
# 比较（关系）运算符：比较两个变量的大小情况
# 赋值运算符：先计算后赋值到新的变量
# 逻辑运算符：与或非的逻辑判断
# 位运算符：把数值看成二进制来进行计算
# 成员运算符：判断字符串、元组、列表、或字典中是否含有成员
# 身份运算符：用来比较两个对象的存储单位，比如判断变量a和b在计算机的内存地址是否一致


# 2.3.1 算术运算符

# 运算符                        描述                                        实例
# +                            加法,两个对象相加                             x = 2+3,x的值为5
# -                            减法,两个对象相减或用于表示负数                 x = 2-3,x的值为-1
# *                            乘法,两个数相乘                               x = 2*3,x的值为6
# /                            除法                                        x = 9/2,x的值为4.5
# %                            取模,获取除法中的余数                         x = 9%2,x的值为1
# **                           幂,求出几个相同因数的积                        x = 2**3,x的值为8
# //                           取整,获取除法中的整数部分                       x = 9//2,x的值为4

# 例:
x = 8
y = 5
print('加法运算符:',x+y)
print('减法运算符:',x-y)
print('乘法运算符:',x*y)
print('除法运算符:',x/y)
print('取模运算符:',x%y)
print('幂运算符:',x**y)
print('取整运算符:',x//y)



# 2.3.2 比较运算符

# 运算符                        描述                                        实例
# ==                           等于,比较两个对象是否相等                      2==3,比较结果为False
# !=                           不等于,比较两个对象是否不相等                  2!=3,比较结果为True
# >                            大于                                        2>3,比较结果为False
# <                            小于                                        2<3,比较结果为True
# >=                           大于等于                                     2>=3,比较结果为False
# <=                           小于等于                                     2<=3,比较结果为True

# 例:
x1 = 2
y1 = 3
print('等于运算符：',x1==y1)
print('不等于运算符：',x1!=y1)
print('大于运算符：',x1>y1)
print('小于运算符：',x1<y1)
print('大于等于运算符：',x1>=y1)
print('小于等于运算符： ',x1<=y1)




# 2.3.3 赋值运算符

# 运算符                        描述                                        实例
# =                            简单的赋值运算符                              c = a + b,将a+b的结果赋值为c
# +=                           加法赋值运算符                                c += a  等效于 c = c + a
# -=                           减法赋值运算符                                c -= a  等效于 c = c - a
# *=                           乘法赋值运算符                                c *= a  等效于 c = c * a
# /=                           除法赋值运算符                                c /= a  等效于 c = c / a
# %=                           取模赋值运算符                                c %= a  等效于 c = c % a
# **=                          幂赋值运算符                                  c **= a  等效于 c = c ** a
# //=                          取整赋值运算符                                c //= a  等效于 c = c // a


# 例：
x2 = 5
y2 = 2

print('简单的赋值运算符:',x2+y2)

x2 += y2
print('加法赋值运算符:',x2)

x2 = 5
x2 -= y2
print('减法赋值运算符:',x2)


x2 = 5
x2 *= y2
print('乘法赋值运算符:',x2)

x2 = 5
x2 /= y2
print('除法赋值运算符:',x2)

x2 = 5
x2 %= y2
print('取模赋值运算符:',x2)

x2 = 5
x2 **= y2
print('幂赋值运算符:',x2)

x2 = 5
x2 //= y2
print('取整赋值运算符:',x2)




# 2.3.4 逻辑运算符

# 定义： 将多个条件进行与或非的逻辑判断，常用于python的条件判断

# 运算符                        描述                                                    实例
#                                如x and y，若x或y为False，则返回False,                    False and 10，返回 False
# And（与）                       若x和y皆为True，则返回True，                              True and True，返回 True
#                                若x和y皆为数字，则返回最大的数值。                          10 and 20 ,返回 20

#                                  如x and y，若x或y为True，则返回True，                     False and 10，返回 10
# Or（或）                          若x和y皆为False，则返回False，                            False and True，返回 True
#                                  若x和y皆为数字，则返回最小的数值。                          10 and 20 ,返回 10

# Not（非）                           如not x，若x为True，则返回False                         not False ，返回 True
#                                    若x为False，则返回True                                  not True ，返回 False

# 逻辑运算符的与或非需要对两个对象进行逻辑判断，这两个对象可以是任意数据类型

# 例：

x3 = False
y3 = 'a'
print('与运算符：', x3 and y3)
print('或运算符：', x3 or y3)
print('非运算符：',not x3)

# 变量x和y的数据类型分别为布尔类型和字符串，逻辑运算符会首先判断对象的真假性，如变量y是空的字符串，则返回False，非空的字符返回True，同理，元组、列表、字典和字符串的判断逻辑相同，最后根据两个对象的真假进行与或非的逻辑判断





# 2.3.5 位运算符


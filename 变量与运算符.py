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




# 变量的深浅拷贝

# 变量的拷贝定义：对变量进行数据处理时为了保留数据处理前的变量而重新定义新的变量，简单来说就是将一个变量数据复制到另一个变量里面
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
# 通过拷贝的方式赋值给变量list_2
list_2 = list_1
# copy.copy是函数方法，该函数来自import copy。
# list_2 = copy.copy(list_1)
# 修改 list_2某个元素的值
list_2[2] = 'b'
# 分别输出 list_1和 list_2,观察变化
print(list_1)
print(list_2)
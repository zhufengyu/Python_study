



# 3.1数字的类型及转换
#

# 数字类型分类：
# 1.整型：没有小数点的数值
# 2.浮点型：带有小数点的数值
# 3.布尔类型：以True和False表示，实质分为1和0，为区分1和0，改为True和False表示
# 4.复数是由一个实数和一个虚数组合构成，可以用 x+yj 或者complex（x，y）表示

# 例：
a = 10
b = 5.5
c = False
d = 2+3j
print(type(a)),print(type(b)),print(type(c)),print(type(d))

# 可以使用特定的方法对4种数据类型进行相互转换
# 例：
#
# 整型分别转换浮点型、布尔型、复数
print('整型转浮点型：',float(a))
print('整型转布尔型：',bool(a))
print('整型转复数：',complex(a))
#
# 浮点型分别转换整型、布尔型、复数
print('浮点型转整型：',int(b))
print('浮点型转布尔型：',bool(1.0))
print('浮点型转复数：',complex(b))
#
# 布尔型分别转换整型、浮点型、复数
print('布尔型转整型：',int(c))
print('布尔型转浮点型：',float(c))
print('布尔型转复数：',complex(c))
#
# 复数只能转换布尔型
print('复数转布尔型：',bool(d))

# 整型、浮点型和布尔型可以想互转换
# 复数只能转换布尔型
# 不支持整型和浮点型转换




# 3.2 字符串的定义及使用


# 3.2.1 字符串的定义
# 字符串是由数字、字母、下划线组成的一串字符，
# 他是编程语言中表示文本的数据类型，主要用于编程、概念说明、函数解释等。字符串在存储上类似字符数组，所以每一位的单个元素都可以提取。
# Python的字符串可以用单引号、双引号、或三引号来表示
# 如果字符串中含有单引号，可以使用双引号或三引号来表示
# 如果字符串含有双引号，可以使用单引号或三引号来表示
# 如果字符串中含有单引号和双引号，可以使用转义字符或三引号表示
# 例：

# 单引号、双引号、三引号的表示方式

a1 = 'Hello world'
b1 = "Hello world"
c1 = """Hello world"""

# 字符串含有双引号的表示方式

d1 = 'Hello "world"'
e = """hello "I" love Python"""

# 字符串含有单引号的表示方式

f = "Hello 'I' love Python"
g = """Hello "I love" Python"""

# 字符串含有单引号和双引号的表示方式

h = """Hello "I" 'love' Python"""
i = 'Hello "I" \'love\' Python'
j = "Hello \"I\" \'love\' Python"

# 转义字符定义

# 转义字符是一种特殊字符常量，以反斜线“\”开头，后面跟一个或几个字符。转义字符具有特殊含义，用于区别原有的意义

# 转义字符表

# 转义字符              意义
# \a                   响铃（BEL）
# \b                   退格（BS），将当前位置移到前一列
# \f                   换页（FF），将当前位置移到下页开头
# \n                   换行（LF），将当前位置移到下一行开头
# \r                   回车（CR），将当前位置移到本行开头
# \t                   水平制表（HT），（跳到下一个TAB位置）
# \v                   垂直制表（VT）
# \\                   代表一个反斜线字符‘\’
# \'                   代表一个单引号字符
# \"                   代表一个双引号字符
# \?                   代表一个问号
# \0                   空字符（NULL）
# \ooo                 1到3位八进制数所代表的任意字符
# \xhh                 1到2位十六进制所代表的任意字符


#字符串操作





# 3.2.2 字符串截取

# 截取格式为：
# 字符串[开始位置:结束位置:间隔位置]
# 定义：开始位置是0，正数代表从左边开始，负数代表从右边开始，默认代表从0开始
#      结束位置是被截取的字符串位置，空值默认取到字符串结尾。
#       间隔位置默认为1截取内容不做处理，如果设置为2，就将截取的内容再隔一取数

# 例：

# 字符串取数
str = 'ABCDEFG'
# 截取第一位到第三位字符
print('截取第一位到第三位字符:'+ str[0:3:])
# 截取字符串全部字符
print('截取字符串全部字符:'+ str[::])
# 截取第七个字符到结尾
print('截取第七个字符到结尾:'+ str[6::])
# 截取从头开始倒数第三个字符之前
print('截取从头开始倒数第三个字符之前:'+ str[:-3:])
# 截取第三个字符
print('截取第三个字符:'+ str[2])
# 截取倒数第一个字符
print('截取倒数第一个字符:'+ str[-1])
# 与原字符串顺序相反的字符串
print('与原字符串顺序相反的字符串:'+ str[::-1])
# 截取倒数第三位到倒数第一位之间的字符串
print('截取倒数第三位到倒数第一位之间的字符串:'+ str[-3:-1:])
# 截取倒数第三位到结尾的字符串
print('截取倒数第三位到结尾的字符串:'+ str[-3::])
# 逆序截取
print('逆序截取:'+ str[:-5:-3])





# 3.2.3 字符串替换


# 替换方法
# 字符串.replace('被替换内容','替换后内容')

# 注意：使用replace替换字符串后仅为临时变量，需要重新赋值才能保存。

# 例：
str1 = 'abcabcabc'
# 单个内容替换
print(str1.replace('c','v'))
# 输出内容为：abvabvabv

# 字符串替换
print(str1.replace('bc','wv'))
# 输出内容为awvawvawv

# 替换成特殊符号（空格）
print(str1.replace('bc',' '))
# 输出结果为：a a a


# 3.2.4 字符串查找

# 查找方法:

# 字符串.find('要查找的内容'[,开始位置,结束位置])

# 定义：
# 开始位置和结束位置表示要查找的范围，若为空值，则表示查找所有，找到目标后会返回目标的第一位内容所在位置，位置从0开始算，如果没找到就返回-1

# 例：
str2 = 'ABCDABC'
# 查找全部
print(str2.find('A'))
# 返回结果0

# 从字符串第四个字符开始查找

print(str2.find('A',3))
# 返回结果4

# 从从第二个字符到第六个字符查找
print(str2.find('C',1,5))
# 返回结果2

# 查找不存在内容
print(str2.find('E'))
# 返回-1


# 除了使用find函数查找字符串中某个内容，使用index函数也可以，index是查找第一次出现的位置，如果查不到子串，抛出异常，而不是-1

# 查找全部
print(str2.index('A'))

# 从字符串第四个开始查找
print(str2.index('A',3))

# 从字符串第二个到第六个开始查找
print(str2.index('A',1,5))

# 查找不存在的内容
# print(str2.index('x'))




# 3.2.5 字符串分割
# 方法：
#     字符串.split('分隔符'，‘分割次数’)
# 注：如果存在分割次数，就仅分割成“分割次数+1”个子字符串，如果空，就默认全部分割

# 例：

str3 = str2

# 全部分割
print(str3.split('B'))

# 分割1次
print(str3.split('B',1))




# 3.2.6 字符串拼接

# 字符串5种实现方式：

str4 = 'Hello Python'

# 1.加号拼接
print('加号拼接:'+str4)

# 2.逗号拼接
print('逗号拼接：', str4)

# 3.直接拼接
print('直接拼接：''Hello Python')

# 4.格式化拼接
print('格式化拼接：'+'%s' %(str4))

# 5.join方法拼接
str_list = ['Hello ','Python']
str4 = ''.join(str_list)
print('join拼接：'+ str4)




# 3.3 元组与列表
#
# 定义：元组和列表非常相似，表现形式上有所不同。
# 区别：1.元组在定义后无法修改只能读取，而列表则支持修改和读取。
#     2.元组使用小括号来定义，而列表使用中括号定义。
#     3.元组列表中元素可以是任何数据类型，每个元素之间使用英文逗号隔开
#     4.如果元组和列表中没有任何元素，说明是一个空的元组或列表

# 例：
# (元组)
tuple_1 = (1,'Python',False,5.5,(1,2,3),['Hello',3])

# （列表）
list_1 = [1,'Python',False,5.5,(1,2,3),['Hello',3]]

# 从元组和列表的定义看，元素一致，可以是整型、字符串、布尔型、浮点型、元组和列表
# 如果元素是一个元组或列表，那么这是一种嵌套模式
# 如果定义元组只有1个元素，则必须在元素后加逗号，否则Python会把小括号作为运算法则小括号。如（1，）


# 元组和列表的操作处理

# 读取
# 元组和列表的读取操作是通过下标索引进行定位读取的，下标索引从0开始，代表第一个元素。

# 例：

print('读取元组第一个元素：',tuple_1[0])
print('读取元组第二个元素：',tuple_1[1])
print('读取元组倒数第二个元素：',tuple_1[-2])
print('读取元组倒数第一个元素：',tuple_1[-1])

print('读取列表第一个元素：',list_1[0])
print('读取列表第二个元素：',list_1[1])
print('读取列表倒数第二个元素：',list_1[-2])
print('读取列表倒数第一个元素：',list_1[-1])

# 下标索引从0开始并以正数表示，代表元组列表的左边开始读取，如果下标索引以负数表示，代表元组列表的右边开始读取。
# 也可以读取元组列表中的连续结果元素，并将其生成一个新的元组或列表，

# 例：

# 读取元组部分元素
print('读取元组第一到第四个元素：',tuple_1[0:4])
print('读取元组倒数第四个到倒数第一个元素：',tuple_1[-4:-1])
print('读取元组倒数第四个到倒数第一个元素，并隔一取数：',tuple_1[-4:-1:2])

# 读取列表部分元素
print('读取列表第一到第四个元素：',list_1[0:4])
print('读取列表倒数第四个到倒数第一个元素：',list_1[-4:-1])
print('读取列表倒数第四个到倒数第一个元素，并隔一取数：',list_1[-4:-1:2])



# 通过元素查找下标、统计元素至出现次数、判读元素是否存在元组或列表、获取元组和列表的总长度

# 例：

tuple_2 = (1,'Python',False,5.5,(1,2,3),['Hello',3],'Python')

# （列表）
list_2 = [1,'Python',False,5.5,(1,2,3),['Hello',3]]


# 通过元素值查找下标索引
# 默认搜索整个元组，并返回元素第一次出现的下标索引
print('Python',tuple_2.index('Python'))


# 在index设置4，7是将元组定位到第四个到第七个元素区间
# 然后在这个区间查找元素
print('第二个元素下标：',tuple_2.index('Python',4,7))
# 列表
print('(1,2,3)下标为：',list_2.index((1,2,3)))

# 统计元素出现次数
print('元组元素Python出现次数：',tuple_2.count('Python'))

# 判断元素是否在元组或列表中
print('Python','Python' in tuple_2)
print('love','love' in list_2)

# 获取元组或列表总长度
print('元组总长度：',len(tuple_2))
print('列表总长度：',len(list_2))



# 修改、删除或添加元素


list_3 = [1,'Python',False,5.5,(1,2,3),['Hello',3]]

# 通过下标索引修改元素值
list_3[1] = 'LOVE Python'
print(list_3)

# 添加元素的四种方法:append函数、extend函数、insert函数、列表相加

# append函数是列表末端追加元素，将列表作为一个整体追加
list_3.append('hello')
print(list_3)


# extend函数是将列表中每一个元素添加到另一个列表中
# 如添加"world"字符串,则将字符串生成列表['world'],然后连接到后面的list_3
list_3.extend(['world'])
print(list_3)

# insert函数是在指定的下标索引前面添加元素，如第三个元素前面添加LOVE

list_3.insert(2,'LOVE')
print(list_3)


# 列表相加，将两个list相加并生成一个新的list对象
list_4 = [1,2,3]
list_5 = list_3 + list_4
print(list_5)

# 删除
# 通过元素值删除

list_3.remove(False)
print(list_3)

# 通过下标索引删除元素

list_3.pop(-1)
print(list_3)

# del函数删除元素
# 通过下标索引删除
del list_3[1]
print(list_3)

# 通过区间范围删除
del list_3[0:2]
print(list_3)

# 删除整个列表
del list_3


































































































# 3.5 数据类型的转化


# 3.5.1 字符串和列表的转换
# 字符串转换成列表使用字符串函数split实现
# 列表转换成字符串使用join函数实现

# 字符串转换列表
str1 = 'Hello world'
list1 = str1.split(' ')
print(list1)

# 列表转换字符串
list1 = ['Hello', 'world']
str1 = ' '.join(list1)
print(str1)

# 其他转换函数
# 字符串转列表
str1 = '[1,2,"Hello"]'
# 字符串和列表数据格式相同，可以使用eval函数处理
list1 = eval(str1)
print(list1)

# list函数是将字符串每个元素作为列表的元素
list2 = list(str1)
print(list2)


# 列表转换字符串
# str函数直接将整个列表转换成字符串
list1 = ['Hello', 'world']
str1 = str(list1)
print(str1)

# 3.5.2 字符串与字典的转换

# 字符串转换字典使用dict函数实现，字典转换字符串使用values（）函数获取字典的值，然后将其转换成字符串。

# 字符串转换字典
str1 = 'Hello'
str2 = 'Python'
dict1 = dict(a=str1,b=str2)
#输出字符串转字典｛'a':'Hello','b':'Python｝
print(dict1)

# 字典转字符串
dict1 = {'a': 'Hello', 'b': 'Python'}
list1 = dict1.values()
str1 = ' '.join(list1)
#输出字典转字符串：Hello Python
print(str1)

#当字符串转换字典时，dict函数需要以key=value的形式作为函数参数，该参数表示字典里的一个键值对。
#当字典转换字符串时，由value函数获取字典的所有值，以列表的形式表示。再将列表转换成字符串，从而实现字典转换为字符串。

# 特殊字符转换字典
# 方法1：eval函数实现
str3 = '{"a":"Hello","b":"Python"}'
dict2 = eval(str3)
print('方法1：', dict2)

# 方法2：json模块的loads函数
# 局限性：如果字符串里的键值对是单引号表示，则该方法无法转换
# 如将str3改为  '{'a':'Hello','b':'Python'}'
import json
dict3 = json.loads(str3)
print('方法2：', dict3)

# 方法3：ast模块的literal_eval函数
import ast
dict4 = ast.literal_eval(str3)
print('方法3：', dict4)


# 3.5.3  列表与字典的转换

# 列表转换字典可以使用dict函数实现，但是列表的元素必须以一个列表或元组的形式表示，以列表或元组的形式表示字典的键值对。
# 字典转换成列表有三种方式：values()、keys()、items()

# 例
# 列表转换字典
list1 = ['a','Hello']
list2 = ['b','Python']
dict1 = dict([list1,list2])
print(dict1)

# 字典转换列表
dict1 = {'a': 'Hello', 'b': 'Python'}
# 获取字典所有值并生成列表
list1 = dict1.values()
print('values()函数:',list(list1))
# 获取字典的所有键并生成列表
list2 = dict1.keys()
print('key()函数:',list(list2))
# 获取字典所有键值并生成列表
list3 = dict1.items()
print('items()函数:',list(list3))








































































































































































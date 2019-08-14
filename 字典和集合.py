# 3.4 集合与字典

# 相同点：集合和字典在某个程度上非常相似，都以大括号来进行定义，并且元素是无序排列的
# 不同点：元素格式和数据类型有所不同，集合只支持数字、字符串和元组（Python中不可变得数据类型），字典支持全部数据类型

# 例：
# 集合：
set_1 = {'Hello','Python',123,(1,'love')}

# 字典：
dict_1 = {'name':'Python',3:4,'mylist':[1,2,3]}

# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：

# d = {key1 : value1, key2 : value2 }

# 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。




# 字典的增删改查

# 定义空的字典
dict1 = {}
# 添加元素
dict1['name'] = 'Python'

print('添加元素：', dict1)

# 修改元素的value
dict1['name'] = 'l love Python'
print('修改元素',dict1)

# 读取元素
# 以中括号的形式读取，不存在则提示错误
name = dict1['name']

print(name)

# 使用get方法读取
# 如果不存在则将字符串‘不存在这个元素’赋值到变量age
age = dict1.get('age','不存在这个元素')
print('读取元素值：',name)
print('读取age值：',age)


# 删除字典元素
del dict1['name']
print(dict1)

# 清空字典所有元素
dict1['name'] = 'Python'
dict1.clear()
print(dict1)

# 删除整个字典对象
del dict1


# 如果字典中嵌套了多个字典或列表，可以从字典外层逐步定位，定位方法由字典元素的key实现

# 例：
# 多重嵌套字典读取方式：
dict1 = {
    'a':'Hello',
    'b':{
        'c':'Python',
        'd':['world','china']
    }
}

# 读取键为c的值
# 由于键c在键b的值里面，因此先读取键b的值，再读取c的值
get_b = dict1['b']
get_c = get_b['c']

# 读取列表值China
# 由于列表是键d的值，因此先读取键b的值，再读取键d的值，最后读取列表的值
get_b = dict1['b']
get_d = get_b['d']
get_china = get_d[1]

# 其他函数与方法
#
# 内置函数
# 比较两个字典元素

cmp(dict1,dict2)


# 计算字典元素的总数。

len(dict)

# 将字典以字符串表示

str(dict)


# 内置方法
# 返回一个字典的浅拷贝
dict.copy()

# 创建一个新字典，将列表或元组的元素做字典的key，value是每个key的值
dict.fromkeys(list,value)

# 如果键在字典dict里，那么返回True，否则返回False
dict.has_key(key)

# 以列表的形式返回字典的键值对，每个键值对以元组表示
dict.items()

# 以列表返回字典所有键
dict.keys()

# 读取字典元素时，但如果键不存在于字典中，将会添加键并将值设为default
dict.setdefault(key,default=None)

# 把字典dect2的键值对更新到dict1里
dict1.update(dict2)

# 以列表返回字典中所有的值
dict.values()

# 4.1：if语句
# Python的条件控制由if语句执行，根据执行结果的True或False来执行相应的代码块。
# 定义：判断某个变量是否符合条件，符合就执行相应的代码块，不符合就执行另一个代码块。
# 例：
number = 1
if number == 1:
    print('Hello Python')
else:
    print('Hello World')

# 对变量多次判断
number = 1
if number == 1:
    print('Hello Python')
elif number == 2:
    print('Hello World')
elif number == 3:
    print('Hellp China')
elif number == 4:
    print('Hello Hello')
# 如果if语句中的代码块包含另一个if语句，称之为if嵌套
# 嵌套是编程语言中常见的代码结构，如：字典嵌套、列表嵌套、if嵌套、循环嵌套。
# if嵌套
number = 1
bool = True
if number == 1:
    # if嵌套
    if bool == True:
        print('Hello Python')
    else:
        print('I Love Python')
else:
    print('刚呆逼')

# 4.2：for循环

# 循环是程序中需要重复执行的代码，Python中循环结构有for循环和while循环。

# 定义：for循环是一种迭代循环机制，迭代即重复执行相同的逻辑操作。每次操作都是基于上一次结果而进行的。
# 范围：Python的for循环可以遍历任何序列的对象，如字符串、元组列表和字典等。
# 循环体是一个可迭代的对象，常用的迭代对象有字符串、列表、字典和rang对象
# 例：
sequence = [1234,566456]
iterating = []
for i in sequence:
    iterating.append(i)
    print(iterating)

# 循环字符串
str1 ='我正在学Python'
result = []
for i in str1:
    result.append(i)
    print(result)

# 循环列表
list1 = ['我','正','在','学','Python']
result = []
for i in list1:
    result.append(i)

# 循环字典
dict1 = {'key':'我','key1':'正','key2':'在','key3':'学','key4':'Python'}
result = []
for i in dict1:
    result.append(i)
    print(result)

# 循环rang对象，rang（10）会生成0-9的范围值
range1 = range(10)
result = []
for i in range1:
    result.append(i)
print(result)

# 第六章会详细讲述


# for循环中可嵌套for循环和if语句
# 实际开发中最常用的方式
# 示例:
# if语句嵌套
result1 = []
result2 = []
for i in range(10):
    if i % 2 == 0:
        result1.append(i)
    else:
        result2.append(i)
print('能被2整除的数有：',result1)
print('不能被2整除的数有：',result2)

#嵌套循环
for i in range(5):
    str1 = ''
    for j in range(3):
        # str1 += str(i) + ','
        str1 = str(i) + ',' + str1
    print('第',i+1,'行的数据是',str1)

# 4.3 while 循环
# 定义：while循环是根据条件判断结果决定是否循环
# 格式：
# while condition:
#     print(iterating)

bool = True
while bool == True:
    print('Hello Python')
    bool = False

# while循环也支持if语句嵌套和循环嵌套，具体与for循环相同

# 在循环过程中，想要终止整个循环或直接跳过当前循环的剩余语句而执行下一轮循环，可以使用break语句和continue语句。
# 这两个语句只能在循环内使用，如果在循环外使用，程序会提示错误信息。
# 例：
# for循环的break语句
# 当i=5时,终止整个循环
result = []
for i in range(10):
    if i == 5:
        break
    else:
        result.append(i)
print('for循环的break：',result)

# for循环的continue
# 当i=5时，跳出当前循环进入下一轮循环
result = []
for i in range(10):
    if i == 5:
        continue
    else:
        result.append(i)
print('for循环的continue：',result)

# while循环的break
result = []
i = 0
while i < 10:
    if i == 5:
        break
    result.append(i)
    i += 1
print('while循环的break：',result)

# while循环的continue
result = []
i = 0
while i < 10:
    if i ==5:
        i += 1
        continue
    result.append(i)
    i += 1
print('while循环的continue：',result)

# 运行结果
# for循环的break： [0, 1, 2, 3, 4]
# for循环的continue： [0, 1, 2, 3, 4, 6, 7, 8, 9]
# while循环的break： [0, 1, 2, 3, 4]
# while循环的continue： [0, 1, 2, 3, 4, 6, 7, 8, 9]

# 从运行结果看，for循环和while循环都分别循环10次当变量等于5时break语句会整个循环停止所以列表的元素值只有0到4
# continue语句将当前循环跳出，继续执行下一轮循环，所以元素值从0到9，不包含5。

# 4.4:推导式
# 推导式又称解析式，是Python一个独有的特性。
# 推导式是可以从一个数据序列构建另一个新的数据序列的结构体。数据序列使我们常说的可循环对象，如字符串、列表、字典、range对象等。
# 分类：推导式主要有列表推导式、集合推导式、和字典推导式，使用方法相似
# 例：
# 列表推导式
result = [x for x in range(5)]
print(result)

# 集合推导式
result = {x for x in range(5)}
print(result)

# 字典推导式
result = {x:x for x in range(5)}
print(result)

# 推导式的语法是相对固定的，通过循环数据序列中的每个元素，然后将每个元素重新组合成新的数据序列。
# 如果对当前元素做一个简单地判断，可以在循环后面加if语句
# 例：
# 列表推导式
result = [x for x in range(10) if x > 5]
print(result)

# 集合推导式
result = {x for x in range(10) if x > 5}
print(result)

# 字典推导式
result = {x:x for x in range(10) if x > 5}
print(result)
# 推导式中只能添加if判断，并且不允许设置多个条件判断，比如在推导式中设置elif和else等分支判断是不允许的

# 4.5 三目运算符
# Python的三元表达式，也可称为三木运算符，属于if语句的简化使用
# 例：
number = 10
result = 'Hello Python' if number >= 10 else 'Hello World'
print(result)

# 上述代码等价于
number = 10
if number >= 10:
    result = 'Hello Python'
else:
    result = 'Hello World'
print(result)
# 这样可以精简代码
# 循环嵌套和if嵌套
# 例：
# 三目运算符的if嵌套
number = 10
result = 'Python' if number < 5 else ('World' if number == 5 else 'China')
print(result)


# 三目运算符的循环嵌套
number = 10
result = [x for x in range(10)] if number > 10 else {x for x in range(10)}
print(result)
# 相比if语句、for循环和while循环，三目运算符还是存在一定的局限性，无法适应多变的需求开发













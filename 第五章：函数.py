

# 5.1:函数的定义
# 函数是指一段实现某些功能的代码块，也叫子程序或方法。
# 在一个程序中如果重复使用某一个功能，可以将该功能定义成一个函数，再次使用时只需直接调用该函数即可。
# 作用：减少代码冗余
# Python的函数以关键词def开头。关键词后时自定义的函数名，函数名后面添加英文格式的小括号，小括号里面可以根据情况来决定是否设置函数参数。
# 自定义的函数名，建议遵循驼峰命名法的命名规则，更容易在同行之间交流。
# 例：
# 函数名getName和get_name都是遵循驼峰命名法
# 函数getName设置参数name，并在函数代码中使用参数
# def get_name():
#     print('my name is Lili')
#
# def getName(name):
#     print('my name is ',name)

# 函数可以有参数也可以无参数。
# 如果函数带有参数，参数格式是可以任意的，如字符串、数字、元组、列表、或对象，均可作为函数参数。
# 格式：若一个函数含有多个参数，每个参数之间必须用英文逗号隔开
# 语法：
# def 函数名(参数1,参数2,参数3):
#     函数体
# 函数关键词def和函数体必须以缩进符进行划分，缩进在关键词def的代码都属于函数体。
# 有时候在函数执行某些处理时，如果想要得到函数的处理结果，可通过return将结果返回。
# return时Python的内置函数，在自定义函数中使用return函数可以将所需要的数据或对象返回到函数外的程序
#
# 一个完整的函数定义主要有：关键词def、函数名、小括号、函数参数、函数体、返回值。

# 5.2：函数参数

# 函数是将程序的某部分功能进行封装，因此函数与函数外的程序之间是紧密相连的，两者之间需要数据传递，通过函数参数和函数返回值来实现
# 函数参数是由函数外的数据传递到函数里，在函数里可以对函数参数进行读写操作
# 例：
# del myFunction(arg1,arg2,*args,**kargs):
#     函数体
#
# 在函数参数的定义语法中，分别定义了4个参数arg1、arg2、*args、**kargs，
# 说明：
# 1.arg1和arg2是开发者自定义的参数名，在函数里，参数名可以当成变量使用
# 2.*args是将多个参数生成一个列表。在函数里可以把args当成一个列表来使用里面的参数。
# 3.**kargs将多个参数以字典的形式表示。在函数里通过字典的读取方式获取kargs里的参数
#
# 按照参数的类型划分，主要分为三种类型：自定义参数arg1或arg2、*args和**kargs
# 使用方法：
def get_name1(arg1,arg2):
    print('1、我们的名字分别为：',arg1,arg2)

def get_name2(*args):
    print('*args的数据格式是：',args)
    print('2、我们的名字分别是：',args[0],args[1])

def get_name3(**kwargs):
    print('**kwargs的数据格式是：',kwargs)
    print('3、我们的名字分别是：',kwargs['name1'],kwargs['name2'])
# 调用函数
get_name1('Luck','Tom')
get_name2('Lily','Mary')
get_name3(name1='LiLei',name2='Tony')

# 此外，参数的三种使用方式可以灵活地组合使用，在函数调用时，需要注意参数的传入顺序和传入方式。
# 例：
# 参数arg1和arg2的灵活使用
def get_name1(arg1,arg2='Lucy'):
    print('arg1和arg2的名字分别是：',arg1,arg2)
# 三种调用方式
get_name1('Tom')
get_name1('Tom','Lucy')
get_name1(arg2='Tom',arg1='Lucy')


def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)
print_welcome("Fred")
w = 4
h = 5
area(w,h)
print("width =", w, " height =", h, " area =", area(w, h))

# 三种参数组合使用三种方式
# 例:
def get_name2(arg1,arg2,*args,**kwargs):
    print('arg1和arg2的名字分别是：',arg1,arg2)
    print('*args的名字分别是：',args[0],args[1])
    print('**kwargs的名字分别是：',kwargs['name'])
# 调用函数
get_name2('Lucy','Tom','Lily','Mary',name='Jack')
# 说明：
# 1.定义自定义参数时，除了定义参数名外还可以定义它的默认值，在调用函数时，如果没有对该参数传递数据，则返回参数值的默认值。
# 2.在函数外调用函数时，数据传递顺序可以自定义排序，传递过程中必须指定已定义的参数，get_name1(arg2='Tom',arg1='Lucy')。
# 3.三种函数参数组合使用时，参数定义顺序最好也按照上述例子。而且数据最好也依次传递，否则在定义和使用过程中都会提示错误信息。


# 5.3 函数的返回值

# 说明：函数与函数外的程序之间存在输入输出关系，将函数处理结果传递到函数外的程序，这个传递过程称之为函数的返回值
# 实现：由关键词return和yield实现
# 差异：return是在返回结果的同时中断函数的执行，yield则是返回结果并不中断函数的执行
# 理解：return比较容易理解，yield可以理解为‘轮转容器’，好比水车，首先yield可以装入数据、函数运行完毕后就会生成一个迭代器（generator object）
#       并将迭代器返回到主程序中，迭代器是Python的特性之一。
#       在主程序中，迭代器可以使用 next（）来读取里面的数据，函数中使用yield好比水车转动后，车轮上的水槽装入水，随着轮子转动，一个个水槽就会装入水。
#       在主程序中读取迭代器的数据好比一个个水槽把水送入水道中并流入田中。
# 例：
# 定义函数
def myReturn():
    for i in range(5):
        return i
# 定义函数
def myYield():
    for i in range(5):
        yield i
# 调用函数myReturn
result1 = myReturn()
print('return数据类型是：',type(result1))
print('这是return的数据：',result1)

# 调用函数yield
result2 = myYield()
print('yield数据类型是：',type(result2))
for i in result2:
    print('这是yield里面的数据：',i)
# 运行结果：
# return数据类型是： <class 'int'>
# # return数据类型是： 0
# # yield数据类型是： <class 'generator'>
# # 这是yield里面的数据： 0
# # 这是yield里面的数据： 1
# # 这是yield里面的数据： 2
# # 这是yield里面的数据： 3
# # 这是yield里面的数据： 4

# 从返回结果来看 result1和 result2， result1是一个数字类型的数据，数值为0，函数 myReturn在第一次循环时，关键词 return
# 将第一次循环的值返回到主程序，函数本身不在执行任何操作。
# result2是一个 generator对象，这代表一个迭代器，通过for循环将迭代器里面的数据输出，数值从0到4,恰好是yield每次循环的数值

# 5.4：函数的调用
# 说明：函数的调用是指可以在函数里面调用其他函数，也可以在主程序里面调用函数。
# 调用方式：使用‘函数名+括号’，程序首先找到括号，认定当前语句代表函数调用，然后根据函数名去查找相应的函数并执行。
# 例：
def fun1():
    print('hi 我是fun1!')
def fun2(name):
    print('hi 我是fun2！，我的名字叫：',name,',我现在要呼喊fun2')
    # 调用函数fun1
    fun1()
def fun3(name):
    print('hi 我是fun3，我的名字叫：',name,',我现在要呼喊fun3')
    # 调用函数fun2
    fun2('Lily')
# 主程序
if __name__=='__main__':
    fun3('Lucy')

# 说明：代码if __name__=='__main__'下的代码是当前文件的主程序代码。当程序运行的时候，主程序首先调用并执行函数，fun3，
# 在fun3里面，它调用了fun2，而fun2调用了fun1，这样形成一个嵌套的函数调用。
# 执行结果：
# hi 我是fun3，我的名字叫： Lucy ,我现在要呼喊fun3
# hi 我是fun2！，我的名字叫： Lily ,我现在要呼喊fun2
# hi 我是fun1!

# 5.5 变量的作用域

# 变量的作用域分为全局变量和局部变量
# 在主程序中定义的变量是全局变量。在函数中定义的变量为局部变量
# 全局变量在所有作用域都可读，局部变量只能在本函数里可读，函数读取变量时，优先读取局部变量，然后再去读取全局变量。
# 函数里可以对变量使用关键词 global,使变量定义成全局变量。
# 例1：
def fun1():
    name = 'Lucy'
    print('hi 我是函数fun1，我的名字叫：',name)
if __name__== '__main__':
    name = 'Lily'
    fun1()
    print('hi 我是主程序，我的名字叫：',name)

# 例2：

# 函数fun1
def fun1():
    # 定义局部变量name
    funName = 'Lucy'
    # 定义全局变量
    global newName
    newName = 'Mary'
    print('hi 我是局部变量，我的名字叫：',funName)
    print('hi 我是全局变量，我在函数fun1里面，我的名字是：',name)
    print('hi 我是全局变量，由函数fun1定义，在函数里使用，我的名字叫：',newName)
# 主程序
if __name__=='__main__':
    # 定义全局变量name
    name = 'Lily'
    fun1()
    print('hi 我是主程序，我在主程序里面，我的名字叫：',name)
    print('hi 我是全局变量，由函数fun1定义，在主程序里面使用，我的名字叫：',newName)
# 说明：
# 上述代码中，函数fun1分别定义了局部变量funname和全局变量newName，主程序定义全局变量name，从代码输出结果看，
# 全局变量name和newName不限制使用范围，而局部变量funname只能在函数里使用
# 运行结果：
'''hi 我是局部变量，我的名字叫： Lucy
hi 我是全局变量，我在函数fun1里面，我的名字是： Lily
hi 我是全局变量，由函数fun1定义，在函数里使用，我的名字叫： Mary
hi 我是主程序，我在主程序里面，我的名字叫： Lily
hi 我是全局变量，由函数fun1定义，在主程序里面使用，我的名字叫： Mary'''





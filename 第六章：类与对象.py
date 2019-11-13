# 6.1类的使用
# 内容：Python的类与对象，类的定义、类的封装与继承
# 类是对象的一个具体描述，对象的属性和方法都是由类进行定义和设置的。
# 类主要分为属性和方法，属性就好比人的姓名、性别和学历等，方法就如同人的四肢和器官，可以实现某些简单操作

# 完整定义语法如下
class Person(object):
    # 定义静态属性
    name = '小刚'

    # 定义动态属性
    def __init__(self):
        """__init__是类的初始方法"""
        self.age = '38'

    # 定义普通方法
    def foot(self):
        """至少有一个self参数"""
        print('这是刚赛的脚，由普通方法实现')

    # 定义类的方法，由classmethod装饰器实现
    @classmethod
    def class_hand(cls):
        """至少有一个cls参数"""
        print('这是刚赛的爪子，由类的方法实现')

    # 定义静态方法，由staticmethod装饰器实现
    @staticmethod
    def static_mouth():
        """默认无参数"""
        print('这是刚赛的嘴，由静态方法实现')


if __name__ == '__main__':
    # 获取静态属性
    # 方法1，直接调用
    print('静态属性：', Person.name)
    # 方法2，实例化后再调用
    Person = Person()
    print('静态属性：', Person.name)

    # 获取动态属性
    Person = Person()
    print('动态属性：', Person.age)

    # 调用普通方法
    Person = Person()
    Person.foot()

    # 调用类方法
    # 方法1，直接调用
    Person.class_hand()
    # 方法2，实例化后调用
    Person = Person()
    Person.class_hand()

    # 调用静态方法
    # 方法1，直接调用
    Person.static_mouth()
    # 方法2，实例化后调用
    Person = Person()
    Person.static_mouth()


# 类的定义由关键词class实现，关键词后为类名，这个可以自定义命名，类名后是一个小括号和object类，这是Python的新式类。
# Python的类分为新式类和经典类。经典类在日常开发中不建议使用，现在都使用新式类进行定义。关于新式类和经典类这边不做详细讲述。可自行研究。
# 在上述类的定义语法中，preson类定义了类的属性和方法。
# 类的属性：类又分为静态属性和动态属性。
# 区别：最大的区别是使用方式不同，
# 类的方法也分为普通方法、类方法和静态方法。
# 区别：普通方法只能实例化后使用，后两者具备两种使用方法。
# 实例化是指在面向对象的编程中，把用类创建对象的过程称为实例化。是将一个抽象的概念类，具体到该类实物的过程。实例化过程中一般由类名 对象名 = new 类名（参数1，参数2...参数n）构成。
# 示例代码逐段运行否则报错：    Person = Person()      TypeError: 'Person' object is not callable        意思是变量名或函数名重复，这里调用使用了同一个类名Person
# 类的定义使用了关键词self，这个关键字代表类本身。这也说明带有self的变量或方法是当前类所定义的动态属性或方法。

# 在定义类的时候，类会自动生成许多内置方法，如代码中的__init__初始化方法，类在实例化的时候，首先自动执行__init__初始化方法，上述代码的Person类是自定义类的初始化方法，
# 如果自定义类的时候没有特殊要求，可以不用重写初始化方法，如果在初始化方法里面设置参数，在调用类的时候，类的实例化也应该设置相应的参数
# 例：
class Person(object):
    def __init__(self, name):
        """重写__init__并设置实例化参数name"""
        self.name = name


if __name__ == '__main__':
    # Person类在实例化时必须设置参数name的值
    Person = Person('小刚')
    print(Person.name)


# 注：if __name__ == '__main__':的作用
# 一个python文件通常有两种使用方法，第一是作为脚本直接执行，第二是 import 到其他的 python 脚本中被调用（模块重用）执行。
# 因此 if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
# 在 if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，
# 而 import 到其他脚本中是不会被执行的
# 详细参照：https://blog.csdn.net/heqiang525/article/details/89879056

# 上述代码演示了__init__初始化方法的使用，在实际开发中根据功能的实现方式决定。
# 以下为常用的内置方法：
# 类的内置方法                                   说明
# __init__(self,...)                              初始化方法，在类实例化得时候被执行调用
# __del__(self)                                   释放类的对象，在对象被删除之前执行
# __new__(cls,*args,**kwd)                        在实例化生成对象时执行，先执行该方法再执行初始化方法
# __getitem__(self,key)                           获取索引key对应的值，等价于seq[key]
# __stt__(self)                                   在使用print时被调用
# __len__(self)                                   在调用内联函数len()时被调用，计算数值长度
# __cmp__(stc,dst)                                两个类stc和dst的比较
# __getattr__(s,name)                             获取name属性的值
# __setattr__(s,name,velue)                       设置name属性的值
# __delattr__(s,name)                             删除name属性
# __getattrvute__()                               __getattrvute__()功能和__getattr__()类似
# __gt__(self,other)                              判断类本身是否大于other类
# __lt__(self,other)                              判断类本身是否小于other类
# __ge__(self,other)                              判断类本身是否大于或等于other类
# __le__(self,other)                              判断类本身是否小于或等于other类
# __eq__(self,other)                              判断类本身是否等于other类
# __call__(self,*args)                            把类实例作为函数调用
# 注：在调用类的属性和方法之前,建议将类实例化后使用,类的实例化也称为对象,类在实例化后,
# 可以直接调用类的属性和方法来实现某些功能或操作,这就是面向对象开发的编程思想.


# 6.2类的封装

# 说明：封装在日常生活都能看到和接触到，比如在使用支付宝进行付款的时候，
# 只需要把二维码给收款方或扫一下收款方的二维码就可以完成支付。无需知道程序如何解析二维码以及资金的交易流向，
# 整个支付功能就可以理解为经过封装处理。
# 封装是将程序中的某些功能的执行过程写到函数或类里面。当程序调用函数或类的时候即可实现程序的功能。

# Python类可以分成两层封装，类在实例化时所生成的对象看做一个已经封装好的对象，调用对象的属性和方法来实现某些功能，
# 这是类的第一层封装
# 有时候需要把类里面的某些属性和方法封装起来，将其设置为类的私有属性或方法，使得这些属性和方法只能在类的内部使用，
# 无法在类的外部调用，这是类的第二层封装

# 第一层封装在6.1已经有所了解
# 类的第二层封装主要是将类的属性或方法设置为私有，只允许在类内部使用。
# 定义私有属性或方法只需要在属性名和方法名之前加双下划线即可

# 例：
class Person(object):
    # 定义私有属性name和公有属性age
    def __init__(self, name):
        self.__name = name
        self.age = 10

    # 定义私有方法
    def __get_age(self):
        """在方法名前面加双下划线"""
        return self.age

    # 定义普通方法
    def get_name(self):
        return self.__name


if __name__ == '__main__':
    p = Person('Ganggang')
    # 读取公有属性和普通方法
    print('公有属性age的属性值：', p.age)
    print('公有方法get_name的返回值：', p.get_name())
    # 强制读取私有属性和调用私有方法
    print('强制读取私有属性，属性值：', p._Person__name)
    print('强制调用私有方法，返回值：', p._Person__get_age())


# 上述代码分别定义私有属性__name、公有属性agr、私有方法__get_age和普通方法get_name。
# 在主程序中，将类实例化生成对象p，然后对象p只能获取公有属性age的属性值和调用公有方法get_name。
# 如果对象p调用私有属性__name和私有方法__get_age程序会提示：AttributeError: 'Person' object has no attribute '__name'等报错
# 但是这并不代表无法在类的外部读取类的私有属性和调用私有方法，可以使用强制性的方式来获取私有属性值和调用私有方法如：
# p._Person__name和 p._Person__get_age()


# 代码运行结果如下：
# 公有属性age的属性值： 10
# 公有方法get_name的返回值： Ganggang
# 强制读取私有属性，属性值： Ganggang
# 强制调用私有方法，返回值： 10

# 6.3类的继承
# 继承常用与父母与子女之间，比如子女外貌长得像父母，因为子女的基因来自父母，编程语言也是如此。
# 如在定义Student类的时候，可以使Student类继承Person类，使得子类Student拥有父类Person的所有属性和方法。
# 而且子类Student可以重写父类的属性和方法或自定义新的属性和方法。

# 例：

# 定义父类Person
class Person(object):
    # 定义私有属性name和公有属性age
    def __init__(self, name):
        self.__name = name
        self.age = 10

    # 定义私有方法
    def __get_age(self):
        """在方法名前面加双下划线"""
        return self.age

    # 定义普通方法
    def get_name(self):
        return self.__name


# 定义子类
class Student(Person):
    # 自定义普通方法
    def studdent_name(self):
        # 继承Person，通过强制操作方法获取父类的私有属性
        return self._Person__name


if __name__ == '__main__':
    s = Student('Laogang')
    # 调用父类的普通方法get_name
    print('调用父类普通方法', s.get_name())
    # 调用父类的私有方法
    print('调用父类私有方法', s._Person__get_age())
    # 调用自定义对的普通方法
    print('调用自定义的普通方法', s.studdent_name())

# 从子类Student的定义看，类名Student后面小括号里面Person是指向父类Person，这是将Student类继承Person类
# 如果Student类需要继承多个类，可以在小括号里面填写，每个类之间使用英文格式的逗号隔开。
# 主程序中子类首先实例化生成对象s，在实例化时需要设置参数，因为子类继承类父类的初始化方法__init__。
# 对象s可以调用Student所有属性和方法，对于父类的私有属性和私有方法，可以通过强制性操作实现
# 运行结果如下：

# 调用父类普通方法 Laogang
# 调用父类私有方法 10
# 调用自定义的普通方法 Laogang

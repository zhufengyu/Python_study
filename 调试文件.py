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

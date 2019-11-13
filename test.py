

class Person(object):
    # 定义私有属性name和公有属性age
    def __init__(self,name):
        self.__name = name
        self.age = 10
    # 定义私有方法
    def __get_age(self):
        """在方法名前面加双下划线"""
        return self.age
    # 定义普通方法
    def get_name(self):
        return self.get_name()
if __name__ == '__main__':
    p = Person('Ganggang')
    # 读取公有属性和普通方法
    print('公有属性age的属性值：',p.age)
    print('公有方法get_name的返回值：',p.get_name())
    # 强制读取私有属性和调用私有方法
    print('强制读取私有属性，属性值：',p._Person__name)
    print('强制调用私有方法，返回值：',p._Person__get_age())

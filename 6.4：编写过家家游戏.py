
# 一个家庭有三个成员：父亲，母亲，儿子。每个人有自己的姓名年龄和自己的小秘密。
# 一个家庭有三个成员，每个成员都有自己的特性但是又隶属于这个家庭
# 那么可以把家庭作为一个父类，父类的属性是家庭成员的共有特性，每个成员为一个子类，子类具有父类的属性之外，还有自己的特有属性。
# 代码如下
import random
class Family():
    # 自定义初始化方法
    def __init__(self,surname,address,income):
        """设置家庭姓氏"""
        self.surname = surname
        self.address = address
        self.income = income
class Father(Family):
    def __init__(self,name,age):
        """继承父类的动态属性"""
        super(Family,self).__init__()
        # 定义动态属性
        self.name = name
        self.age = age
        self.__secret = '我外面有人'
    def action(self):
        money = random.randint(100, 1000)
        return money
class Mother(Family):
    def __init__(self,name,age):
        """继承父类的动态属性"""
        super(Family,self).__init__()
        # 定义动态属性
        self.name = name
        self.age = age
        self.__secret = '我有很多私房钱'
    def action(self):
        money = random.randint(100, 500)
        return -money
class Son(Family):
    def __init__(self,name,age):
        """继承父类的动态属性"""
        super(Family,self).__init__()
        # 定义动态属性
        self.name = name
        self.age = age
        self.__secret = '刚赛喜欢隔壁的小花'
    def action(self):
        money = random.randint(0, 100)
        return -money
if __name__ == '__main__':
    # 将四个类实例化生成对象
    family = Family('刚','宿迁市宿豫区大兴镇',1000)
    father = Father('老板','60')
    mother = Mother('总','55')
    son = Son('赛','30')
    # 家庭自我介绍
    print('这是一个姓' + family.surname + '的家庭，他们生活在' + family.address)
    print('我是父亲' + family.surname + father.name + '，今年' + str(father.age) + '岁')
    print('我是母亲' + family.surname + mother.name + '，今年' + str(mother.age) + '岁')
    print('我是儿子' + family.surname + son.name + '，今年' + str(son.age) + '岁')
    # 家庭费用开支
    father_money = father.action()
    family.income += father_money
    print(family.surname + father.name + '今天赚了' + str(father_money) + '元，家庭剩余资产：' + str(family.income) + '元')
    mother_money = mother.action()
    family.income += mother_money
    print(family.surname + mother.name + '今天花了' + str(-mother_money) + '元，家庭剩余资产：' + str(family.income) + '元')
    son_money = son.action()
    family.income += son_money
    print(family.surname + son.name + '今天花了' + str(-son_money) + '元，家庭剩余资产：' + str(family.income) + '元')
    # 家庭成员小秘密
    print(family.surname + father.name + '告诉我一个小秘密' + father._Father__secret)
    print(family.surname + mother.name + '告诉我一个小秘密' + mother._Mother__secret)
    print(family.surname + son.name + '告诉我一个小秘密' + son._Son__secret)


# 说明：
#        1.上述代码一个定义了四个类,父类Family,子类分别是:Father、Mother、Son。
#        2.代码中调用了标准库random，用于随机生成数字，作为家庭收支情况。
#        3.Family类：用于描述家庭基本情况，姓氏、住址、资产。初始化方法里分别设置动态属性surname、address、income，代表姓氏、住址、资产。
#        4.Father、Mother、Son类：用于描述每个家庭成员。在重写初始化方法的时候，使用了super(Family,self).__init__()，可以把父类的初始化方法所定义的动态属性一并继承到子类的初始化方法。
#        如果不使用此方法，子类重写初始化方法会覆盖父类的初始化方法。若想要子类也继承父类的属性，要么在子类重写初始化方法时重定义父类的属性，要么使用super函数继承。

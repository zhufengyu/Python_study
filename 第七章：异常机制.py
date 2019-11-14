# Python的异常机制

# 7.1 了解异常

# 异常机制定义：异常机制是指程序运行过程中出现错误而进行处理操作。
# 异常机制作用：一般情况下，程序在运行中出现错误会停止运行并发送错误信息，如果在程序中加入异常机制，
#             当程序运行中出现错误时，它会捕捉错误信息并执行相应的处理，这样保证程序继续运行。

# 异常的定义：异常是程序在执行过程中出现问题而导致程序无法执行。
# 例：程序的逻辑或算法错误、计算机的资源不足或IO错误等
# 注：不管是哪一种异常，只要程序运行中出现错误都可以认为是异常，并且抛出异常信息。我们可以感觉异常信息了解异常的具体信息

# 举例说明：
# "C:\Program Files\Python37\python.exe" F:/Python_study/调试文件.py
#   File "F:/Python_study/调试文件.py", line 23
#     s = studen('lucy')
#     ^
# NameError: name 'student' is not defined

# 从异常信息看，Traceback是异常跟踪信息，从File "F:/Python_study/调试文件.py", line 23看，在调试文件.py文件里的第23行出现错误
# s = studen('lucy')是程序错误的具体位置，最后一行是这个异常的错误类型和说明错误原因的提示信息。
# NameError是错误类型，name 'student' is not defined是错误原因，这个错误原因是指代码中的student没有定义

# Python的异常是由类定义的，所有的异常都来自于BaseException类。不同类型的异常都继承自父类BaseException。

# 异常类的结构如下：

#                                        BaseException（所有异常的基类）
#
# Keyboardinterrupt(键盘中断)   Exception（异常：NameError、ValueError、IOError、ImportError等）  SystemExit（Python解释器退出）

# 解释：BaseException的子类有Keyboardinterrupt、Exception和SystemExit。而所有异常都是由子类Exception定义和描述。

# 常见异常如下

# Python的异常类表

# 异常类                   说明
# AttributeError          访问一个对象没有的属性，比如foo.x ，但是foo没有属性x
# IOError                 输入输出异常，如无法打开文件
# ImportError             无法引入模块或包，通常是路径问题或名称错误
# IndentationError        语法错误，代码没有正确对齐
# IndexError              下标索引超出序列边界
# KeyError                访问字典里不存在的键
# KeyboardInterrupt       用户中断执行
# NameError               访问一个没有申明的变量或对象
# SyntaxError             语法错误，代码出现错误
# TypeError               传入对象类型与定义的不符合
# UnboundLocalError       访问一个还未被设置的局部变量
# ValueError              传入无效的参数或数值
# UnicodeError            编码的相关错误
# TabError                Tab和空格混用
# MemoryError             计算机内存溢出错误
# OverflowError           数值运算超出最大限制


# 7.2  捕捉异常
# 对异常信息有了一定了解后，使用异常机制对这些异常进行捕捉并处理
# Python的异常机制语法如下

try:
# 程序运行的代码
except NameError as err:
    # 只捕捉NameError的错误类型
    print('出错了，错误信息是：', err)
except Exception as err:
    # 捕捉全部的错误类型
    print('出错了，错误信息是：', err)
except:
    # 捕捉全部的错误类型，但是没有错误信息
    print('出错了')
else:
    print('如果无异常就执行此处代码')
finally:
    print('不管是否异常都执行此处代码')

# 完整的异常机制语法由4个关键词组成：try、except、else和finally。每个关键词有不同用处。
# 其中try和except是必不可少的，else和finally可以根据实际需求来决定是否添加。
# 四个关键词说明如下：
# try：用于检测程序代码是否出现异常，检测的代码可以是程序的全部代码或程序的部分代码
# except：用于捕捉异常信息并对异常进行处理，若关键词后面设置异常类型，在捕捉过程中根据异常类型而选择相应的except
# else：如果关键词try里面没有出现异常，程序会执行关键词里面的代码
# finally：不管关键词try是否出现异常，当关键词try、except或else的代码执行完了后，最终会自动执行此关键词里面的代码

# 例：

if __name__ == '__main__':
    try:
        s = Student('Laogang')
        pass
    except NameError as err:
        print('这是NameError错误，错误信息是：', err)
    except Exception as err:
        print('这是Exception错误，错误信息是：', err)
    else:
        print('如果没有异常执行此处代码')
    finally:
        print('不管有没有异常都会执行此处代码')

# 运行结果如下：
# "C:\Program Files\Python37\python.exe" F:/Python_study/调试文件.py
# 这是NameError错误，错误信息是： name 'Student' is not defined
# 不管有没有异常都会执行此处代码

# 由于Student是未定义的变量或对象，因此程序在执行过程中会出现NameError异常，异常信息会被except NameError as err所捕捉，并执行相应处理。
# 最后程序还会执行finally里面的代码。
# 如果设置多个关键词except，当异常出现的时候，异常捕捉从上到下执行，只要符合其中一个条件，程序就会执行该except里面的代码。

# 注：一个异常机制可以支持多个异常机制嵌套，但是嵌套过多会使代码结构变得相当复杂，不利于维护和阅读。
# 例：
if __name__ == '__main__':
    try:
        s = Student('Laogang')
    except Exception as err:
        try:
            print('这是第一个错误，错误信息是：', err)
            s = Student('Laogang')
        except Exception as err:
            print('这是第二个错误，错误信息是：', err)

# 7.3 自定义异常
# 异常一般是由程序运行过程中遇到错误的时候而生成的，但有时候我们也需要自己抛出一些异常信息，让程序去捕捉和处理
# 自定义异常抛出除了监测错误之外，还可以用于代码的布局设计和程序的逻辑控制，通过抛出异常可以执行不同的代码块。

# 格式：自定义异常抛出由关键词raise实现，关键词后面填写异常类型和异常信息。如下代码所示：

if __name__ == '__main__':
    try:
        raise NameError('自定义异常抛出')
    except Exception as err:
        print('这是Exception错误')


# 说明：上述示例主动抛出NameError异常，NameError是已经定义好的异常类。
# 如果在自定义异常抛出或异常捕捉的时候不想使用Python内置的异常类，可以自定义一个异常类。只要自定义的异常类继承Exception类即可。
# 例：
class MyError(Exception):
    pass


if __name__ == '__main__':
    try:
        # 抛出自定义异常
        raise MyError('自定义异常抛出')
    # 捕捉自定义异常类
    except Exception as err:
        print('这是MyError错误，错误信息是：', err)

# 说明：在自定义异常MyError中，代码中的pass是一个空语句，这是为了保持程序结构的完整性。它不会做任何事情，只用于占位。



# 4.6：猜数字游戏


# 导入标准库random
import random
number = random.randint(0,100)
while 1:
    # 内置input函数用于给用户提供数值输入
    # 由于input函数是生成字符串，所以要把字符串转换成数字
    getNum = int(input('请输入你的数字：'))
    if getNum == number:
        # 判断成功就终止整个while循环
        print('恭喜你猜对了！')
        break
    elif getNum > number:
        print('你的数字比结果大了！')
    else:
        print('你的数字比结果小了！')























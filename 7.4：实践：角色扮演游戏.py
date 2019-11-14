'''
狼人杀是目前比较流行的桌面游戏，主要由狼人、特殊村民和普通村民组成。狼人目标是杀掉所有村民，村民目标是找出狼人。
根据游戏本质我们调整游戏的规则，游戏设计说明如下：
1.自定义两个异常类，以控制角色猜测错误次数和判断胜利条件
2.定义玩家与角色，并将两者随机匹配，使得每次游戏的玩家角色不会重复。
3.每个玩家只能对其身份进行两次猜测，总错误次数不能超过五次，否则游戏结束。
4.如果每个玩家的身份都猜对则游戏胜利。

根据规则，代码如下
'''

import random

'''自定义异常类'''


class MuchError(Exception):
    pass


class Victory(Exception):
    pass


'''定义玩家与角色'''
player = ['小刚', '老刚', '大刚', '刚老铁']
role = ['女巫', '猎人', '狼人', '村民', '守卫', '长老', '预言家', '白狼王']

'''将玩家与角色的顺序打乱并重新匹配'''
player = random.sample(player, len(player))
role = random.sample(role, len(player))
# print('游戏中的身份有：' + '、'.join(role))
matching = {}
for t in range(len(player)):
    matching[player[t]] = role[t]
'''游戏逻辑'''
try:
    result, err = 0, 0
    for t in player:
        for i in range(2):
            guess = input('你认为' + t + '的身份是：')
            if guess == matching[t]:
                result += 1
                print('你猜对了！')
                break
            else:
                err += 1
                print('猜错了，你还有' + str(1 - i) + '次机会')
        if err > 5:
            raise MuchError('错误次数超过5次，游戏结束')
    try:
        if result == len(player):
            raise Victory('恭喜你全部猜对了')
    except Victory as errInfo:
        print(errInfo)


except MuchError as errInfo:
    print(errInfo)

'''游戏一共三个部分：自定义异常类、玩家与角色设定与匹配和游戏逻辑。其中游戏逻辑是整个游戏的核心代码，
它是在一个try····except机制里面完成的。具体说明如下：
1.首先将每位玩家进行循环遍历，保证每个玩家都可以进行身份猜测。
2.然后对每个玩家再循环两次，代表每位玩家的身份有两次猜测机会，每循环一次都会执行if···else判断，判断猜测是否正确。
3.最后分别判断错误次数err和正确次数result。如果错误次数大于5抛出异常MuchError，直接终止try里面的for循环，
并控制程序执行。如果正确次数等于4，也就是所有玩家身份都确认了，抛出自定义异常Victory'''

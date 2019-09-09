import time
# 每组队伍的游戏过程
def guess(i):
    correct = 0
    start = time.time()
    for k in range(len(i)):
        # 显示词语
        print(('%d,%s')%(k + 1,i[k]))
        flag = input('请答题，对请输入y，跳过请输入任意键')
        sec = time.time() - start
        # 统计用时
        if (50 <= sec <= 60):
            print('还有10秒钟')
        if (sec >= 60):
            print('时间到！游戏结束！')
            break
        # 答对就累加1
        if (flag == 'y'):
            correct +=1
            continue
        else:
            continue
    return correct
    # 遍历每组队伍，调用ansewr函数实现游戏
def team(guessWord):
    for i in guessWord:
        correct = guess(i)
        str_temp = ('恭喜你答对了%d道题') % (correct)
        print(str_temp)
        print('##########下一组###########')
# 主程序定义游戏内容，然后调用team函数开始游戏
if __name__== '__main__':
    guessWord = []
    guessWord.append(['娇妹','金鸡独立','狼吞虎咽','鹤立鸡群','手舞足蹈','卓别林','穿越火线'])
    guessWord.append(['扭秧歌','偷看美女','大摇大摆','回眸一笑','市场营销','自恋','处女座'])
    guessWord.append(['狗急跳墙]','捧腹大笑','目不转睛','愁眉苦脸','暗恋','臭袜子','趁火打劫'])
    team(guessWord)

# 函数guess说明：
# 定义函数team和guess分别代表队伍和游戏
# 1.函数guess是整段代码中最底层的函数，也是实现猜词语的游戏功能
# 2.函数参数i代表当前队伍的词语题目，函数变量correct和start代表答对的题目数和开始时间
# 3.函数里面的循环是将词语的题目遍历输出，每条题目通过比划者输入的内容来判断当前题目是答对或跳过
# 4.在遍历的过程中加入时间的计算和判断，超时自动中断循环
# 5.答对了题目，函数变量correct加1，否则进行下一个循环

# 函数team说明：
# 1.函数team是通过循环词组 guessWord ， guessWord是该函数参数并且是一个长度为三的二维列表，，也就是说列表有三个元素，每个元素是一个列表。
# 2.每次循环 guessWord得到它的元素值，然后调用guess函数并将元素值作为函数参数。
# 3.最后获取guess函数的返回值，返回值代表当前队伍答对题目数量


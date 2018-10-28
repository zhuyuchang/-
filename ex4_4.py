import random
n=0
s1=random.randint(0,100)
while True:
    n=n+1
    s2=eval(input('请输入0-100之间的整数:'))
    if s2<s1:
       print('很遗憾,小了')
    elif s2>s1:
       print("很遗憾,大了")
    else:
        print("预测{}次,你猜对啦!")
    break

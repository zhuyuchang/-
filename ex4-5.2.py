import random
s1=random.randint(0,100)
count=0;
while True:
   try:
      s2=eval(input('请输入0-100之间的整数:'))
   except:
      print("输入必须为整数!")
      continue

count += 1
if s2<s1:
    print('很遗憾,小了')
elif n==p:
    print('预测{}次,你猜中啦!'.format(count))
else:
    print("很遗憾,大了")
    

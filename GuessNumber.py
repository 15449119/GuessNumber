import random
rint=random.randint(1,100)
count=0
while True:
    guess=int(input("-----请输入您猜的数字:------  \n" ))
    if guess>rint:
        print('高了')
        count+=1
        continue
    elif guess<rint:
        print('低了')
        count+=1
        continue
    elif guess==rint:
        print('恭喜你，猜对了！')
        count+=1
        break
if  count<=5:
    print("真是太棒了！！！只猜了 %d 次就猜对了！" % count)
elif count>5 and count<=10:
    print("不错不错！猜了 %d 次~" % count)
elif count>10 and count<=20:
    print("终于猜对了，猜了 %d 次！" % count)
elif count>20:
    print("肩上的单子还很重啊，同志！猜了 %d 次才猜对" % count)
print('欢迎使用猜数游戏，下次见~~')

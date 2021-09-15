import random
secret = random.randint(0,10)
i = 500
print("您的账户余额为：",i)
o = 0
while o < 3:
    number = int(input("请输入您想要输入的数字："))
    if number > secret:
        i = i-100
        print("您猜大了,您共有三次机会，此次是第",o+1,"次，剩余金币：",i)
    elif number < secret:
        i = i-100
        print("您猜小了,您共有三次机会，此次是第",o+1,"次，剩余金币：",i)
    else:
        print("恭喜您猜中了，本次数字为：",secret,"奖励金额",500)
        print("您当前账户余额为：",i+500)
        break
    o = o+1

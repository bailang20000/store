# 导入随机数包
import random
# 导入py工具类
from 数据库工具 import *
# 定义初始化界面
def initial_interface():
    print("==============================================")
    print("|------------中国工商银行账户管理系统------------|")
    print("|------------1、开户              ------------|")
    print("|------------2、取钱              ------------|")
    print("|------------3、存钱              ------------|")
    print("|------------4、转账              ------------|")
    print("|------------5、查询              ------------|")
    print("|------------6、退出              ------------|")
    print("==============================================")

# 字典库
# bank_name = "中国北京老牛湾迪迦分行"
# bank = {}
#
# def bank_kaihu(yonghuming,mima,guojia,shengfen,jiedao,menpaihao,zhanghu):
#     bank[yonghuming] = {
#         "mima":mima,
#         "guojia":guojia,
#         "shengfen":shengfen,
#         "jiedao":jiedao,
#         "menpaihao":menpaihao,
#         "zhanghu":zhanghu,
#         "bank_name":bank_name,
#         "money":0
#     }
#     return 1

def kaihu():
    user_name = input("请输入您的用户名")
    password = int(input("请输入您的密码"))
    print("下面请输入您的地址")
    country = input("\t\t请输入您所在的国家")
    provinces = input("\t\t请输入您的省份")
    streets = input("\t\t请输入您的街道")
    house_number = input("\t\t请输入您的门牌号")
    account_number = random.randint(10000000,99999999)
    money = 0
    bank_name = "中国建设银行北京分行"
    # 对用户数量进行计数
    sql1 = "select count(*) from t_user"
    h1 = []
    numbers = enquirt(sql1,h1)
    # 对用户数量进行指定查询
    sql2 = "select * from t_user where userame = %s"
    h2 = [user_name]
    numbers1 = enquirt(sql2,h2)
    if numbers[0][0] > 100:
        print("用户已满")
        return 3
    elif len(numbers1) != 0:
        print("用户名已存在")
        return 2
    else:
        sql2 = "insert into t_user values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
        h2 = [account_number,user_name,password,country,provinces,streets,house_number,money,bank_name]
        users(sql2,h2)
        print("恭喜您开户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
        '''
        print(info % (user_name,account_number,country,provinces,streets,house_number,money,bank_name))
        return 1
    # status = bank_kaihu(yonghuming,mima,guojia,shengfen,jiedao,menpaihao,zhanghu)
    # if status == 1:
    #     print("恭喜您开户成功，以下是您的信息")
    #     info = '''
    #                 ------------个人信息------------
    #                 用户名:%s
    #                 账号：%s
    #                 密码：*****
    #                 国籍：%s
    #                 省份：%s
    #                 街道：%s
    #                 门牌号：%s
    #                 余额：%s
    #                 开户行名称：%s
    #     '''
    #     print(info % (yonghuming,mima,guojia,shengfen,jiedao,menpaihao,bank[yonghuming]["money"],bank_name))


# 定义取钱方法 （账户，密码，账户余额）
def quqian(t1, t2, t3):
    # 定义查询输入的账号
    sql1 = "select * from t_user where account=%s"
    h1 = [t1]
    numbers = enquirt(sql1, h1)
    # 判断查询出来的账号和输入的账号相同
    if numbers[0][0] == t1:
        # 判断密码是否正确
        if numbers[0][2] == t2:
            if numbers[0][7] >= t3:
                # 余额=余额+存入的钱数
                sql2 = "update t_user set money=money-%s where account=%s"
                h2 = [t3, t1]
                users(sql2, h2)
                info = '''
                            ------------存款凭证------------
                                    用户名:%s
                                    银行账号：%s
                                    取款金额：%s
                                    账户余额：%s
                                    开户行名称：%s
    
                        '''
                print(info % (numbers[0][1], numbers[0][0], t3, numbers[0][7], numbers[0][9]))
            else:
                print("账户余额不足")
                return False
        else:
            print("密码输入错误")
            return False
    else:
        print("用户不存在")
        return False

# 定义存钱方法 （账户，密码，存款金额）
def cunqian(t1,t2,t3):
    # 定义查询输入的账号
    sql1 = "select * from t_user where account=%s"
    h1 = [t1]
    numbers = enquirt(sql1,h1)
    # 判断查询出来的账号和输入的账号相同
    if numbers[0][0] == t1:
        # 判断密码是否正确
        if numbers[0][2] == t2:
            # 余额=余额+存入的钱数
            sql2 = "update t_user set money=money+%s where account=%s"
            h2 = [t3,t1]
            users(sql2,h2)
            info = '''
                                ------------存款凭证------------
                                        用户名:%s
                                        银行账号：%s
                                        存款金额：%s
                                        账户余额：%s
                                        开户行名称：%s
    
                            '''
            print(info % (numbers[0][1],numbers[0][0],t3,numbers[0][7],numbers[0][9]))
            return True
        else:
            print("密码输入错误")
    else:
        print("用户不存在")
        return False

# 定义转账方法
def zhuanzhang(t1,t2,t3,t4):
    # 定义查询转出的账号
    sql1 = "select * from t_user where account=%s"
    h1 = [t1]
    numbers1 = enquirt(sql1,h1)
    # 定义查询转入的账号
    sql2 = "select * from t_user where account=%s"
    h2 = [t4]
    numbers2 = enquirt(sql2,h2)
    # 判断转出账号是否存在
    if numbers1[0][0] == t1:
        # 判断转出账户密码是否正确
        if numbers1[0][2] == t2:
            # 判断转出账号是否存在
            if numbers2[0][0] == t4:
                # 判断余额是否大于转出金额
                if numbers1[0][7] >= t3:
                    # 转出账号账户余额=账户余额-转出金额
                    sql3 = "update t_user set money = money - %s where account = %s"
                    h3 = [t3,t1]
                    users(sql3,h3)
                    # 转入账户账户金额=账户余额+转出金额
                    sql4 = "update t_user set money = money + %s where account = %s"
                    h4 = [t3,t4]
                    users(sql4,h4)
                    print("转账成功")
                else:
                    print("您的账户余额不足")
            else:
                print("转入账户输入异常")
        else:
            print("密码输入错误")
    else:
        print("转出账户不是本行账户或输入异常")
        return 1

def chaxun(t1,t2):
    sql1 = "select * from t_user where account=%s"
    h1 = [t1]
    numbers1 = enquirt(sql1,h1)
    if numbers1[0][0] == t1:
        if numbers1[0][2] == t2:
            info = '''
                                    ------------个人信息------------
                                            当前账号:%s
                                            用户名：%s
                                            密码：******
                                            余额：%s元
                                            国家：%s
                                            省份：%s
                                            街道：%s
                                            门牌号：%s
                                            开户行名称：%s
                                '''
            # 每个元素都可传入%
            print(info % (numbers1[0][0],numbers1[0][1],numbers1[0][7],numbers1[0][3],numbers1[0][4],numbers1[0][5],numbers1[0][6],numbers1[0][9]))
        else:
            print("密码输入错误")
    else:
        print("账号不是本行账户或输入错误")

while True:
    initial_interface()
    begin = input("请选择业务:")
    # 开户
    if begin == "1":
        k1 = kaihu()
        print(k1)
    # 取钱
    elif begin == "2":
        q1 = int(input("请输入账号："))
        q2 = int(input("请输入密码："))
        q3 = int(input("请输入取款金额"))
        k2 = quqian(q1,q2,q3)
        print(k2)
    # 存钱
    elif begin == "3":
        c1 = int(input("请输入账号："))
        c2 = int(input("请输入密码："))
        c3 = int(input("请输入存款金额"))
        k3 = cunqian(c1,c2,c3)
        print(k3)
    # 转账
    elif begin == "4":
        z1 = int(input("请输入转出账号："))
        z2 = int(input("请输入转出账号的密码："))
        z3 = int(input("请输入转出金额："))
        z4 = int(input("请输入转入的账号："))
        k4 = zhuanzhang(z1,z2,z3,z4)
        print(k4)
    # 查询
    elif begin == "5":
        x1 = int(input("请输入账号："))
        x2 = int(input("请输入密码："))
        chaxun(x1,x2)
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")
        break
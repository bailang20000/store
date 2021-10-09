# 导入pymysql包
import pymysql
# 定义 本机地址 账号 密码 数据库 的变量
host = "localhost"
user = "root"
passwd = "123456"
database = "bank"

# 定义增，删，改方法
#  sql1：sql增，删，改语句，sql2执行的增，删，改条件
def users(sql1,sql2):
    # 连接数据库： 本机地址 账号 密码 数据库
    mysql = pymysql.connect(host=host,user=user,passwd=passwd,database=database)
    # 创建控制台
    cursor = mysql.cursor()
    # 创建sql语句并执行sql语句
    cursor.execute(sql1,sql2)
    # 提交数据到数据库
    mysql.commit()
    # 关闭控制台
    cursor.close()
    # 关闭数据库连接
    mysql.close()

# 定义查询方法
#  sql1：sql查询语句，sql2：查询的约束条件，sql3：查询一条，所有，n条数据，sql4：约束sql3查询n条数据
def enquirt(sql1,sql2,sql3="all",sql4=1):
    # 连接数据库： 本机地址 账号 密码 数据库
    mysql = pymysql.connect(host=host,user=user,passwd=passwd,database=database)
    # 创建控制台
    cursor = mysql.cursor()
    # 创建sql语句并执行sql语句
    cursor.execute(sql1, sql2)
    if sql3 == "all":
        return cursor.fetchall()
    elif sql3 == "one":
        return cursor.fetchone()
    elif sql3 == "many":
        return cursor.fetchmany(sql4)
    # 提交数据到数据库
    mysql.commit()
    # 关闭控制台
    cursor.close()
    # 关闭数据库连接
    mysql.close()

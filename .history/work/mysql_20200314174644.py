import pymysql
import time

"""
选择数据库
1.联调TTSP2.5
2.联调TDTP2.0
"""
print("请输入想要连接的数据库：")
choice = input()

if choice == "1":
    print("正在连接联调TTSP2.5数据库")
    db = pymysql.connect("10.10.7.27","ttsp","ttsp","ttsp-2.5")
    #创建一个游标
    cursor = db.cursor()
    print("数据库连接成功")
    time.sleep(2)

    input_id = input("""请输入需要的抽取的运营商编码或应用编码:\n""")
    if input_id[0] == "A":
        sql_app = "select app_secret,public_secret from `ttsp-2.5`.a_traffic_app where id = '%s'"%(input_id)
        # 执行sql语句
        cursor.execute(sql_app)
        #抽取一条
        data = cursor.fetchone()
        print("APP私钥:"+(data[0])+"\n")
        print("APP公钥:"+(data[1])+"\n")

    elif input_id[0] == "C":
        sql_biz = "select platform_private_secret,platform_public_secret from `ttsp-2.5`.a_traffic_biz where op_id = '%s'" %input_id
        # 执行sql语句
        cursor.execute(sql_biz)
        #抽取一条
        data = cursor.fetchone()
        print("运营商私钥:"+(data[0])+"\n")
        print("运营商私钥:"+(data[1])+"\n")
    else:
        print("请重新输入")

#     #查找对应公私钥
#     sql_biz = "select app_secret,public_secret from `ttsp-2.5`.a_traffic_biz where op_id = 'C120020180200007'"
#     # 执行sql语句
#     cursor.execute(sql_biz)
#     #抽取一条
#     data = cursor.fetchone()
#     print("私钥:"+(data[0]))
#     print("公钥:"+(data[1]))


#     db.close()

# elif choice == "2":
#     print("正在连接联调TDTP2.5数据库")
#     db = pymysql.connect("10.10.3.101","reader","reader",)
#     print("数据库连接成功")
#     db.close()

else:
    print("请从新选择")



    
import pymysql

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
    print("数据库连接成功")
    #创建一个游标
    cursor = db.cursor()
    #查找对应公私钥
    sql_biz = "select app_secret,public_secret from `ttsp-2.5`.a_traffic_biz where op_id = 'C120020180200007'"
    # 执行sql语句
    cursor.execute(sql_biz)
    data = cursor.fetchone()
    print((data[0]))

    db.close()

elif choice == "2":
    print("正在连接联调TDTP2.5数据库")
    db = pymysql.connect("10.10.3.101","reader","reader",)
    print("数据库连接成功")
    db.close()

else:
    print("请从新选择")



    
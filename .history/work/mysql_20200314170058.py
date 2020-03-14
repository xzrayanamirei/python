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
    print(0)
elif choice == "2":
    print("正在连接联调TDTP2.5数据库")
else:
    print("请从新选择")



    
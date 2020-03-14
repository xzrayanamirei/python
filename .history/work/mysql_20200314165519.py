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
    db = pymysql.connect(host="10.10.7.27", 
                     user="ttsp", 
                     password="ttsp", 
                     port="3306", 
                     database="ttsp-2.5", 
                     charset='utf8')
    print(0)
elif choice == "2":
    print("正在连接联调TDTP2.5数据库")
else:
    print("请从新选择")



    
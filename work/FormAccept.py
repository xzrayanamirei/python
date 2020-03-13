import requests
import base64
import binascii
import json
import time

#base_64反解16进制
qr_code = '''
AQJ0tv5xj7flCeK816EnzHy+tgkJ7TyAukK5Qeqaemzp+87ylEgmW7f9GDxuzkklK39LfR6BtXQY/71jB3OXWuEZADAGBU0PEAP/HaQLyiMFG8ttLnodM+TLX05NM4W2GCq2jE84sTdaTtpuL5sjMpLugPHfk+A6eMuhM+fJMwiQc/wIKNKRIU5GQ0GHR5MlGEBDQYdHkyUYQAYDUs4GA1LuADAgIAMTFDFDiScPAAIAAQAAAAAAAAAAQ0GHR5J5MIgAAAAAAAAAAAAAAAAFkW1geJYcT0vSlIiOrgTD7dkdZyjUyWrUUJBJCq51qlPwKeOLRIXX5aYXlx9X+izA0mUO7DmtFqCl9EnePM06
'''
hex_code = base64.b64decode(qr_code).hex()

#定义福码机构
list_biz = ("0001","0002","0016","0025","0030")
print(len(hex_code))

if hex_code[132:136] in list_biz and len(hex_code) == 540 :
    print("这是福州的码")
else:
    print("这不是福州的码，请确认")
    print("支付机构号是："+hex_code[132:136])
    exit()


#时间戳转化
def time_YmdHMS (TimeStamp):
    TimeStamp +=1483200000
    # print(TimeStamp)
#元组化时间
    timeArray = time.localtime(TimeStamp)
#时间格式重组
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
    return str(otherStyleTime)

print("########二维码解析开始########")
print("二维码版本号:"+hex_code[0:2])
print("#####平台授权域#####")
print("公钥类型:"+hex_code[2:4])
print("公钥:"+hex_code[4:132])
print("支付服务机构码:"+hex_code[132:136])
print("公钥失效时间:"+time_YmdHMS(int(hex_code[136:144],16)))
print("平台证书号:"+hex_code[144:148])
print("平台签名:"+hex_code[148:276])
print("#####业务信息域#####")
print("二维码识别号:"+hex_code[276:308])
print("二维码生成时间:"+time_YmdHMS(int(hex_code[308:316],16)))
print("二维码失效时间:"+time_YmdHMS(int(hex_code[316:324],16)))
print("用户身份标识:"+hex_code[324:344])
print("消费金额上限:"+str(int(hex_code[344:348],16)))
# print("业务其他信息:"+hex_code[348:412])
# print("交通行业使用:"+hex_code[348:412][0:52])
# print("用户支付方式:"+hex_code[348:412][52:56])
# print("预留信息域:"+hex_code[348:412][56:62])
# print("版本号:"+hex_code[348:412][62:64])
print("#####交通行业使用########")
print("行业标识:"+hex_code[348:412][0:52][0:4])
print("凭证类型:"+hex_code[348:412][0:52][4:6])
print("进出站使用限制:"+hex_code[348:412][0:52][6:8])
print("站点限制:"+hex_code[348:412][0:52][8:24])
print("行程单号:"+hex_code[348:412][0:52][24:40])
print("本行程关联的进站或上车站点编码:"+hex_code[348:412][0:52][40:44])
print("本行程扫码进站或上车时间:"+hex_code[348:412][0:52][44:52])







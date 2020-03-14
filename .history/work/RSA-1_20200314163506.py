import datetime
import random
import requests
import hashlib
import json
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

requests = """
certName=null&certNo=1&certType=0&channelNo=5200&channelUserId=9998899988999889&mobile=18559865700
"""

businessdata = json.dumps(requests)

print(businessdata)



def sign(signflag,baseRequest):
#http请求body
print(baseRequest)
#加签标志
if not RSA: 
    return baseRequest
else:
#取请求体中的业务数据
businessdata = json.dumps(baseRequest)


# #读取私钥（.key格式，可使用openssl或java.keytools产生）
# with open(keypath,'r') as rsaKeyFile:
# rsaKey = rsaKeyFile.read().replace("\n",'')
# print(rsaKey)
# rsaKeyBytes = base64.b64decode(rsaKey)
# print(rsaKeyBytes)

# #SHA256摘要，RSA加密
# priKey = RSA.importKey(rsaKeyBytes)
# signer = PKCS1_v1_5.new(priKey)
# #加密请求计算
# hash_obj = SHA256.new(business_data.encode('utf-8'))
# signature = base64.b64encode(signer.sign(hash_obj))
# print(signature)

# #把签名加进请求体并返回
# baseRequest['sign'] = signature.decode()
# print(baseRequest)
# return baseRequest


# def validata(signflag,cerpath,res):
# if not signflag: return res
# else:
# #取业务数据和签名
# data = res['data']
# sign = res['sign']
# #此处cer已转换成pem格式，使用openssl工具
# #openssl x509 -inform der -pubkey -noout -in xxxxx.cer>xxxxx.pem
# cert = open(cerpath).read().replace("-----BEGIN PUBLIC KEY-----\n","").replace("-----END PUBLIC KEY-----\n","").replace("\n","")
# print(cert)


# #验签逻辑同加签
# pubBytes = base64.b64decode(cert)
# pubKey = RSA.importKey(pubBytes)
# signer = SHA256.new(json.dumps(data).encode("utf-8"))
# verifier = PKCS1_v1_5.new(pubKey)
# return verifier.verify(signer,base64.b64decode(sign))
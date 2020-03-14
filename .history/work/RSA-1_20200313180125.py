# -*- coding:utf-8 -*-
import rsa

def jia_qian_demo():
    """
    加签验签
    """
    public_key, private_key = rsa.newkeys(2048)  # 创建

    # print ('公钥:')
    pub_pkcs = public_key.save_pkcs1()
    # print (pub_pkcs)
    # print ('私钥:')
    priv_pkcs = private_key.save_pkcs1()
    # print(priv_pkcs)

    # 假设以上得到的公钥及私钥 一下演示加签验签

    mess = 'hello word'
    print ('加密前数据'+str(mess))

    # 加载公钥私钥
    public_key = rsa.PublicKey.load_pkcs1(pub_pkcs)
    private_key = rsa.PrivateKey.load_pkcs1(priv_pkcs)
    # print ('加载到的公钥')
    # print (public_key)
    # print ('加载到的私钥')
    # print (private_key)

    mess = '重要信息不可泄露'
    result_sign = rsa.sign(mess.encode(), private_key, 'SHA-256')
    # print ('加签结果' + str(result_sign))

    result_verify = rsa.verify(mess.encode(), result_sign, public_key)

    print ("验签结果"+str(result_verify))

if __name__ == '__main__':
    jia_qian_demo()
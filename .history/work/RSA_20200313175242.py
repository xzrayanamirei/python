# -*- coding:utf-8 -*-
import rsa

def jia_qian_demo():
    """
    加签验签
    :return:
    """
    public_key, private_key = rsa.newkeys(1024)  # 创建

    print ('公钥:')
    pub_pkcs = public_key.save_pkcs1()
    print (pub_pkcs)
    print ('私钥:')
    priv_pkcs = private_key.save_pkcs1()
    print(priv_pkcs)

    # 假设以上得到的公钥及私钥 一下演示加签验签

    mess = 'hello word'
    print ('加密前数据'+str(mess))

    # 加载公钥私钥
    public_key = rsa.PublicKey.load_pkcs1(pub_pkcs)
    private_key = rsa.PrivateKey.load_pkcs1(priv_pkcs)
    print ('加载到的公钥')
    print (public_key)
    print ('加载到的私钥')
    print (private_key)

    mess = '重要信息不可泄露'
    result = rsa.sign(mess.encode(), private_key, 'SHA-1')
    print ('加签结果')
    print (result)

    result = rsa.verify(mess.encode(), result, public_key)  # 验签失败抛出异常
    print ('验签结果')
    print (result)

if __name__ == '__main__':
    jia_qian_demo()
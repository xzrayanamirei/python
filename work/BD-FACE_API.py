import requests
import base64
import json
# 1，准备好申请的人脸识别api，API Key， Secret Key
api_key = 'soDdAVlkALjKWUeQDXPmL3Ar'
Secret_Key = 'DKxuvo6c32wBVOiNBhfUiKHoKT7GdbQ2'

api1='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(api_key,Secret_Key)
# api2="https://aip.baidubce.com/rest/2.0/face/v3/match"

# 2,获取token值，拼接API
def get_token():
    response=requests.get(api1)
    access_token=eval(response.text)['access_token']
    api2="https://aip.baidubce.com/rest/2.0/face/v3/match"+"?access_token="+access_token
    return api2

# 3,读取图片数据
def read_img(img1,img2):
    with open(img1,'rb') as f:
        pic1=base64.b64encode(f.read())
    with open(img2,'rb') as f:
        pic2=base64.b64encode(f.read())
    params=json.dumps([
        {"image":str(pic1,"utf-8"),"image_type":'BASE64',"face_type":"LIVE"},
        {"image":str(pic2,"utf-8"),"image_type":'BASE64',"face_type":"IDCARD"}
    ])
    return params

# 4，发起请求拿到对比结果
def analyse_img(file1,file2):
    params=read_img(file1,file2)
    api=get_token()
    content=requests.post(api,params).text
    # print(content)
    score=eval(content)['result']['score']
    if score>80:
        print('图片识别相似度度为'+str(score)+',是同一人')
    else:
        print('图片识别相似度度为'+str(score)+',不是同一人')
file1path = r'C:\bwton\2.png'
file2path = r'C:\bwton\2.png'

analyse_img(file1path,file2path)
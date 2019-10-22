'''
@1.扫码进群
'''
import requests
from demo.xm005 import login,get_id

def invite_group(token,uuid):
    path = 'https://gateway.xmzt.cn/tourapi/trip/invited/qr'
    data = {"client": "ios", "refCode": "ACF37H3B", "token": token,
            "groupId":"2702726632","userId": uuid, "version": 1.0}
    r = requests.post(url= path ,data= data).json()
    return r

if __name__ == '__main__':
    psd = 123456
    i = 0
    for phone in range(13900000300,13900000400):
        i = i + 1
        token = login(phone,psd)
        print(token)
        uuid = get_id(token)
        print('{}第{}个进群:'.format(phone,i),invite_group(token,uuid))
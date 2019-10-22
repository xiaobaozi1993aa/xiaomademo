'''
@1.获取网易第三方账号
'''
import requests
from demo.xm005 import login


def get_wangyi(token):
    path = 'https://gateway.xmzt.cn/talkback/user/account'
    data = {"token":token}
    r = requests.get(url = path,params = data)
    print(r.json())

if __name__ == '__main__':
    for phone in range(13900000001, 13900000100):
        token = login(phone,123456)
        get_wangyi(token)
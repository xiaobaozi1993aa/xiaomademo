import requests
import ssl
import pymysql
def login(phone,psd):
    path = 'https://gateway.xmzt.cn/user/login'
    data = {"client":"w'x","password":psd,"phone":phone,"version":3}
    r = requests.post(url=path, data=data).json()
    print('用户登陆:',r.get('reMsg'))
    print('token:',r.get('rel'))
    return r.get('rel')

if __name__ == '__main__':
    login(13066909086,123456)
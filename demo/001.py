import requests
from requests import exceptions

#

def login(phone,psd):
    path = 'https://gateway.xmzt.cn/user/login'
    data = {"client":"w'x","password":13066909086,"phone":123456,"version":3}
    try:
        r = requests.post(url=path, data=data,timeout = 1)
        globals()['timeapp'] = r.elapsed.total_seconds()
        print('耗时:{}s'.format(globals()['timeapp']))
    except exceptions.Timeout as e:
        print(e,globals()['timeapp'],'time out')

if __name__ == '__main__':
    login(13066909086, 123456)
# try:
#     assert r.json().get('reMsg') == '操作成功'
#     print('用户登陆:', r.json().get('reMsg'))
#     print('token:', r.json().get('rel'))
#     return r.json().get('rel')
# except:
#     pass
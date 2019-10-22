'''
@1.解散群
'''

import requests
from demo.xm005 import login

def jiesan(token):
    path = 'https://gateway.xmzt.cn/talkback/group/remove?token=%s' % token
    data = {"groupId":2705330452}
    r = requests.get(url = path ,params=data)
    print(r.json())

if __name__ == '__main__':
    token = login(13800000001,123456)
    jiesan(token)
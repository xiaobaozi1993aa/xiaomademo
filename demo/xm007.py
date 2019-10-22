'''
@1.行程群批量添加车辆
'''

import requests
from demo.xm005 import login


def add_car(token,car,uuid):
    path = 'https://gateway.xmzt.cn/talkback/group/addDriver'
    data = {"client":"ios","groupId":"2702747810","licencePlate":car,
            "token":token,"userId":uuid,"version":"1.0.1"}
    r = requests.get(url = path,params= data).json()
    return r

if __name__ == '__main__':
    phone = 13900000703
    psd = 123456
    token = login(phone,psd)
    uuid = (a for a in range(187270,187310))
    num = (a for a in range(1000,1040))
    d = zip(num, uuid)
    i = 0
    for a in d:
        i = i+1
        aa = str(a[0])
        car = '川QQ' + aa
        uuid = a[1]
        print('第{}辆添加'.format(i),add_car(token,car,uuid))

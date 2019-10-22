'''
@1.队伍批量添加车辆
'''
import requests
from demo.xm005 import login


def add_car(token,car):
    path = 'https://gateway.xmzt.cn/talkback/group/teamAddOrUpdtOrDelDriver'
    data = {"groupId":"2705711532","licencePlate":car,
            "token":token,"addOrUpdtOrDel":"1"}
    r = requests.get(url = path,params= data).json()
    return r

if __name__ == '__main__':
    phone = (a for a in range(13900000110,13900000150))
    num = (a for a in range(1000, 1041))
    d = zip(num, phone)
    i = 0
    for a in d:
        i = i + 1
        aa = str(a[0])
        car = '川QQ' + aa
        phone = a[1]
        token = login(phone, 123456)
        print('第{}辆添加'.format(i), add_car(token, car))


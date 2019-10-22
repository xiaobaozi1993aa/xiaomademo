'''
@1.登录创建订单群
'''
import requests
import redis
import json



def login(phone,psd):
    path = 'https://gateway.xmzt.cn/user/login'
    data = {"client":"w'x","password":psd,"phone":phone,"version":3}
    r = requests.post(url=path, data=data).json()
    print('用户登陆:',r.get('reMsg'))
    print('token:',r.get('rel'))
    return r.get('rel')

#获取userid
def get_id(token):
    path = 'https://gateway.xmzt.cn/user/user/personal'
    data = {"token":token}
    r = requests.get(url=path, params=data).json()
    print("用户ID:",r.get('rel').get('userId'))
    return r.get('rel').get('userId')

# bookPeople 预订人
# visitorList 出行人
# carList 司机

#提交订单
def get_order(token,i):
    data = {"openInvoice": 0, "bookPeople": {"name": "芒", "phone": "13010000001"},
            "carList": [{"phone": "13010000002", "carNumber": "川QQ1234", "numberType": 0}],
            "cost": [{"costType": 1, "visitorList": [{"name": "我呢", "idCard": "130101199305010018",
                                                      "phone": "%s" % i}]}], "lineId": 33, "departDate": "2019-10-19"}
    headers = {
        "Content-Type": "application/json"
    }
    path = 'https://gateway.xmzt.cn/tourapi/order/line?token=%s' % token
    #data = {"token":token}
    r = requests.post(url=path, data=json.dumps(data),headers = headers).json()
    print("提交订单:", r.get("reMsg"),r.get('rel'))
    print(data)
    return r.get('rel')

#修改状态为40
def update_state(orderid):
    path = ' https://gateway.xmzt.cn/tourapi/test/order/state'
    data = {"orderId": orderid,"state":40}
    r = requests.post(url=path, data=data).json()
    print(data)
    print('修改成功', r)

def order_true(orderid):

    path = 'https://gateway.xmzt.cn//tourapi/trip/order'
    data = {"orderId":orderid}
    r = requests.post(url = path, data = data).json()
    print(data)
    print("提交订单:", r)
    #return r.get('rel')

#修改状态为60
def update_state2(orderid):
    path = ' https://gateway.xmzt.cn/tourapi/test/order/state'
    data = {"orderId": orderid, "state": 60}
    r = requests.post(url=path, data=data).json()
    print(data)
    print('修改成功', r)


if __name__ == '__main__':
    psd = 123456
    a = (phone for phone in range(13900000400, 13900000500))
    b = (i for i in range(13900000500, 13900000600))
    c = zip(a,b)
    for d in c:
        phone = d[0] #app账号
        i = d[1] #出行人账号
        token = login(phone,psd)
        get_id(token)
        orderid = get_order(token, i)
        update_state(orderid)
        order_true(orderid)
        update_state2(orderid)
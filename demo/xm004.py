" @ 批量用户景点线路购买"
import requests
import pymysql
import json
import time


#发送短信验证码
def get_mcode(phone):
    url = 'https://gateway.xmzt.cn/user/sendValidate'
    data = {"phone": "%s" % phone}
    r = requests.get(url=url, params=data).json()
    print(data)
    print('短信注册:',r.get('reMsg'))


#获取手机验证码
def get_messafe_code(phone):
    db = pymysql.Connect('xmzt-data.mysql.rds.aliyuncs.com', 'xmztapi', '3GY9kxeY1YZb', 'tour')
    cursor = db.cursor()
    cursor.execute('select sms_content from msg_log_sms where mobile = "%s" order by id desc limit 1' % phone)
    data = cursor.fetchone()
    mcode = str(data)[11:17]
    print('验证码:',mcode)
    return mcode

#用户注册
def register(phone,psd,mcode):
    path = 'https://gateway.xmzt.cn/user/register/phone'
    data = {"client":"w'x","password":psd,"phone":phone,"verificationCode":mcode,"version":3}
    r = requests.post(url=path, data=data).json()
    print('用户注册:',r.get('reMsg'))


#用户登陆
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

# id = 110101198001010010
#选择路线
# def choose_line(token,uuid):
#     path = 'https://gateway.xmzt.cn/tourapi/line/detail'
#     data = {"client":"ios","lineId":33,"token":token,"userId":uuid,"version":1.0}
#     r = requests.get(url=path, params=data).json()
#     print("选择路线:",r.get('reMsg'),r)
#     return r
# #
# #
# #获取出发日期
# def get_date(token,uuid):
#     path = 'https://gateway.xmzt.cn/tourapi/line/prices'
#     data = {"client": "ios", "lineId": 33, "token": token, "userId": uuid, "version": 1.0}
#     r = requests.get(url=path, params=data).json()
#     print("选择路线:",r)
#
#
# #添加出游人
# def add_people(token,uuid):
#     path = 'https://gateway.xmzt.cn/tourapi/sysUserVisitors/saveUserIntegral'
#     data = {"certificateType":1,"client":"ios","identityCard":110101198001010010,"name":"我爱你",
#             "tel":"13066909086","token":token,"type":1,
#             "userId":uuid,"version":1.0}
#     r = requests.post(url=path, params=data).json()
#     print("添加出游人:", r)


# bookPeople 预订人
# visitorList 出行人
# carList 司机
data = {"openInvoice":0,"bookPeople":{"name":"芒","phone":"13800000007"},
         "carList":[{"phone":"13800000008","carNumber":"川QQ1234","numberType":0}],
         "cost":[{"costType":1,"visitorList":[{"name":"我呢","idCard":"130101199305010018",
           "phone":"13800000009"}]}],"lineId":33,"departDate":"2019-10-15"}

#提交订单
def get_order(token):
    headers = {
        "Content-Type": "application/json"
    }
    path = 'https://gateway.xmzt.cn/tourapi/order/line?token=%s' % token
    #data = {"token":token}
    r = requests.post(url=path, data=json.dumps(data),headers = headers).json()
    print("提交订单:", r.get("reMsg"),r.get('rel'))
    return r.get('rel')


# #查找id
# def get_sql_id(orderid):
#     db = pymysql.Connect('xmzt-data.mysql.rds.aliyuncs.com', 'xmztapi', '3GY9kxeY1YZb', 'tour')
#     cursor = db.cursor()
#     cursor.execute('select id from tour_order where order_id = "%s"' % orderid)
#     data = cursor.fetchone()
#     print('订单id:',data[0])
#     return data[0]
#
#




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

#
#
# #订单确认
# def order_ture(id):
#     headers = {"Accept": "*/*",
#                "Accept-Encoding": "gzip, deflate",
#                "Content-Type": "application/json;charset=UTF-8",
#                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#                "Connection": "keep-alive"}
#     path ='http://mana.xmzt.cn/a/tour/order/tourOrder/refund'
#     data = {"type":3,"id":id}
#     r = requests.post(url=path, data=data,headers = headers).text
#     print("订单确认:")
#


if __name__ == '__main__':
    #phone = 15800000000
    #for phone in range(13800000067,13800000100):
        phone = 13900000703
        psd = 123456
        get_mcode(phone)
        mcode = get_messafe_code(phone)
        register(phone,psd,mcode)
        token = login(phone,psd)
        # time.sleep(1)
        # uuid = get_id(token)
        # orderid = get_order(token)
        # update_state(orderid)
        # order_true(orderid)
        # update_state2(orderid)



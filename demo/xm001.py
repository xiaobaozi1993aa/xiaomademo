'''
@1.抢优惠券
'''


import requests
import pymysql
from Common.redis_common import content_redis


url = 'https://gateway.xmzt.cn'
#发送短信验证码
def get_mcode(phone):
    url = 'https://gateway.xmzt.cn/user/sendValidate'
    data = {"phone": "%s" % phone}
    r = requests.get(url=url, params=data).json()
    print('短信注册:',r.get('reMsg'))


#获取手机验证码
def get_messafe_code(phone):
    value = 'USER:SMSCODE:%s:1' % phone
    db = content_redis()
    mcode = db.get(value).decode('utf8')
    print('验证码:', mcode)
    return mcode
#用户注册
def register(phone,psd,mcode):
    path = 'https://gateway.xmzt.cn/user/register/phone'
    data = {"client":"w'x","password":psd,"phone":phone,"verificationCode":mcode,"version":3}
    r = requests.post(url=path, data=data).json()
    print('用户注册:',r.get('reMsg'),r)


#用户登陆
def login(phone,psd):
    path = 'https://gateway.xmzt.cn/user/login'
    data = {"client":"w'x","password":psd,"phone":phone,"version":3}
    r = requests.post(url=path, data=data)
    print(r.elapsed.total_seconds())
    try:
        assert r.json().get('reMsg') == '操作成功'
        print('用户登陆:', r.json().get('reMsg'))
        print('token:', r.json().get('rel'))
        return r.json().get('rel')
    except:
        print('wow')

#获取userid
def get_id(token):
    path = 'https://gateway.xmzt.cn/user/user/personal'
    data = {"token":token}
    r = requests.get(url=path, params=data)
    print('userid',r.json().get('rel').get('userId'))
    print(r.elapsed.total_seconds())
    print(r.elapsed.total_seconds())

    return r.json().get('rel').get('userId')

#抢优惠券
def couponx(token,id):
    path = 'https://gateway.xmzt.cn/tourapi/user/coupon/getCoupon'
    data = {"client":"w'x","couponId":22,"token":token,"userId":id,"version":1.0}
    r = requests.post(url=path, data=data).json()
    try:
        assert r.get('reMsg') != 'you'
        print(id,":已领取",r.get('reMsg'))
    except:
        r = requests.post(url=path, data=data).json()
        print(id,":已领取",r.get('reMsg'))
        print(r.elspsed)
    finally:
        return None

if __name__ == '__main__':
        #phone = 15800000020
    for phone in range(13900000001,13900000101):
        psd = 123456
        get_mcode(phone)
        mcode = get_messafe_code(phone)
        register(phone,psd,mcode)
        # token = login(phone,psd)
        # id = get_id(token)
        # couponx(token,id)
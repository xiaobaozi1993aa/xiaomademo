import requests
import ssl
import pymysql




url = 'https://gateway.xmzt.cn'
#发送短信验证码
def get_mcode(phone):
    url = 'https://gateway.xmzt.cn/user/sendValidate'
    data = {"phone": "%s" % phone}
    r = requests.get(url=url, params=data).json()
    #print('短信注册:',r.get('reMsg'))


#获取手机验证码
def get_messafe_code(phone):
    db = pymysql.Connect('xmzt-data.mysql.rds.aliyuncs.com', 'xmztapi', '3GY9kxeY1YZb', 'tour')
    cursor = db.cursor()
    cursor.execute('select sms_content from msg_log_sms where mobile = "%s" order by id desc limit 1' % phone)
    data = cursor.fetchone()
    mcode = str(data)[11:17]
    #print('验证码:',mcode)
    return mcode

#用户注册
def register(phone,psd,mcode):
    path = 'https://gateway.xmzt.cn/user/register/phone'
    #api = ''.join([url, path])
    data = {"client":"w'x","password":psd,"phone":phone,"verificationCode":mcode,"version":3}
    r = requests.post(url=path, data=data).json()
    #print('用户注册:',r.get('reMsg'),r)


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
    print('userid',r.get('rel').get('userId'))
    return r.get('rel').get('userId')



#抢优惠券
def couponx(token,id):
    path = 'https://gateway.xmzt.cn/tourapi/user/coupon/getCoupon'
    data = {"client":"w'x","couponId":19,"token":token,"userId":id,"version":1.0}
    r = requests.post(url=path, data=data).json()
    #print(r)
    print(id,":已领取",r.get('reMsg'))


if __name__ == '__main__':
        phone = 15800000019
    #for phone in (15800000013,15800000017):
        psd = 199308
        get_mcode(phone)
        mcode = get_messafe_code(phone)
        register(phone,psd,mcode)
        token = login(phone,psd)
        id = get_id(token)
        couponx(token,id)
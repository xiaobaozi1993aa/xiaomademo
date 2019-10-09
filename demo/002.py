from xmzt.xm001 import *
import requests


# for phone in range(13000000000,13000000010):
#     psd = 123456
#     get_mcode(phone)
#     mcode = get_messafe_code(phone)
#     register(phone,psd,mcode)


def qiaodao(token):
    url = "https://gateway.xmzt.cn/tourapi/sysUserSign/signIn"
    data = {"token":token}
    r = requests.post(url = url,data = data)
    print(r.json())

token =login(15802767637,123456)

qiaodao(token)
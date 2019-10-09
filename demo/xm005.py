from xmzt.xm004 import login,get_id
import requests



def place(token,uuid):
    # path ='https://gateway.xmzt.cn/talkback/group/isShareLocationOrIsAutoplay'
    # data = {"client":"ios","groupId":2691598179,
    #         "isShareLocation":0,"token":token,"userId":uuid,"version":1.0}
    path = "https://gateway.xmzt.cn/talkback/group/isShareLocationOrIsAutoplay?" \
           "client=ios&groupId=2691598179&isShareLocation=1&" \
           "token={}&userId={}&version=1.0".format(token, uuid)
    r = requests.get(url=path).json()
    print("开启定位:",r)


if __name__ == '__main__':
    for phone in range(13010000190,13010000192):
        psd = 123456
        token = login(phone,psd)
        uuid = get_id(token)
        place(token,uuid)
'''
@1.群主移除成员
'''
import requests
from demo.xm005 import login,get_id


def qingli(token,uuid):
    path = 'https://gateway.xmzt.cn/talkback/group/removeMembers'
    data = {"token":token,"userIds":uuid,"tid":2705330452}
    r = requests.get(url = path ,params = data)
    print(r.json())


if __name__ == '__main__':
    token = login(13800000001,123456)
    uuid = '187100'
    qingli(token,uuid)
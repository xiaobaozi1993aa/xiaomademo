'''
@1.创建队伍
'''

import requests
from demo.xm005 import login,get_id

# 创建队伍
def creat_group(token):
    path = 'https://gateway.xmzt.cn/talkback/group/normal/create'
    data = {"token":token}
    r = requests.post(url = path,data= data)
    print('创建队伍耗时{}S'.format(r.elapsed.total_seconds()))
    print(r.json())
    print(r.json().get('rel'))
    return r.json().get('rel')

# 生成口令
def kouling(token,g_id):
    path = 'https://gateway.xmzt.cn/talkback//group/teamInfo'
    data = {"groupId":g_id,"token":token}
    r = requests.get(url = path, params = data)
    print('生成口令耗时{}S'.format(r.elapsed.total_seconds()))
    print(r.json().get('rel').get('teamPwdcard'))
    return r.json().get('rel').get('teamPwdcard')

# 加入队伍
def join_team(token,kl):
    path = 'https://gateway.xmzt.cn/talkback/group/joinTeam'
    data = {"groupPwdcard":kl,"token":token}
    r = requests.post(url=path, data=data)
    print('加入队伍:',r.json().get('reMsg'),'耗时{}S'.format(r.elapsed.total_seconds()))
    print(r.json())
    return r.json()

# 退出队伍
# def leave_team(g_id,uuid):
#     path = 'https://gateway.xmzt.cn/talkback/group/leave'
#     data = {"groupId":g_id,"userId":uuid}
#     r = requests.post(url=path, data=data)
#     print('退出队伍{}S'.format(r.elapsed.total_seconds()))
#     print(r.json())

# 解散/退出队伍
def remove_team(g_id,token):
    path = 'https://gateway.xmzt.cn/talkback/group/removeTeam'
    data = {"groupId": g_id, "token":token}
    r = requests.post(url=path, data=data)
    print('解散队伍{}S'.format(r.elapsed.total_seconds()))
    print(r.json())

if __name__ == '__main__':
    token = login(13800000001,123456)
    uuid = get_id(token)
    g_id = creat_group(token)
    kl = kouling(token,g_id)
    join_team(token, kl)
    # leave_team(g_id,uuid)
    # remove_team(g_id, token)


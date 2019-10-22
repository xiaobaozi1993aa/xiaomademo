'''
@1.批量加入队伍
@2.批量解散队伍
'''

from demo.xm005 import login,get_id
from demo.xm010 import join_team,remove_team

i = 0

# for phone in range(13900000001, 13900000100):
#     i += 1
#     token = login(phone,123456)
#     dw = join_team(token, 478926).get('rel')
#     print(phone,'第{}个加入{}队伍成功'.format(i,dw))

# #
for phone in range(13900000001, 13900000100):
    i += 1
    token = login(phone, 123456)
    uuid = get_id(token)
    remove_team(2705711532, token)
    print(phone, '第{}个退出队伍成功'.format(i))
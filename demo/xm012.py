'''
@1.队伍口令排序,去重,统计,验证
'''


from demo.xm005 import login
from demo.xm010 import creat_group,kouling

kllist = []
for phone in range(13900000300, 13900000400):
    token = login(phone,123456)
    g_id = creat_group(token)
    kllist.append(kouling(token,g_id))                # 列表添加
kllist.sort()                                       # 列表排序
abcd = list(set(kllist))                                # 列表去重
print(abcd)
print(len(abcd))                                  # 列表统计个数





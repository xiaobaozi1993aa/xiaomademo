# FileName : db_common.py
# Author   : xiao'bao
# DateTime : 2019-9-29 17点48分
# SoftWare : PyCharm


import os
import sys
import re
#读取设备信息名称
readDeviceId = os.popen('adb devices').readlines()
def deviceID(i):
    if i == 30:
        deviceId = '1234566'  # 指定单机执行
    else:
        deviceId = re.findall(r'^\w*\b', readDeviceId[i + 1])[0]
    return deviceId

if __name__ == '__main__':
    devices
deviceAndroidVersion = os.popen('adb -s %s shell getprop ro.build.version.release' % deviceId).readlines()
deviceVersion = (deviceAndroidVersion[0]).strip('\n')
print(deviceVersion)
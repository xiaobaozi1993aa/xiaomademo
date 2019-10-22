import os
import sys
import re
import time

# 获取设备名
def get_deviceID(i):
    readDeviceId = os.popen('adb devices').readlines()
    if i == 30:
        deviceId = '1234566'  # 指定单机执行
    else:
        deviceId = re.findall(r'^\w*\b', readDeviceId[i + 1])[0]
        if deviceId != None:
            print(deviceId)
        else:
            print('检查设备是否插入')
    return deviceId


# 获取版本号
def get_version0(id):
    deviceAndroidVersion = os.popen('adb -s %s shell getprop ro.build.version.release' % id).readlines()
    deviceVersion = (deviceAndroidVersion[0]).strip('\n')
    print(deviceVersion)

# 开始测试
def start_monkey(id):
    if id != None:
        os.popen('adb shell monkey -p cn.xmzt.www --throttle 100 --ignore-crashes '
             '--ignore-timeouts --ignore-security-exceptions --ignore-native-crashes '
             '--monitor-native-crashes -v -v -v 30>d:\小马\monkey\mylog.log')
    else:
        print('检查设备是否插入')




if __name__ == '__main__':
    i = 0
    now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())  # 时间字符串
    id = get_deviceID(i)
    get_version0(id)
    start_monkey(id)
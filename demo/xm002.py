import threading
import time
import requests
def get_triplist():
    host = 'https://gateway.xmzt.cn/tourapi/tourTrip/tripList'
    data = {"isFinish":0,"currentCityCode":440300,"token":"cfengdev"}
    for i in range(10):
        r = requests.get(url = host,params = data).json()
        print('线程:',i)
" https://gateway.xmzt.cn/tourapi/tourTrip/tripList?isFinish=0&currentCityCode=440300&token=cfengdev"

if __name__ == '__main__':      #单个接口多线程压测
    try:
        #token = login(19930808119, 123456)
        i = 0
        tasks_number = 1
        print('=========Test Start=========')
        time1 = time.perf_counter()
        while i < tasks_number:
            t = threading.Thread(target=get_triplist())
            t.start()
            i += 1
        time2 = time.perf_counter()

        times = time2 - time1
        print('=========Test End=========')
        print('共耗时: {}'.format(times))
        print('平均耗时: {}'.format(times / 100))
    except Exception as e:
        print(e)

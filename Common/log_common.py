import logging
import time

class TestLog(object):

    def __init__(self,logger=None):

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = "D:\\小马\\xm_log\\"
        self.log_name = self.log_path + self.log_time + 'test.log'

    def get_log(self):
        if not self.logger.handlers:        #这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
            fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # a是追加模式
            fh.setLevel(logging.INFO)

            # 再创建一个handler，用于输出到控制台

            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义handler的输出格式
            formatter = logging.Formatter(
                '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

            #  添加下面一句，在记录日志之后移除句柄
            # self.logger.removeHandler(ch)
            # self.logger.removeHandler(fh)
            # 关闭打开的文件
            fh.close()
            ch.close()

        return self.logger
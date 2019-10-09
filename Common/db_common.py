# FileName : db_common.py
# Author   : xiao'bao
# DateTime : 2019-9-26 17点09分
# SoftWare : PyCharm

import pymysql
from Common.log_common import TestLog

logger = TestLog().get_log()

#数据库连接
def connect(db_base):
    try:
        db = pymysql.connect('xmzt-data.mysql.rds.aliyuncs.com', 'xmztapi', '3GY9kxeY1YZb', db_base)
        logger.info('{}库连接成功'.format(db_base))
        return db
    except Exception as e:
        logger.error(e)

#返回游标对象
def get_cursor(db):
    try:
        cursor = db.cursor
        logger.info('游标对象简历成功')
        return cursor
    except Exception as e:
        logger.error('获取游标对象失败，报错如下:{}'.format(e))

#单行数据查询
def select_one(db,sql):
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        logger.info('查询返回数据：{}'.format(data))
    except Exception as e:
        cursor.close()
        logger.error('查询返回数据失败,报错如下:{}'.format(e))


def update(db,sql):
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        logger.info('{}:修改成功'.format(sql))
        db.commit()
        logger.info('修改后提交')
    except Exception as e:
        cursor.close()
        logger.error('查询返回数据失败,报错如下:{}'.format(e))




if __name__ == '__main__':
    db = connect('tour')
    cursor = get_cursor(db)
    sql = 'update tour_order set state = 40 where order_id = "1120569622540849152"'
    update(db,sql)

#调用模板
# def get_mcode(mobile):
#     db = connect('tour')
#     cursor = get_cursor(db)
#     sql = 'update tour_order set state = 40 where order_id = "mobile"' % mobile
#     update(db, sql)

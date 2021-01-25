# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 22:44
# @Author  : Yu
# @Site    : 
# @File    : connect_db.py
# @Software: PyCharm
# @FunctionDescription：简要描述
import pymysql

db_config = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "port": 3309,
    "db": 'apps'
}


class DbConnect:
    def __init__(self, db_conf):
        self.db_conf = db_conf
        try:
            self.conn = pymysql.connect(**db_config)
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            print('数据库连接失败：', e)

    def select(self, sql_str):
        """
        查询操作
        :param sql_str:
        :return:
        """
        if self.conn:
            self.cursor.execute(sql_str)
            results = self.cursor.fetchall()
            yield results

    def execute(self, sql_str):
        if self.conn:
            try:
                self.cursor.execute(sql_str)
                self.conn.commit()
            except Exception as e:
                print('{0}执行失败！\n{1}'.format(sql_str, e))
                self.conn.rollback()

    def close(self):
        if self.conn:
            self.conn.close()


if __name__ == '__main__':
    sql_select = 'SELECT id, goodscode from apiapp_goods WHERE goodscode = "sp_199922";'
    sql = 'delete from apiapp_goods where goodscode = "sp_199922";'
    db = DbConnect(db_config)
    result = db.select(sql_select)
    print(next(result))
    db = DbConnect(db_config)
    resu = db.execute(sql)
    db = DbConnect(db_config)
    result = db.select(sql_select)
    print(next(result))
    print(db.conn.ping())

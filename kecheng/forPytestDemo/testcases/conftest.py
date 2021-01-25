# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 19:51
# @Author  : Yu
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
# @FunctionDescription：配置文件
import pytest
import requests
from kecheng.forPytestDemo.common.connect_db import db_config, DbConnect

login_url = r'http://49.235.92.12:7005/api/v1/login'
body = {
    "username": "test",
    "password": "123456"
}


@pytest.fixture(scope='session')
def login():
    request_session = requests.Session()
    response_obj = request_session.post(url=login_url, json=body)
    new_header = {
        "Authorization": "Token " + response_obj.json()["token"]
    }
    request_session.headers.update(new_header)
    yield request_session
    request_session.close()


@pytest.fixture(scope='session')
def db_conn():
    db = DbConnect(db_config)
    yield db
    print('关闭数据库连接对象')


@pytest.fixture()
def delete_by_goodscode(db_conn):
    def delete_goods(goodscode):
        sql = 'delete from apiapp_goods where goodscode = "%s";' % goodscode
        db_conn.execute(sql)

    return delete_goods


if __name__ == '__main__':
    print(next(login()))

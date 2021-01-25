# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 19:48
# @Author  : Yu
# @Site    : 
# @File    : test_GetUserInfo.py
# @Software: PyCharm
# @FunctionDescription：使用登陆fixture，获取用户信息
import requests


def test_get_user_info(login):
    user_info_url = r'http://49.235.92.12:7005/api/v1/userinfo'
    response = login.get(user_info_url)
    print(response.text)

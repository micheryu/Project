# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 21:15
# @Author  : Yu
# @Site    : 
# @File    : Day08_UseSessionRelevanceRoute.py
# @Software: PyCharm
import requests
import re

admin_url = 'http://49.235.92.12:7005/admin/login/?next=/admin/'
admin_session = requests.Session()
print("未登录时cookie：", admin_session.cookies)
admin_response = admin_session.get(admin_url)
print("登录后cookie：", dict(admin_session.cookies))
print(admin_response.text)
csrfmiddlewaretoken = re.findall("name='csrfmiddlewaretoken' value='(.*?)'", admin_response.text)[0]
body = {"csrfmiddlewaretoken": csrfmiddlewaretoken,
        "username": "admin",
        "password": "yoyo123456",
        "next": "/admin/"}

login_response = admin_session.post(admin_url, json=body)
print(login_response.text)

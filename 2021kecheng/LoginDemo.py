# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 22:47
# @Author  : Yu
# @Site    : 
# @File    : LoginDemo.py
# @Software: PyCharm
import requests
import re

login_url_str = 'http://49.235.92.12:8200/users/login/'
login_session = requests.Session()

home_page_response_str = login_session.get(login_url_str)
csrf_token_str = re.findall("name='csrfmiddlewaretoken' value='(.*?)'", home_page_response_str.text)
username = '1234@qq.com'
password = '123456'
# print(csrf_token_str)

login_api_response = login_session.post(login_url_str, {"username": username, "password": password,
                                                        "csrfmiddlewaretoken": csrf_token_str[0]})
print(login_api_response.url)

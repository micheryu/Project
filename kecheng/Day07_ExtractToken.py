# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 20:10
# @Author  : Yu
# @Site    : 
# @File    : Day07_ExtractToken.py
# @Software: PyCharm
import requests
import re
import jsonpath
import json

host = r'http://49.235.92.12:7005/'
login_api = r'api/v1/login'
body = {"username": "test", "password": "123456"}
request_session = requests.Session()
response_login = request_session.post(host + login_api, json=body)
# print(response_obj.text, type(response_obj.text))
use_request_json_extract_token = json.loads(response_login.text)["token"]
use_json_extract_token = response_login.json()["token"]
use_jsonpath_extract_token = jsonpath.jsonpath(eval(response_login.text), '$..token')[0]
use_re_findall_extract_token = re.findall('"token": "(.*?)"', response_login.text)[0]
print("使用requests.json()提取的token：{0}\n使用jsonpath提取的token:{1}\n引用json模块提取的token：{2}\n使用re.findall提取的token：{3}".format(
    use_request_json_extract_token, use_jsonpath_extract_token, use_json_extract_token, use_re_findall_extract_token))

userinfo_api = r'api/v1/userinfo'
header_dict = {
    "Authorization": "Token {}".format(use_jsonpath_extract_token)
}
request_session.headers.update(header_dict)
response_userInfo = request_session.get(host + userinfo_api)
print(response_userInfo.json())

# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 20:59
# @Author  : Yu
# @Site    : 
# @File    : RequestDemo.py
# @Software: PyCharm
import requests

url_1_str = 'http://japi.juhe.cn/qqevaluate/qq'
url_2_str = 'http://apis.juhe.cn/lottery/types'
appKey_1_str = 'fad490d3c82c66371735adfc5d38fbc5'
appKey_2_str = '64725444ffad986bd97ce1e36c727fe9'
qqNum_str = '1475002003'
qqResponse = requests.get(url_1_str, {"key": appKey_1_str, "qq": qqNum_str})
print(qqResponse.json()['result']['data']['conclusion'])
print(qqResponse.json().get('result', '没取到').get('data').get('conclusion'))

lotteryResponse = requests.get(url_2_str, {"key": appKey_2_str})
print(lotteryResponse.text)
print(lotteryResponse.json()['result'])


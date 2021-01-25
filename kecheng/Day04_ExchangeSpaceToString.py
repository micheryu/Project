# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 21:24
# @Author  : Yu
# @Site    : 
# @File    : Day04_ExchangeSpaceToString.py
# @Software: PyCharm
import re

s = 'We are Happy!'
print(s.replace(' ', '%20'))
print(re.sub(r' ', '%20', s))

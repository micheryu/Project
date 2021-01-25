# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 20:42
# @Author  : Yu
# @Site    : 
# @File    : Day10_9x9.py
# @Software: PyCharm

for i in range(1, 10):
    for j in range(1, i+1):
        print('{1}*{0}={2}'.format(i, j, i * j), end='\t')
    print()

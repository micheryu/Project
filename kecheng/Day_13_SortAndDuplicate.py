# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 21:13
# @Author  : Yu
# @Site    : 
# @File    : Day_13_SortAndDuplicate.py
# @Software: PyCharm
# @FunctionDescription：简要描述
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
print('从小到大排序：', sorted(a))
print('从大到小排序：', sorted(a, reverse=True))
print('利用集合去重后：', set(a))

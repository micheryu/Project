# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 23:13
# @Author  : Yu
# @Site    : 
# @File    : Day10_OperationList.py
# @Software: PyCharm

# def operation_list(list_obj):
#     return list_obj[::-1]

# print(operation_list([1, 2, 3, 4, 5]))
list_obj = [1, 2, 3, 4, 5, 6, 7]
print(list_obj[::-1])
print([i for i in list_obj if i % 2 == 1])

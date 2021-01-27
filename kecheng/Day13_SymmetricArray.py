# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 21:44
# @Author  : Yu
# @Site    : 
# @File    : Day13_SymmetricArray.py
# @Software: PyCharm
# @FunctionDescription：简要描述

def is_symmetric_array(list_obj: list):
    if len(list_obj) % 2 == 1:
        return False
    else:
        for index in range(int(len(list_obj) / 2)):
            if list_obj[index] == list_obj[-(index + 1)]:
                pass
            else:
                return False

        return True


list_ob = [0, 1, 2, 3, 3, 2, 1, 0]
list_oc = ['a', 'b', 'c', 1, 1, 'c', 'b', 'a']
print(is_symmetric_array(list_ob), is_symmetric_array(list_oc))

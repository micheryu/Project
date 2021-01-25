# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 22:02
# @Author  : Yu
# @Site    : 
# @File    : Day03_ChangeValue.py
# @Software: PyCharm
a = 'hello'
b = 'world'

# 交换a和b的值

# 1.利用=进行赋值
a, b = b, a
print("new value a is: %s" % a)
print("new value b is: {}".format(b))

a = 'hello'
b = 'world'
# 2.引入变量c
c = a
print("new value a is: %s" % b)
print("new value b is: {}".format(c))

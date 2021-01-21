# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 23:34
# @Author  : Yu
# @Site    : 
# @File    : Day09_PalindromeNumber.py
# @Software: PyCharm

def check_palindrome_number(number):
    return str(number) == str(number)[::-1]


print(check_palindrome_number('123a321'))

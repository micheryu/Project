# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 22:12
# @Author  : Yu
# @Site    : 
# @File    : Day03_NarcissisticNumber.py
# @Software: PyCharm

"""
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求1000以内的水仙花数（3位数）
"""

# 方法一
num: int = 100
_list = []
while num < 1000:
    left_num = num // 100
    mid_num = (num // 10) % 10
    right_num = num % 10
    if left_num * 100 + mid_num * 10 + right_num == left_num ** 3 + mid_num ** 3 + right_num ** 3:
        _list.append(num)
    num += 1
print("1000以内的水仙花数有：", _list)


# 方法二
def maxNarcissisticNum():
    narcissisticNumList = []
    for left_num_int in range(1, 10):
        for mid_num_int in range(0, 10):
            for right_num_int in range(0, 10):
                if left_num_int * 100 + mid_num_int * 10 + right_num_int == left_num_int ** 3 + mid_num_int ** 3 \
                        + right_num_int ** 3:
                    narcissisticNumList.append(left_num_int * 100 + mid_num_int * 10 + right_num_int)

    return narcissisticNumList


print("1000以内的水仙花数是：{}".format(maxNarcissisticNum()))
# 方法三 列表推导式
print("1000以内的水仙花数是：%s" % str([left_num ** 3 + mid_num ** 3 + right_num ** 3
                               for left_num in range(1, 10) for mid_num in range(0, 10) for
                               right_num in
                               range(0, 10) if
                               left_num * 100 + mid_num * 10 + right_num == left_num ** 3
                               + mid_num ** 3 + right_num ** 3]))

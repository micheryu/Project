# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 22:42
# @Author  : Yu
# @Site    : 
# @File    : Day09_PerfectNumber.py
# @Software: PyCharm
import time


def do_something_time(func):
    def inner(*args, **kw):
        time1 = time.time()
        func(*args, **kw)
        time2 = time.time()
        print('函数运行时间为：{0}'.format(time2 - time1))

    return inner


@do_something_time
def PerfectNumber(maxNum):
    num_list = []
    if maxNum <= 1:
        return num_list
    else:
        for x in range(1, maxNum):
            sum_num = 0
            for y in range(1, x):
                if x % y == 0:
                    sum_num += y

            if x == sum_num:
                num_list.append(sum_num)
    print(num_list)


if __name__ == '__main__':
    PerfectNumber(1000)

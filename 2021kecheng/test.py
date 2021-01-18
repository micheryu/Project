# import time
#
#
# def do_something_time(func):
#     def inner(*args, **kw):
#         time1 = time.time()
#         #  print(time1)
#         func(*args, **kw)
#         time.sleep(2)
#         time2 = time.time()
#         #  print(time2)
#         print('函数运行时间为：{0}'.format(time2 - time1))
#
#     return inner
#
#
# @do_something_time
# def add(num1, num2):
#     print(num1 + num2)
#
#
# add(1, 11)


# def sum_number(num):
#     if num == 1:
#         return 1
#     temp = sum_number(num - 1)
#     return num + temp
#
#
# print(sum_number(4))
# import sys
#
#
# class Cat:
#     @staticmethod
#     def eat():
#         print('这是：', sys._getframe().f_code.co_name)
#
#     @classmethod
#     def drink(cls):
#         print("这是：{0}类.{1}方法".format(cls.__name__, sys._getframe().f_code.co_name))
#
#
# tom = Cat()
# tom.eat()
# tom.drink()


class Too:
    count = 1

    def __init__(self, name):
        self.name = name
        Too.count += 1
        print('name:', self.name)

    @classmethod
    def too(cls):
        print('类方法：', cls.count)


Too('水桶')
Too('斧子')
Too('锯子')
print(Too.count)
Too.too()

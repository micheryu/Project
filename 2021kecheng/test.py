import time


def do_something_time(func):
    def inner(*args, **kw):
        time1 = time.time()
        #  print(time1)
        func(*args, **kw)
        time.sleep(2)
        time2 = time.time()
        #  print(time2)
        print('函数运行时间为：{0}'.format(time2 - time1))

    return inner


@do_something_time
def add(num1, num2):
    print(num1 + num2)


add(1, 11)

# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 22:16
# @Author  : Yu
# @Site    : 
# @File    : read_txt.py
# @Software: PyCharm
# @FunctionDescription：简要描述
import os


class OperationTxtFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_data(self, data_list):
        with open(self.file_path, 'w')as f:
            for data in data_list:
                for key, value in data.items():
                    f.write(key + ',' + value + '\n')
        print('写入成功！')

    def read_file(self, path=None):
        if path:
            self.file_path = path
        with open(self.file_path, 'r', encoding='utf-8') as f:
            results = f.read()
            return results


a = [
    {"yoyo1": "123456"},
    {"yoyo2": "123456"},
    {"yoyo3": "123456"},
]
file_path_str = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'data.txt')
A = OperationTxtFile(file_path_str)
A.write_data(a)

print('读取{}文件内容如下：'.format(file_path_str))
print(A.read_file(file_path_str))

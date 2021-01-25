# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 21:58
# @Author  : Yu
# @Site    : 
# @File    : read_yaml.py
# @Software: PyCharm
# @FunctionDescription：读取yaml文件

import os
from ruamel import yaml


def get_yaml_data(yaml_path, key):
    """
    读取yaml文件并转换成dict
    :param key:
    :param yaml_path:
    :return:
    """
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = f.read()
        return yaml.safe_load(data)[key]


if __name__ == '__main__':
    current_path = os.path.realpath(__file__)
    print(current_path)
    root_dir = os.path.dirname(os.path.dirname(current_path))
    print(root_dir)
    yaml_path_str = os.path.join(root_dir, 'data', 'data.yml')
    print(yaml_path_str)
    print(get_yaml_data(yaml_path_str, 'param'))

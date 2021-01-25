# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 22:12
# @Author  : Yu
# @Site    : 
# @File    : test_add_goods.py
# @Software: PyCharm
# @FunctionDescription：测试添加商品

import pytest
from kecheng.forPytestDemo.common.read_yaml import get_yaml_data
import os

curr_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
yam_path = os.path.join(curr_path, 'data', 'data.yml')


@pytest.mark.parametrize("test_input,check_point", get_yaml_data(yam_path, 'param'))
def test_add_goods_01(login, delete_by_goodscode, test_input, check_point):
    """
    添加商品
    :param login:
    :param test_input:
    :param check_point:
    :return:
    """
    delete_by_goodscode(goodscode='sp_199922')
    url = 'http://49.235.92.12:7005/api/v2/goods'
    body = {
        "goodsname": test_input["goodsname"],
        "goodscode": test_input["goodscode"],
        "merchantid": "10001",
        "merchantname": "悠悠学堂"
    }
    response = login.post(url, json=body)
    # print(response.text)
    assert response.json()['code'] == check_point['code']
    assert response.json()['msg'] == check_point['msg']

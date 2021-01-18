# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 22:16
# @Author  : Yu
# @Site    : 
# @File    : test_serachGoodsInfo.py
# @Software: PyCharm

import requests
import pytest


def test_get_goods_info():
    """
    根据商品id查询商品信息
    :param goodsId:
    :return:
    """
    goodsId = 1
    url = "http://49.235.92.12:7005/api/v1/goods/{}".format(goodsId)

    response = requests.get(url)

    assert response.json().get("code") == 0
    assert response.json().get("msg") == 'success!'

#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time : 2020/12/23 10:53
import requests
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
print(response.content.decode())
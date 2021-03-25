#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time : 2020/12/23 15:
import requests
from bs4 import BeautifulSoup
respond = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
page = respond.content.decode()
soup = BeautifulSoup(page,'lxml')
script = soup.find(id='getListByCountryTypeService2true')
print(script.string)
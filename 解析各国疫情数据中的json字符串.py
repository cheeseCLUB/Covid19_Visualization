#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time : 2021/3/25 15:49
import requests
from bs4 import BeautifulSoup
import re
import json
#1.获取首页内容
#1.1发送请求，获取响应
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
page = response.content.decode()
#2.提取各国疫情数据
soup = BeautifulSoup(page,'lxml')
script = soup.find(id = 'getListByCountryTypeService2true')
countries_text = script.string
json_str = re.findall((r'(\[.*\])'),countries_text)[0]
"""
此段正则表达式是要提取'getListByCountryTypeService2true'标签中的json字符串部分，
即一对中括号里的部分，而在正则表达式中中括号有自己的含义，故加\进行转义，当中的.*为任意字符无限次的进行匹配，即中括号里的所有内容,又由于findall方法返回的是
一个列表，取[0]个元素就能提取出json格式的内容
"""
#3把json内容转换为python类型的数据
last_day_corona_virus = json.loads(json_str)
print(last_day_corona_virus)#得到了python类型的各国疫情数据（是个列表，元素为一个个字典0.）

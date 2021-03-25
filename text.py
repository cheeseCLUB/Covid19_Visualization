#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time : 2020/12/23 10:33
import requests
response = requests.get('https://www.baidu.com')

#打印所使用的的编码
#print(response.encoding)
#更改所使用的编码为utf8
#response.encoding = 'utf8'
#print(response.text)

#打印响应体的二进制数据
#print(response.content)
#response类下的content (响应体的byte类型）解码出来默认是按utf8来解码的，所以不用每次都写上两行的代码了
print(response.content.decode())
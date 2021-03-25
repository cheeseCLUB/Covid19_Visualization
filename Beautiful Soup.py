#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time : 2020/12/23 11:07
from bs4 import BeautifulSoup
import requests
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
text = response.content.decode()
soup = BeautifulSoup(text,'lxml') #第二个参数lxml是解析器

#print(soup)
#一.根据标签名进行查找
    #find方法用于搜索文档树  find(self,name=None,attrs={},recursive=True,text=None,**kwargs)
    #name:标签名      attrs:属性字典     recursive:是否递归循环查找（是否只查找子标签）    text：根据文本内容查找
    #找到第一个title标签
script = soup.find('script')
#二.根据属性查找 :查找id为getListByCountryTypeService2true的标签
    #方式1 通过命名参数进行指定
script2 = soup.find(id='getListByCountryTypeService2true')
    #方式2 使用attrs来指定属性字典进行查找  防止有些属性名是关键字，不能用方式1
script3 = soup.find(attrs={'id':'getListByCountryTypeService2true'})
#三.根据文本内容进行查找
text = soup.find(text='具体标签文本')

#find函数返回的是一个tag对象，此类型对象可以获取标签的name（标签名），attrs(标签的所有属性，其中class属性是一个列表)，text(获取标签文本内容)
print(type(script))
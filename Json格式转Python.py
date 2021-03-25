#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time : 2021/3/25 14:27
import json
#1.1准备Json字符串
json_str = '[{"provinceName":"美国","currentconfirmedCount":1115312,"confirmedCount":1465966}]'
#1.2把Json字符串转化为Python类型的数据
python_dict = json.loads(json_str)
print(python_dict)#{'provinceName': '美国', 'currentconfirmedCount': 1115312, 'confirmedCount': 1465966}
#可见，转化为Python类型的数据之后引号都变成了单引号，而Json类型的数据都是单引号
print(type(python_dict))#<class 'list'>转化为了Python格式的列表（因为Json里带[]）
print(type(python_dict[0]))#<class 'dict'>列表其中每个元素格式为字典
#2.把Json格式的文件转化为Python类型的数据
#2.1构造指向文件的文件对象
with open('D:\Pycharm\workspace\Covid19 Visualization\\test.json','r') as fp:
    python_list = json.load(fp)#注意，转换json格式文件时用load方法而不是loads
    print(python_list)#结果同上
    print(type(python_list))#结果同上
    print(type(python_list[0]))#结果同上
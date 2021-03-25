#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time : 2021/3/25 15:00
import json
#1.把PYTHON转换为JSON字符串
#1.1准备python类型的数据
json_str = '[{"provinceName":"美国","currentconfirmedCount":1115312,"confirmedCount":1465966}]'
python_dict = json.loads(json_str)
#1.2把PYTHON转化为Json字符串
json_str = json.dumps(python_dict,ensure_ascii=False)#ensure_ascii=false是不是用ascii码，这样汉字就正常显示了
print(json_str)
#2.把python以json格式储存到文件中
#2.1构建要写入的文件对象
with open('D:\Pycharm\workspace\Covid19 Visualization\\test2.json','w') as fp:
    #2.2把python以JSON格式存储到文件中
    json.dump(python_dict,fp,ensure_ascii=False)

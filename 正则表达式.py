#正则表达式常用表达式：
# +:前一字符出现1次或无数次
# *:前一字符出现0次1次或无数次
# ?:前一字符出现0或1次
# {x}:具体出现x次
# .:匹配除换行符（\n）以外的所有字符
# \d:匹配[0-9]数字
# \w:匹配字母数字_和中文

#re.findall(pattern,string,flags)
#          （正则表达式，被查字符串，匹配模式）
#扫描整个string字符串，返回所有与pattern匹配的列表
#例如re.finall（“\d”,"hao1ran2"）>>["1","2"]
import re

# 1.findall方法，返回匹配的结果列表
# rs = re.findall('\d',"hao13ran24")
# print(rs) #['1','3','2','4']

# 2.findall方法，flag参数的作用
# rs = re.findall('a.bc','a\nbc',re.DOTALL)
# print(rs) # ['a\nbc']
# 原本.不能匹配\n，但是加入匹配模式DOTALL就可以了

# 3.findall中分组的使用（括号的使用）
# rs = re.findall('a.+bc','a\nbc',re.DOTALL)
# print(rs) # ['a\nbc']
# rs = re.findall('a(.+)bc','a\nbc',re.DOTALL)
# print(rs)# ['\n']
# 当正则表达式中有分组时，只查找括号内匹配的内容，括号两边是用来定位的，即“只找a之后，bc之前的内容”

# 4.正则中r原串的使用
# 在不使用r原串的时候，遇到转义符怎么做
rs = re.findall('a\nbc','a\nbc')
print(rs)  #['a\nbc']
rs = re.findall('a\\nbc','a\\nbc')
                # 想要匹配字符\，n只是一个普通字符
print(rs)   #[],并不能匹配上
#当时用r原串时
rs = re.findall(r'a\\nbc','a\\nbc')
print(rs)   #['a\\nbc'],匹配成功，r原串可以消除转义字符带来的影响
rs = re.findall(r'a\nbc','a\nbc')
print(rs)   #['a\nbc'],匹配成功，说明r原串对转义


#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time : 2021/3/25 17:26
import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm
class CoronaVirusSpider(object):
    def __init__ (self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    #1.获取首页内容
    #1.1发送请求，获取响应
    def get_content_from_url(self,url):
        """
        根据URL，获取相应内容的字符串数据
        :param url: 请求的url
        :return: 返回相应内容的字符串
        """
        response = requests.get(url)
        return response.content.decode()

    def parse_home_page(self,home_page):
        """
        解析首页内容，获取解析后的python数据
        :param home_page: 首页的内容
        :return: 解析后的python数据
        """
        #解析
        soup = BeautifulSoup(home_page,'lxml')
        #提取
        script = soup.find(id = 'getListByCountryTypeService2true')
        countries_text = script.string
        #找到json字符串段
        json_str = re.findall((r'(\[.*\])'),countries_text)[0]
        #转化为python类型
        corona_virus_data = json.loads(json_str)
        return corona_virus_data

    def save(self,data,path):
        #以json格式保存
        with open (path,'w',encoding='utf8') as fp:
            json.dump(data,fp,ensure_ascii=False)
    def crawl_last_day_corona_virus(self):
        """
        采集最近一天的各国疫情信息
        :return:
        """
        #1.发送请求，获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        #2.解析首页内容，获取最近一天的各国疫情数据
        last_day_corona_virus = self.parse_home_page(home_page)
        #3.保存数据
        self.save(last_day_corona_virus,'D:\Pycharm\workspace\Covid19 Visualization\\last_day_corona_virus.json')
    def crawl_corona_virus(self):
        """
        采集从1月23号以来各国疫情数据
        :return:
        """
        #1加载各国疫情数据
        with open('D:\Pycharm\workspace\Covid19 Visualization\\last_day_corona_virus.json',encoding='utf-8') as fp:
            last_day_corona_virus = json.load(fp)
        #print(last_day_corona_virus)
        #2遍历各国疫情数据
        #定义列表，用于存储各国从1月23日以来的json数据
        corona_virus_list = []
        for country in tqdm(last_day_corona_virus,'下载进度'):#tqdm库可以在run的时候显示for循环的进度
            #3.发送请求，获取各国从1月23号至今的json数据
            statistics_data_url = country['statisticsData']#这是一串串的url，定位到各国23号以来的所有数据
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            #4.把json数据转换为python类型的数据，添加到列表中
            statistics_data = json.loads(statistics_data_json_str)['data']
            #print(statistics_data)
            for one_day in statistics_data:#再遍历一遍各国每一天的数据，添加上国名和缩写，因为原来并不显示国名
                one_day['provinceName'] = country['provinceName']
                one_day['countryShortCode'] = country['countryShortCode']
            #print(statistics_data)
            #将各元素（某一国所有天的数据）放到列表里去
            corona_virus_list.extend(statistics_data)
            corona_virus_list.extend(statistics_data)
            #5.把列表以json格式保存为文件
            self.save(corona_virus_list,'D:\Pycharm\workspace\Covid19 Visualization\\corona_virus.json')
    def run(self):
        #self.crawl_last_day_corona_virus()
        self.crawl_corona_virus()
if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()

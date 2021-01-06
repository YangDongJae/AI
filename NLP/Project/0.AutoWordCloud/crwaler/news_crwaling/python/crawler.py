from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml.html
from selenium import webdriver
import re
import numpy as np


class crwaler_daum:
    def __init__(self):
        self.title = []
        self.body = []
        self.date = []
        self.newsrooms = []
        self.page = input('데이터를 얻고자하는 페이지 수를 입력하시오.')
        self.df = None
    
    def set_df(self,df):
        self.df = df
        
    def get_df(self):
        return self.df
        
        
    def get_date(self):
        return self.date
    
    def get_newsrooms(self):
        return self.newsrooms
    
    def get_title(self):
        return self.title
    
    def set_title(self , title):
        self.title.append(title)
        
    def get_body(self):
        return self.body

    def set_body(self , body):
        self.body.append(body)
    
    def crwaling_title(self):
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crwaler/news_crawling/chromedriver.exe')
        url = 'https://search.daum.net/search?w=news&req=tab&q=%EB%B3%B4%EA%B1%B4%EB%B3%B5%EC%A7%80%EB%B6%80&cluster=n&viewio=i&repno=0&n=10&p=1&pattern_yn=n&DA=PGD'
        response = requests.get(url , verify = False)
        root = lxml.html.fromstring(response.content)

        
        for i in range(int(self.page)):
            url = 'https://search.daum.net/search?w=news&req=tab&q=%EB%B3%B4%EA%B1%B4%EB%B3%B5%EC%A7%80%EB%B6%80&cluster=n&viewio=i&repno=0&n=10&p={}&pattern_yn=n&DA=PGD'.format(i + 1)
            response = requests.get(url , verify = False)
            root = lxml.html.fromstring(response.content)
            
            for j in range (10):
                # print(root.xpath('//*[@id="newsResultUL"]/li[{}]/div/div/div/a'.format(j + 1))[0].text_content())
                self.title.append(root.xpath('//*[@id="newsResultUL"]/li[{}]/div/div/div/a'.format(j + 1))[0].text_content())

        return self.get_title()
    
    def crwaling_body(self):
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crwaler/news_crawling/chromedriver.exe')
        url = 'https://search.daum.net/search?w=news&req=tab&q=%EB%B3%B4%EA%B1%B4%EB%B3%B5%EC%A7%80%EB%B6%80&cluster=n&viewio=i&repno=0&n=10&p=1&pattern_yn=n&DA=PGD'
        response = requests.get(url , verify = False)
        root = lxml.html.fromstring(response.content)

        
        for i in range(int(self.page)):
            url = 'https://search.daum.net/search?w=news&req=tab&q=%EB%B3%B4%EA%B1%B4%EB%B3%B5%EC%A7%80%EB%B6%80&cluster=n&viewio=i&repno=0&n=10&p={}&pattern_yn=n&DA=PGD'.format(i + 1)
            response = requests.get(url , verify = False)
            root = lxml.html.fromstring(response.content)
            
            for j in range (10):
                #print(root.xpath('//*[@id="newsResultUL"]/li[{}]/div/div/p'.format(j + 1))[0].text_content())
                self.body.append(root.xpath('//*[@id="newsResultUL"]/li[{}]/div/div/p'.format(j + 1))[0].text_content())
        
        return self.get_body()
            
    def crwaling_date(self):
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crwaler/news_crawling/chromedriver.exe')
        url = 'https://search.daum.net/search?w=news&req=tab&q=%EB%B3%B4%EA%B1%B4%EB%B3%B5%EC%A7%80%EB%B6%80&cluster=n&viewio=i&repno=0&n=10&p=1&pattern_yn=n&DA=PGD'
        response = requests.get(url , verify = False)
        root = lxml.html.fromstring(response.content)

        
        for i in range(int(self.page)):
            url = 'https://search.daum.net/search?w=news&req=tab&q=%EB%B3%B4%EA%B1%B4%EB%B3%B5%EC%A7%80%EB%B6%80&cluster=n&viewio=i&repno=0&n=10&p={}&pattern_yn=n&DA=PGD'.format(i + 1)
            response = requests.get(url , verify = False)
            root = lxml.html.fromstring(response.content)
            
            for j in range (10):
                self.date.append(root.xpath('//*[@id="newsResultUL"]/li[{}]/div[2]/div/span[1]/text()[1]'.format(j + 1)))
                # print(root.xpath('//*[@id="newsResultUL"]/li[{}]/div[2]/div/span[1]/text()[1]'.format(j + 1)))
            
        return self.get_date()

        
    def crwaling_newsroom(self):
        
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crwaler/news_crawling/chromedriver.exe')
        url = 'https://search.daum.net/search?w=news&req=tab&q=%EB%B3%B4%EA%B1%B4%EB%B3%B5%EC%A7%80%EB%B6%80&cluster=n&viewio=i&repno=0&n=10&p=1&pattern_yn=n&DA=PGD'
        response = requests.get(url , verify = False)
        root = lxml.html.fromstring(response.content)

        
        for i in range(int(self.page)):
            url = 'https://search.daum.net/search?w=news&req=tab&q=%EB%B3%B4%EA%B1%B4%EB%B3%B5%EC%A7%80%EB%B6%80&cluster=n&viewio=i&repno=0&n=10&p={}&pattern_yn=n&DA=PGD'.format(i + 1)
            response = requests.get(url , verify = False)
            root = lxml.html.fromstring(response.content)
            
            for j in range (10):
                #print(root.xpath('//*[@id="newsResultUL"]/li[{}]/div[2]/div/span[1]/text()[2]'.format(j + 1)))
                self.newsrooms.append(root.xpath('//*[@id="newsResultUL"]/li[{}]/div[2]/div/span[1]/text()[2]'.format(j + 1)))
    
        return self.get_newsrooms()
        
    def run_crwaling(self):
        self.crwaling_title()
        self.crwaling_body()
        self.crwaling_date()
        self.crwaling_newsroom()
        
    def make_dataframe(self):
        df_title = pd.DataFrame({'title' : self.get_title()})
        df_body = pd.DataFrame({'body' : self.get_body()})
        df_date = pd.DataFrame(self.get_date())
        df_news = pd.DataFrame(self.get_newsrooms())
        
        df = pd.concat([df_title , df_body , df_date , df_news],axis = 1 )
        
        df.columns = ['title','body','date','news']
        

        return df
    
    def drop_null(self):
        self.run_crwaling()
        df = self.make_dataframe()

        
        for i in range (len(df['date'])):
            if df['date'][i] is None:
                print(df['date'][i])
                df.drop([i] , axis = 0 , inplace = True)
                
        return df



# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:47:57 2020
@author: Mohw-IN
"""

from selenium import webdriver
import lxml.html
import requests
import pandas as pd   


class CrwalerDaum: 
    def __init__(self):
        self.title = []
        self.body = []
        self.date = []
        self.newsrooms = []
        self.page = None
        self.df = None
        self.keyword = None
        self.url = None
        #self.chrome_driver = input('chrome driver를 설치한 후 경로를 입력하시오.')

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
        
    def get_page(self):
        return self.page
    
    def set_page(self , page):
        self.page = page
        
    def get_keyword(self):
        return self.keyword
    
    def set_url(self , url):
        self.url = url
        
    def get_url(self):
        return self.url
    
    def set_keyword(self , keyword):
        self.keyword = keyword
    
    def crwaling_title(self):
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crawling_software/crwaler/news_crwaling/chromedriver.exe')
        
        url = self.url
        
        response = requests.get(url , verify = False)
        root = lxml.html.fromstring(response.content)

        for i in range(int(self.get_page())):
            
            url = self.url.format(i)
            
            response = requests.get(url , verify = False)
            root = lxml.html.fromstring(response.content)
            
            for j in range (10):
                print(root.xpath('//*[@id="newsResultUL"]/li[{}]/div/div/div/a'.format(j + 1))[0].text_content())
                self.title.append(root.xpath('//*[@id="newsResultUL"]/li[{}]/div/div/div/a'.format(j + 1))[0].text_content())
                
        chrome_driver.quit()

        return self.get_title()
    
    def crwaling_body(self):
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crawling_software/crwaler/news_crwaling/chromedriver.exe')
        
        url = self.url  

        response = requests.get(url , verify = False)
        root = lxml.html.fromstring(response.content)

        
        for i in range(int(self.get_page())):
            
            url = self.url.format(i)
            
            response = requests.get(url , verify = False)
            root = lxml.html.fromstring(response.content)
            
            for j in range (10):
                print(root.xpath('//*[@id="newsResultUL"]/li[{}]/div/div/p'.format(j + 1))[0].text_content())
                self.body.append(root.xpath('//*[@id="newsResultUL"]/li[{}]/div/div/p'.format(j + 1))[0].text_content())
                
            print('\n')
        
        chrome_driver.quit()
        
        return self.get_body()
            
    def crwaling_date(self):
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crawling_software/crwaler/news_crwaling/chromedriver.exe')
        
        url = self.url

        response = requests.get(url , verify = False)
        root = lxml.html.fromstring(response.content)
       
        for i in range(int(self.get_page())):
            
            url = self.url.format(i)
            
            response = requests.get(url , verify = False)
            root = lxml.html.fromstring(response.content)
            
            for j in range (10):
                self.date.append(root.xpath('//*[@id="newsResultUL"]/li[{}]/div[2]/div/span[1]/text()[1]'.format(j + 1)))
                print(root.xpath('//*[@id="newsResultUL"]/li[{}]/div[2]/div/span[1]/text()[1]'.format(j + 1)))
            print('\n')
            
        chrome_driver.quit()            
            
        return self.get_date()

        
    def crwaling_newsroom(self):
        
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crawling_software/crwaler/news_crwaling/chromedriver.exe')
        
        url = self.url
        
        response = requests.get(url , verify = False)
        root = lxml.html.fromstring(response.content)
        
        for i in range(int(self.get_page())):
            
            url = self.url.format(i)
            response = requests.get(url , verify = False)
            root = lxml.html.fromstring(response.content)
            
            for j in range (10):
                print(root.xpath('//*[@id="newsResultUL"]/li[{}]/div[2]/div/span[1]/text()[2]'.format(j + 1)))
                self.newsrooms.append(root.xpath('//*[@id="newsResultUL"]/li[{}]/div[2]/div/span[1]/text()[2]'.format(j + 1)))
                
        chrome_driver.quit()        
        
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
        page = input('페이지')
        keyword = input('keyword')
        self.set_page(page)
        self.set_keyword(keyword)
        self.set_url('https://search.daum.net/search?w=news&req=tab&q=' + self.get_keyword() + '&cluster=n&viewio=i&repno=0&n=10&p={}&pattern_yn=n&DA=PGD')
        self.run_crwaling()
        df = self.make_dataframe()
        df.to_csv('data.csv' , encoding = 'utf-8')
        

        
        for i in range (len(df['date'])):
            if df['date'][i] is None:
                print(df['date'][i])
                df.drop([i] , axis = 0 , inplace = True)
                
        df = df.drop_duplicates(['title','body','date','news'] , keep = 'first')
                
        return df
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import lxml.html
import pandas as pd   

class HealthWelfareCrwaler:
    def __init__(self):
        self.title = []
        self.df = None
        self.url = 'https://www.mohw.go.kr/react/al/sal0301ls.jsp?PAR_MENU_ID=04&MENU_ID=0403&BOARD_ID=140&page={}'
        
    def set_title(self, title):
        self.title.append(title)
        
    def get_title(self):
        return self.title
    
    def get_url(self):
        return self.url
    
    def crawling_title(self, page):
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crawling_software/news_crawling/chromedriver.exe')

        response = requests.get(self.get_url() , verify = False)
        root = lxml.html.fromstring(response.content)
        
        for i in range(1, page):
            url = self.get_url().format(i)
            response = requests.get(url , verify = False)
            root = lxml.html.fromstring(response.content, parser = lxml.html.HTMLParser(encoding = 'utf-8'))
            
            for j in range(1,15):
                self.set_title((root.xpath('//*[@id="sub_content"]/div[2]/table/tbody/tr[{}]/td[2]/a/text()'.format(j))[0]))
                
        chrome_driver.quit()
                
        return self.get_title()
    
    def make_dataframe(self,data):
        df = pd.DataFrame(data)
        
        return df


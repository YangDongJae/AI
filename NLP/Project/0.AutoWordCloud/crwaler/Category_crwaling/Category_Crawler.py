# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 17:23:03 2020
@author: Mohw-IN
"""
import ControlCrawler
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import timedelta
import re

remote = ControlCrawler.ControlCrawler()

class NaverNewsCategory:
    def __init__(self):
        self.date = datetime.datetime.today().strftime('%Y%m%d')
        
    def get_date(self):
        return self.date
    
    def down_date(self):
        """
        Returns
        -------
        TYPE : string
            Date -1 : Last Day
        """
    
        date = datetime.datetime.today() - timedelta(days = 1)
        self.date = date.strftime('%Y%m%d')
        
        return self.date
    
    def down_date_set(self,start_date):
        """
        

        Parameters
        ----------
        start_date : date.time
            date tie using datetime package

        Returns
        -------
        string
            YYYYMMDD

        """
        date = start_date - timedelta(days = 1)
        
        return date
            
    
    def get_url_list(self,main_category_num,middle_category_num,date,page):
        """
        
        category number \n
        main_category : 100. Politics 101. Economic 102. Society 103.Life/Culture 104.world 105.IT/Science\n
        middle_category : \n
            100 : Politics\n
                264 : 청와대\n
                265 : 국회/정당\n
                268 : 북한\n
                266 : 행정\n
                267 :국방 / 외교\n
                269 : 정치 일반\n
            101 : Economic\n
                259 : 금융\n
                258 : 증권\n
                261 : 산업 / 재계\n
                771 : 중기/벤처\n
                260 : 부동산\n
                262 : 글로벌 경제\n
                310 : 생활경제\n
                263 : 경제일반\n
            102 : Society\n
                249 : 사건사고\n
                250 : 교육\n
                251 : 노동\n
                254 : 언론\n
                252 : 환경\n
                59b : 인권/복지\n
                255 : 식품 / 의료\n
                256 : 지역\n
                276 : 인물\n
                257 : 사회 일반\n
            103 : Life & Culture\n
                241 : 건강정보\n
                239 : 자동차/시승기\n
                240 : 도로 / 교통\n
                237 : 여행 / 레저\n
                238 : 음식 / 맛집\n
                376 : 패션 / 뷰티\n
                242 : 공연 / 전시\n
                243 : 책\n
                244 : 종교\n
                248 : 날씨\n
                245 : 생활문화 일반\n
            104 : World\n
                232 : 미국 / 중남미\n
                233 : 유럽\n
                234 : 중동 / 아프리카\n
                322 : 세계 일반\n
            105 : IT / Science\n
                731 : 모바일\n
                226 : 인터넷\n
                227 : 통신/뉴미디어\n
                230 : IT 일반\n
                732 : 보안 / 해킹\n
                283 : 컴퓨터\n
                229 : 게임 / 리뷰\n
                228 : 과학 일반\n
        date : YYYYMMDD \n
        page : int\n
        """       
        url_list = []
        news = []
        max_page = None
        # setting web driver to get object
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crawling_software/crwaler/news_crwaling/chromedriver.exe')
        url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1={}&sid2={}&date={}&page={}'\
                .format(main_category_num , middle_category_num , date , page)
        chrome_driver.get(url)
        html = chrome_driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        #get max page
        check_next = re.findall(r'\d+' , soup.find('div',{'paging'}).get_text())
        check_next = list(map(int , check_next))
        
        max_page = max(check_next)
        
        if max_page % 10 != 0:
            max_page = max(check_next)
            
        #get next button           
        next_button = soup.find('a',{'class':'next nclicks(fls.page)'})
        if next_button:
            res_next = True
        elif not next_button:
            res_next = False
        
        #get newsroom
        html_newsroom = soup.find('div',{'class':'list_body newsflash_body'})
        news_room = html_newsroom.find_all('span',{'class':'writing'})
        
        for b in range(len(news_room)):
            news.append(news_room[b].get_text())
            
        # get aritcle url
        html_url = soup.find('div',{'class':'list_body newsflash_body'})
        for a in html_url.find_all('a', href = True):
            url_list.append((a['href']))

        chrome_driver.quit()

        return list(dict.fromkeys(url_list)), news , max_page , res_next
    
    def crawling_article(self,url):
        """
        
        Parameters
        ----------
            url : (list) Article URL to get data. \n
            
        Returns : 
        ----------
            (list) title , date , article data
            
        """
        chrome_driver = webdriver.Chrome('D:/바탕 화면/인턴/python/crawling_software/crwaler/news_crwaling/chromedriver.exe')
        chrome_driver.get(url)
        html = chrome_driver.page_source
        soup = BeautifulSoup(html , 'html.parser')
        
        title = soup.find('div',{'class':'article_info'}).find('h3',{'id':'articleTitle'}).get_text()
        date = soup.find('div', {'class':'article_info'}).find('span',{'class':'t11'}).get_text()
        article = soup.find('div',{'id':'articleBodyContents'}).text

        chrome_driver.quit()

        return title , date , article

        #add .text behind article line ^^

    def run_category_service(self, main_category, middle_category , count):
        """
        
        Parameters
        -------------------------------
            main_category : (list) main_category code numbers which user selected \n
            middle_category : (list) middle_category conde number which user selected \n
            count : (int) the number of user want parsing count. and parsing data is page * 20
                
        Returns
        -------------------------------
            (list) parsing news title, newsroom , date , article
            
        """

        url = []
        news_room = []
        
        title = []
        date = []     
        article = []
        main_value = []
        middle_value = []

        
        if count % 20 != 0:
            page = count // 20 + 1
        
        else:
            page = count // 20
    
        
        for main in range (len(main_category)):
            for middle in middle_category[main]:
                for page_count in range (1, page + 1):
                    print("MAIN CODE : " , main_category[main],"  SUB CODE : ", middle ,"의",page_count,"번째 페이지 기사 URL 들을 가져오는 중 입니다." )
                    url_value , news_room_value , max_page , res_next = self.get_url_list(main_category[main] , middle , self.get_date() , page_count)
                    url.append(url_value)
                    news_room.append(news_room_value)
                    
                    if len(url) < 20:
                        self.down_date()
                        page = 1
                
                for parsing_count in range (count):
                    print("------------------------")
                    counter = 1                                
                    try:
                        for stuff_url in url[parsing_count]:
                            print(counter, "번째 기사의 데이터를 수집 중 입니다.")
                            p_title , p_date , p_article = self.crawling_article(stuff_url)
                            title.append(p_title)
                            date.append(p_date)
                            article.append(p_article)
                            main_value.append(main_category[main])
                            middle_value.append(middle)
                            counter += 1
                    except IndexError:
                        break
            
        return title, news_room , date , article , main_value , middle_value

    def run_date_service(self, main_category , middle_category):
        """
        
        Parameters
        ----------
        main_category : List
            main_category code numbers which user selected.
        middle_category : List
            middle_category conde number which user selected.
        count : Int
            the number of user want parsing count. and parsing data is page * 20.
        strat_date : String
            YYYY
            M or MM
            D or DD
        end_date : String
            YYYY
            M or MM
            D or DD
        Returns
        -------
        title , news_room , date , article
        """
        
        count , end_date = remote.subtraction_date()        
        url = []
        news_room = []
        
        title = []
        date = []     
        article = []
        main_value = []
        middle_value = []

        for main in range (len(main_category)):
            for middle in middle_category[main]:
                for date_count in range (count + 1):
                    page = 1
                    
                    while True:
                        #print("---------\n",page,"---------\n")
                        print("MAIN CODE : " , main_category[main],"  SUB CODE : ", middle ,"의",end_date.strftime('%Y%m%d'),"날짜",page,"번째 페이지 기사 URL 들을 가져오는 중 입니다." )
                        
                        url_value , news_room_value,max_page,check_next = self.get_url_list(main_category[main] , middle , end_date.strftime('%Y%m%d') , page)
                        url.append(url_value)                       
                        news_room.append(news_room_value)
                        

                        if check_next is False:
                            for i in range (1 , max_page % 10):
                                print("MAIN CODE : " , main_category[main],"  SUB CODE : ", middle ,"의",end_date.strftime('%Y%m%d'),"날짜",page + i,"번째 페이지 기사 URL 들을 가져오는 중 입니다." )
                                
                                url_value , news_room_value,max_page,check_next = self.get_url_list(main_category[main] , middle , end_date.strftime('%Y%m%d') , page + i)
                                url.append(url_value)                       
                                news_room.append(news_room_value)
                                
                            break          
                        page += 1
                    end_date = self.down_date_set(end_date)

        for parsing_count in range (count + 1):
            print("------------------------")
            counter = 1                                
            try:
                for stuff_url in url[parsing_count]:
                    print(counter, "번째 기사의 데이터를 수집 중 입니다.")
                    p_title , p_date , p_article = self.crawling_article(stuff_url)
                    title.append(p_title)
                    date.append(p_date)
                    article.append(p_article)
                    main_value.append(main_category[main])
                    middle_value.append(middle)
                    counter += 1
            except IndexError:
                break                    
                        

        return title, news_room , date , article , main_value , middle_value
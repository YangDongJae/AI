import datetime
from datetime import timedelta
from datetime import date

class ControlCrawler:
    def to_oneArray_list(self, two_array_list):
        """

        Parameters
        ----------            
            two_array_list : (list) Two array List
        
        Return 
        ----------            
            (list) One Array List convert list from parameter

        """
        return_list = sum(two_array_list, [])
        
        return return_list

    def get_middle_list(self , main_category_code):
        """
        
        Parameters
        ----------
        main_category_code : (int)List
            Main Category Number "100","101","102","103","104","105"

        Returns
        -------
        list : sub contents code number
        list : the number which user's choose category


        """
        if main_category_code == "100":
            middle_value_category = []
            True_value = ["264","265","268","266","267","269"]
            print("                264 : 청와대\n                265 : 국회/정당\n                268 : 북한\n                266 : 행정\n                267 : 국방 / 외교\n                269 : 정치 일반\n")
            middle_value_category.append(input("데이터를 수집할 중 분류 카테고리를 , 로 구분하여 다중 선택하십시오").split(','))
            
            return True_value , middle_value_category
        
        elif main_category_code == "101":
            middle_value_category = []
            True_value = ["259","258","261","771","260","262","310","263"]
            print("                259 : 금융\n                258 : 증권\n                261 : 산업 / 재계\n                771 : 중기/벤처\n                260 : 부동산\n                262 : 글로벌 경제\n                310 : 생활경제\n                263 : 경제일반\n")
            middle_value_category.append(input("데이터를 수집할 중 분류 카테고리를 , 로 구분하여 다중 선택하십시오").split(','))
            
            return True_value , middle_value_category
        
        elif main_category_code == "102":
            middle_value_category = []
            True_value = ["249","250","251","254","252","59b","255","256","276","257"]
            print("                249 : 사건사고\n                250 : 교육\n                251 : 노동\n                254 : 언론\n                252 : 환경\n                59b : 인권/복지\n                255 : 식품 / 의료\n                256 : 지역\n                276 : 인물\n                257 : 사회 일반\n")
            middle_value_category.append(input("데이터를 수집할 중 분류 카테고리를 , 로 구분하여 다중 선택하십시오").split(','))
            
            return True_value , middle_value_category
            
        elif main_category_code == "103":
            middle_value_category = []
            True_value = ["241","239","240","237","238","376","242","243","244","248","245"]
            print("                241 : 건강정보\n                239 : 자동차/시승기\n                240 : 도로 / 교통\n                237 : 여행 / 레저\n                238 : 음식 / 맛집\n                376 : 패션 / 뷰티\n                242 : 공연 / 전시\n                243 : 책\n                244 : 종교\n                248 : 날씨\n                245 : 생활문화 일반\n")
            middle_value_category.append(input("데이터를 수집할 중 분류 카테고리를 , 로 구분하여 다중 선택하십시오").split(','))
            
            return True_value , middle_value_category
            
        elif main_category_code == "104":
            middle_value_category = []
            True_value = ["232","233","234","322"]
            print("                232 : 미국 / 중남미\n                233 : 유럽\n                234 : 중동 / 아프리카\n                322 : 세계 일반\n")
            middle_value_category.append(input("데이터를 수집할 중 분류 카테고리를 , 로 구분하여 다중 선택하십시오").split(','))
            
            return True_value , middle_value_category
            
        elif main_category_code == "105":
            middle_value_category = []
            True_value = ["731","226","227","230","732","283","229","228"]
            print("                731 : 모바일\n                226 : 인터넷\n                227 : 통신/뉴미디어\n                230 : IT 일반\n                732 : 보안 / 해킹\n                283 : 컴퓨터\n                229 : 게임 / 리뷰\n                228 : 과학 일반\n")
            middle_value_category.append(input("데이터를 수집할 중 분류 카테고리를 , 로 구분하여 다중 선택하십시오").split(','))
            
            return True_value , middle_value_category
        
    def subtraction_date(self):
        start_year , start_month , start_days = map(int, input("데이터 수집을 시작 날짜를 아래의 형식으로 입력하여 주십시오 \n \t 2020,10,12 \n").split(','))
        end_year , end_month , end_days = map(int, input("데이터 수집을 종료할 날짜를 아래의 형식으로 입력하여 주십시오 \n \t 2020,10,21\n").split(','))
        
        start_date = date(start_year , start_month , start_days)
        end_date = date(end_year , end_month , end_days)
        
        delta = end_date - start_date
      
        return delta.days , end_date
        

import Category_Crawler
import ControlCrawler
import pandas as pd


crawler = Category_Crawler.NaverNewsCategory()
remote = ControlCrawler.ControlCrawler()

sorry = "잘못된 값을 입력하셨습니다. 다시 입력하여 주십시오"


count = 0
while True:
    select_service = input(
        "원하고자 하는 서비스의 유형을 선택하십시오.\n"
        "1. 카테고리별 데이터 수집하기\n"
        "2. 날짜별 데이터 수집하기\n"
        "3. 전체 데이터 수집하기\n"
        "4. 종료 \n"
    )
    try:
        if select_service == '4':
            break
        
        elif int(select_service) <= 0 or int(select_service) > 4:
            print(sorry)
        
        else:
            select_service = int(select_service)
            if select_service == 1:
                main_count = 0
                while True:
                    if main_count < 4:
                        middle_category = []
                        main_category = []
                        True_value = ["100","101","102","103","104","105","0"]
                        breaker = []
                        print("---------------")
                        print("100. 정치 \n")
                        print("101. 경제 \n")
                        print("102. 사회 \n")
                        print("103. 생활/문화 \n")
                        print("104. 세계 \n")
                        print("105. IT/과학 \n")
                        print("0. 뒤로가기")
                        print("---------------")
    
                        main_category.append(input('데이터를 수집할 대 분류 카테고리를 , 로 구분하여 다중 선택하십시오\n').split(','))
                        main_category = remote.to_oneArray_list(main_category)
                        
                        if "0" in main_category:
                            break                        
                        
                        for main_value in main_category:
                            if main_value not in True_value:
                                breaker.append("False")
                                
                        if len(breaker) == 0:                       
                            for main_category_element in main_category:
                                if "100" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("100")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
                                                
                                                      
                                            
                                elif "101" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("101")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
            
                                elif "102" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("102")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
                                    
                                elif "103" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("103")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
            
                                elif "104" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("104")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
            
                                elif "105" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("105")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
                                else:
                                    main_count += 1
                                    if main_count == 3:
                                        print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                        break
                                    print(sorry, "," , main_count ,"회 오류")
                            
                            count = eval(input("수집하고자 하는 기사의 개수를 입력하여 주십시오."))
                            title , news_room , date , article , main , middle = crawler.run_category_service(main_category,middle_category,count)
                            
                            remote_service = input("수집한 데이터를 CSV 파일로 생성할까요?\n 파일 생성을 원할 시 create라고 입력하십시오 \n")
                            
                            if remote_service == 'create':
                                df = pd.DataFrame({'Title':title,
                                                   'date' : date,
                                                   'article' : article,
                                                   'main_code' : main,
                                                   'middle_code': middle})  
 
                                df.to_csv('news_crawling_data.csv')
                        
                        break
                    break

            elif select_service == 2:
                main_count = 0
                while True:
                    if main_count < 4:
                        middle_category = []
                        main_category = []
                        True_value = ["100","101","102","103","104","105","0"]
                        breaker = []
                        print("---------------")
                        print("100. 정치 \n")
                        print("101. 경제 \n")
                        print("102. 사회 \n")
                        print("103. 생활/문화 \n")
                        print("104. 세계 \n")
                        print("105. IT/과학 \n")
                        print("0. 뒤로가기")
                        print("---------------")
    
                        main_category.append(input('데이터를 수집할 대 분류 카테고리를 , 로 구분하여 다중 선택하십시오\n').split(','))
                        main_category = remote.to_oneArray_list(main_category)
                        
                        if "0" in main_category:
                            break                        
                        
                        for main_value in main_category:
                            if main_value not in True_value:
                                breaker.append("False")
                                
                        if len(breaker) == 0:                       
                            for main_category_element in main_category:
                                if "100" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("100")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
                                                
                                                      
                                            
                                elif "101" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("101")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
            
                                elif "102" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("102")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
                                    
                                elif "103" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("103")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
            
                                elif "104" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("104")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
            
                                elif "105" == main_category_element:
                                    middle_count = 0                                                 
                                    while True:
                                        breaker = []
                                        if middle_count < 4:
                                            middle_True_value , middle_value_list = remote.get_middle_list("105")
                                            middle_value_list = remote.to_oneArray_list(middle_value_list)
                                            
                                            for middle_value in middle_value_list:                                               
                                                if middle_value not in middle_True_value:
                                                    breaker.append("False")
                                            
                                            if len(breaker) == 0:
                                                middle_category.append(middle_value_list)
                                                break
                                            else:
                                                middle_count += 1
                                                if middle_count == 3:
                                                    print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                                    break
                                                print(sorry, "," , middle_count ,"회 오류")
                                else:
                                    main_count += 1
                                    if main_count == 3:
                                        print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                                        break
                                    print(sorry, "," , main_count ,"회 오류")
                            

                            title , news_room , date , article , main , middle = crawler.run_date_service(main_category,middle_category)
                            
                            remote_service = input("수집한 데이터를 CSV 파일로 생성할까요?\n 파일 생성을 원할 시 create라고 입력하십시오 \n")
                            
                            if remote_service == 'create':
                                df = pd.DataFrame({'Title':title,
                                                   'date' : date,
                                                   'article' : article}) 
                                df.to_csv('news_crawling_data.csv')
                                
                        break
                    break
                
            elif select_service == 3:
                main_category = ['100','101','102','103','104','105']
                middle_category = [['264','265','268','266','267','269'],
                                   ['259','258','261','771','260','262','310','263'],
                                   ['249','250','251','254','252','59b','255','256','276','257'],
                                   ['241','239','240','237','238','376','242','243','244','248','245'],
                                   ['232','233','234','322'],
                                   ['731','226','227','230','732','283','229','228']]
                
                service = input("1. 원하는 페이지 양만큼 데이터 수집하기 \n2. 날짜별로 데이터 수집하기\n")
                
                if service == "1":
                    count = eval(input("수집하고자 하는 기사의 개수를 입력하여 주십시오."))
                    title , news_room , date , article , main , middle = crawler.run_category_service(main_category,middle_category,count)                    
                
                    remote_service = input("수집한 데이터를 CSV 파일로 생성할까요?\n 파일 생성을 원할 시 create라고 입력하십시오 \n")
                    
                    if remote_service == 'create':
                        df = pd.DataFrame({'Title':title,
                                           'date' : date,
                                           'article' : article,
                                           'main_code' : main,
                                           'middle_code': middle})  
 
                        df.to_csv('news_crawling_data.csv')
                        
                elif service == "2":
                    title , news_room , date , article , main , middle = crawler.run_date_service(main_category,middle_category)
                    
                    remote_service = input("수집한 데이터를 CSV 파일로 생성할까요?\n 파일 생성을 원할 시 create라고 입력하십시오 \n")
                    
                    if remote_service == 'create':
                        df = pd.DataFrame({'Title':title,
                                           'date' : date,
                                           'article' : article}) 
                        df.to_csv('news_crawling_data.csv')                    
            
                    
                else:
                    main_count += 1
                    if main_count == 3:
                        print("입력 3회 오류로 인하여 서비스를 종료합니다.")
                        break
                    print(sorry, "," , main_count ,"회 오류")                    
                
            elif select_service == 4:
                break                
        
    except ValueError:
        print("!!! WARING !!!" , sorry)
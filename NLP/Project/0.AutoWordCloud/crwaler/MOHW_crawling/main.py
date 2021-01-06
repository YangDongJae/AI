# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:05:31 2020
@author: Mohw-IN
"""
import pandas as pd
import MakeWordCloud
import MorphologicalAnalysis
import CrawlingLabelData
crwaler = CrawlingLabelData.HealthWelfareCrwaler()
tagger = MorphologicalAnalysis.MorphologicalAnalysis()
w_cloud = MakeWordCloud.MakeWordColud()
    
    
def main():
    
    while True:
        data = input('\n what do you want on our service? \n 1. Extract Noun \n 2. Extracnt Morphological analysis \n 3. noun Frequency analysis \n 4. make wordcloud with noun \n 5. to csv \n 6. quit \n please enter the number \n')
        

             
        if data == '1' or data == '2' or data == '3' or data == '4' or data == '5':
            page = input(' how many do you want for get data?')
            stuff = crwaler.crawling_title(int(page))
            print(stuff)
            print(choice_service(data , stuff ))
                    
        elif data == '6':
            print('-------------------')
            break
                
        else:
            print('-----------------------\n please check your input number \n -----------------------')            
      
            
def choice_service(num,data):
    if num == '1':
        return tagger.extract_nouns(tagger.contents_fillter(data))
    
    elif num == '2':
        return tagger.morphological_analysis(tagger.contents_fillter(data))
        
    elif num == '3':
        return tagger.count_morphological(tagger.extract_nouns(tagger.contents_fillter(data)))
            
        
    elif num == '4':
        wc_data = tagger.count_morphological(tagger.extract_nouns(tagger.contents_fillter(data)))
        w_cloud.set_cloud()
        return w_cloud.make_cloud(wc_data)        
    
    elif num == '5':
        df = crwaler.make_dataframe(tagger.contents_fillter(data))
        df.to_csv('welfare&health.csv')
        
        
    
main()
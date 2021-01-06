import MakeWordCloud
import MorphologicalAnalysis
import CrwalingDaum
crwaler = CrwalingDaum.CrwalerDaum()
tagger = MorphologicalAnalysis.MorphologicalAnalysis()
w_cloud = MakeWordCloud.MakeWordColud()
    
    
def main():
    while True:
        data_1 = input('Please refer to the example and enter the number to use service. \n 1. use title \n 2. use article \n 3. Exit \n')    
        if data_1 == '1' or data_1 == '2':
            df = crwaler.drop_null()
            df
            stuff = choice_data(data_1)
            
            while True:
                data = input('\n what do you want on our service? \n 1. Extract Noun \n 2. Extracnt Morphological analysis \n 3. noun Frequency analysis \n 4. make wordcloud with noun \n 5. to csv \n  6. quit \n please enter the number \n')
                
                if data == '1' or data == '2' or data == '3' or data == '4':
                    print(choice_service(data , stuff ))
                    
                elif data == '5':
                    if data_1 == '1':
                        df = df['title']
                        df.to_csv('data_title.csv')
                    
                    elif data_1 =='2':
                        df = df['body']
                        df.to_csv('data_body.csv')
                    
                elif data == '6':
                    print('-------------------')
                    break
                
                else:
                    print('-----------------------\n please check your input number \n -----------------------')
                    
                    
                
        
        elif data_1 == '3':
            print('Good bye')
            break
        
        else:
            print('-----------------------\n please check your input number \n -----------------------')
            


def choice_data(data):
        if data == '1':
            return tagger.contents_fillter(crwaler.get_title())
        
        elif data == '2':
            return tagger.contents_fillter(crwaler.get_body())
        
        elif data == '3':
            return 'Exist'
        
        else:
            print('please check your enter')
            
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
        
        
    
main()
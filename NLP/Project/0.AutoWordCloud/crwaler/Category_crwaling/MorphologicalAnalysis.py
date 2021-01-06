import re
from collections import Counter
from eunjeon import Mecab
import nltk
from nltk.corpus import stopwords
from IPython.display import set_matplotlib_formats
    
class MorphologicalAnalysis:

    def __init__(self):
        self.tagger = Mecab()
        self.Regualr_contents = []
        self.result_contents = []
        self.morphological_list = []
        self.fillter = '[!"#$%&\'()*+,-./:;<=>?[\]^_`{|}~“”·]'
        
    def get_result_contents(self):
        return self.result_contents

    def set_result_contents(self,content):
        self.result_contents.append(content)
    
    def get_morphological_list(self):
        return self.morphological_list

    def set_morphological_list(self,content):
        self.morphological_list.append(content)
        
    def contents_fillter(self,contents):        
        for i in range(len(contents)):
            self.set_result_contents(re.sub(self.fillter , '', contents[i]))
            
        return self.get_result_contents()
            
    def morphological_analysis(self, fillter_contents):
        return_list = []
        for i in range (len(fillter_contents)):
            return_list.append(self.tagger.pos(fillter_contents[i]))
        
        return return_list
    
    def extract_nouns(self, fillter_contents):
        for i in range (len(fillter_contents)):
            self.set_morphological_list(self.tagger.nouns(fillter_contents[i]))
        
        result_list = sum(self.get_morphological_list(),[])
        
        return result_list
    
    def count_morphological(self,morphological_data):
        count = Counter(morphological_data)
        tag_count = []
        tags = []
        return_list = []
        
        for n , c in count.most_common(100):
            dics = {'tag':n , 'count':c}
            if len(dics['tag']) >= 2 and len(tags) <= 49:
                tag_count.append(dics)
                tags.append(dics['tag'])
  

        for tag in tag_count:

            print(" {:<14}".format(tag['tag']), end='\t')

            print("{}".format(tag['count']))
        
        for tag in tag_count:
            return_list.append(tag['tag'])
            return_list.append(tag['count'])
            
        result_words = []
        result_count = []

        for i in range (0,len(return_list),2):
            result_words.append(return_list[i])
    
        for j in range (1, len(return_list),2):
            result_count.append(return_list[j])

        result = dict(zip(result_words , result_count))
        
        return result
            
    
    def to_one_list(self,morphological_data):
        one_list = sum(morphological_data , [])
        return one_list
    
    def count_test_module(self, data):
        count = Counter(data)
        words = dict(count.most_common())
        
        return words
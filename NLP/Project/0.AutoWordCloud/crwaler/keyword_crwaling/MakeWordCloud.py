import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from IPython.display import set_matplotlib_formats
import matplotlib

class MakeWordColud:
    def set_cloud(self):
        matplotlib.rc('font',family = 'Malgun Gothic')

        set_matplotlib_formats('retina')

        matplotlib.rc('axes',unicode_minus = False)

    def make_cloud(self, data):
        wordcloud = WordCloud(font_path = 'C:/Windows/Fonts/malgun.ttf', background_color='white',colormap = "Accent_r",\
                              width=1500, height=1000).generate_from_frequencies(data)
        
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()
        
    def drop_words(self, words_list):
        words = []
        count = eval(input('how many have words to deleted in the list?'))

        for i in range(count):
            words.append(input('please add words to delete from list'))
        
        if len(words) > 0:
            for i in words_list:
                for j in words:
                    if i == j :
                        words_list.remove(j)
        else:
            print('please enter your word')
            
        return words_list
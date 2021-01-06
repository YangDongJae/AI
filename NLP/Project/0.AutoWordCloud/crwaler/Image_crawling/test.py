from selenium import webdriver
import time

class ImageParser:
    def __init__(self):
        self.wb = webdriver.Chrome('D:/바탕 화면/인턴/python/crawling_software/crwaler/news_crwaling/chromedriver.exe')
        self.sleep_between_interactions = 1
        self.search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
        
    def set_sleep_between_intercations(self, num:int):
        self.sleep_between_interactions = num

    def get_wb(self):
        return self.wb
    
    def scroll_to_end(self,wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(self.sleep_between_interactions)
        
    def set_url(self , url):
        self.url = url
        
    def get_image_url(self, keyword , max_links_to_get):
        wd = self.get_wb()
        
        wd.get(self.search_url.format(q = keyword))
        
        image_urls = set()
        image_count = 0
        results_start = 0
        
        while image_count < max_links_to_get:
            self.scroll_to_end(wd)
            
            thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
            number_results = len(thumbnail_results)
            
            print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
            
            for img in thumbnail_results[results_start:number_results]:
                try:
                    img.click()
                    time.sleep(self.sleep_between_interactions)
                except Exception:
                    continue
                
                actual_images = wd.find_element_by_css_selector('img.n3VNCb')
            
                for actual_image in actual_images:                
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                        image_urls.add(actual_image.get_attribute('src'))      
                
                image_count = len(image_urls)
                
                if len(image_urls) >= max_links_to_get:
                    print(f"Found: {len(image_urls)} image links, done!")
                    break
            else:
                print("Found:", len(image_urls), "image links, looking for more ...")
                time.sleep(30)
                return
                load_more_button = wd.find_element_by_css_selector(".mye4qd")
                if load_more_button:
                    wd.execute_script("document.querySelector('.mye4qd').click();")
            results_start = len(thumbnail_results)
            
        return image_urls
    
test = ImageParser()

test.get_image_url('dog', 10)
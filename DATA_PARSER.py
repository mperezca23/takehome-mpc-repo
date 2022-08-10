import re

class ParseSearchUrls():
    
    def __init__(self, url):
        self.df_col = url
    # method to extract seach engine domains from url    
    def search_engine(url):
        return re.findall(r'[bgmy][iosa]\w*\.\w*', url)
    # method to extract keyword search from url    
    def key_word(url):
        return re.findall(r'[?&]q=([^&#]*)', url)
    
    
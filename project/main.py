from bs4 import BeautifulSoup
import sys
from urllib.parse import urlparse
from tqdm import tqdm
import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import stopwords
from urllib import request, error
from urllib.request import Request, urlopen
from nltk.tokenize import RegexpTokenizer
from urllib.error import HTTPError, URLError
import json
from http.client import InvalidURL
from time import gmtime, strftime
from openpyxl import load_workbook

tokenizer = RegexpTokenizer(r'\w+')

class SiteAnalyzer:

    def __init__(self):
        pass
    
    def url_validator(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc, result.path])
        except:
            return False

    def parse_page_for_subpages(self, url, search_list):

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        raw = BeautifulSoup(webpage, 'html.parser', from_encoding="iso-8859-1")

        for link in raw.find_all('a'):
            temp = link.get('href')
            if self.url_validator(temp) is False and temp is not None :
                temp = url+str(temp).removeprefix("/")

            if self.url_validator(temp) and url in temp and temp not in search_list:
                search_list.append(temp)

    def get_soup(self, url):
        try:
            raw = BeautifulSoup(
                urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read(), 
                'html.parser',
                from_encoding="iso-8859-1"
                ).get_text()

            return raw
        except (error.HTTPError, error.URLError) as e:
            pass

    def tokenize_soup(self, raw):
        tokens = tokenizer.tokenize(raw)
        tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
        return tokens_without_sw
        
    def textify_data(self, tokenized_data):
        return nltk.Text(tokenized_data)

    def tag_data(self, tokenized_data):
        return nltk.pos_tag(tokenized_data)

    def add_to_datasheet(self, excel_sheet, data_tuple, horizontal_header = False, vertical_header = False):

        pass


def main(argv=None):
    analyzer = SiteAnalyzer()
    # if argv is None:
    #     argv = sys.argv
    # urls = []
    
    argv = [
        # 'deep',
        '-o',
        'sheet.xlsx',
        'https://www.apptunix.com/',
        'https://trio.dev/',
        'https://youteam.io/',
        'https://www.daxx.com/',
        # 'https://distantjob.com/',
        # 'https://relevant.software/',
        # 'https://remotemore.com/',
        # 'https://www.peerbits.com/',
        # 'https://codersera.com/',
        # 'https://www.makeitinua.com',
        # 'https://soshace.com/',
        # 'https://intersog.com/',
        # 'https://x-team.com/',
        # 'https://www.quickmonday.com/',
        # 'https://hackernoon.com/',
        # 'https://www.classicinformatics.com',
        # 'https://www.remoteco.com/',
        # 'https://remoteplatz.com/',
        # 'https://stormotion.io/',
        # 'https://www.trustshoring.com/',
        'https://geektastic.com/'
    ]
    try:   
        wb = load_workbook(filename = str(argv[argv.index('-o')+1]))

        if '-o' in argv and wb:
            temp_list = []

            for link in argv:
                if analyzer.url_validator(link):
                    temp_list.append(link)

            search_list = []

            if 'deep' in argv:
                for link in temp_list:
                    try:
                        analyzer.parse_page_for_subpages(link, search_list)
                    except HTTPError:
                        pass
            else: 
                search_list = temp_list

            results = {}

            for link in tqdm(search_list):
                if analyzer.url_validator(link) and ".pdf" not in link:
                    print(link)
                    try:
                        _ = analyzer.get_soup(link)
                    except InvalidURL:
                        continue
                    if _ is None:
                        continue
                    try:
                        _ = analyzer.tokenize_soup(_)
                        _ = analyzer.textify_data(_)
                        fd = nltk.FreqDist(_)
                    except TypeError:
                        continue

                    for key, value in dict(fd.most_common(10)).items():
                        if key not in results:
                            results.update({key:value})
                        else:
                            results[key] += value
                        
                    analyzer.add_to_datasheet(wb, input_array)    
                
    except ValueError:
        print("To select output file, please, pass -o a.xlsx file as an argument")
        exit() 
  
if __name__ == "__main__":
    main()
    
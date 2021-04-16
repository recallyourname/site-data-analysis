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

tokenizer = RegexpTokenizer(r'\w+')

class SiteAnalyzer:

    def __init__(self):
        pass

    def get_soup(self, url):
        try:
            raw = BeautifulSoup(
                urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read(), 
                'html.parser'
                ).get_text()

            return raw

        except error.HTTPError:
            pass

    def tokenize_soup(self, raw):  
        tokens = tokenizer.tokenize(raw)
        tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
        return tokens_without_sw

    def textify_data(self, tokenized_data):
        return nltk.Text(tokenized_data)

    def tag_data(self, tokenized_data):
        return nltk.pos_tag(tokenized_data)

    def import_data_to_excel():
        pass
    
    def url_validator(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc, result.path])
        except:
            return False

def main(argv=None):
    analyzer = SiteAnalyzer()
    # if argv is None:
    #     argv = sys.argv
    # urls = []
    argv = [
        'https://www.apptunix.com/',
        'https://trio.dev/',
        'https://youteam.io/',
        'https://www.daxx.com/',
        'https://distantjob.com/',
        'https://relevant.software/',
        'https://remotemore.com/',
        'https://www.peerbits.com/',
        'https://codersera.com/',
        'https://www.makeitinua.com',
        'https://soshace.com/',
        'https://intersog.com/',
        'https://x-team.com/',
        'https://remotedevjobs.xyz/',
        'https://www.quickmonday.com/',
        'https://remoteok.io/',
        'https://hackernoon.com/',
        'https://www.classicinformatics.com',
        'https://www.remoteco.com/',
        'https://remoteplatz.com/',
        'https://stormotion.io/',
        'https://www.trustshoring.com/',
        'https://geektastic.com/',
        'https://geektastic.com/about',
        'https://geektastic.com/blog'
    ]
    
    for arg in argv:
        if analyzer.url_validator(arg):
            _ = analyzer.get_soup(arg)
            if _ is None:
                continue
            _ = analyzer.tokenize_soup(_)
            _ = analyzer.textify_data(_)
            fd = nltk.FreqDist(_)
            print(fd.tabulate(10))

if __name__ == "__main__":
    main()
    
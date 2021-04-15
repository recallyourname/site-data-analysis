from bs4 import BeautifulSoup
import sys
from urllib.parse import urlparse
from tqdm import tqdm
import nltk

class SiteAnalyzer:

    def __init__(self):
        pass

    def get_soup():
        pass

    def import_data_to_excel():
        pass


def url_validator(url):
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
        'https://geektastic.com/'
    ]
    
    for arg in tqdm(argv):
        if url_validator(arg):
            _ = analyzer.get_soup()
            if _ is None:
                continue
            _ = analyzer.import_data_to_excel()

            

if __name__ == "__main__":
    nltk.download()
    main()
    
import requests, json
from bs4 import BeautifulSoup
from caching import Cache
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


START_URL = "https://www.japan-guide.com/e/e2011_where.html"
FILENAME = "japanblooms_cache.json"

PROGRAM_CACHE = Cache(FILENAME)

def access_page_data(url):
    data = PROGRAM_CACHE.get(url)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data)
    return data

main_page = access_page_data(START_URL)

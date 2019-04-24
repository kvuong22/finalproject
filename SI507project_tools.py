import requests, json
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
# from SI507project_dbcreate import Base
import csv
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

#
def get_bloom_site_data(START_URL):
    main_page = access_page_data(START_URL)
    main_soup = BeautifulSoup(main_page, features="html.parser")
    body_content = main_soup.find('div',{'class':'page_section__body'})

    each_section = body_content.find_all('section',{'class':'spot_list'})
    # print(type(each_section))

    site_bloom_lst = []
    each_spot = body_content.findChildren('div', {'class':'spot_list__spot__main_info'})
    for spot in each_spot:
        each_spot_lst = []
#     # print (spot)
#     # print(type(spot))
        if spot.findChild('h1',{'class':'spot_list__spot__name'}):
            spot_name = spot.findChild('h1',{'class':'spot_list__spot__name'})
        # print(spot.findChild('h1',{'class':'spot_list__spot__name'}))
            each_spot_lst.append(spot_name.text.replace('•', ''))
# # print(each_spot_lst)
        if spot.findChild('span',{'class':'spot_meta__content'}):
            bloom_time = spot.findChild('span',{'class':'spot_meta__content'})
            each_spot_lst.append(bloom_time.text)
        site_bloom_lst.append(each_spot_lst)
    return site_bloom_lst

bloom_site_data = get_bloom_site_data(START_URL)

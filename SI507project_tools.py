import requests, json
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
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

main_soup = BeautifulSoup(main_page, features="html.parser")
body_content = main_soup.find('div',{'class':'page_section__body'})

list_of_cities = body_content.find_all('h3')

# cities_lst = []
data_lst = []
for city in list_of_cities:
    data_lst.append(city.text)
for c in list_of_cities:
    info_content = c.find_all('section',{'class':'spot_list'})
    for section in info_content:
        each_section_lst = []

    # cities_lst.append(city.text)
# print(cities_lst)

# info_content = main_soup.find('section',{'class':'spot_list'})
#
# locations = info_content.find_all('h1 class="spot_list__spot__name"')
#
# location_info_lst = []
# for c in locations:
#     location_info_lst.append(c.string)






#     all_info.append(spot_name.text)
#
# print(all_info)

#models for database
class Cities(Base):
    __tablename__ = 'cities'
    City_ID = Column(Integer, primary_key=True, autoincrement=True)
    City_Name = Column(String(250))
    Admin = Column(String(250))
    Population = Column(Integer)


class Locations(Base):
    __tablename__ = "locations"
    Location_ID = Column(Integer, primary_key=True, autoincrement=True)
    Location_Name
    City = Column(Integer, ForeignKey('cities.City_ID'))
    Bloom_Date = Column(String(150))
    cities = relationship('Cities')

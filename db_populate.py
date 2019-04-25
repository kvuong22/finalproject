from app import Bloomsite, Area, Bloomdate, session
# from SI507project_tools import *
import csv

#dictionary to look up where the site is located at for populating appropriate area id
data_dict = {'Shinjuku Gyoen':'Tokyo',
'Ueno Park':'Tokyo',
'Chidorigafuchi':'Tokyo',
'Sumida Park':'Tokyo',
'Sankeien Garden':'Yokohama',
'Mitsuike Park (Mitsuike Koen)':'Yokohama',
'Tsurugaoka Hachimangu Shrine':'Kamakura',
'Kawazu': 'Kawazu',
'Northern Shores of Kawaguchiko':'Fuji Five Lakes',
'Chureito Pagoda':'Fuji Five Lakes',
'Akagi Senbonzakura':'Gunma',
'Matsumoto Castle':'Nagano',
'Takato Castle Ruins Park':'Nagano',
'Takada Castle':'Niigata',
'Kenrokuen':'Kanazawa',
'Yamazakigawa Riverside':'Nagoya',
'Nagoya Castle':'Nagoya',
'Hikone Castle':'Hikone',
"Philosopher's Path":'Kyoto',
'Maruyama Park':'Kyoto',
'Arashiyama':'Kyoto',
'Heian Shrine':'Kyoto',
'Kema Sakuranomiya Park':'Osaka',
'Osaka Castle':'Osaka',
'Expo 70 Commemorative Park':'Osaka',
'Osaka Mint Bureau':'Osaka',
'Nara Park':'Nara',
'Mount Yoshinoyama':'Yoshino',
'Himeji Castle':'Himeji',
'Handayama Botanical Garden':'Okayama',
'Korakuen Garden and Okayama Castle':'Okayama',
'Tottori Castle Ruins':'Tottori',
'Inaba Senbonzakura':'Tottori',
'Hiroshima Peace Park':'Hiroshima',
'Miyajima':'Hiroshima',
'Megijima Island':'Takamatsu',
'Matsuyama Castle':'Matsuyama',
'Fukuoka Castle (Maizuru Park)':'Fukuoka',
'Kumamoto Castle':'Kumamoto',
'Mikamine Park':'Sendai',
'Hanamiyama Park':'Fukushima',
'Miharu Takizakura':'Fukushima',
'Kitakami':'Tohoku',
'Kakunodate':'Tohoku',
'Hirosaki Castle':'Tohoku',
'Matsumae Park':'Hokkaido',
'Goryokaku Fort':'Hokkaido',
'Maruyama Park and Hokkaido Shrine':'Hokkaido'}



#function for getting data to populate in Site table
def get_site_info(lst):
    for site in lst:
        site_info = Bloomsite.query.filter_by(sitename=site[0]).first()
        if not site_info:
            area_namecheck_key = data_dict[site[0]]
            # print(area_namecheck_key) prints out each area
            areacheck = Area.query.filter_by(areaname=area_namecheck_key).first()
            bloomcheck = Bloomdate.query.filter_by(bloomdate=site[1]).first()
            if areacheck and bloomcheck:
                areamatch = areacheck.id
                bloommatch = bloomcheck.id
                # a_id = Area.query.filter_by(.id).first()
                site_info = Bloomsite(sitename=site[0],area_id=areamatch,bloom_id=bloommatch)
        session.add(site_info)
        session.commit()


#function to get data to populate in Bloomdate table
def get_bloomdate_info(lst):
    for site in lst:
        # for spot in site:
        # print(site[1])
        bloomdate_info = Bloomdate.query.filter_by(bloomdate=site[1]).first()
        if not bloomdate_info:
            bloomdate_info = Bloomdate(bloomdate=site[1])
        session.add(bloomdate_info)
        session.commit()


#function to get data to populate in Area table
def get_area_info(area_file):
    csvfile = open(area_file, 'r', encoding='utf-8')
    reader = csv.reader(csvfile)
    header =next(csvfile)

    for row in reader:
        area_info = Area.query.filter_by(areaname=row[1]).first()
        if area_info:
            if row[2] not in area_info.areatype:
                area_info.areatype=(row[2])

        else:
            area_info = Area(areaname=row[1],areatype=row[2])
        session.add(area_info)
        session.commit()

import unittest
from SI507project_tools import *
import sqlite3

#tests for data scraped from website
class TestDataScrape(unittest.TestCase):
    #testing to see if [Shinjuku Gyoen, Early April] are in the list of lists with data scraped from website
    def test_scraping_site(self):
        results = get_bloom_site_data(START_URL)
        results_lst = ['Shinjuku Gyoen', 'Early April']
        self.assertTrue(results[0],results_lst)


    #testing the length of the lists of lists; manually counted 48 sites on the website that should have scraped
    def test_list_length(self):
        results = get_bloom_site_data(START_URL)
        self.assertEqual(len(results),48)


    #testing to make sure the type returned from get_bloom_site_data function is indeed a list
    def test_type(self):
        results = get_bloom_site_data(START_URL)
        self.assertEqual(list,type(results))




class TestDatabaseAreasTable(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("jp_bloom.db")
        self.cur = self.conn.cursor()


    def test_for_areas_table(self):
        self.cur.execute("select id, areaname, areatype from areas where areaname = 'Nagano'")
        data = self.cur.fetchone()
        self.assertEqual(data, (7, 'Nagano', 'Prefecture'), "Testing data that results from selecting Nagano")


    def tearDown(self):
    	self.conn.commit()
    	self.conn.close()



class TestDatabaseBloomsitesTable(unittest.TestCase):
        def setUp(self):
            self.conn = sqlite3.connect("jp_bloom.db")
            self.cur = self.conn.cursor()


        def test_for_areas_table(self):
            self.cur.execute("select id, sitename, area_id, bloom_id from bloomsites where id = '18'")
            data = self.cur.fetchone()
            self.assertEqual(data, (18, 'Hikone Castle', 11, 4), "Testing data that results from selecting id being 18")


        def tearDown(self):
        	self.conn.commit()
        	self.conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)

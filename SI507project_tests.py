import sqlite3
import unittest

class ProjectSQLiteDBTests(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect("jpbloomsites.sqlite")
        self.cur = self.conn.cursor()
        

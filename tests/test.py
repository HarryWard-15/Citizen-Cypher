import unittest
import connection.sqlconnector as sqlconnector
class UserTest(unittest.TestCase):
    def init_user(self):
        cursor = sqlconnector.create_cursor()

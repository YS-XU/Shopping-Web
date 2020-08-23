import unittest
from application import app
from application.db.db import get_all_users

class TestShoppingWebDatabase(unittest.TestCase):
    def setUp(self):
        self.app = app #initialize the app instance

    def test_user_query(self):
        with self.app.app_context(): #use the application context to run the SQL function
            data = get_all_users() # call the db function
        self.assertEqual(len(data),4) # the list that it returns must have a length of 4

if __name__ == '__main__':
    unittest.main()

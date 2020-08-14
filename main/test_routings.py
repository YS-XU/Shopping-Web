from app import app
import unittest

class TestRoutesForShopping(unittest.TestCase): #write test cases using unittest library

    def setUp(self):
        # creates a test client
        self.app = app.test_client()

        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self): #function to be called after evey test
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        with self.app.session_transaction() as session: #we are giving session values
            session['user'] = None
        result = self.app.get('/register/')
        self.assertEqual(result.status_code, 200)  # assert the status code of the response

    def test_shopping_cart_status(self):
        result = self.app.get('/shoppingcart/')
        self.assertEqual(result.status_code,200)

    def test_clothing_bottom(self):
        result = self.app.get('/items/clothing/bottom/')
        self.assertEqual(result.status_code,200)

    def test_user_home_without_user_status(self):
        with self.app.session_transaction() as session: #we are giving session values
            session['user'] = None
        result = self.app.get('/userhome/')
        self.assertEqual(result.status_code,200)

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the response data
        self.assertIn('html',result.data.decode('ASCII')) #comparing to see if there is a 'html' string inside of the result data

    # def test_register_page(self):
    #     result = self.app

if __name__ == '__main__':
    unittest.main()

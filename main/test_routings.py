from application import app
import unittest

class TestStatusCodeOfRoutings(unittest.TestCase):

    def setUp(self): #function to initialize the variables that will be used during the test cases
        self.app = app.test_client() # creates a test client
        self.app.testing = True # propagate the exceptions to the test client

    def tearDown(self): #function to be called after evey test
        pass

    #==========================================
    # Test cases -- testing routings of pages |
    #==========================================

    # --Making sure the pages return back a 200(OK response) STATUS RESPONSE
    def test_register_page_success_code(self):
        with self.app.session_transaction() as session: #Giving session values to this client
            session['user'] = None
        result = self.app.get('/register/') # GET the register page by url -- will RETURN a result OBJECT
        self.assertEqual(result.status_code, 200)  # check if the status code of the RESULT is equal to 200

    def test_shopping_cart_status(self):
        result = self.app.get('/shoppingcart/')
        self.assertEqual(result.status_code,200)


    # -- Make sure it returns a 302(redirection) status code

    def test_register_page_redirect_code(self):
        with self.app.session_transaction() as session:
            session['user'] = 'jimmytran1620@gmail.com'
        result = self.app.get('/register/')
        self.assertEqual(result.status_code,302)

if __name__ == '__main__':
    unittest.main()

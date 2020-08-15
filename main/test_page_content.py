import unittest
from application import app

    #===========================================
    # Test cases -- testing page content of URLs
    #===========================================

class TestPageContent(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client() #init the test client instance
        self.app.testing = True # configure that app to be on test mode

    def tearDown(self):
        pass

    # Testing the webpage to see if response give back the right page content
    def test_home_page_content(self):
        response = self.app.get('/')
        self.assertIn(b'<h2 class="category-captions"> Accessories </h2>',response.data) #check if there is the text 'Accessories' in the webpage content

    def test_register_page_content(self):
        with self.app.session_transaction() as session:
            session['user'] = 'jimmytran1620@gmail.com'
        response = self.app.get('/register/')
        self.assertIn(b'Redirecting',response.data)

if __name__ == '__main__':
    unittest.main()

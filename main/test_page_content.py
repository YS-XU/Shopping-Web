import unittest
from application import app

class TestPageContent(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client() #init the test client instance
        self.app.testing = True
        self.counter = 0

    # Testing the webpage to see if response give back the right page content
    def test_home_page_content(self):
        response = self.app.get('/')
        self.assertIn(b'Accessories',response.data) #check if there is the text 'Accessories' in the webpage content

    def test_register_page_content(self):
        with self.app.session_transaction() as session:
            session['user'] = 'jimmytran1620@gmail.com'
        response = self.app.get('/register/')
        self.assertIn(b'Redirecting',response.data) # this response

if __name__ == '__main__':
    unittest.main()

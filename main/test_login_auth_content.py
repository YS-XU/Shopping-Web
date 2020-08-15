import unittest
from application import app

#These test cases are to ensure that the right users are able to log in

#Test cases -- status code , and page content
class TestShoppingWebLoginInAuthentication(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client() #init the client instance
        self.app.test = True

    #validate status codes NEED DONE!!! --------------------------------------------------


    # validate page contents

    def test_login_in_with_false_crudentials(self):
        response = self.app.post( # do a post method for the /login/ and pass in username and password
            '/login/',
            data = dict(username='jimmytr1620@gmail.com',password='testing'),
            follow_redirects=True # go to the latest response status, which should be the final page
        )
        print(response.data)
        self.assertIn(b'<title>Register/Login</title>',response.data)

    def test_login_in_with_correct_crudentials(self):
        response = self.app.post(
            '/login/',
            data = dict(username='jimmytran1620@gmail.com',password='testing'),
            follow_redirects=True
        )
        self.assertIn(b'<title> Account </title>',response.data)


if __name__ == '__main__':
    unittest.main()

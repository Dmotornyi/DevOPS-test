import unittest
from app import app
from UserLogin import UserLogin
from flask_login import current_user


class MyTestCase(unittest.TestCase):
#    def test_something(self):
#        self.assertEqual(True, False)

    def testLogin(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/txt')
        self.assertTrue(b'Please login' in response.data)

    def testCurentUserName(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="test2@test2", psw="test2"), follow_redirects=True)
        self.assertIn(b'Hi test2', response.data)



if __name__ == '__main__':
    unittest.main()

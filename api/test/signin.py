import requests
import unittest


class TestToken(unittest.TestCase):

    def test_invalid_account(self):
        r = requests.get('http://localhost:5000/api/token/', auth=('hy456', '1234'))  # invalid password
        self.assertEquals(401, r.status_code)                                         # Unauthorized Access

    def test_valid_account(self):
        r = requests.get('http://localhost:5000/api/token/', auth=('hy456', '123'))
        self.assertEqual(200, r.status_code)
        token = r.json().get('token')
        self.assertTrue(token is not None)

    def test_signin_with_token(self):
        """
        Gets token and sign in with token.
        """
        r = requests.get('http://localhost:5000/api/token/', auth=('hy456', '123'))
        token = r.json().get('token')
        r = requests.get('http://localhost:5000/api/board/', auth=(token, 'unused'))
        self.assertEqual(200, r.status_code)
        self.assertEqual('OK', r.json().get('status'))


if __name__ == '__main__':
    unittest.main()

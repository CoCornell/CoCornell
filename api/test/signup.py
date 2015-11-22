import requests
import unittest

from mysite.models.user import User


class TestSignup(unittest.TestCase):

    def test_get_signup(self):
        r = requests.get('http://localhost:5000/api/signup/')
        self.assertEquals(405, r.status_code)                        # Method Not Allowed

    def test_signup_fail(self):
        r = requests.post('http://localhost:5000/api/signup/', {})   # netid is empty
        self.assertEqual(400, r.status_code)                         # Bad Request
        self.assertEqual('error', r.json().get('status'))

        data = {"netid": "hy456", "password": "123", "name": "yhf"}
        r = requests.post('http://localhost:5000/api/signup/', data) # Netid existed
        self.assertEqual(400, r.status_code)                         # Bad Request

    def test_signup_success(self):
        netid = "netid"
        password = "password"
        name = "test_name"
        data = {"netid": netid, "password": password, "name": name}
        r = requests.post('http://localhost:5000/api/signup/', data)
        self.assertEqual('OK', r.json().get('status'))
        self.assertEqual(200, r.status_code)

        try:
            user = r.json().get('user')
            self.assertTrue(user is not None)
            self.assertEqual(netid, user.get('netid'))
            self.assertTrue(user.get('password') is None)
            self.assertEqual(name, user.get('name'))
        finally:
            User.delete_user(netid)


if __name__ == '__main__':
    unittest.main()

import requests
import unittest


class TestBoard(unittest.TestCase):

    def get_token(self):
        """
        Sign in to get token.
        """
        r = requests.get('http://localhost:5000/api/token/', auth=('hy456', '123'))
        return r.json().get('token')

    def test_get_boards(self):
        r = requests.get('http://localhost:5000/api/board/', auth=(self.get_token(), 'unused'))
        self.assertEquals(200, r.status_code)
        boards = r.json().get('boards')
        self.assertTrue(isinstance(r.json().get('boards'), list))
        board = boards[0]
        self.assertTrue('id' in board)
        self.assertTrue('name' in board)

    def test_get_boards_count(self):
        r = requests.get('http://localhost:5000/api/board/count/', auth=(self.get_token(), 'unused'))
        self.assertEquals(200, r.status_code)
        self.assertTrue(r.json().get('count') >= 0)


if __name__ == '__main__':
    unittest.main()

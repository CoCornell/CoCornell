import requests


r = requests.get('http://localhost:5000/api/token/', auth=('hy456', '123'))
token = r.json().get('token')

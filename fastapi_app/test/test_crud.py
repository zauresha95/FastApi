import requests
import sys,os 

# root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root_folder)
# print(root_folder)
# from assets.test_data import * 
# sys.path.append("..assets")
# from ..assets  import *

data = {
  "name": "Misha",
  "email": "misha@mail.ru",
  "phone": 79991234567
}

data2 = {
  "name": "Dima",
  "email": "dima@mail.ru",
  "phone": 79991234567
}

data3 = {
  "name": "Tima",
  "email": "dima@mail.ru",
  "phone": 79991234567
}

port = 8005
id = 1
def test_post(port):
  res = requests.post(f"http://127.0.0.1:{port}/", json = data)
  print('post', res.status_code)

def test_put(port, id):
  res = requests.put(f"http://127.0.0.1:{port}/{id}", json = data2)
  print('put', res.status_code)

def test_get(port, id):
  res = requests.get(f"http://127.0.0.1:{port}/{id}")
  print('get', res.status_code, res.json())

def test_delete(port, id):
  res = requests.delete(f"http://127.0.0.1:{port}/{id}")
  print('delete', res.status_code)

def test_patch(port, id):
  res = requests.patch(f"http://127.0.0.1:{port}/{id}", json = data3)
  print('patch', res.status_code)

test_post(port)
test_get(port,id)
test_put(port,id)
test_get(port,id)
test_patch(port,id)
test_get(port,id)
test_delete(port,id)
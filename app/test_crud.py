import requests
data = {
  "name": "zaure",
  "email": "zaure@mail.ru",
  "phone": 79991234567,
  "created": "2022-10-09",
  "updated": "2022-10-09"
}

data2 = {
  "name": "saule",
  "email": "zaure@mail.ru",
  "phone": 79991234567,
  "created": "2022-10-09",
  "updated": "2022-10-09"
}

res = requests.post("http://127.0.0.1:8004/", json = data)
#id = res.json().get('id')
# print('post',res.json(),res.status_code)

# res = requests.put(f"http://127.0.0.1:8004/1", json = data2)
# print('put',res,res.status_code,res._content)

# id = 1
# res = requests.get(f"http://127.0.0.1:8004/{id}")
# print('get',res.json(),res.status_code)

# res = requests.delete("http://127.0.0.1:8000/1")
# print('delete',res.json(),res.status_code)
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

port = 8002
id = 1
#res = requests.post(f"http://127.0.0.1:{port}/", json = data)
# print('post',res.status_code,res._content)
# #print('post',res.json(),res.status_code)

res = requests.put(f"http://127.0.0.1:{port}/{id}", json = data2)
# print('put',res,res.status_code,res._content)


res = requests.get(f"http://127.0.0.1:{port}/{id}")
# print('get',res.json(),res.status_code)

#res = requests.delete(f"http://127.0.0.1:{port}/2")
#print('delete',res.json(),res.status_code)
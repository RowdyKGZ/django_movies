import json
str_ = 'abc'

with open('test.json', 'r+') as j:
    a = json.loads(j.read())
print(a)

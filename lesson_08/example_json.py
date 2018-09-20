import json

d = {
    'url': 'www.area51.pe',
    'name': 'Area 51 Training Center',
    'version': 1,
    'is_responsive': False,
    'account': None,
    'list': [1, 2, 3]
}

data = json.dumps(d)
print(data)

print(type(data))
print(json.loads(data))

d = json.loads('[null, true, false, "string", 1, 2, 0]')
print(d)
print(type(d))

import requests

r = requests.get('http://api.github.com/events')
print(dir(r))
print(r.headers)
print(r.encoding)
print(r.text) # text return str type
print(r.json()) # json() parse text to dict type, if is possible
print(r.history) # redirect http to https

r = requests.get('https://api.github.com/events')
print(r.history) # not redirect

r = requests.get('http://httpbin.org/get', params={'id': 1, 'name': 'carlos'})
print(r, r.url)

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r, r.json())

r = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r)

r = requests.delete('http://httpbin.org/delete')
print(r)

r = requests.head('http://httpbin.org/get')
print(r)

r = requests.get('http://httpbin.org/get', headers={'user-agent': 'my-app'})
print(r, r.headers)

r = requests.get('http://httpbin.org/cookies', cookies={'cookie': 'data'})
print(r, r.cookies)


import requests
r = requests.get('http://example.com')
print(r.text)

url = 'http://example.com'
par = {'k1': 'v1', 'k2': 'v2'}
r = requests.get(url, params=par)
print(r.url)


import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json'
location = 'delhi technological university'
params = {
    'key': '######################################',
    'address': location
}
r = requests.get(url=url, params=params)
data = r.json()
location = data['results'][1]['geometry']['location']
lat, long = location['lat'], location['lng']
print(lat, long)


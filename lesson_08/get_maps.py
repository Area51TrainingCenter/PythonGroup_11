import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json'
location = 'delhi technological university'
params = {
    'key': "AIzaSyBJzSdqiWjEhfLbmSWYm5xBe3aPXtq6yeM",
    'address': location
}
r = requests.get(url=url, params=params)
data = r.json()
print(data)
#location = data['results'][1]['geometry']['location']
#lat, long = location['lat'], location['lng']
#print(lat, long)


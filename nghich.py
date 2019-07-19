import requests
import json
URL = "http://127.0.0.1:8000/api/v1/Vrr_Geoip_Data/"
r = requests.get(url = URL,)
data=json.loads(r.content.decode('utf-8'))

for i in data['results']:
    if i['is_active'] == 1:
        print (i)



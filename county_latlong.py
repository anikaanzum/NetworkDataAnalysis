# Get county from Lat Long
import urllib.request, json, requests
import sys
#import urlopen
latitude= sys.argv[1]
longitude=sys.argv[2]
with urllib.request.urlopen("https://geo.fcc.gov/api/census/area?lat="+latitude+"+&lon="+longitude+"&format=json") as url:
    data = json.loads(url.read().decode())
    #print(data)

#print(json.dumps(data, indent=4, sort_keys=True))

#print("state=",data['results'][0]['state_name'])
print(data['results'][0]['county_name'])

from pymongo import Connection
from collections import Counter 
import time 

# Create connection to MongoDB Server
server = ''
port = 37627
db_name = ''
username = ''
password = ''

connection = Connection(server, port)
db = connection[db_name]
db.authenticate(username, password)
events = db.events

# queries
events.count() # 610 

# 1. query how many by each candidate: who had most? who had least?
candidates = []
for c in events.find({'candidate': {'$gt': "A"}}):
	candidates.append(c['candidate'])
candidate_event_count = Counter(candidates)
# Kucinich had most with 69, Ron Paul least with 5

# 2. query by state: which had most? which had least?
states = []
for s in events.find({'state': {'$gt': "A"}}):
	states.append(s['state']) 
state_event_count = Counter(states)
# Iowa had most with 139; WV, AR, ID, MO, KY all tied for least with 1

# 3. query by city: which had most?
cities = []
for c in events.find({'city': {'$gt': "A"}}):
	cities.append(c['city'])
city_event_count = Counter(cities)
# Des Moines with 38, followed by Washington with 37

# 4. What was the most popular event in the most popular city?
desmoines = events.find_one({"city": "Des Moines"}, {"latlng": 1})
dmlatlng = desmoines["latlng"]
dmevents = []
for e in events.find({"latlng": {"$near": dmlatlng}}, {"event_type": 1}).limit(38):
	dmevents.append(e["event_type"])
dm_event_count = Counter(dmevents) # 17 speeches 

# 5. what other cities are within the box bounded by [40.8, -96.7] and [43.6, -91.6]
box_events = []
box_cities = []
for b in events.find({"latlng": {"$within": {"$box": [[40.8, -96.7], [43.6, -91.6]]}}}):
	box_events.append(b['event_type'])
	box_cities.append(b['city'])
box_cities_count = Counter(box_cities)
len(box_cities_count) # 37 
# how many events there?
len(box_events) # 111
# what was the most frequent type of event?
box_events_count = Counter(box_events) # Speech 

# 6. what other cities are within a 100 mile radius around 2nd most popular city?
dc = events.find_one({ "$and": [{"city": "Washington"},  {"state": "DC"}]}, {"latlng": 1})
dc_events = []
dc_cities = []
miles = float(100 / 3963.192)
for d in events.find({"latlng": {"$within": {"$centerSphere": [dc['latlng'],  miles]}}}):
	dc_events.append(d['event_type'])
	dc_cities.append(d['city'])
dc_cities_count = Counter(dc_cities) # 6
# how many events there? 
dc_events_count = Counter(dc_events) # 25 speeches

# 7. how many kilometers did the candidate with least events travel?
# (assume only stops on this itinerary)
# what was the avg distance travelled per day? 
rp = [] 
for r in events.find({'candidate': "Ron Paul"}).sort('date'):
	rp.append(r)

from googlemaps import GoogleMaps 
api_key = 'AIzaSyB6oAxbPdpY0R2-u11vujuFrJbjoGUUq2Q'
gmaps = GoogleMaps(api_key)

distance = 0 
for i in range(0,len(rp)-1):
	r_start = rp[i]['latlng']
	r_end = rp[i+1]['latlng']
	a_start = gmaps.latlng_to_address(r_start[0], r_start[1])
	a_end = gmaps.latlng_to_address(r_end[0], r_end[1])
	directions = gmaps.directions(a_start, a_end)
	distance += directions['Directions']['Distance']['meters']
	time.sleep(1)

kms = distance / 1000.0 # ~ 9255.8 km traveled 
days = rp[4]['date'] - rp[0]['date'] # 56 days 
kms_per_day = kms/56 # avg of ~165 kms/day

connection.disconnect()
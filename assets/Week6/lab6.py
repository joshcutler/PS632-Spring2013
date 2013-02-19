# 1. Huffington Post pollster api

# pip install pollster
from pollster import Pollster 

pollster = Pollster()

# current estimate of president's job approval
chart = pollster.charts(topic='obama-job-approval')[0]
chart.estimates

example_topics = ['2012-gop-primary', '2012-senate', '2012-governor', '2012-president', '2012-house']

# list charts about Texas
pollster.charts(state='TX')

# calculate margin between Obama and Romney from poll
poll = pollster.polls(chart='2012-general-election-romney-vs-obama')[0]
question = [ x['subpopulations'][0] for x in poll.questions if x['chart'] == '2012-general-election-romney-vs-obama'][0]
obama = [x for x in question['responses'] if x['choice'] == 'Obama'][0]
romney = [x for x in question['responses'] if x['choice'] == 'Romney'][0]
print obama['value'] - romney['value']

# check methodology in recent polls about the house 
chart = pollster.chart(slug='us-health-bill')
print [[x.pollster, x.method] for x in chart.polls()]

# 2. Google Maps

#pip install googlemaps
from googlemaps import GoogleMaps 
api_key = 'AIzaSyB6oAxbPdpY0R2-u11vujuFrJbjoGUUq2Q'
gmaps = GoogleMaps(api_key)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
lat, lng = gmaps.address_to_latlng(whitehouse)
print lat, lng

destination = gmaps.latlng_to_address(38.897096, -77.036545)
print destination 

dlat, dlng = gmaps.address_to_latlng('326 Perkins Library, Durham, NC 27708')
print dlat, dlng 
duke = gmaps.latlng_to_address(dlat, dlng)
print duke 

local = gmaps.local_search('restaurant near ' + duke)
print local['responseData']['results'][0]['titleNoFormatting']

directions = gmaps.directions(duke, whitehouse)
print directions['Directions']['Distance']['meters']

for step in directions['Directions']['Routes'][0]['Steps']:
	print step['descriptionHtml']

embassies = [[38.917228,-77.0522365], # afghanistan
	[38.9076502, -77.0370427], # australia
	[38.916944, -77.048739] # barbados
	]

minDistance = 1000000
answer = {}
for i in range(len(embassies)):
	latlng = embassies[i]
	address = gmaps.latlng_to_address(latlng[0], latlng[1])
	directions = gmaps.directions(whitehouse, address)
	distance = directions['Directions']['Distance']['meters']
	if distance < minDistance:
		local = gmaps.local_search('embassy near ' + address)
		if address.split(" ")[0] == 'Embassy':
			answer['name'] = address.split(',')[0]
		else: 
			answer['name'] = local['responseData']['results'][0]['titleNoFormatting']
		answer['distance'] = distance 
		answer['address'] = address 
		answer['directions'] = directions['Directions']['Routes'][0]['Steps']
		cafe = gmaps.local_search('cafe near ' + address)
		answer['cafe'] = cafe['responseData']['results'][0]['titleNoFormatting']
		bar = gmaps.local_search('bar near ' + address)
		answer['bar'] = bar['responseData']['results'][0]['titleNoFormatting']

# which embassy is closest to the White House in meters? 
print "{0} is closest to the White House".format(answer['name'])

# how far is it? 
print "{0} is {1} meters from the White House".format(answer['name'], answer['distance'])

# what is its address? 
print "The address is {0}".format(answer['address'])

# if I wanted to hold a morning meeting there, which cafe would you suggest?
print "A nice cafe would be {0}".format(answer['cafe'])

# if I wanted to hold an evening meeting there, which bar would you suggest? 
print "A nearby bar would be {0}".format(answer['bar'])

# how would I get from the White House to the embassy? 
print "To get to {0} from the White House: ".format(answer['name'])
for step in answer['directions']:
	print step['descriptionHtml']

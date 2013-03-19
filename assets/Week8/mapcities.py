import csv, time
from googlemaps import GoogleMaps 
api_key = 'AIzaSyB6oAxbPdpY0R2-u11vujuFrJbjoGUUq2Q'
gmaps = GoogleMaps(api_key)

infile = open('campaign.csv', "rU")
outfile = open('latlong.csv', "wb")
reader = csv.reader(infile)
writer = csv.writer(outfile)


Headers = ["Date", "Person",  "Time", "EventType", "City", "State", "Lat", "Long"]

writer.writerow(Headers)

count = 1
for row in reader: 
	if row != Headers:
		city, state = row[4], row[5]
		address = "{0}, {1}".format(city, state)
		lat, lng = gmaps.address_to_latlng(address)
		output = row + [lat, lng]
		writer.writerow(output)
		time.sleep(1)
		print count 
		count += 1

outfile.close()
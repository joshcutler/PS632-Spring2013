from pymongo import Connection, GEO2D, ASCENDING
import time
from datetime import datetime

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

# input data from csv 
import csv
infile = open('latlong.csv', "rU")
reader = csv.reader(infile)

for row in reader:
	if row[0] != "Date":
		print row 
		date = row[0]
		# formatted_date = time.strptime(date, "%m/%d/%Y")
		tstruct = time.strptime(date, "%d-%b-%y")
		formatted_date = datetime.fromtimestamp(time.mktime(tstruct))
		person = row[1]
		event_type = row[3]
		city = row[4]
		state = row[5]
		lat = float(row[6])
		lng = float(row[7])
		events.insert({"date": date,
									"candidate": person, 
									"date": formatted_date,
									"event_type": event_type,
									"city": city,
									"state": state,
									"latlng": [lat, lng]
			})
events.create_index([("latlng", GEO2D), ("candidate", ASCENDING)])

connection.disconnect()

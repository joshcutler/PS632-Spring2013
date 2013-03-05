# Go to mongolab: https://mongolab.com/
# Create a New Database
# Get the connection string

server = ''
port = 33877
db_name = ''
username = ''
password = ''

from pymongo import Connection
connection = Connection(server, port)
db = connection[db_name]
db.authenticate(username, password)

test = db.test
test.insert({'herp': 'derp'})
test.find_one()

connection.disconnect()

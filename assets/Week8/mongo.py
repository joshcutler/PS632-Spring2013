# brew install mongodb
# pip install pymongo

# MongoDB is a document store.  We can store arbitrary objects.
# Everything is JSON

# First we must get a connection to our database
# Create a connection to the MongoDB server
from pymongo import Connection
connection = Connection('localhost', 27017)
# Get a DB 
db = connection.inclass_db #use whatever db name you want

# Next we need to grab our 'collection'
# In mongoDB a collection is a bundle of documents.  Think of it like a table from last week.
collection = db.first_collection

# Lets make some fake data
import datetime
import random
for i in range(0,100):
	collection.insert({"author": "Josh",
        		  "text": "Some stuff!",
        		  "tags": ["mongodb", "python", "pymongo"],
        		  "date": datetime.datetime.utcnow(),
        		  "my_random": random.random()})
# N.B. we could have passed in an array and it would have worked.
items = []
for i in range(0, 100):
	items.append({"author": "Matt",
        		  "text": "Some other stuff!",
        		  "tags": ["mongodb", "python", "pymongo"],
        		  "date": datetime.datetime.utcnow(),
        		  "my_random": random.random()})

collection.insert(items)

# Lets see what happened
db.collection_names()
collection.count()

# Lets retrieve these documents
collection.find_one()
collection.find_one({'author': 'Josh'})
collection.find_one({'author': 'Matt'})

# Now lets get multiple results
for item in collection.find({'author': 'Josh'}):
	print item

# You can count with queries as well
collection.find({'author': 'Josh'}).count()

# Lets do some more interesting queries
# See documentation here: http://docs.mongodb.org/manual/reference/operators/
collection.find_one({'my_random': {'$lt': 0.5}})

for item in collection.find({'my_random': {'$lt': 0.5}}).sort('my_random1 desc'):
	print item

# Lets remove Matt's things
collection.remove({'author': 'Matt'})
collection.count()

# Update a record
first = collection.find_one()
collection.update({'_id': first['_id']}, {'$set': {'tags': ['a', 'b']}})

collection.update({'my_random': {'$lt': 0.1}}, {'$set': {'my_random': 0}}, multi=True)
collection.find({'my_random': 0}).count()

# Indices
collection.find({"my_random": {"$gt": .5}}).sort('author').explain()

from pymongo import ASCENDING, DESCENDING
collection.create_index([("my_random", DESCENDING), ("author", ASCENDING)])

# Notice how we never defined a schema?  We just used dictionaries of data.
# No classes necessary.

# We can do geospatial indexing, map reduce and a whole lot more




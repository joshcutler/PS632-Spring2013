# Databases - NoSQL, MongoDB, and CouchDB

## In Class
These database types work with *documents*. You're basically using a bunch of dictionaries so you don't have to worry about schema. There are others that rely on a graph framework, but don't worry about them for now. A third type is key-value storage, like Cassandra and Voldemort. A final type is NoSQL databases explicitly for text corpuses (e.g. SOLR). These allow for Natural Language Processing (NLP). 

RDBMS databases work on the CAP Theorem. This theorem emphasizes three properties of a database. Consistency - records are consistent. Availability - you want to be able to get stuff in and out. Partition tolerance - some elements can fail without the whole thing failing.

NoSQL databases ignore the CAP theorem--they're meant to be fast. If you're a statistician, you already have measurement error in your records so who cares about a little more noise (as long as it isn't systematic). You can see why this wouldn't work for a bank but it's fine for less important things.

### Indexing

Indexing is when we give indices to records. It's a mapping from database column to unique ID's that make lookup really quick. There are a number of data structures that make data lookup fast: binary trees, sorted arrays, etc. 

The simplest type is called an inverted index. This is defined on the *column space* of a table (e.g. Name in a record: a=1, b=2, etc). The lookup is then as fast as a dictionary. You can also represent longer records as trees. The records `ae, ab, bc, be` could be stored in two trees: one beginning with "a" and linking to "e" and "b", and another starting with "b" and linking to "c" and "e". 

You can also have joint indices over multiple columns of a table. 

### Mongo.py example
After we create a collection we can run `collection.count()` and `db.collections`. 

Then, we quickly create 100 records with a list. 

Once we've added our records, we can do the following
```
a = collection.find_one()
a['author'] # Josh
a['my_random'] # a random number
```

There are lots of fun operators we can use: http://docs.mongodb.org/manual/reference/operators/

Another cool thing we can do is `.explain()` where you get Mongo to tell you about how it plans to execute a query. The explain object also has some details such as `['nscanned']` to tell you how many objects it looked at. 

Where should we put our index? (timestamp is a good place to start)


## In Lab

Make sure everyone understands:

- connecting to a Mongo database
- querying a database
- looping through results
- importing a csv file
- `Counter()`
- `time.sleep()`
- geospatial indexing

Walk them through the database in CSV and Mongo formats. Show them how to connect and run a couple sample queries.

Then, set them loose to answer a few questions using the database.  

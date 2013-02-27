import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#Connect to the local database
engine = sqlalchemy.create_engine('sqlite:///geog.db', echo=True)

Base = declarative_base() 

# Schemas 
class Town(Base):
	__tablename__ = 'towns'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	population = Column(Integer)
	numdept = Column(Integer)

	def __init__(self, name, population, numdept):
		self.name = name 
		self.population = population
		self.numdept = numdept

	def __repr__(self):
		return "<Town('%s')>" % (self.name)

class Distance(Base):
	__tablename__ = 'distances'

	id = Column(Integer, primary_key=True)
	towndepart = Column(String)
	townarrive = Column(String)
	distance = Column(Integer)

	def __init__(self, towndepart, townarrive, distance):
		self.towndepart = towndepart
		self.townarrive = townarrive
		self.distance = distance 

	def __repr__(self):
		return "<Distance('%s', '%s', '%s')" % (self.towndepart, self.townarrive, self.distance)

class Department(Base):
	__tablename__ = 'departments'

	id = Column(Integer, primary_key=True)
	deptname = Column(String)
	numregion = Column(Integer)

	def __init__(self, deptname, numregion):
		self.deptname = deptname 
		self.numregion = numregion

	def __repr__(self):
		return "<Department('%s')" % self.id 

class Region(Base):
	__tablename__ = 'regions'

	id = Column(Integer, primary_key=True)
	regname = Column(String)

	def __init__(self, regname):
		self.regname = regname 

	def __repr__(self):
		return "<Region('%s')" % self.id 

#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
	Town('A', 110000, 1),
	Town('B', 80000, 3),
	Town('C', 300000, 3),
	Town('D', 50000, 2),
	Town('E', 113000, 2),
	Town('F', 70000, 1)
])

session.add_all([
	Distance('A', 'E', 50),
	Distance('A', 'F', 60),
	Distance('B', 'C', 50),
	Distance('B', 'D', 60),
	Distance('C', 'B', 50),
	Distance('D', 'B', 60),
	Distance('D', 'E', 30),
	Distance('E', 'A', 50),
	Distance('E', 'B', 60),
	Distance('E', 'D', 30),
	Distance('E', 'F', 100),
	Distance('F', 'A', 60)
])

session.add_all([
	Department('Department 1', 1),
	Department('Department 2', 1),
	Department('Department 3', 3),
	Department('Department 4', 2)
])

session.add_all([
	Region('Region 1'),
	Region('Region 2'),
	Region('Region 3')
])

session.commit()

# Some querying 
for town in session.query(Town).order_by(Town.id):
	print town.name, town.population

# TODO: 
# 1. Display, by region and department, the number of cities having more than 100000 inhabitants.
# 2. Display the list of all the one-way connections between two cities for which the population of one of the 2 cities is lower than 80000 inhabitants. 
# 3. Display the list of cities 2 road sections apart, and the distance which separates them.
# 4. Display the list of cities 4 road sections apart (there can be shorter connections of 2 or 3 sections), and the distance which separates them.
# 5. Display the number of inhabitants per region and department. Suppose that the population of a region is that of the cities which are part of the road network.
# 6. Give the name of the region which has the longest road network and the number of kilometers of this network. 
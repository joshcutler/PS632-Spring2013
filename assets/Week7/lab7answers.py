import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#Connect to the local database
engine = sqlalchemy.create_engine('sqlite:///geog.db', echo=True)

Base = declarative_base() 

# Schemas
class Region(Base):
	__tablename__ = 'regions'

	id = Column(Integer, primary_key=True)
	name = Column(String)

	def __init__(self, name):
		self.name = name 

	def __repr__(self):
		return "<Region('%s')>" % self.id 

class Department(Base):
	__tablename__ = 'departments'

	id = Column(Integer, primary_key=True)
	deptname = Column(String)
	numregion = Column('regionid', Integer, ForeignKey('regions.id'))

	numreg = relationship("Region", 
		primaryjoin = numregion == Region.id)

	def __init__(self, deptname):
		self.deptname = deptname 

	def __repr__(self):
		return "<Department('%s')>" % self.id 

class Town(Base):
	__tablename__ = 'towns'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	population = Column(Integer)
	numdept = Column(Integer, ForeignKey('departments.id'))
	numdept = relationship("Department", 
		primaryjoin = numdept == Department.id)

	def __init__(self, name, population):
		self.name = name 
		self.population = population

	def __repr__(self):
		return "<Town('%s')>" % (self.name)

class Distance(Base):
	__tablename__ = 'distances'

	id = Column(Integer, primary_key=True)
	towndepart = Column(String, ForeignKey('towns.name'))
	townarrive = Column(String, ForeignKey('towns.name'))
	distance = Column(Integer)

	td = relationship("Town", 
		primaryjoin= towndepart == Town.name)
	ta = relationship("Town", 
		primaryjoin = townarrive == Town.name)
	
	def __init__(self, distance):
		self.distance = distance 

	def __repr__(self):
		return "<Distance('%s', '%s', '%s')>" % (self.towndepart, self.townarrive, self.distance)

#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

reg1 = Region('Region 1')
reg2 = Region('Region 2')
reg3 = Region('Region 3')
session.add_all([reg1, reg2, reg3])

dept1 = Department('Department 1')
dept1.numregion = reg1 

dept2 = Department('Department 2')
dept2.numregion = reg1 

dept3 = Department('Department 3')
dept3.numregion = reg3 

dept4 = Department('Department 4')
dept4.numregion = reg2 

session.add_all([dept1, dept2, dept3, dept4])

a = Town('A', 110000, 1)
b = Town('B', 80000, 3)
c =	Town('C', 300000, 3)
d = Town('D', 50000, 2)
e =	Town('E', 113000, 2)
f = Town('F', 70000, 1)

session.add_all([a,b,c,d,e,f])

ae = Distance(50)
ae.td, ae.ta = a, e 

af = Distance(60)
af.td, af.ta = a, f 

bc = Distance(50)
bc.td, bc.ta = b, c 

bd = Distance(60)
bd.td, bd.ta = b, d 

cb = Distance(50)
cb.td, cb.ta = c, b 

db = Distance(60)
db.td, db.ta = d, b 

de = Distance(30)
de.td, de.ta = d, e 

ea = Distance(50)
ea.td, ea.ta = e, a 

eb = Distance(60)
eb.td, eb.ta = e, b 

ed = Distance(30)
ed.td, ed.ta = e, d 

ef = Distance(100)
ef.td, ef.ta = e, f 

fa = Distance(60)
fa.td, fa.ta = f, a 






session.commit()

exit()

# Some querying 
for town in session.query(Town).order_by(Town.id):
	print town.name, town.population
 
# 1. Display, by department, the cities having more than 100000 inhabitants.
for t in session.query(Town).filter(Town.population>100000).group_by(Town.numdept).order_by(Town.numdept):
	print "Department", t.numdept, "Town", t.name

# 2. Display the list of all the one-way connections between two cities for which the population of one of the 2 cities is lower than 80000 inhabitants. 
for d in session.query(Town, Distance).filter(Town.population<80000).filter(or_(Distance.townarrive==Town.name, Distance.towndepart==Town.name)).order_by(Town.name).distinct():
	print d[1]

# 3. Display the list of cities 2 road sections apart, and the distance which separates them.
# for d in session.query(Distance).

# 4. Display the number of inhabitants per region and department. Suppose that the population of a region is that of the cities which are part of the road network.
# 5. Give the name of the region which has the longest road network and the number of kilometers of this network. 
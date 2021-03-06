import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_, func, select, union_all
from sqlalchemy.orm import relationship, backref, sessionmaker, aliased

#Connect to the local database
engine = sqlalchemy.create_engine('sqlite:///geog.db', echo=True)

Base = declarative_base() 

# Schemas
class Region(Base):
	__tablename__ = 'regions'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	departments = relationship("Department")

	def __init__(self, name):
		self.name = name 

	def __repr__(self):
		return "<Region('%s')>" % self.id 

class Department(Base):
	__tablename__ = 'departments'

	id = Column(Integer, primary_key=True)
	deptname = Column(String)
	region_id = Column(Integer, ForeignKey('regions.id'))	
	towns = relationship("Town")

	def __init__(self, deptname):
		self.deptname = deptname 

	def __repr__(self):
		return "<Department('%s')>" % self.id 

class Town(Base):
	__tablename__ = 'towns'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	population = Column(Integer)
	dept_id = Column(Integer, ForeignKey('departments.id'))
	# distances = relationship("Distance")
	# distance_id = Column(Integer, ForeignKey('distances.id'))
	# distance = relationship("Distance", backref="towns")

	def __init__(self, name, population):
		self.name = name 
		self.population = population

	def __repr__(self):
		return "<Town('%s')>" % (self.name)

	def add_road(self, destination, dist):
		d = Distance(self, destination, dist)
		self.roads_from.append(d)
		destination.roads_to.append(d)

	def can_get_to(self):
		return [x.townarrive for x in self.roads_from]

	def can_get_from(self):
		return [x.towndepart for x in self.roads_to]

distance_table = Table('distance', Base.metadata,
	Column('towndepart_id', Integer, ForeignKey('depart.id'), primary_key=True),
	Column('townarrive_id', Integer, ForeignKey('arrive.id'), primary_key=True),
	Column('distance', Integer)
)

class Distance(Base):
	# __tablename__ = 'distances'

	# id = Column(Integer, primary_key=True)
	# towndepart_id = Column(Integer, ForeignKey('towns.id'))
	# townarrive_id = Column(Integer, ForeignKey('towns.id'))
	# distance = Column(Integer)

	# td = relationship("Town", 
	# 	primaryjoin= towndepart_id == Town.id)
	# ta = relationship("Town", 
	# 	primaryjoin = townarrive_id == Town.id)
	
	def __init__(self, town1, town2, distance):
		self.towndepart_id = town1.id
		self.townarrive_id = town2.id
		self.distance = distance 

	def __repr__(self):
		return "<Distance('%s', '%s', '%s')>" % (self.towndepart, self.townarrive, self.distance)

#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

# Create regions
reg1 = Region('Region 1')
reg2 = Region('Region 2')
reg3 = Region('Region 3')
session.add_all([reg1, reg2, reg3])

# Create departments, nested in regions
dept1 = Department('Department 1')
reg1.departments.append(dept1)

dept2 = Department('Department 2')
reg1.departments.append(dept2)

dept3 = Department('Department 3')
reg3.departments.append(dept3)

dept4 = Department('Department 4')
reg2.departments.append(dept4)

session.add_all([dept1, dept2, dept3, dept4])

# Create towns, nested in departments
a = Town('A', 110000)
dept1.towns.append(a)

b = Town('B', 80000)
dept3.towns.append(b)

c =	Town('C', 300000)
dept3.towns.append(c)

d = Town('D', 50000)
dept2.towns.append(d)

e =	Town('E', 113000)
dept2.towns.append(e)

f = Town('F', 70000)
dept1.towns.append(f)

session.add_all([a,b,c,d,e,f])

mapper(Distance, distance, properties={
	'towndepart_id': relationship(Town, primaryjoin=distances.c.towndepart_id==towns.c.id, backref='roads_from'),
	'townarrive_id': relationship(Town, primaryjoin=distances.c.townarrive_id==towns.c.id, backref='roads_to')
	}
)
ae = Distance(a, e, 50)
# ae.td, ae.ta = a, e 

# af = Distance(60)
# af.td, af.ta = a, f 

# bc = Distance(50)
# bc.td, bc.ta = b, c 

# bd = Distance(60)
# bd.td, bd.ta = b, d 

# cb = Distance(50)
# cb.td, cb.ta = c, b 

# db = Distance(60)
# db.td, db.ta = d, b 

# de = Distance(30)
# de.td, de.ta = d, e 

# ea = Distance(50)
# ea.td, ea.ta = e, a 

# eb = Distance(60)
# eb.td, eb.ta = e, b 

# ed = Distance(30)
# ed.td, ed.ta = e, d 

# ef = Distance(100)
# ef.td, ef.ta = e, f 

# fa = Distance(60)
# fa.td, fa.ta = f, a 

# session.add_all([ae, af, bc, bd, cb, db, de, ea, eb, ed, ef, fa])
session.commit()

# Some querying 
for town in session.query(Town).order_by(Town.id):
	print town.name, town.population
 
# 1. Display, by department, the cities having more than 100000 inhabitants.
for t in session.query(Town).filter(Town.population>100000).group_by(Town.dept_id).order_by(Town.dept_id):
	print "Department", t.dept_id, "Town", t.name

# 2. Display the list of all the one-way connections between two cities for which the population of one of the 2 cities is lower than 80000 inhabitants. 
for d in session.query(Town, Distance).filter(Town.population<80000).filter(or_(Distance.townarrive==Town.name, Distance.towndepart==Town.name)).order_by(Town.name).distinct():
	print d[1]

# 3. Display the list of cities 2 road sections apart, and the distance which separates them.
# for d1 in session.query(Town, Distance):
# 	td = d1.towndepart
# 	for d2 in session.query(Distance).filter(Distance.townarrive=td):
# 		print d1.towndepart, d2.townarrive, d1.distance+d2.distance

# degree1 = session.query(Distance.townarrive, Distance.distance).all()
# degree1_alias = aliased(degree1, name="deg1")
# degree2 = session.query(Distance.towndepart, Distance.distance).filter(Distance.towndepart==degree1_alias.c.townarrive)
# deg2 = union_all(select([Distance.townarrive]))

# 4. Display the number of inhabitants per department (bonus: per region). 
for p in session.query(Town.population, func.sum(Town.population)).group_by(Town.dept_id).all():
	print p[1]

# 5. Give the name of the region which has the longest road network and the number of kilometers of this network. 
for r in session.query(Town.distances.distance, func.sum(Town.distances.distance)).group_by(Town.dept_id).all():
	print r 

# for r in session.query(Distance.distance, func.sum(Distance.distance)).group_by().all():

# distance_arrivals = session.query(Distance.townarrive, Distance.distance).all()
# da_alias = aliased(distance_arrivals, name="da")
# dept_arrive = session.query(Town.dept_id).filter(Town.name==da_alias.c.townarrive).all()
# print dept_arrive

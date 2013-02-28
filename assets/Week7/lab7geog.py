import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_, func
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

	def __init__(self, name, population):
		self.name = name 
		self.population = population

	def __repr__(self):
		return "<Town('%s')>" % (self.name)

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

# TODO: Create towns, nested in departments

session.commit()

# Some example querying 
for town in session.query(Town).order_by(Town.id):
	print town.name, town.population

# TODO: 
# 1. Display, by department, the cities having more than 100000 inhabitants.
# 2. Display the list of all the one-way connections between two cities for which the population of one of the 2 cities is lower than 80000 inhabitants. 
# 3. Display the number of inhabitants per department (bonus: do it per region as well). 

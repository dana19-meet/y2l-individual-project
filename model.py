from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Activity(Base):
	__tablename__="activities"
	activity_id=Column(Integer,primary_key=True)
	name=Column(String)
	minage=Column(Integer)
	maxage=Column(Integer)
	atype=Column(String)
	content=Column(String)
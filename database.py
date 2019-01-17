
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_activity(name,minage,maxage,atype,content):
	activity_object = Activity(
		name= name,
		minage=minage,
		maxage=maxage,
		atype=atype,
		content=content)
	session.add(activity_object)
	session.commit()

def query_by_id(activity_id):
	activity = session.query(Activity).filter_by(
		activity_id=activity_id).first()
	return activity

def query_all_activities():
	activities = session.query(Activity).all()
	return activities

def query_by_name(activity_name):
	activities=session.quert(Activity).filter_by(
		activity_name=activity_name).all()
	return activities
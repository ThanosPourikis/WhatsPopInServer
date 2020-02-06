import sqlite3
from flask import g
import json
import os

DATABASE="Database/data.db"

def create_database():
	con = get_db()
	with open('Database/schema.sql',mode='r') as f:
		con.executescript(f.read())
	con.commit()
	return "Success"

def get_db():
	db = getattr(g, '_database', None)
	if(not(os.path.exists (DATABASE) ) ):
		create_database()
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

def query_db(query,args=(),one=False):
	con = get_db()
	cursor = con.cursor()
	cursor.execute(query)
	return (cursor.fetchall())	

def fetch_tables():
	con = get_db()
	li = con.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
	return json.dumps(li)

def getAllEvents():
	con = get_db()
	qq = con.execute("SELECT * FROM EVENT").fetchall()
	return json.dumps(qq)

def add_event(name,place,category,description,creatorid,image,date,time):
	con = get_db()
	querry = "INSERT INTO EVENT(NAME,PLACE,CATEFORY,DESCRIPTION,CREATORID,IMAGE,DATE,TIME) VALUES({},{},{},{},{},{},{},{})".format(name,place,category,description,creatorid,image,date,time)
	con.execute(querry)

def SelectUser(user):
	con = get_db()
	query = 'SELECT * FROM USERS WHERE EMAIL = "{}"'.format(user)
	query = con.execute(query).fetchall
	return query.fetchall()

def insertUser(email,password):
	con = get_db()
	querry = "INSERT INTO USERS(EMAIL,PASSWORD) VALUES('{}','{}')".format(email,password)
	print(querry)
	con.execute(querry)
	return "200"



	
	
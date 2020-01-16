import sqlite3
from flask import g
import json

DATABASE="Database/data.db"


def get_db():
    db = getattr(g, '_database', None)
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

def add_event(name,place,catefory,description,creatorid,image,date,time):
	con = get_db()
	querry = "INSERT INTO TABLE(NAME,PLACE,CATEFORY,DESCRIPTION,CREATORID,IMAGE,DATE,TIME) VALUES({},{},{},{},{},{},{},{})".format(name,place,catefory,description,creatorid,image,date,time)
	con.execute(querry)

def create_database():
	con = get_db()
	with open('Database/schema.sql',mode='r') as f:
		con.executescript(f.read())
	con.commit()
	return "Success"


	
	
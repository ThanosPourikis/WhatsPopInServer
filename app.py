from flask import Flask
import json
from Database.db import *
import sqlite3
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('event')

def check():
	with app.app_context():
			print(fetch_tables())
			print(create_database())

class Event(Resource):
	def get(self,event_id):
		li = query_db("SELECT * FROM EVENT WHERE EVENTID = {}".format(event_id))
		if( li is null):
			abort(404, message="Event {} doesn't exist".format(event_id))
		return json.dump(li)
	def put(self,):
		pass




class Events(Resource):
	def get(self):
		li = query_db("SELECT * FROM EVENT")
		return json.dumps(li)

api.add_resource(Event,'/event/<event_id>')
api.add_resource(Events,'/events_list')

if __name__ == '__main__':
	
	app.run(debug=True)
from flask import Flask,render_template,redirect
import json
from Database.db import *
import sqlite3
from forms import Create_Event,Login,SignUp
from config import SECRET_KEY
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SECRET_KEY"]= (SECRET_KEY)
bcrypt = Bcrypt(app)


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/get")
def get():
	return getAllEvents()

@app.route("/login",methods=['GET','POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		usr = SelectUser(form.email.data)
		print(usr)
		#print(bcrypt.check_password_hash(usr.password,form.password.data))
		return redirect("/")
	else:
		print(form.errors)
		print(form.email.errors)
		print(form.password.errors)
	return render_template('login.html',form = form)

@app.route('/signUp',methods=['GET','POST'])
def signUp():
	form=SignUp()
	if form.validate_on_submit():
		passHash =  bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		print(form.email.data,passHash)
		insertUser(form.email.data,passHash)
		return redirect('/')
	print(form.errors)
	return render_template('signUp.html',form = form)

@app.route("/tables")
def tables():
	return fetch_tables()



@app.route("/createEvent",methods=["GET","POST"])
def createEvent():
	form = Create_Event()
	if form.validate_on_submit():
		add_event(form.name.data,form.place.data,form.category.data,form.description.data,
		form.creatorId.data,form.image.data,form.date.data,form.time.data)
		return "200"
	return render_template("createEvent.html",form = form)

if __name__ == '__main__':
	
	app.run(debug=True)
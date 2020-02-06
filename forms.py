from flask_wtf	import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email

class Create_Event(FlaskForm):
	name = StringField('Name',validators=[DataRequired()])
	place = StringField('Place',validators=[DataRequired()])
	category = StringField('Category',validators=[DataRequired()])
	description = StringField('Description',validators=[DataRequired()])
	creatorId = StringField('Creators Id',validators=[DataRequired()])
	image = StringField('Image',validators=[DataRequired()])
	date = StringField('Date',validators=[DataRequired()])
	time = StringField('Time',validators=[DataRequired()])
	submit = SubmitField('Create')

class Login(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	submit = SubmitField('Login')

class SignUp(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()],id='email')
	password = PasswordField('Password',validators=[DataRequired()],id='password')
	passwordCon = PasswordField('Password',validators=[DataRequired()],id='password')
	submit = SubmitField('SignUp')
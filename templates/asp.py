from flask import Flask, render_template, redirect, url_for, request, session, flash,Markup
from functools import wraps
#from flask.ext.mysqldb import MySQL
from flask.ext.sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)
#mysql = MySQL()
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'allnawash'
#app.config['MYSQL_DATABASE_DB'] = 'shopping_cart'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
app.secret_key = "aswa23ewd4rfeiu7"
#conn = mysql.connect()
#cursor = conn.cursor()

#app.config.from_object('config'),instance_relative_config=True
#app.config.from_pyfile('config.py')
db =  SQLAlchemy(app)

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			message = Markup("<span class='error'>You need to log in to perform this action.</span>")
			flash(message)
			return redirect(url_for('login'))
	return wrap

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['email'] == 'me@you.com' and request.form['password'] == 'password':
			session['logged_in'] = True
			return redirect(url_for('shoes'))
			
			
		elif request.form['email'] == 'admin@feeton.com' and request.form['password'] == 'admin':
			session['logged_in'] = True
			return redirect(url_for('manage'))
		else:
			error = "Invalid username or password."
	return render_template('login.html', error = error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('home'))
	

@app.route('/reg',methods=['GET','POST'])
def register():
	error = None
	if request.method == 'POST':
		new_user_email = request.form['email']
		new_user_password = request.form['password']
		if not new_user_email or not new_user_password:
			error = "Enter a valid email and password to register."
		user_reg = Users(new_user_email,new_user_password)
		db.session.add(user_reg)
		db.session.commit()
		flash('You have been successfully registered.')
	return render_template('register.html',error = error)

@app.route('/shoes')
@login_required
def shoes():
	return render_template('shoes.html')

@app.route('/manage')
@login_required
def manage():
	return render_template('mgt.html')



if __name__=='__main__':
	app.run(debug = True)

'''
	
	'''
#this is used to import clases from flask 	`
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from functools  import wraps
from models import *
# import sqlite3
#this is the application object
app = Flask(__name__)

app.secret_key = "S2q3q3kbpy27"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
	

db = SQLAlchemy(app)

# from models import *
# these are the routes, they specify the path to the urls


@app.route('/dashboard')
def dashboard():
	users = db.session.query(User).all()
	return render_template("dashboard.html", users=users)#this is a tempalte page

@app.route('/', methods=['GET', 'POST'])
def home():




	# name = request.form['name']
	# phone_number = request.form['phone_number']
	# email = request.form['email']
	# address = request.form['address']
	# table = request.form['table']
	# # if not name or not phone_number or not email or not address or not table:
	# # 	flash("All fields are required. Please try again.")
	# # 	return redirect(url_for('success'))
	# # else:
	# db.session.add(name)
	# db.session.add(phone_number)
	# db.session.add(email)
	# db.session.add(address)
	# db.session.add(table)
	# db.session.commit()
	# db.session.close()
	# flash('New entry was successfully posted!')
	# return redirect(url_for('success'))
	return render_template("home.html")#this is a tempalte page



@app.route('/admin', methods=['GET', 'POST'])
def admin():
	error = None
	if  request.method == 'GET':
		if request.form['username'] != 'admin' or request.form['password'] != 'myAdmin':
			error = 'Invalid login details, Please meet the Admin'
		else:
			session['logged_in'] = True
			flash('Login sucessfull')
			return redirect(url_for('dashboard'))
	return render_template('admin.html', error=error)#this is a tempalte page

@app.route('/registered')
def success():
	return render_template('success.html')#this is a tempalte page



@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You have been logged out')
	return redirect(url_for('home'))

# def connect_db():
#     return sqlite.connect('posts.db')



if __name__ == '__main__':
	app.run(debug = True) 
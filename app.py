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
	users = db.session.query(User).order_by(User.name)
	return render_template("dashboard.html", users=users)#this is a tempalte page

@app.route('/', methods=['GET', 'POST'])
def home():
	error = None
	if request.method == 'POST':
		name = request.form['name']
		phone_number = request.form['phone_number']
		email = request.form['email']
		address = request.form['address']
		table = request.form['table']
		if not name or not email:
			error = "Please check your entires"
			if not phone_number.isdigit():
				error = "Please enter a valid Phone Number"
		user_reg = User(name,phone_number,email,address,table)
		db.session.add(user_reg)
		db.session.commit()
		flash('Registration Successfull.')
	return render_template('home.html',error = error)
	return render_template("home.html")#this is a tempalte page



@app.route('/admin', methods=['GET', 'POST'])
def admin():
	error = None
	if  request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'myAdmin':
			error = 'Invalid login details, Please meet the Admin'
		else:
			session['logged_in'] = True
			flash('Login sucessfull')
			return redirect(url_for('dashboard'))
	return render_template('admin.html', error=error)#this is a tempalte page





@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You have been logged out')
	return redirect(url_for('home'))

# def connect_db():
#     return sqlite.connect('posts.db')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    elif request.method != "POST":
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)

@app.route('/admin_insert', methods=['GET', 'POST'])
def insert():
	error = None
	if request.method == 'POST':
		name = request.form['name']
		phone_number = request.form['phone_number']
		email = request.form['email']
		address = request.form['address']
		table = request.form['table']
		if not name or not email:
			error = "Please check your entires"
			if not phone_number.isdigit():
				error = "Please enter a valid Phone Number"
		user_reg = User(name,phone_number,email,address,table)
		db.session.add(user_reg)
		db.session.commit()
		flash('Registration Successfull.')
	return render_template('admin_insert.html',error = error)
	return render_template("admin_insert.html")#this is a tempalte page

if __name__ == '__main__':
	app.run(debug = True) 
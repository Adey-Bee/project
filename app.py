#this is used to import clases from flask 
from flask import Flask, render_template, redirect, url_for, request

#this is the application object
app = Flask(__name__)
	
# these are the routes, they specify the path to the urls
@app.route('/')
def home():
	return "hello Word" #this will show on the index page

@app.route('/welcome')
def welcome():
	return render_template("welcome.html")#this is a tempalte page


@app.route('/login', methods= ['GET', 'POST'])
def login():
	error = None
	if  request.method == 'POST':
		if request.form['username'] != 'admin' or 	if request.form['password'] !== 'myAdmin':
			error = 'Invalid login details, Please meet the Admin'
		else:
			return redirect(url_for('home'))

	return render_template('login.html', error=error)#this is a tempalte page

if __name__ == '__main__':
	app.run(debug = True) 
from flask import Flask, render_template, url_for, redirect, request
from database import *
from flask import session as login_session
import os

app = Flask(__name__)
app.secret_key = "dana-meet"

@app.route('/',methods=['POST','GET'])
def home():
	print("login_session",login_session)
	if request.method=='POST':
		user = query_user_by_email(request.form['email'])
		if user != None and user.password==request.form['password']:
			login_session['name'] = user.name
			login_session['email'] = user.email
			return redirect(url_for('home_logged_in'))
		return redirect('/')
	if request.method=='GET':
		return render_template('home.html')

@app.route('/sign_up',methods=['POST','GET'])
def sign_up():
	if request.method=='POST':
		add_user(request.form['name'],
			request.form['email'],
			request.form['password'])
		return redirect(url_for('home'))
	if request.method=='GET':
		return render_template('sign_up.html')

@app.route('/home_logged_in', methods=['GET','POST'])
def home_logged_in():
	print("login_session",login_session)
	if request.method=='GET':
		if 'email' in login_session:
			user=query_user_by_email(login_session['email'])
			return render_template('home_logged_in.html', user=user)
		else:
			return render_template('home.html')
		

@app.route('/add_activity', methods=['POST','GET'])
def add_new_activity():
	if request.method=='POST':
		user = query_user_by_email(login_session['email'])
		add_activity(request.form['activity_name'],request.form['min-age'],request.form['max-age'],
			request.form['activity-type'],request.form['content'],user)
		return redirect(url_for('activities'))
	return render_template('add_activity.html')

@app.route('/activities',methods=['POST','GET'])
def activities():
	if request.method=='GET':
		activities=query_all_activities()
		return render_template('activities.html',activities=activities)

@app.route('/activities_guest',methods=['POST','GET'])
def activities_guest():
	if request.method=='GET':
		activities=query_all_activities()
		return render_template('activities_guest.html',activities=activities)

@app.route('/search', methods=['POST'])
def search():
	if request.method=='POST':
		activities=query_by_name(request.form['name'])
		return render_template('activities.html',activities=activities)

@app.route('/logout')
def logout():
	del login_session['email']
	if 'user_name' in login_session.keys(): 
		del login_session['user_name']
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)


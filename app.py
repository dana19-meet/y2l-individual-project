from flask import Flask, render_template, url_for, redirect, request
from database import *
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
	if request.method=='GET':
		return render_template('home.html')

@app.route('/add_activity', methods=['POST','GET'])
def add_new_activity():
	if request.method=='POST':
		add_activity(request.form['activity_name'],request.form['min-age'],request.form['max-age'],
			request.form['activity-type'],request.form['content'])
		return redirect(url_for('activities'))
	return render_template('add_activity.html')

@app.route('/activities',methods=['POST','GET'])
def activities():
	if request.method=='GET':
		activities=query_all_activities()
		return render_template('activities.html',activities=activities)

@app.route('/search', method=['POST'])
def search():
	if request.method=='POST':
		activites=query_by_name(activity_name)
		return re
if __name__ == '__main__':
	app.run(debug=True)


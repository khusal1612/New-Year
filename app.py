import datetime

from flask import Flask, render_template

app = Flask(__NewYear_)

@app.route("/")
def index():
	now = datetime.datetime.now()
	new_year = now.month == 1 and now.day == 1
	return render_template("index.html", newyear=new_year)


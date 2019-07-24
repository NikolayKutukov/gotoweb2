from flask import Flask, render_template
import datetime
import random
date=str(datetime.date)
temp=random.randint(0,30)
app = Flask(__name__)
condition=['солнечно','облачно','дождь']
curcondition=random.choice(condition)
@app.route('/')
def mysite():
    return render_template('page.html')


@app.route('/me')
def cat():
    return render_template('page me.html')

@app.route('/weather')
def weather():
    return render_template('weather.html',condition=curcondition, temp=temp)
app.run(debug=True)
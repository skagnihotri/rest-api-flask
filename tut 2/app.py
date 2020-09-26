from flask import Flask, render_template, redirect

app = Flask(__name__)


friend = ["anmol", "ashish", "prateek"]
num = 7

@app.route('/')
def index() :
	return render_template('index.html', my_friend = friend, number = num)

@app.route('/about')
def about() :
	return "<h1> About Page </h1>"

@app.route('/home')
def home() :
	return redirect('/')

if __name__ == '__main__':
	app.run(debug = True)
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index() :
	return render_template('index.html')

@app.route('/home')
def home():
	return redirect('/')

@app.route('/submit', methods = ['POST'])
def submit_details() :
	if request.method == 'GET' :
		return "Nothing"

	# print(request.form['num1'])
	# print(request.form['num2'])
	n1 = int(request.form['num1'])
	n2 = int(request.form['num2'])

	# print(request.files)
	f = request.files['userfile']
	# print(f)
	f.save(f.filename)

	return f"<center> <h1> The Sum is :- {n1+n2} </h1> </center>"

if __name__ == '__main__':
	app.run(debug = True)
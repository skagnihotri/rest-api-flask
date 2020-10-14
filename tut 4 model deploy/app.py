from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route('/')
def home() :
	return render_template('index.html')

@app.route('/about')
def about():
	return '<h1>This is a test classification project deploy</h1>'

@app.route('/', methods = ['POST'])
def classify() :
	sentence = request.form['text_box']
	pred = model.single_prediction(sentence)
	pred = pred.split('.')
	pred = ' '.join(pred)
	return render_template('index.html', prediction = pred)

if __name__ == '__main__':
	# app.run(debug = True)
	app.run()

from flask import Flask, request, render_template, redirect
import send_mail

app = Flask(__name__)

@app.route('/')
def home() :
	return render_template("index.html")

@app.route('/', methods = ['POST'])
def home_submit() :
	sender = request.form['from']
	reciever = request.form['to']
	subject = request.form['subject']
	message = request.form['message']
	password = request.form['password']
	
	send_mail.email(sender, reciever, subject, message, password)
	return render_template("index.html", done = True)
	
if __name__ == '__main__':
	app.run()
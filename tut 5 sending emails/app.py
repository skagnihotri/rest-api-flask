from flask import Flask, request, render_template, redirect

app = Flask(__name__)


if __name__ == '__main__':
	app.run(debug = True)
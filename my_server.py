from flask import Flask, request, render_template
from my_model import *

app = Flask(__name__)

# Simple routing with Template
@app.route("/")
def index():
    return render_template('myIndexTemplate.html')

# Simple routing with two arguments "name" and "surname" with Template
@app.route("/name")
def name():
    name = request.args.get("name")
    surname = request.args.get("surname")
    return render_template('myTemplate.html', nameTemp=name, surnameTemp=surname)

# API Routing to get JSON file
@app.route("/readFile")
def readFileRoute():
    result = readTxtToJSON()
    return str(result)

if __name__ == "__main__":
	app.run()
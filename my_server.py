from flask import Flask, request, render_template
from my_model import *

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/hello")
def hello():
    nome = request.args.get("nome")
    cognome = request.args.get("cognome")
    #response = "I am %s %s" % (nome, cognome)
    return render_template('myTemplate.html', nomeTemp=nome, cognomeTemp=cognome)

@app.route("/readFile")
def readFileRoute():
    result = readTxtToJSON()
    return str(result)

app.run()
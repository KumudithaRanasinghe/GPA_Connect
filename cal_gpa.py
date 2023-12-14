from flask import Flask, render_template

#Create a Flask Interface
app = Flask(__name__)


#Create a route decorator

@app.route('/')

def index():
    return "<h1>hello world!<h1>"

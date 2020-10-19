from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/films/list')

def list_of_films():
    return render_template("index.html")

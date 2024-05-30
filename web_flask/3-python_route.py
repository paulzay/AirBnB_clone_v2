#!/usr/bin/python3

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hello_again():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return f"C {escape(text.replace("_", " "))}"

@app.route('/python/<text>', strict_slashes=False)
def python_is(text):
    return f"Python {escape(text.replace("_", " "))}"

if __name__ == "__main__":
    app.run(debug=True)

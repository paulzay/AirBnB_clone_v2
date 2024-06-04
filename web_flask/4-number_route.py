#!/usr/bin/python3
"""docs"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    """home"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_again():
    """hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """c is fun"""
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text):
    """py is cool"""
    return "Python " + text.replace("_", " ")


@app.route('/number<n>', strict_slashes=False)
def only_nums(n):
    """n"""
    if type(n) is int:
        return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

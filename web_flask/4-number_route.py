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
    """c"""
    return f"C {escape(text.replace("_", " "))}"


@app.route('/python/<text>', strict_slashes=False)
def python_is(text):
    """py"""
    return f"Python {escape(text.replace("_", " "))}"


@app.route('/number<n>', strict_slashes=False)
def only_nums(n):
    """n"""
    if type(n) is int:
        return f"{n} is a number"


if __name__ == "__main__":
    app.run(debug=True)

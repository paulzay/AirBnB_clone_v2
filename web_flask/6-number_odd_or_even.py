#!/usr/bin/python3
"""docs"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    """docs"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_again():
    """docs"""
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


@app.route('/number/<int:n>', strict_slashes=False)
def only_nums(n):
    """n"""
    if type(n) is int:
        return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """docs"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """docs"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001')

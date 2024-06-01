#!/usr/bin/python3
"""docs"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """home route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_again():
    """hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """c is fun"""
    return "C" + text.replace("_", " ")


if __name__ == "__main__":
    app.run(debug=True)

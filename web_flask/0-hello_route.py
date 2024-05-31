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


if __name__ == "__main__":
    app.run(debug=True)

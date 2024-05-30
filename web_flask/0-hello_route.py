#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hello_again():
    return "HBNB"

if __name__ == "__main__":
    app.run(debug=True)

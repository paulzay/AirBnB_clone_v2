#!/usr/bin/python3

from flask import Flask, render_template
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

@app.route('/number<n>', strict_slashes=False)
def only_nums(n):
    if type(n) == int:
      return f"{n} is a number"

@app.route('/number_template/<n>', strict_slashes=False)
def num_template(n):
    return render_template('5-number.html', n=n)
    

if __name__ == "__main__":
    app.run(debug=True)
 
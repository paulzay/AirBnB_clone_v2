#!/usr/bin/python3
"""docs"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list')
def home():
    return render_template('7-states_list.html')


@app.teardown_appcontext
def close():
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
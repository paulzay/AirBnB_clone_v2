#!/usr/bin/python3
"""docs"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def home():
    """docs"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close():
    """docs"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")

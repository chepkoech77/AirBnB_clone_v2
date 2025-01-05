#!/usr/bin/python3
"""This module defines two routes"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Print HELLO HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Print HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

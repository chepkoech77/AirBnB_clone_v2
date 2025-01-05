#!/usr/bin/python3
"""This module defines routes"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """Runs on port 5000"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

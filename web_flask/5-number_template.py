#!/usr/bin/python3
"""This module defines two routes"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Print HELLO HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Print HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Print text"""
    return "C " + text.replace('_', ' ')


@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    """Outputs a text"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Prints number if number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Renders an html template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

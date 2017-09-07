# -*- coding: utf-8 -*-
"""Angular-Flask-Docker-Skeleton

    Simple Flask app

"""
from flask import Flask

app = Flask(__name__)

@app.route("/api")
def hello():
    return "Hello World from Flask using Python 3.6.2!!"
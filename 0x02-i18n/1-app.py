#!/usr/bin/env python3
"""
0. Basic Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    Babel_default_locale = "en"
    Babel_default_timezone = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
bable = Babel(app)
@app.route('/')
def index():
    """
    0. Basic Flask app
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()

#!/usr/bin/env python3
"""
0. Basic Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    Babel_default_locale = "en"
    Babel_default_timezone = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user(id):
    """
    Validate user login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary if id is valid else None
    """
    return users.get(int(id), 0)


@babel.localeselector
def get_locale():
    """get Configuration variable"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    0. Basic Flask app
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)

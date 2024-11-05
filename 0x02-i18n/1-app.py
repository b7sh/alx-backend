#!/usr/bin/env python3
'''
Route module for the API - Basic Babel setup
'''


from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    ''' Setup - Babel configuration '''
    LANGUAGES = ['en', 'fr']
    # these are the defaults
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# set the above class object as the configuration for the app
app.config.from_object('1-app.Config')


@app.route('/')
def index() -> str:
    ''' Return: 1-index.html '''
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()

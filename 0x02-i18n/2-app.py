#!/usr/bin/env python3
'''
Route module for the API - Get locale from request
'''


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    ''' Setup - Babel configuration '''
    LANGUAGES = ['en', 'fr']
    # these are the inherent defaults just btw
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# set the above class object as the configuration for the app
app.config.from_object('2-app.Config')


@app.route('/')
def index() -> str:
    ''' Return: 2-index.html '''
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    ''' Determines best match for supported languages '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()

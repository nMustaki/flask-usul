# -*- coding: utf-8 -*-
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPLOADDIR = os.path.join(BASEDIR, "static/uploads")
SECRET_KEY = 'dslffsdlfksdfsdf43t5l,,l;m'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')

WTF_CSRF_ENABLED = True
CSRF_SESSION_KEY = "rt4354;.vfd[;[].;-%*)()(%^%$"

BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = "Europe/Paris"
AUTH_USE_TOKEN = False
BCRYPT_LOG_ROUNDS = 13
ASSETS_DEBUG = False

LOG_FILENAME = 'flask-usul.log'
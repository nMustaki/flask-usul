# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.babel import Babel
from flask.ext.assets import Environment


db = SQLAlchemy()

babel = Babel()
login_manager = LoginManager()

assets = Environment()

# from app.models import User

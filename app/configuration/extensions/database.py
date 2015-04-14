# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy


db = None


def init(app):
    global db
    db = SQLAlchemy()
    db.init_app(app)
    # with app.app_context():
    #     # Extensions like Flask-SQLAlchemy now know what the "current" app
    #     # is while within this block.
    #     db.create_all()

# -*- coding: utf-8 -*-
from app.configuration.extensions import db


def initDatabase(app):
    db.init_app(app)
    # with app.app_context():
    #     # Extensions like Flask-SQLAlchemy now know what the "current" app
    #     # is while within this block.
    #     db.create_all()

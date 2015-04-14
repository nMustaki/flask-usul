# -*- coding: utf-8 -*-
from flask.ext.admin import Admin
from .database import db
from app.blueprints.admin.user_admin import UserView


admin = None


def init(app):
    global admin
    admin = Admin(app, name="Admin")  # , index_view=MyAdminIndexView
    admin.add_view(UserView(db.session, name="Users", endpoint="users"))

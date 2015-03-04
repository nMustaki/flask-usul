# -*- coding: utf-8 -*-
from flask.ext.admin import Admin
from . import db
from app.blueprints.admin.user_admin import UserView
from app.blueprints.admin.dyn_elem_admin import DynElemView


def initAdmin(app):
    admin = Admin(app, name="Admin")  # , index_view=MyAdminIndexView())
    admin.add_view(UserView(db.session, name="Utilisateurs", endpoint="users"))
    # Homepage
    admin.add_view(DynElemView(db.session, "reasons", "home", name=u"Points forts",
                   endpoint=u"points-forts", category=u"Accueil"))
    admin.add_view(DynElemView(db.session, "testimonials", "home", name="Avis client",
                   endpoint=u"avis-clients", category=u"Accueil"))
    admin.add_view(DynElemView(db.session, "bulletpoints", "home", name=u"Bulletpoints",
                   endpoint=u"bulletpoints", category=u"Accueil"))

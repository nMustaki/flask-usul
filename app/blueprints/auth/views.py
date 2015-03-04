# -*- coding: utf-8 -*-
from werkzeug.security import check_password_hash
from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_required, login_user, logout_user, confirm_login
from app.models.user import User
from . import mod


@mod.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email'] or None
        password = request.form['password'] or None
        user = User.query.filter_by(email=email).first()
        if user and password:
            if check_password_hash(user.password, password) and login_user(user, remember=False):
                return redirect(request.args.get("next") or url_for("home.index"))
        flash(u"Erreur : vos identifiants sont invalides.", "error")
    return render_template("login.html")


@mod.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    if request.method == "POST":
        confirm_login()
        flash(u"Authentification renouvellée.")
        return redirect(request.args.get("next") or url_for("home.index"))
    return render_template("login.html")


@mod.route("/logout")
@login_required
def logout():
    logout_user()
    flash(u"Vous êtes déconnecté.")
    return redirect(url_for("home.index"))

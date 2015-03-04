# -*- coding: utf-8 -*-
from itertools import groupby
from flask import Blueprint, render_template, current_app, session, g, redirect, url_for
from app.models.dynelem import DynElem


mod = Blueprint('home', __name__, url_prefix="/<lang_code>")


@mod.url_defaults
def add_language_code(endpoint, values):
    if current_app.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
        values['lang_code'] = session['lang_code']
        g.lang_code = session['lang_code']
    values.setdefault('lang_code', g.lang_code)


@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    session['lang_code'] = values.pop('lang_code')
    g.lang_code = session.get('lang_code', None)


@mod.route('/change/<new_lang_code>')
def change(new_lang_code):
    session['lang_code'] = new_lang_code
    return redirect(url_for('home.index'))


@mod.route('/')
def index():
    dico = {}
    elems = DynElem.query.all()
    for key, group in groupby(elems, lambda x: x.elem_type):
        dico[key] = [x for x in group]
    return render_template("index.html", dico=dico)

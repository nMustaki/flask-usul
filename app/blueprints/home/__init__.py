# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, current_app, session, g, redirect, url_for


mod = Blueprint('home', __name__, url_prefix="/<lang_code>")


@mod.route('/')
def index():
    return render_template("index.html")


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

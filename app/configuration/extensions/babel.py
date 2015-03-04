# -*- coding: utf-8 -*-
from flask import session, g, current_app
from app.configuration.extensions import babel


def initBabel(app):
    babel.init_app(app)

    # @app.before_request
    # def before_request():
    #     if request.view_args is None:
    #         if 'lang_code' not in session.keys():
    #             return redirect('/fr' + request.full_path)
    #         else:
    #             return redirect('/'+session['lang_code']+request.full_path)

    @app.context_processor
    def inject_lang():
        return dict(sess_lang=session['lang_code'])

    @babel.localeselector
    def get_locale():
        g.lang_code = session['lang_code']
        return g.get('lang_code', current_app.config["BABEL_DEFAULT_LOCALE"])

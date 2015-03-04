# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask.ext.login import login_required


def create_app(devel=False, testing=False):
    app = Flask(__name__)

    configure_configuration(app, devel, testing)
    configure_extensions(app)
    configure_logging(app)
    configure_error_handlers(app)
    # configure_root(app)
    configure_blueprints(app)
    return app


def configure_configuration(app, devel, testing):
    if devel is True:
        app.debug = True
    if app.debug:
        app.config["ASSETS_DEBUG"] = True
        app.config["BCRYPT_LOG_ROUNDS"] = 1
    app.config.from_object('app.config')


def configure_extensions(app):
    from app.configuration.extensions.database import initDatabase
    initDatabase(app)

    # Flask login
    from app.configuration.extensions.login import initLogin
    initLogin(app)

    # flask-admin
    from app.configuration.extensions.admin import initAdmin
    initAdmin(app)

    # assets
    from app.configuration.extensions.assets import initAssets
    initAssets(app)

    # Babel
    from app.configuration.extensions.babel import initBabel
    initBabel(app)


##################
# Error handlers #
##################
def configure_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    @login_required
    def error_500(error):
        from traceback import format_exc
        # db.session.rollback()
        if app.config['DEBUG']:
            return format_exc(), 500, {'Content-Type': 'text/plain'}
        return render_template('500.html'), 500


#################
# Logs handlers #
#################
def configure_logging(app):
    file_handler = RotatingFileHandler(
        app.config["LOG_FILENAME"], 'a', 1 * 1024 * 1024, 1)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.WARNING)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
    app.logger.info('startup')
    app.logger.info(app.config["BASEDIR"])


##############
# Blueprints #
##############
def configure_blueprints(app):
    from app.blueprints.home import mod as home_module
    app.register_blueprint(home_module)
    from app.blueprints.auth import mod as auth_module
    app.register_blueprint(auth_module)

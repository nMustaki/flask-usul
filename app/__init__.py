# -*- coding: utf-8 -*-
import pkgutil
import importlib
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
    app.config.from_object('app.configuration.config')


def configure_extensions(app):
    app.logger.info("Importing extensions")
    from app.configuration.extensions.database import init
    init(app)

    imported = []
    errors = []
    for _, name, _ in pkgutil.walk_packages(['app/configuration/extensions'], prefix="app.configuration.extensions."):
        try:
            modu = importlib.import_module(name)
            modu.init(app)
            imported.append(name)
        except Exception as e:
            errors.append(name + " : " + str(e))
    app.logger.info("Successfully imported extensions : " + ", ".join(imported))
    if len(errors):
        app.logger.error("Extensions import errors : " + ", ".join(errors))


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
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('startup')
    app.logger.info(app.config["BASEDIR"])


##############
# Blueprints #
##############
def configure_blueprints(app):
    imported = []
    imported_names = []
    import_errors = []
    app.logger.info("Importing blueprints")
    for _, name, _ in pkgutil.walk_packages(['app/blueprints'], prefix="app.blueprints."):
        try:
            modu = importlib.import_module(name)
            mod = modu.mod
            if mod not in imported:
                app.register_blueprint(modu.mod)
                imported.append(mod)
                imported_names.append(name)
        except Exception as e:
            import_errors.append(name + " : " + str(e))
    app.logger.info("Successfully imported blueprints : " + ", ".join(imported_names))
    if len(import_errors):
        app.logger.error("Blueprints import error : " + ", ".join(import_errors))

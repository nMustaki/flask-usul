# -*- coding: utf-8 -*-
from flask.ext.assets import Bundle
# from app.configuration.extensions import assets
from flask.ext.assets import Environment


assets = None


def init(app):
    global assets
    assets = Environment()
    assets.init_app(app)

    js = Bundle(
        'js/vendor/jquery-1.11.2.min.js', 'js/vendor/bootstrap.min.js', 'js/custom.js',
        output='js/packed.js', filters='rjsmin')
    css = Bundle(
        'css/vendor/bootstrap.min.css', 'css/utils.css', 'css/custom.css',
        output='css/packed.css', filters='cssmin')
    assets.register('js_all', js)
    assets.register('css_all', css)

# -*- coding: utf-8 -*-
import base64
from app.models.user import User
from flask.ext.login import LoginManager


login_manager = None


def init(app):
    global login_manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message = u"Veuillez vous authentifier pour accéder à cette page."
    login_manager.setup_app(app)

    @login_manager.user_loader
    def load_user(userid):
        return User.query.get(int(userid))

    @login_manager.token_loader
    def load_user_token(token):
        if app.config['AUTH_USE_TOKEN'] is True:
            return User.query.filter_by(token=token).first()
        return False

    @login_manager.request_loader
    def load_user_from_request(request):
        ''' For API handling '''

        # first, try to login using the token url arg
        if app.config['AUTH_USE_TOKEN'] is True:
            token = request.args.get('token')
            if token:
                user = User.query.filter_by(token=token).first()
                if user:
                    return user

            # next, try to login using Basic Auth
            token = request.headers.get('Authorization')
            if token:
                token = token.replace('Basic ', '', 1)
                try:
                    token = base64.b64decode(token)
                except TypeError:
                    pass
                user = User.query.filter_by(token=token).first()
                if user:
                    return user
        # finally, return None if both methods did not login the user
        return None

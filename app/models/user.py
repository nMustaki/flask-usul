import re
from werkzeug.security import check_password_hash
from flask.ext.login import UserMixin
from app.configuration.extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(50), index=True, nullable=False)
    token = db.Column(db.String(50), index=False, unique=True)
    active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, password, email, name="", active=True, token=None):
        self.password = password
        self.email = email
        self.name = name
        self.active = active
        self.token = token

    def __repr__(self):
        return '<User %r>' % (self.email)

    def is_active(self):
        return self.active

    def get_auth_token(self):
        return self.token

    def validates(self, password_confirmation=None):
        if not self.email or not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", self.email):
            raise ValueError("Invalid email")
        if self.active not in [True, False]:
            raise ValueError("Invalid active state")
        if not self.password and not self.token:
            raise ValueError("Missing password or token.")
        if self.password and password_confirmation:
            if not check_password_hash(self.password, password_confirmation):
                raise ValueError("Password confirmation does not match with password")
        return True

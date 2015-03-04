# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash
from app.models.user import User


def init_db(db):

    # db.drop_all()
    # db.create_all()

    if not User.query.filter_by(email="sdd@ere.fr").first():
        usr = User(name="Nathan",
                   email="dds@sdffdk.fr",
                   password=unicode(generate_password_hash("fdskdsdjfdshfds")),
                   active=True)
        db.session.add(usr)

    db.session.commit()

if __name__ == "__main__":
    from app import create_app
    from app.configuration.extensions import db
    new_app = create_app(False)
    with new_app.app_context():
        init_db(db)

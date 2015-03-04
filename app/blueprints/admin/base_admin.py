from wtforms.csrf.session import SessionCSRF
from wtforms.meta import DefaultMeta
from flask import session, redirect, url_for, request
from datetime import timedelta
from flask.ext.admin import form
from flask.ext.admin.contrib import sqla
from flask.ext.login import current_user


class SecureForm(form.BaseForm):
    class Meta(DefaultMeta):
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = b'EPj00jpfj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym'
        csrf_time_limit = timedelta(minutes=20)

        @property
        def csrf_context(self):
            return session


class ModelAdmin(sqla.ModelView):
    form_base_class = SecureForm

    def is_accessible(self):
        return current_user.is_authenticated()

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next=request.url))

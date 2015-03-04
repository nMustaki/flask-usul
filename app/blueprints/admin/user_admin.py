# -*- coding: utf-8 -*-
from .base_admin import ModelAdmin
from app.models.user import User
from wtforms.fields import PasswordField


class UserView(ModelAdmin):
    column_labels = dict(name=u'Prénom Nom',
                         email="Courriel",
                         active="Actif")

    def scaffold_form(self):
        form_class = super(UserView, self).scaffold_form()
        form_class.password_confirmation = PasswordField('Mot de passe')
        return form_class

    column_sortable_list = ('name', 'active')
    form_excluded_columns = ['password']

    def on_model_delete(self, model):
        if User.query.count() == 1:
            raise IndexError("Cannot delete last user")

    def on_model_change(self, form, model, is_created=False):
        if not model.id:
            model.id = None
        if form.data['password_confirmation']:
            model.password = form.data['password_confirmation']

    # Visible columns in the list view
    column_exclude_list = ['password']

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(UserView, self).__init__(User, session, **kwargs)

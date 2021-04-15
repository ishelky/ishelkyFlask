from flask_admin import Admin, helpers, expose
from flask import url_for, redirect, request
import flask_login as login
from wtforms import form, fields, validators

class LoginForm(form.Form): pass
    # login = fields.StringField(validators=[validators.required()])
    # password = fields.PasswordField(validators=[validators.required()])
    #
    # def validate_login(self, field):
    #     user = self.get_user()
    #
    #     if user is None:
    #         raise validators.ValidationError('Invalid user')
    #
    #     # we're comparing the plaintext pw with the the hash from the db
    #     if not user.check_password(self.password.data):
    #         # to compare plain text passwords use
    #         # if user.password != self.password.data:
    #         raise validators.ValidationError('Invalid password')

#    def get_user(self):
   #     pass
    # return db.session.query(User).filter_by(username=self.login.data).first()


class MyAdminIndexView(admin.AdminIndexView): pass

    # @expose('/')
    # def index(self):
    #     if not login.current_user.is_authenticated:
    #         return redirect(url_for('.login_view'))
    #     return super(MyAdminIndexView, self).index()
    #
    # @expose('/login/', methods=('GET', 'POST'))
    # def login_view(self):
    #     # handle user login
    #     form = LoginForm(request.form)
    #     if helpers.validate_form_on_submit(form):
    #         user = form.get_user()
    #         login.login_user(user)
    #
    #     if login.current_user.is_authenticated:
    #         return redirect(url_for('.index'))
    #     self._template_args['form'] = form
    #     return super(MyAdminIndexView, self).index()
    #
    # @expose('/logout/')
    # def logout_view(self):
    #     login.logout_user()
    #     return redirect(url_for('.index'))


admin = Admin(name='Админ панель',
              index_view=MyAdminIndexView(),
              base_template='admin/my_admin.html',
              template_mode='bootstrap3')

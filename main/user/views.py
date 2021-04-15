from flask import render_template,redirect,url_for,flash
from flask_login import current_user, login_user,logout_user
from main.user.models import User
from ..user import user
from .forms import LoginForm

@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('user.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



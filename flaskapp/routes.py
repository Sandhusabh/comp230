from flask import render_template, url_for, flash, redirect, abort, request
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_user import roles_required

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')

@app.route("/order", methods=['GET', 'POST'])
def order():
    return render_template('login.html', title='Login')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username = form.username.data, email = form.email.data, password = hash_pw)
        role = Role(name='admin')
        new_user.roles.append(role)
        db.session.add(new_user)

        db.session.commit()
        flash('Congrats! Your account been created successfully', 'info')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
@roles_required('admin')     
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/menu")
def menu():
    return render_template('menu.html', title='Menu')

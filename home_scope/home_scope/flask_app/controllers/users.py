from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import Users
from flask_app.models.home import Homes
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return redirect('/user/login')


@app.route('/user/login')
def login():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')


@app.route('/user/logged_in/process', methods=['POST'])
def login_success():
    user = Users.login_validator(request.form)
    if not user:
        flash("invalid email/password")
        return redirect('/user/login')
    session['user_id'] = user.id
    print(user.id)
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = Users.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return render_template('dashboard.html', user=user, homes= Homes.fetch_all())



@app.route('/user/registration/process', methods=['POST'])
def register_success():
    if not Users.validate_regis_form(request.form):
        return redirect('/user/login')
    user_id = Users.save(request.form)
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/user/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect('/user/login')





from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.home import Home
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('login2.html')


@app.route('/user/login', methods=['POST'])
def login_success():
    user = User.login_validator(request.form)
    if not user:
        flash("invalid email/password")
        return redirect('/')
    session['user_id'] = user.id
    print(user.id)
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user = User.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/')
    return render_template('dashboard.html', user=user, homes= Home.fetch_all())



@app.route('/user/register', methods=['POST'])
def register_success():
    if not User.validate_regis_form(request.form):
        return redirect('/')
    user_id = User.save(request.form)
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/user/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect('/')





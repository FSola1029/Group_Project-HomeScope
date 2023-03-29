from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.home import Home
from flask_app.models.user import User


@app.route('/homes/new/one')
def create_homes():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return render_template('new.html', user=user, homes= User.fetch_id({"id":session['user_id']}))


@app.route('/homes/new/process', methods=['POST'])
def homes_process():
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Home.validating_homes(request.form):
        return redirect('/homes/new/one')
    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'street_address': request.form['street_address'],
        'description': request.form['description'],
        'price': request.form['price'],
        }
        
    Home.save(data)
    return redirect('/dashboard')


@app.route('/homes/now/<int:id>')
def view_homes():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return render_template('view.html', user=user, users= User.fetch_id({"id":session['user_id']}))


@app.route('/my/homes/<int:homes_id>')
def view_homes_two(homes_id):
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return render_template('view.html', user=user, users=Home.fetch_by_user_id ({"id":homes_id}), logged= User.fetch_id({"id":session['user_id']}))


@app.route('/homes/edit/<int:id>')
def edit_homes(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return render_template('edit.html',user=user, homes=Home.fetch_id({'id': id}))


@app.route('/homes/edit/process/<int:id>', methods=['POST'])
def editing_process_homes(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Home.validating_homes(request.form):
        return redirect(f'/homes/edit/{id}')
    data = {
        'id': id,
        'name': request.form['name'],
        'street_address': request.form['street_address'],
        'description': request.form['description'],
        'price': request.form['price'],
    }
    Home.update(data)
    return redirect('/dashboard')


@app.route('/homes/delete/<int:id>')
def delete_homes(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    Home.delete({'id':id})
    return redirect('/dashboard')




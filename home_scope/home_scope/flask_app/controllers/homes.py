from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.home import Homes
from flask_app.models.user import Users


@app.route('/homes/new/one')
def create_homes():
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('new.html', homes= Users.fetch_id({"id":session['user_id']}))


@app.route('/homes/new/process', methods=['POST'])
def homes_process():
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Homes.validating_homes(request.form):
        return redirect('/nfts/new/one')
    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'street_address': request.form['street_address'],
        'description': request.form['description'],
        'price': request.form['price'],
        }
        
    Homes.save(data)
    return redirect('/dashboard')


@app.route('/homes/now/<int:id>')
def view_homes():
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('view.html',users= Users.fetch_id({"id":session['user_id']}))


@app.route('/my/homes/<int:homes_id>')
def view_homes_two(homes_id):
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('view.html',users= Homes.fetch_by_user_id ({"id":homes_id}), logged= Users.fetch_id({"id":session['user_id']}))


@app.route('/homes/edit/<int:id>')
def edit_homes(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('edit.html',homes= Homes.fetch_id({'id': id}))


@app.route('/homes/edit/process/<int:id>', methods=['POST'])
def editing_process_homes(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Homes.validating_homes(request.form):
        return redirect(f'/homes/edit/{id}')
    data = {
        'id': id,
        'name': request.form['name'],
        'street_address': request.form['street_address'],
        'description': request.form['description'],
        'price': request.form['price'],
    }
    Homes.update(data)
    return redirect('/dashboard')


@app.route('/homes/delete/<int:id>')
def delete_homes(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    Homes.delete({'id':id})
    return redirect('/dashboard')




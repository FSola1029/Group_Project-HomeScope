from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models.home import Home
from flask_app.models.user import User


@app.route('/homes/new')
def create_homes():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    home_types = Home.home_types()
    return render_template('new.html', user=user, homes= User.fetch_id({"id":session['user_id']}), home_types = home_types)


@app.route('/homes/add', methods=['POST'])
def homes_process():
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Home.validating_homes(request.form):
        return redirect('/homes/new')
    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'street_address': request.form['street_address'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zipcode': request.form['zipcode'],
        'description': request.form['description'],
        'bed': request.form['bed'],
        'bath': request.form['bath'],
        'sq_ft': request.form['sq_ft'],
        'price': request.form['price'],
        'type': request.form['type'],
        'image': ""
        }
    print(data)
    Home.save(data)
    return redirect('/dashboard')


@app.route('/homes/view/<home_type>')
def view_homes(home_type):
    homes = Home.get_homes_by_type({'type': home_type})
    return render_template('view.html', homes=homes)


# @app.route('/homes/now/<int:id>')
# def view_homes():
#     if 'user_id' not in session:
#         return redirect('/user/login')
#     user = User.fetch_id({"id":session['user_id']})
#     if not user:
#         return redirect('/user/logout')
#     return render_template('view.html', user=user, users= User.fetch_id({"id":session['user_id']}))


# @app.route('/my/homes/<int:homes_id>')
# def view_homes_two(homes_id):
#     if 'user_id' not in session:
#         return redirect('/user/login')
#     user = User.fetch_id({"id":session['user_id']})
#     if not user:
#         return redirect('/user/logout')
#     return render_template('view.html', user=user, users=Home.fetch_by_user_id ({"id":homes_id}), logged= User.fetch_id({"id":session['user_id']}))


@app.route('/homes/edit/<home_id>')
def edit_homes(home_id):
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    home_types = Home.home_types()
    return render_template('edit.html',user=user, home=Home.fetch_id({'id': home_id}), home_types=home_types)


@app.route('/homes/update/<int:home_id>', methods=['POST'])
def update_homes(home_id):
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Home.validating_homes(request.form):
        return redirect(url_for('edit_homes', home_id=home_id))
    data = {
        'id': home_id,
        'user_id': session['user_id'],
        'name': request.form['name'],
        'street_address': request.form['street_address'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zipcode': request.form['zipcode'],
        'description': request.form['description'],
        'bed': request.form['bed'],
        'bath': request.form['bath'],
        'sq_ft': request.form['sq_ft'],
        'price': request.form['price'],
        'type': request.form['type'],
        'image': ""
        }
    Home.update(data)
    return redirect('/dashboard')


@app.route('/homes/delete/<int:id>')
def delete_homes(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    Home.delete({'id':id})
    return redirect('/dashboard')



